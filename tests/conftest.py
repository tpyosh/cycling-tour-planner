from __future__ import annotations

import shutil
from pathlib import Path

import pytest


@pytest.fixture
def repo_copy(tmp_path: Path) -> Path:
    source = Path(__file__).resolve().parents[1]
    target = tmp_path / "repo"
    shutil.copytree(
        source,
        target,
        ignore=shutil.ignore_patterns(".git", ".venv", ".pytest_cache", "__pycache__", "*.pyc"),
    )
    return target
