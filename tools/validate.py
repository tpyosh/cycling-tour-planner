#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker
from ruamel.yaml.error import YAMLError

from lib.data import CATALOG_FILES, DATA_SCHEMAS, build_index, load_repository


REFERENCE_FIELDS = {
    "routes": "route.",
    "transport": "transport.",
    "transport_alternatives": "transport.",
    "visits": "place.",
    "optional_visits": "place.",
    "food": "food.",
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


def _day_references(day: dict[str, Any]) -> list[tuple[str, str]]:
    refs = [(field, ref) for field in REFERENCE_FIELDS for ref in day[field]]
    refs.extend(("stay.preferred", ref) for ref in day["stay"]["preferred"])
    refs.extend(("stay.fallback", ref) for ref in day["stay"]["fallback"])
    for field in ("start", "finish"):
        if day[field].startswith(KNOWN_PREFIXES):
            refs.append((field, day[field]))
    return refs


def _validate_catalog(data: dict[str, dict[str, Any]]) -> tuple[list[str], dict[str, dict[str, Any]]]:
    errors: list[str] = []
    items = [item for relative in CATALOG_FILES for item in data[relative]["items"]]
    seen: set[str] = set()
    for item in items:
        item_id = item["id"]
        if item_id in seen:
            errors.append(f"ERROR catalog: duplicate id: {item_id}")
        seen.add(item_id)
        margin = item.get("visit_constraints", {}).get("arrival_margin_minutes", {})
        if margin and margin["min"] > margin["max"]:
            errors.append(f"ERROR catalog: arrival margin min exceeds max: {item_id}")
    return errors, build_index(data)


def validate_repository(root: Path) -> list[str]:
    try:
        data = load_repository(root)
    except (OSError, ValueError, YAMLError) as exc:
        return [f"ERROR {exc}"]

    errors = _schema_errors(root, data)
    if errors:
        return errors

    catalog_errors, index = _validate_catalog(data)
    errors.extend(catalog_errors)

    evidence_ids: set[str] = set()
    for evidence in data["evidence/sources.yaml"]["items"]:
        evidence_id = evidence["id"]
        if evidence_id in evidence_ids:
            errors.append(f"ERROR evidence/sources.yaml: duplicate id: {evidence_id}")
        evidence_ids.add(evidence_id)
        if evidence["subject"] not in index:
            errors.append(f"ERROR evidence/sources.yaml {evidence_id}: unknown subject id: {evidence['subject']}")
        dates = [item["date"] for item in evidence.get("date_windows", [])]
        if dates != sorted(dates) or len(dates) != len(set(dates)):
            errors.append(f"ERROR evidence/sources.yaml {evidence_id}: date_windows must be unique and ascending")
        for dated in evidence.get("date_windows", []):
            previous_end: str | None = None
            for window in dated["windows"]:
                if window["start"] >= window["end"]:
                    errors.append(f"ERROR evidence/sources.yaml {evidence_id} {dated['date']}: window start must be before end")
                if previous_end and window["start"] < previous_end:
                    errors.append(f"ERROR evidence/sources.yaml {evidence_id} {dated['date']}: windows must be ascending and non-overlapping")
                previous_end = window["end"]

    issue_ids: set[str] = set()
    for issue in data["issues.yaml"]["items"]:
        issue_id = issue["id"]
        if issue_id in issue_ids:
            errors.append(f"ERROR issues.yaml: duplicate id: {issue_id}")
        issue_ids.add(issue_id)
        for subject in issue["subjects"]:
            if subject not in index:
                errors.append(f"ERROR issues.yaml {issue_id}: unknown subject id: {subject}")
        for evidence_id in issue["evidence"]:
            if evidence_id not in evidence_ids:
                errors.append(f"ERROR issues.yaml {issue_id}: unknown evidence id: {evidence_id}")
        for dependency_id in issue.get("dependencies", []):
            if dependency_id == issue_id:
                errors.append(f"ERROR issues.yaml {issue_id}: issue cannot depend on itself")
            elif dependency_id not in issue_ids and dependency_id not in {item["id"] for item in data["issues.yaml"]["items"]}:
                errors.append(f"ERROR issues.yaml {issue_id}: unknown dependency id: {dependency_id}")
        if issue["status"] in {"resolved", "wont_fix"} and not issue["resolution"]:
            errors.append(f"ERROR issues.yaml {issue_id}: closed issue requires resolution")
        if issue["status"] in {"open", "in_progress"} and issue["resolution"]:
            errors.append(f"ERROR issues.yaml {issue_id}: open issue must not have resolution")

    trip = data["trip.yaml"]
    plan = data["plan/current.yaml"]
    days = plan["days"]
    if (trip["start_date"] is None) != (trip["end_date"] is None):
        errors.append("ERROR trip.yaml: start_date and end_date must both be set or both be null")
    if trip["start_date"] and trip["start_date"] > trip["end_date"]:
        errors.append("ERROR trip.yaml: start_date must not be after end_date")
    if days and not trip["start_date"]:
        errors.append("ERROR trip.yaml: dates are required when plan/current.yaml contains days")

    day_dates = [day["date"] for day in days]
    if day_dates != sorted(day_dates) or len(day_dates) != len(set(day_dates)):
        errors.append("ERROR plan/current.yaml: day dates must be unique and ascending")
    for day_index, day in enumerate(days):
        day_date = day["date"]
        distance = day["self_riding"]["distance_km"]
        if distance["min"] > distance["max"]:
            errors.append(f"ERROR plan/current.yaml day {day_date}: distance min exceeds max")
        if trip["start_date"] and not (trip["start_date"] <= day_date <= trip["end_date"]):
            errors.append(f"ERROR plan/current.yaml day {day_date}: date outside trip range")
        for field, ref in _day_references(day):
            expected = "stay." if field.startswith("stay.") else REFERENCE_FIELDS.get(field)
            if expected and not ref.startswith(expected):
                errors.append(f"ERROR plan/current.yaml day {day_date}: invalid id prefix in {field}: {ref}")
            if ref not in index:
                errors.append(f"ERROR plan/current.yaml day {day_date}: unknown id: {ref}")
            elif index[ref].get("status") in {"deferred", "rejected"}:
                errors.append(f"ERROR plan/current.yaml day {day_date}: references {index[ref]['status']} candidate: {ref}")
        for field in REFERENCE_FIELDS:
            if len(day[field]) != len(set(day[field])):
                errors.append(f"ERROR plan/current.yaml day {day_date}: duplicate reference in {field}")
        if day_index < len(days) - 1 and not day["stay"]["preferred"]:
            errors.append(f"ERROR plan/current.yaml day {day_date}: overnight stay is required")
        if day_index < len(days) - 1 and day["finish"] != days[day_index + 1]["start"]:
            errors.append(f"ERROR plan/current.yaml day {day_date}: finish does not match the next day start")

    for contingency in plan["contingencies"]:
        refs = contingency["transport"] + contingency["transport_alternatives"]
        for ref in refs:
            if ref not in index:
                errors.append(f"ERROR plan/current.yaml {contingency['id']}: unknown transport id: {ref}")

    days_by_date = {day["date"]: day for day in days}
    segment_ids: set[str] = set()
    displayed_targets: set[tuple[str, str]] = set()
    for segment in data["estimates/distances.yaml"]["segments"]:
        segment_id = segment["id"]
        if segment_id in segment_ids:
            errors.append(f"ERROR estimates/distances.yaml: duplicate segment id: {segment_id}")
        segment_ids.add(segment_id)
        day = days_by_date.get(segment["date"])
        if not day:
            errors.append(f"ERROR estimates/distances.yaml {segment_id}: date is not in current plan")
            allowed_targets: set[str] = set()
        else:
            allowed_targets = set(day["visits"] + day["optional_visits"] + day["food"])
        origin_ref = segment["origin"].get("ref")
        if origin_ref and origin_ref not in index:
            errors.append(f"ERROR estimates/distances.yaml {segment_id}: unknown origin ref: {origin_ref}")
        previous_distance: int | float | None = None
        for point in segment["points"]:
            if point["target"] not in allowed_targets:
                errors.append(f"ERROR estimates/distances.yaml {segment_id}: target is not used on that day: {point['target']}")
            if previous_distance is not None and point["distance_km"] < previous_distance:
                errors.append(f"ERROR estimates/distances.yaml {segment_id}: cumulative distances must not decrease")
            previous_distance = point["distance_km"]
            if segment["display"]:
                key = (segment["date"], point["target"])
                if key in displayed_targets:
                    errors.append(f"ERROR estimates/distances.yaml: multiple displayed distances for {segment['date']} {point['target']}")
                displayed_targets.add(key)

    for item in index.values():
        if item["id"].startswith("transport.") and item.get("departure") and item.get("arrival"):
            if datetime.fromisoformat(item["departure"]) >= datetime.fromisoformat(item["arrival"]):
                errors.append(f"ERROR catalog/transport.yaml {item['id']}: departure must be before arrival")

    lodging = data["research/lodging.yaml"]
    candidate_keys: set[str] = set()
    for search in lodging["stay_searches"]:
        day = days_by_date.get(search["date"])
        if day:
            if search["preferred_area_ref"] not in day["stay"]["preferred"]:
                errors.append(f"ERROR research/lodging.yaml {search['date']}: preferred area differs from current plan")
            if search["fallback_area_refs"] != day["stay"]["fallback"]:
                errors.append(f"ERROR research/lodging.yaml {search['date']}: fallback areas differ from current plan")
        allowed_areas = {search["preferred_area_ref"], *search["fallback_area_refs"]}
        priorities: list[int] = []
        for candidate in search["candidates"]:
            key = candidate["candidate_key"]
            if key in candidate_keys:
                errors.append(f"ERROR research/lodging.yaml: duplicate candidate key: {key}")
            candidate_keys.add(key)
            if candidate["area_ref"] not in allowed_areas:
                errors.append(f"ERROR research/lodging.yaml {key}: area is outside preferred/fallback areas")
            if candidate["area_ref"] not in index:
                errors.append(f"ERROR research/lodging.yaml {key}: unknown area id: {candidate['area_ref']}")
            priorities.append(candidate["phone_check"]["priority"])
            result = candidate["phone_check"]["result"]
            if candidate["phone_check"]["status"] == "pending" and (
                candidate["status"] != "availability_unknown"
                or result["availability"] is not None
                or result["called_at"] is not None
            ):
                errors.append(f"ERROR research/lodging.yaml {key}: pending check claims a result")
        if priorities != list(range(1, len(priorities) + 1)):
            errors.append(f"ERROR research/lodging.yaml {search['date']}: priorities must be consecutive")
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
