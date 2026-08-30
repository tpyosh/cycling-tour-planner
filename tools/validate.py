#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker
from ruamel.yaml.error import YAMLError

from lib.data import CATALOG_FILES, DATA_SCHEMAS, build_index, load_repository


REFERENCE_FIELDS = {
    "routes": "route.", "transport": "transport.", "transport_alternatives": "transport.", "visits": "place.",
    "optional_visits": "place.", "food": "food.",
}
KNOWN_PREFIXES = ("place.", "route.", "stay.", "food.", "transport.")


def _schema_errors(root: Path, data: dict[str, dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    checker = FormatChecker()
    for relative, schema_name in DATA_SCHEMAS.items():
        with (root / "schema" / schema_name).open(encoding="utf-8") as stream:
            schema = json.load(stream)
        validator = Draft202012Validator(schema, format_checker=checker)
        for error in sorted(validator.iter_errors(data[relative]), key=lambda item: list(item.path)):
            location = ".".join(str(part) for part in error.path) or "root"
            errors.append(f"ERROR {relative} {location}: {error.message}")
    return errors


def _all_day_references(day: dict[str, Any]) -> list[tuple[str, str]]:
    refs = [(field, ref) for field in REFERENCE_FIELDS for ref in day[field]]
    refs.extend(("stay.preferred", ref) for ref in day["stay"]["preferred"])
    refs.extend(("stay.fallback", ref) for ref in day["stay"]["fallback"])
    for field in ("start", "finish"):
        value = day[field]
        if value.startswith(KNOWN_PREFIXES):
            refs.append((field, value))
    return refs


def validate_repository(root: Path) -> list[str]:
    try:
        data = load_repository(root)
    except (OSError, ValueError, YAMLError) as exc:
        return [f"ERROR {exc}"]
    errors = _schema_errors(root, data)

    catalog_items = [item for relative in CATALOG_FILES for item in data[relative].get("items", [])]
    seen: set[str] = set()
    duplicates: set[str] = set()
    for item in catalog_items:
        item_id = item.get("id")
        if item_id in seen:
            duplicates.add(item_id)
        seen.add(item_id)
        if item.get("status") == "adopted":
            errors.append(f"ERROR catalog: forbidden status adopted: {item_id}")
    for item_id in sorted(duplicates):
        errors.append(f"ERROR catalog: duplicate id: {item_id}")

    index = build_index(data) if not duplicates else {item["id"]: item for item in catalog_items}
    for evidence in data["evidence/sources.yaml"].get("items", []):
        subject = evidence.get("subject")
        if subject not in index:
            errors.append(f"ERROR evidence/sources.yaml {evidence.get('id')}: unknown subject id: {subject}")

    trip = data["trip.yaml"]
    plan = data["plan/current.yaml"]
    days = plan.get("days", [])
    parsed_dates: list[date] = []
    for day in days:
        day_date = day.get("date", "unknown")
        try:
            parsed = date.fromisoformat(day_date)
            parsed_dates.append(parsed)
        except (TypeError, ValueError):
            continue
        distance = day.get("cycling", {}).get("distance_km", {})
        if isinstance(distance, dict) and distance.get("min", 0) > distance.get("max", 0):
            errors.append(f"ERROR plan/current.yaml day {day_date}: cycling distance min exceeds max")
        for field, ref in _all_day_references(day):
            expected = "stay." if field.startswith("stay.") else REFERENCE_FIELDS.get(field)
            if expected and not ref.startswith(expected):
                errors.append(f"ERROR plan/current.yaml day {day_date}: invalid id prefix in {field}: {ref}")
            if ref not in index:
                errors.append(f"ERROR plan/current.yaml day {day_date}: unknown {ref.split('.', 1)[0]} id: {ref}")
            elif index[ref].get("status") in {"deferred", "rejected"}:
                errors.append(f"ERROR plan/current.yaml day {day_date}: references {index[ref]['status']} candidate: {ref}")
        for field in REFERENCE_FIELDS:
            refs = day.get(field, [])
            if len(refs) != len(set(refs)):
                errors.append(f"ERROR plan/current.yaml day {day_date}: duplicate reference in {field}")
        for label, refs in (
            ("visits/optional_visits", day.get("visits", []) + day.get("optional_visits", [])),
            ("transport/transport_alternatives", day.get("transport", []) + day.get("transport_alternatives", [])),
            ("stay preferred/fallback", day.get("stay", {}).get("preferred", []) + day.get("stay", {}).get("fallback", [])),
        ):
            if len(refs) != len(set(refs)):
                errors.append(f"ERROR plan/current.yaml day {day_date}: duplicate reference across {label}")

    for contingency in plan.get("contingencies", []):
        contingency_id = contingency.get("id", "unknown")
        refs = contingency.get("transport", []) + contingency.get("transport_alternatives", [])
        for ref in refs:
            if ref not in index:
                errors.append(f"ERROR plan/current.yaml {contingency_id}: unknown transport id: {ref}")
            elif index[ref].get("status") in {"deferred", "rejected"}:
                errors.append(
                    f"ERROR plan/current.yaml {contingency_id}: references "
                    f"{index[ref]['status']} candidate: {ref}"
                )
        if len(refs) != len(set(refs)):
            errors.append(f"ERROR plan/current.yaml {contingency_id}: duplicate transport reference")

    if parsed_dates != sorted(parsed_dates) or len(parsed_dates) != len(set(parsed_dates)):
        errors.append("ERROR plan/current.yaml: day dates must be unique and ascending")
    if parsed_dates:
        start = date.fromisoformat(trip["start_date"])
        end = date.fromisoformat(trip["end_date"])
        for parsed in parsed_dates:
            if parsed < start or parsed > end:
                errors.append(f"ERROR plan/current.yaml day {parsed.isoformat()}: date outside trip range")
        if parsed_dates[-1] > end or parsed_dates[-1] > date(2026, 9, 28):
            errors.append("ERROR plan/current.yaml: itinerary ends after 2026-09-28")
    for day in days[:-1]:
        if not day.get("stay", {}).get("preferred"):
            errors.append(f"ERROR plan/current.yaml day {day.get('date')}: overnight stay is required")

    ferry_present = any(
        day.get("date") == "2026-09-27" and "transport.tomakomai-sendai-ferry" in day.get("transport", [])
        for day in days
    )
    if not ferry_present:
        errors.append("ERROR plan/current.yaml: required 2026-09-27 Tomakomai-Sendai ferry is missing")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate trip repository data")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate_repository(args.root.resolve())
    if errors:
        print("\n".join(errors))
        return 1
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
