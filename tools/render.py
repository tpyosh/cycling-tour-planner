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
    prepared["departure_time"] = (
        datetime.fromisoformat(item["departure"]).strftime("%H:%M") if item["departure"] else None
    )
    prepared["arrival_time"] = (
        datetime.fromisoformat(item["arrival"]).strftime("%H:%M") if item["arrival"] else None
    )
    return prepared


def prepare_context(data: dict[str, dict[str, Any]]) -> dict[str, Any]:
    index = build_index(data)
    plan = data["plan/current.yaml"]
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
        adopted.update(day["stay"]["preferred"])
        adopted.update(day["stay"]["fallback"])
        preferred = [index[item_id] for item_id in day["stay"]["preferred"]]
        fallback = [index[item_id] for item_id in day["stay"]["fallback"]]
        day["preferred_names"] = [item["name"] for item in preferred]
        day["fallback_names"] = [item["name"] for item in fallback]
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
    for evidence in data["evidence/sources.yaml"]["items"]:
        if evidence["recheck_before_trip"] and evidence["subject"] in adopted:
            rechecks.append({"name": index[evidence["subject"]]["name"], "claims": evidence["claims"]})
    return {
        "trip": data["trip.yaml"],
        "days": days,
        "recommendations": plan["recommendations"],
        "pre_trip_todos": plan["pre_trip_todos"],
        "contingencies": contingencies,
        "rechecks": rechecks,
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
    print("Rendered docs/itinerary.md and docs/pins.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
