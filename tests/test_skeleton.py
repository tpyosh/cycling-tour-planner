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


def test_chatgpt_research_bridges_are_not_tracked(repo_copy: Path) -> None:
    result = subprocess.run(
        [sys.executable, str(repo_copy / "tools" / "chatgpt_research.py"), "--root", str(repo_copy), "audit"],
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "audit passed" in result.stdout

    forbidden = repo_copy / "prompts" / "new-chatgpt-request.md"
    forbidden.write_text("temporary bridge", encoding="utf-8")
    result = subprocess.run(
        [sys.executable, str(repo_copy / "tools" / "chatgpt_research.py"), "--root", str(repo_copy), "audit"],
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 1
    assert "forbidden" in result.stdout

    disguised = repo_copy / "research" / "notes.md"
    disguised.write_text("あなたは、調査者です。\nWebを調査し、根拠を示してください。\n## 0. Preflight\n", encoding="utf-8")
    result = subprocess.run(
        [sys.executable, str(repo_copy / "tools" / "chatgpt_research.py"), "--root", str(repo_copy), "audit"],
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 1
    assert "possible direct ChatGPT research prompt" in result.stdout


def test_chatgpt_research_preflight_rejects_tracked_path(repo_copy: Path) -> None:
    result = subprocess.run(
        [
            sys.executable,
            str(repo_copy / "tools" / "chatgpt_research.py"),
            "--root",
            str(repo_copy),
            "preflight",
            "prompts/new-chatgpt-request.md",
        ],
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 1
    assert "must be below" in result.stdout


def test_chatgpt_research_request_lifecycle(repo_copy: Path) -> None:
    tool = repo_copy / "tools" / "chatgpt_research.py"
    base = [sys.executable, str(tool), "--root", str(repo_copy)]
    request_id = "test-research-bridge"

    result = subprocess.run([*base, "init", request_id], text=True, capture_output=True, check=False)
    assert result.returncode == 0, result.stdout + result.stderr
    prompt = repo_copy / ".codex" / "local" / "chatgpt-research" / request_id / "prompt.md"

    result = subprocess.run([*base, "preflight", str(prompt)], text=True, capture_output=True, check=False)
    assert result.returncode == 0, result.stdout + result.stderr

    result = subprocess.run([*base, "gc", request_id], text=True, capture_output=True, check=False)
    assert result.returncode == 0, result.stdout + result.stderr
    assert not prompt.parent.exists()


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
