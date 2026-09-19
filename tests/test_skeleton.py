from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from ruamel.yaml import YAML


def run(root: Path, script: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(root / "tools" / script), "--root", str(root)], text=True, capture_output=True, check=False)


def test_empty_skeleton_validates(repo_copy: Path) -> None:
    result = run(repo_copy, "validate.py")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Validation passed." in result.stdout


def test_rendering_is_deterministic(repo_copy: Path) -> None:
    first = run(repo_copy, "render.py")
    assert first.returncode == 0, first.stdout + first.stderr
    paths = [repo_copy / "docs" / name for name in ("itinerary.md", "pins.md", "issues.md", "lodging-calls.md")]
    before = {path.name: path.read_bytes() for path in paths}
    second = run(repo_copy, "render.py")
    assert second.returncode == 0, second.stdout + second.stderr
    after = {path.name: path.read_bytes() for path in paths}
    assert before == after
    assert "# " in (repo_copy / "docs" / "itinerary.md").read_text(encoding="utf-8")
    assert "宿泊調査は未着手" in (repo_copy / "docs" / "lodging-calls.md").read_text(encoding="utf-8")


def test_unknown_plan_reference_fails(repo_copy: Path) -> None:
    yaml = YAML()
    trip_path = repo_copy / "trip.yaml"
    with trip_path.open(encoding="utf-8") as stream:
        trip = yaml.load(stream)
    trip["start_date"] = "2030-01-01"
    trip["end_date"] = "2030-01-01"
    trip["origin"] = "出発地"
    with trip_path.open("w", encoding="utf-8") as stream:
        yaml.dump(trip, stream)

    plan_path = repo_copy / "plan" / "current.yaml"
    with plan_path.open(encoding="utf-8") as stream:
        plan = yaml.load(stream)
    plan["days"] = [{
        "date": "2030-01-01",
        "start": "出発地",
        "finish": "到着地",
        "cycling": {"distance_km": {"min": 0, "max": 0}},
        "routes": [],
        "transport": [],
        "transport_alternatives": [],
        "visits": ["place.missing"],
        "optional_visits": [],
        "food": [],
        "stay": {"preferred": [], "fallback": []},
        "notes": [],
    }]
    with plan_path.open("w", encoding="utf-8") as stream:
        yaml.dump(plan, stream)

    result = run(repo_copy, "validate.py")
    assert result.returncode == 1
    assert "unknown id: place.missing" in result.stdout
