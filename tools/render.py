#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from lib.data import build_index, load_repository
from validate import validate_repository


WEEKDAYS = "月火水木金土日"
ISSUE_STATUS_LABELS = {
    "open": "未着手",
    "in_progress": "確認中",
    "resolved": "解決済み",
    "wont_fix": "対応しない",
}
ISSUE_PRIORITY_LABELS = {"high": "高", "medium": "中", "low": "低"}


def short_date(value: str) -> str:
    parsed = date.fromisoformat(value)
    return f"{parsed.month}/{parsed.day}"


def dated_heading(value: str) -> str:
    parsed = date.fromisoformat(value)
    return f"{parsed.month}/{parsed.day}（{WEEKDAYS[parsed.weekday()]}）"


def resolve_name(value: str, index: dict[str, dict[str, Any]]) -> str:
    return index[value]["name"] if value in index else value


def format_windows(windows: list[dict[str, str]]) -> str:
    return " / ".join(f'{window["start"]}–{window["end"]}' for window in windows)


def format_km(value: int | float) -> str:
    return f"{value:g}"


def prepare_distance_index(data: dict[str, dict[str, Any]]) -> dict[tuple[str, str], dict[str, Any]]:
    result: dict[tuple[str, str], dict[str, Any]] = {}
    for segment in data["estimates/distances.yaml"]["segments"]:
        if not segment["display"]:
            continue
        for point in segment["points"]:
            prepared = dict(point)
            prepared["origin_label"] = segment["origin"]["label"]
            prepared["distance_display"] = format_km(point["distance_km"])
            if point.get("additional_distance_km", 0) > 0:
                prepared["additional_distance_display"] = format_km(point["additional_distance_km"])
            result[(segment["date"], point["target"])] = prepared
    return result


def prepare_transport(item: dict[str, Any], index: dict[str, dict[str, Any]]) -> dict[str, Any]:
    prepared = dict(item)
    prepared["from_name"] = resolve_name(item["from"], index)
    prepared["to_name"] = resolve_name(item["to"], index)
    prepared["departure_time"] = (
        datetime.fromisoformat(item["departure"]).strftime("%H:%M") if item["departure"] else None
    )
    prepared["arrival_time"] = (
        datetime.fromisoformat(item["arrival"]).strftime("%H:%M") if item["arrival"] else None
    )
    if "booking" in item:
        prepared["booking"] = dict(item["booking"])
        prepared["booking"]["amount"] = f'{item["booking"]["amount_yen"]:,}円'
        prepared["booking"]["change_deadline_display"] = datetime.fromisoformat(
            item["booking"]["change_deadline"]
        ).strftime("%Y年%m月%d日 %H:%M")
    return prepared


def prepare_context(data: dict[str, dict[str, Any]]) -> dict[str, Any]:
    index = build_index(data)
    distance_index = prepare_distance_index(data)
    plan = data["plan/current.yaml"]
    evidence_items = data["evidence/sources.yaml"]["items"]
    raw_issues = data["issues.yaml"]["items"]
    open_issue_subjects = {
        subject
        for issue in raw_issues
        if issue["status"] in {"open", "in_progress"}
        for subject in issue["subjects"]
    }
    windows_by_subject_date: dict[tuple[str, str], list[dict[str, str]]] = {}
    for evidence in evidence_items:
        for dated in evidence.get("date_windows", []):
            windows_by_subject_date[(evidence["subject"], dated["date"])] = dated["windows"]
    days: list[dict[str, Any]] = []
    adopted: set[str] = set()
    for raw_day in plan["days"]:
        day = dict(raw_day)
        for field in ("routes", "transport", "visits", "optional_visits", "food"):
            adopted.update(day[field])
            day[f"{field}_items"] = [index[item_id] for item_id in day[field]]
        day["transport_items"] = [prepare_transport(index[item_id], index) for item_id in day["transport"]]
        day["transport_alternative_items"] = [
            prepare_transport(index[item_id], index) for item_id in day["transport_alternatives"]
        ]
        for field in ("visits", "optional_visits"):
            prepared_visits = []
            for item_id in day[field]:
                item = dict(index[item_id])
                windows = windows_by_subject_date.get((item_id, day["date"]))
                if windows:
                    item["availability_display"] = format_windows(windows)
                if (day["date"], item_id) in distance_index:
                    item["distance"] = distance_index[(day["date"], item_id)]
                prepared_visits.append(item)
            day[f"{field}_items"] = prepared_visits
        adopted.update(day["stay"]["preferred"])
        adopted.update(day["stay"]["fallback"])
        preferred = [index[item_id] for item_id in day["stay"]["preferred"]]
        fallback = [index[item_id] for item_id in day["stay"]["fallback"]]
        day["preferred_names"] = [item["name"] for item in preferred]
        day["fallback_names"] = [item["name"] for item in fallback]
        prepared_food = []
        for item_id in day["food"]:
            item = dict(index[item_id])
            if (day["date"], item_id) in distance_index:
                item["distance"] = distance_index[(day["date"], item_id)]
            prepared_food.append(item)
        day["food_items"] = prepared_food
        day["start_name"] = resolve_name(day["start"], index)
        day["finish_name"] = resolve_name(day["finish"], index)
        day["short_date"] = short_date(day["date"])
        day["dated_heading"] = dated_heading(day["date"])
        days.append(day)
    contingencies = []
    for raw_contingency in plan["contingencies"]:
        contingency = dict(raw_contingency)
        contingency["dated_heading"] = dated_heading(contingency["date"])
        contingency["transport_items"] = [
            prepare_transport(index[item_id], index) for item_id in contingency["transport"]
        ]
        contingency["transport_alternative_items"] = [
            prepare_transport(index[item_id], index)
            for item_id in contingency["transport_alternatives"]
        ]
        contingencies.append(contingency)
    rechecks = []
    for evidence in evidence_items:
        if (
            evidence["recheck_before_trip"]
            and evidence["subject"] in adopted
            and evidence["subject"] not in open_issue_subjects
        ):
            rechecks.append({"name": index[evidence["subject"]]["name"], "claims": evidence["claims"]})
    issues = []
    for raw_issue in raw_issues:
        issue = dict(raw_issue)
        issue["status_label"] = ISSUE_STATUS_LABELS[issue["status"]]
        issue["priority_label"] = ISSUE_PRIORITY_LABELS[issue["priority"]]
        issue["identified_at_display"] = short_date(issue["identified_at"])
        issue["related_date_display"] = " / ".join(short_date(value) for value in issue["related_dates"])
        issue["subject_names"] = [resolve_name(subject, index) for subject in issue["subjects"]]
        issue["anchor"] = issue["id"].replace(".", "-")
        issues.append(issue)
    for day in days:
        day["issue_items"] = [
            issue
            for issue in issues
            if day["date"] in issue["related_dates"] and issue["status"] in {"open", "in_progress"}
        ]
    return {
        "trip": data["trip.yaml"],
        "days": days,
        "recommendations": plan["recommendations"],
        "pre_trip_todos": plan["pre_trip_todos"],
        "contingencies": contingencies,
        "rechecks": rechecks,
        "open_issues": [issue for issue in issues if issue["status"] in {"open", "in_progress"}],
        "closed_issues": [issue for issue in issues if issue["status"] in {"resolved", "wont_fix"}],
    }


def render_repository(root: Path) -> None:
    errors = validate_repository(root)
    if errors:
        raise ValueError("Cannot render invalid repository:\n" + "\n".join(errors))
    context = prepare_context(load_repository(root))
    environment = Environment(
        loader=FileSystemLoader(root / "templates"),
        undefined=StrictUndefined,
        autoescape=False,
        keep_trailing_newline=True,
        trim_blocks=False,
        lstrip_blocks=False,
    )
    output_dir = root / "docs"
    output_dir.mkdir(exist_ok=True)
    for template_name, output_name in (
        ("itinerary.md.j2", "itinerary.md"),
        ("pins.md.j2", "pins.md"),
        ("issues.md.j2", "issues.md"),
    ):
        rendered = environment.get_template(template_name).render(**context)
        rendered = re.sub(r"\n{3,}", "\n\n", rendered)
        rendered = re.sub(r"(^- .+)\n\n(?=- )", r"\1\n", rendered, flags=re.MULTILINE)
        rendered = rendered.rstrip() + "\n"
        (output_dir / output_name).write_text(rendered, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Render trip Markdown documents")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        render_repository(args.root.resolve())
    except (OSError, ValueError) as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        return 1
    print("Rendered docs/itinerary.md, docs/pins.md, and docs/issues.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
