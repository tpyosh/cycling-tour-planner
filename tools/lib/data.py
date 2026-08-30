from __future__ import annotations

from datetime import date, datetime
from pathlib import Path
from typing import Any

from ruamel.yaml import YAML


DATA_SCHEMAS = {
    "trip.yaml": "trip.schema.json",
    "constraints.yaml": "constraints.schema.json",
    "catalog/places.yaml": "places.schema.json",
    "catalog/routes.yaml": "routes.schema.json",
    "catalog/stay_areas.yaml": "stay_areas.schema.json",
    "catalog/food.yaml": "food.schema.json",
    "catalog/transport.yaml": "transport.schema.json",
    "evidence/sources.yaml": "evidence.schema.json",
    "issues.yaml": "issues.schema.json",
    "plan/current.yaml": "itinerary.schema.json",
    "estimates/distances.yaml": "distances.schema.json",
}

CATALOG_FILES = [
    "catalog/places.yaml",
    "catalog/routes.yaml",
    "catalog/stay_areas.yaml",
    "catalog/food.yaml",
    "catalog/transport.yaml",
]


def repository_root(script_file: str) -> Path:
    return Path(script_file).resolve().parents[2]


def _json_compatible(value: Any) -> Any:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: _json_compatible(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_json_compatible(item) for item in value]
    return value


def load_yaml(path: Path) -> dict[str, Any]:
    yaml = YAML(typ="safe")
    with path.open(encoding="utf-8") as stream:
        data = yaml.load(stream)
    if not isinstance(data, dict):
        raise ValueError(f"{path}: top-level YAML value must be a mapping")
    return _json_compatible(data)


def load_repository(root: Path) -> dict[str, dict[str, Any]]:
    return {relative: load_yaml(root / relative) for relative in DATA_SCHEMAS}


def build_index(data: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {
        item["id"]: item
        for relative in CATALOG_FILES
        for item in data[relative]["items"]
    }
