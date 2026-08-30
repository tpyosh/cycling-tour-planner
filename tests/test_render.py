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
    issues_path = repo_copy / "docs/issues.md"
    itinerary_path.unlink(missing_ok=True)
    pins_path.unlink(missing_ok=True)
    issues_path.unlink(missing_ok=True)

    result = render(repo_copy)
    assert result.returncode == 0, result.stdout + result.stderr
    assert itinerary_path.exists()
    assert pins_path.exists()
    assert issues_path.exists()

    itinerary = itinerary_path.read_text(encoding="utf-8")
    pins = pins_path.read_text(encoding="utf-8")
    issues = issues_path.read_text(encoding="utf-8")
    assert "| 9/24 | 函館市街 → 鹿部 | 105–130 km | 鹿部 | 南茅部 / 森町 |" in itinerary
    assert "## 9/23（水）" in itinerary
    assert "シゲちゃんすし" in itinerary
    assert "# 出発前の再確認" in itinerary
    assert "水無海浜温泉 — **潮汐上の入浴可能候補時間: 05:00–11:00 / 19:00–22:00**" in itinerary
    assert "### 日程リスク" in itinerary
    assert "[9/24に水無海浜温泉の朝枠へ到着できるか未確認](issues.md#issue-mizunashi-arrival-window-20260924)" in itinerary
    assert "# 自然条件で利用時間が変わる立ち寄り先" not in itinerary
    assert "| 9/28 | 08:00–12:00 / 20:00–22:00 |" not in itinerary
    assert "函館市「2026年 水無海浜温泉入浴可能時間表」" not in itinerary
    assert "水無海浜温泉 — 2026年9月の函館市公式入浴可能時間表" not in itinerary
    assert "苫小牧→仙台 太平洋フェリー — 運航・予約状況" in itinerary
    assert "**予約番号:** N231" in itinerary
    assert "**船名・客室:** いしかり / Ｓ寝台（洋室）" in itinerary
    assert "**料金:** 15,000円（インターネット割引）" in itinerary
    assert "**変更期限:** 2026年09月26日 23:59まで" in itinerary
    assert "## 通常旅程（9/21出発）" in itinerary
    assert "県営名古屋空港（小牧／NKM） 08:25 → 青森空港（AOJ） 09:45" in itinerary
    assert "# 予備：9/21に出発できない場合" in itinerary
    assert "## 9/22（火） 名古屋 → むつ方面" in itinerary
    assert "9/22の「むつ→恐山→薬研→下風呂」は" in itinerary
    assert "# 旅行前TODO" in itinerary
    assert "`水無海浜温泉`" in pins
    assert "9/24に水無海浜温泉の朝枠へ到着できるか未確認" in issues
    assert '<a id="issue-mizunashi-arrival-window-20260924"></a>' in issues
    assert "`issue.mizunashi-arrival-window-20260924`" in issues
    assert "朝枠を使う場合" in issues


def test_render_is_deterministic(repo_copy: Path) -> None:
    first = render(repo_copy)
    assert first.returncode == 0, first.stdout + first.stderr
    before = {
        name: (repo_copy / "docs" / name).read_bytes()
        for name in ("itinerary.md", "pins.md", "issues.md")
    }
    second = render(repo_copy)
    assert second.returncode == 0, second.stdout + second.stderr
    after = {
        name: (repo_copy / "docs" / name).read_bytes()
        for name in ("itinerary.md", "pins.md", "issues.md")
    }
    assert before == after
