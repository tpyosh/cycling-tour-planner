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
ISSUE_STATUS_LABELS = {"open": "未着手", "in_progress": "確認中", "resolved": "解決済み", "wont_fix": "対応しない"}
ISSUE_PRIORITY_LABELS = {"high": "高", "medium": "中", "low": "低"}
USER_ACTION_TIMING_GROUPS = [
    ("do_now", "今すぐ行う"),
    ("after_decision", "判断後に行う"),
    ("before_departure", "出発までに行う"),
    ("day_before", "前日まで／出発前に行う"),
    ("same_day", "当日に行う"),
    ("blocked", "保留（依存事項の解消後に行う）"),
]


def short_date(value: str) -> str:
    parsed = date.fromisoformat(value)
    return f"{parsed.month}/{parsed.day}"


def dated_heading(value: str) -> str:
    parsed = date.fromisoformat(value)
    return f"{parsed.month}/{parsed.day}（{WEEKDAYS[parsed.weekday()]}）"


def resolve_name(value: str, index: dict[str, dict[str, Any]]) -> str:
    return index[value]["name"] if value in index else value


def prepare_transport(item: dict[str, Any], index: dict[str, dict[str, Any]]) -> dict[str, Any]:
    prepared = dict(item)
    prepared["from_name"] = resolve_name(item["from"], index)
    prepared["to_name"] = resolve_name(item["to"], index)
    prepared["departure_time"] = datetime.fromisoformat(item["departure"]).strftime("%H:%M") if item["departure"] else None
    prepared["arrival_time"] = datetime.fromisoformat(item["arrival"]).strftime("%H:%M") if item["arrival"] else None
    return prepared


def prepare_context(data: dict[str, dict[str, Any]]) -> dict[str, Any]:
    index = build_index(data)
    evidence_items = data["evidence/sources.yaml"]["items"]
    raw_issues = data["issues.yaml"]["items"]
    evidence_by_id = {item["id"]: item for item in evidence_items}
    windows = {
        (evidence["subject"], dated["date"]): dated["windows"]
        for evidence in evidence_items
        for dated in evidence.get("date_windows", [])
    }
    distance_index: dict[tuple[str, str], dict[str, Any]] = {}
    for segment in data["estimates/distances.yaml"]["segments"]:
        if segment["display"]:
            for point in segment["points"]:
                distance_index[(segment["date"], point["target"])] = {
                    **point,
                    "origin_label": segment["origin"]["label"],
                    "distance_display": f'{point["distance_km"]:g}',
                }

    issues = []
    for raw in raw_issues:
        issue = dict(raw)
        issue["status_label"] = ISSUE_STATUS_LABELS[issue["status"]]
        issue["priority_label"] = ISSUE_PRIORITY_LABELS[issue["priority"]]
        issue["identified_at_display"] = short_date(issue["identified_at"])
        issue["related_date_display"] = " / ".join(short_date(value) for value in issue["related_dates"])
        issue["subject_names"] = [resolve_name(value, index) for value in issue["subjects"]]
        issue["anchor"] = issue["id"].replace(".", "-")
        issues.append(issue)

    days = []
    adopted: set[str] = set()
    for raw in data["plan/current.yaml"]["days"]:
        day = dict(raw)
        for field in ("routes", "visits", "optional_visits", "food"):
            adopted.update(day[field])
            prepared_items = []
            for item_id in day[field]:
                item = dict(index[item_id])
                if (day["date"], item_id) in distance_index:
                    item["distance"] = distance_index[(day["date"], item_id)]
                if (item_id, day["date"]) in windows:
                    item["availability_display"] = " / ".join(
                        f'{window["start"]}–{window["end"]}' for window in windows[(item_id, day["date"])]
                    )
                prepared_items.append(item)
            day[f"{field}_items"] = prepared_items
        adopted.update(day["transport"])
        adopted.update(day["stay"]["preferred"])
        adopted.update(day["stay"]["fallback"])
        day["transport_items"] = [prepare_transport(index[item_id], index) for item_id in day["transport"]]
        day["transport_alternative_items"] = [prepare_transport(index[item_id], index) for item_id in day["transport_alternatives"]]
        day["preferred_names"] = [index[item_id]["name"] for item_id in day["stay"]["preferred"]]
        day["fallback_names"] = [index[item_id]["name"] for item_id in day["stay"]["fallback"]]
        day["start_name"] = resolve_name(day["start"], index)
        day["finish_name"] = resolve_name(day["finish"], index)
        day["short_date"] = short_date(day["date"])
        day["dated_heading"] = dated_heading(day["date"])
        day["issue_items"] = [issue for issue in issues if day["date"] in issue["related_dates"] and issue["status"] in {"open", "in_progress"}]
        days.append(day)

    contingencies = []
    for raw in data["plan/current.yaml"]["contingencies"]:
        item = dict(raw)
        item["dated_heading"] = dated_heading(item["date"])
        item["transport_items"] = [prepare_transport(index[value], index) for value in item["transport"]]
        item["transport_alternative_items"] = [prepare_transport(index[value], index) for value in item["transport_alternatives"]]
        contingencies.append(item)

    open_issue_subjects = {subject for issue in raw_issues if issue["status"] in {"open", "in_progress"} for subject in issue["subjects"]}
    rechecks = [
        {"name": index[item["subject"]]["name"], "claims": item["claims"]}
        for item in evidence_items
        if item["recheck_before_trip"] and item["subject"] in adopted and item["subject"] not in open_issue_subjects
    ]

    lodging = data["research/lodging.yaml"]
    lodging_searches = []
    for raw in lodging["stay_searches"]:
        search = dict(raw)
        search["dated_heading"] = dated_heading(search["date"])
        search["preferred_area_name"] = resolve_name(search["preferred_area_ref"], index)
        search["fallback_area_names"] = [resolve_name(value, index) for value in search["fallback_area_refs"]]
        search["call_order_area_names"] = [resolve_name(value, index) for value in search["call_order_area_refs"]]
        lodging_searches.append(search)

    plan = data["plan/current.yaml"]
    user_actions = []
    for raw in data["user_actions.yaml"]["actions"]:
        item = dict(raw)
        item["related_names"] = [resolve_name(value, index) for value in item["related_subjects"]]
        item["deadline_display"] = short_date(item["deadline"]) + "まで" if item["deadline"] else "期限未設定（{}）".format(dict(USER_ACTION_TIMING_GROUPS)[item["timing"]])
        item["evidence_sources"] = [evidence_by_id[value]["source"] for value in item["evidence"]]
        user_actions.append(item)
    return {
        "trip": data["trip.yaml"],
        "days": days,
        "recommendations": plan["recommendations"],
        "contingencies": contingencies,
        "rechecks": rechecks,
        "open_issues": [item for item in issues if item["status"] in {"open", "in_progress"}],
        "closed_issues": [item for item in issues if item["status"] in {"resolved", "wont_fix"}],
        "lodging_traveler": lodging["traveler"],
        "lodging_policy": lodging["policy"],
        "lodging_searches": lodging_searches,
        "lodging_common_questions": lodging["common_phone_questions"],
        "lodging_explicit_web_unavailable": lodging["explicit_web_unavailable"],
        "user_actions": user_actions,
        "user_action_timing_groups": USER_ACTION_TIMING_GROUPS,
    }


def render_repository(root: Path) -> None:
    errors = validate_repository(root)
    if errors:
        raise ValueError("Cannot render invalid repository:\n" + "\n".join(errors))
    context = prepare_context(load_repository(root))
    environment = Environment(loader=FileSystemLoader(root / "templates"), undefined=StrictUndefined, autoescape=False, keep_trailing_newline=True, trim_blocks=False, lstrip_blocks=False)
    output_dir = root / "docs"
    output_dir.mkdir(exist_ok=True)
    for template_name, output_name in (
        ("itinerary.md.j2", "itinerary.md"),
        ("pins.md.j2", "pins.md"),
        ("issues.md.j2", "issues.md"),
        ("lodging-calls.md.j2", "lodging-calls.md"),
        ("user-actions.md.j2", "user-actions.md"),
    ):
        rendered = environment.get_template(template_name).render(**context)
        rendered = re.sub(r"\n{3,}", "\n\n", rendered).rstrip() + "\n"
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
    print("Rendered traveler documents.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
