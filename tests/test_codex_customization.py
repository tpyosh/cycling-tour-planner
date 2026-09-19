from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def run_check(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(root / "tools" / "check_codex_customization.py"), "--root", str(root)],
        text=True,
        capture_output=True,
        check=False,
    )


def test_codex_customization_is_valid(repo_copy: Path) -> None:
    result = run_check(repo_copy)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Codex customization validation passed." in result.stdout


def test_legacy_skill_location_is_rejected(repo_copy: Path) -> None:
    legacy = repo_copy / ".codex" / "skills" / "legacy"
    legacy.mkdir(parents=True)
    (legacy / "SKILL.md").write_text("---\nname: legacy\ndescription: legacy\n---\n", encoding="utf-8")

    result = run_check(repo_copy)
    assert result.returncode == 1
    assert "legacy repository skill location" in result.stdout


def test_trip_specific_date_in_foundation_is_rejected(repo_copy: Path) -> None:
    path = repo_copy / ".agents" / "skills" / "cycling-trip-research" / "references" / "evidence-and-risk.md"
    path.write_text(path.read_text(encoding="utf-8") + "\n対象日: 2030-01-02\n", encoding="utf-8")

    result = run_check(repo_copy)
    assert result.returncode == 1
    assert "trip-specific ISO date" in result.stdout
