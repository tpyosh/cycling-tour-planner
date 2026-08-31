from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from ruamel.yaml import YAML


def run(root: Path, script: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(root / "tools" / script), "--root", str(root)],
        text=True,
        capture_output=True,
        check=False,
    )


def test_lodging_research_validates_and_renders(repo_copy: Path) -> None:
    validation = run(repo_copy, "validate.py")
    assert validation.returncode == 0, validation.stdout + validation.stderr

    output = repo_copy / "docs" / "lodging-calls.md"
    output.unlink(missing_ok=True)
    rendering = run(repo_copy, "render.py")
    assert rendering.returncode == 0, rendering.stdout + rendering.stderr
    text = output.read_text(encoding="utf-8")

    assert "ホテルニュー下風呂" in text
    assert "0175-36-2021" in text
    assert "鹿部 → 森町 → 南茅部" in text
    assert "温泉旅館 吉の湯" in text
    assert "Web満室として電話対象から除外する宿" in text
    assert "明示的なWeb満室を記録した宿泊候補はありません" in text


def test_pending_phone_checks_do_not_claim_availability(repo_copy: Path) -> None:
    yaml = YAML(typ="safe")
    with (repo_copy / "research" / "lodging.yaml").open(encoding="utf-8") as stream:
        data = yaml.load(stream)

    candidates = [
        candidate
        for search in data["stay_searches"]
        for candidate in search["candidates"]
    ]
    assert candidates
    assert all(candidate["status"] == "availability_unknown" for candidate in candidates)
    assert all(candidate["phone_check"]["status"] == "pending" for candidate in candidates)
    assert all(candidate["phone_check"]["result"]["availability"] is None for candidate in candidates)
