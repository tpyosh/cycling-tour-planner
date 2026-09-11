from __future__ import annotations

import subprocess
import sys
from pathlib import Path

def run(root: Path, script: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(root / "tools" / script), "--root", str(root)], text=True, capture_output=True, check=False)


def test_repository_validates(repo_copy: Path) -> None:
    result = run(repo_copy, "validate.py")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Validation passed." in result.stdout


def test_repository_renders_deterministically(repo_copy: Path) -> None:
    first = run(repo_copy, "render.py")
    assert first.returncode == 0, first.stdout + first.stderr
    paths = [repo_copy / "docs" / name for name in ("itinerary.md", "pins.md", "issues.md", "lodging-calls.md")]
    before = {path.name: path.read_bytes() for path in paths}
    second = run(repo_copy, "render.py")
    assert second.returncode == 0, second.stdout + second.stderr
    after = {path.name: path.read_bytes() for path in paths}
    assert before == after
    itinerary = (repo_copy / "docs" / "itinerary.md").read_text(encoding="utf-8")
    lodging = (repo_copy / "docs" / "lodging-calls.md").read_text(encoding="utf-8")
    principles = (repo_copy / "PRINCIPLES.md").read_text(encoding="utf-8")
    assert "2026年9月 三陸旅行" in itinerary
    assert "石巻 → 女川" in itinerary
    assert "各日の昼食・夕食は独立した一食として評価" in principles
    assert "## 設計原則" not in itinerary
    assert "認識した上で除外" in itinerary
    assert "女川港" in itinerary
    assert "鮪立集落・唐桑御殿型住宅" in itinerary
    assert "9/23（水） チェックイン" in lodging


def test_unknown_plan_reference_fails(repo_copy: Path) -> None:
    plan_path = repo_copy / "plan" / "current.yaml"
    plan = plan_path.read_text(encoding="utf-8")
    plan_path.write_text(plan.replace("place.kadonowaki-school", "place.missing", 1), encoding="utf-8")

    result = run(repo_copy, "validate.py")
    assert result.returncode == 1
    assert "unknown id: place.missing" in result.stdout


def test_unknown_candidate_decision_reference_fails(repo_copy: Path) -> None:
    plan_path = repo_copy / "plan" / "current.yaml"
    plan = plan_path.read_text(encoding="utf-8")
    plan_path.write_text(plan.replace("place.onagawa-port, decision", "place.missing, decision", 1), encoding="utf-8")

    result = run(repo_copy, "validate.py")
    assert result.returncode == 1
    assert "unknown candidate decision id: place.missing" in result.stdout


def test_candidate_decision_cannot_overlap_active_reference(repo_copy: Path) -> None:
    plan_path = repo_copy / "plan" / "current.yaml"
    plan = plan_path.read_text(encoding="utf-8")
    plan_path.write_text(plan.replace("place.onagawa-port, decision", "place.onmaeya, decision", 1), encoding="utf-8")

    result = run(repo_copy, "validate.py")
    assert result.returncode == 1
    assert "candidate decision overlaps active reference: place.onmaeya" in result.stdout
