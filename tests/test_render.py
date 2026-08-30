from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def render(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(root / "tools/render.py"), "--root", str(root)],
        text=True,
        capture_output=True,
        check=False,
    )


def test_rendered_documents_contain_expected_content(repo_copy: Path) -> None:
    itinerary_path = repo_copy / "docs/itinerary.md"
    pins_path = repo_copy / "docs/pins.md"
    itinerary_path.unlink(missing_ok=True)
    pins_path.unlink(missing_ok=True)

    result = render(repo_copy)
    assert result.returncode == 0, result.stdout + result.stderr
    assert itinerary_path.exists()
    assert pins_path.exists()

    itinerary = itinerary_path.read_text(encoding="utf-8")
    pins = pins_path.read_text(encoding="utf-8")
    assert "| 9/24 | 函館市街 → 鹿部 | 105–130 km | 鹿部 | 南茅部 / 森町 |" in itinerary
    assert "## 9/23（水）" in itinerary
    assert "シゲちゃんすし" in itinerary
    assert "# 出発前の再確認" in itinerary
    assert "苫小牧→仙台 太平洋フェリー — 運航・予約状況" in itinerary
    assert "`水無海浜温泉`" in pins


def test_render_is_deterministic(repo_copy: Path) -> None:
    first = render(repo_copy)
    assert first.returncode == 0, first.stdout + first.stderr
    before = {
        name: (repo_copy / "docs" / name).read_bytes()
        for name in ("itinerary.md", "pins.md")
    }
    second = render(repo_copy)
    assert second.returncode == 0, second.stdout + second.stderr
    after = {
        name: (repo_copy / "docs" / name).read_bytes()
        for name in ("itinerary.md", "pins.md")
    }
    assert before == after
