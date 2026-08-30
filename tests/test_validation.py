from __future__ import annotations

import copy
import subprocess
import sys
from pathlib import Path

from ruamel.yaml import YAML


def load(path: Path) -> dict:
    yaml = YAML()
    yaml.preserve_quotes = True
    with path.open(encoding="utf-8") as stream:
        return yaml.load(stream)


def save(path: Path, data: dict) -> None:
    yaml = YAML()
    with path.open("w", encoding="utf-8") as stream:
        yaml.dump(data, stream)


def validate(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(root / "tools/validate.py"), "--root", str(root)],
        text=True,
        capture_output=True,
        check=False,
    )


def test_valid_repository_passes(repo_copy: Path) -> None:
    result = validate(repo_copy)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Validation passed." in result.stdout


def test_unknown_id_fails(repo_copy: Path) -> None:
    path = repo_copy / "plan/current.yaml"
    data = load(path)
    data["days"][3]["visits"].append("place.unknown")
    save(path, data)
    result = validate(repo_copy)
    assert result.returncode == 1
    assert "unknown place id: place.unknown" in result.stdout


def test_duplicate_id_fails(repo_copy: Path) -> None:
    path = repo_copy / "catalog/places.yaml"
    data = load(path)
    item = next(item for item in data["items"] if item["id"] == "place.osorezan")
    data["items"].append(copy.deepcopy(item))
    save(path, data)
    result = validate(repo_copy)
    assert result.returncode == 1
    assert "duplicate id: place.osorezan" in result.stdout


def test_adopted_status_fails(repo_copy: Path) -> None:
    path = repo_copy / "catalog/places.yaml"
    data = load(path)
    data["items"][0]["status"] = "adopted"
    save(path, data)
    result = validate(repo_copy)
    assert result.returncode == 1
    assert "forbidden status adopted" in result.stdout


def test_rejected_reference_fails(repo_copy: Path) -> None:
    path = repo_copy / "catalog/places.yaml"
    data = load(path)
    item = next(item for item in data["items"] if item["id"] == "place.osorezan")
    item["status"] = "rejected"
    save(path, data)
    result = validate(repo_copy)
    assert result.returncode == 1
    assert "references rejected candidate: place.osorezan" in result.stdout


def test_invalid_distance_fails(repo_copy: Path) -> None:
    path = repo_copy / "plan/current.yaml"
    data = load(path)
    data["days"][0]["cycling"]["distance_km"] = {"min": 11, "max": 10}
    save(path, data)
    result = validate(repo_copy)
    assert result.returncode == 1
    assert "cycling distance min exceeds max" in result.stdout


def test_end_date_overrun_fails(repo_copy: Path) -> None:
    path = repo_copy / "plan/current.yaml"
    data = load(path)
    data["days"][-1]["date"] = "2026-09-29"
    save(path, data)
    result = validate(repo_copy)
    assert result.returncode == 1
    assert "date outside trip range" in result.stdout


def test_required_return_ferry_fails(repo_copy: Path) -> None:
    path = repo_copy / "plan/current.yaml"
    data = load(path)
    data["days"][6]["transport"] = []
    save(path, data)
    result = validate(repo_copy)
    assert result.returncode == 1
    assert "required 2026-09-27 Tomakomai-Sendai ferry is missing" in result.stdout
