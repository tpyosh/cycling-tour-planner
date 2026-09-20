#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


TEXT_ASSET_SUFFIXES = {".md", ".yaml", ".yml", ".j2", ".toml"}
EXCLUDED_DIRECTORIES = {".git", ".venv", ".pytest_cache", "__pycache__"}

# 自走・輪行の個別行為を別の語で表さないための検出パターン。文字列は
# Unicode escape にして、このチェック自体を検索結果へ混ぜない。
FORBIDDEN_PATTERNS = {
    "self_riding": re.compile(r"\u8d70\u884c|\u5b9f\u8d70|\u81ea\u529b\u79fb\u52d5|\u81ea\u8ee2\u8eca\u79fb\u52d5|\u81ea\u8ee2\u8eca\u51fa\u767a|\u81ea\u8ee2\u8eca\u30eb\u30fc\u30c8|\u81ea\u8ee2\u8eca\u533a\u9593"),
    "bike_transport": re.compile(r"\u81ea\u8ee2\u8eca\u8fbc\u307f|\u81ea\u8ee2\u8eca\u904b\u8cc3"),
}


def check_terminology(root: Path) -> list[str]:
    errors: list[str] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix not in TEXT_ASSET_SUFFIXES:
            continue
        if any(part in EXCLUDED_DIRECTORIES for part in path.relative_to(root).parts):
            continue
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            for label, pattern in FORBIDDEN_PATTERNS.items():
                if pattern.search(line):
                    errors.append(f"ERROR {path.relative_to(root)}:{line_number}: use the approved {label} terminology")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Check approved self-riding and bike-transport terminology")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = check_terminology(args.root.resolve())
    if errors:
        print("\n".join(errors))
        return 1
    print("Terminology validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
