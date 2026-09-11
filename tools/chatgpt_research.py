#!/usr/bin/env python3
"""Enforce the lifecycle boundary for disposable ChatGPT research bridges."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path


REQUEST_ID = re.compile(r"^[a-z0-9][a-z0-9-]*$")
DIRECT_PROMPT_SIGNALS = ("あなたは、", "Webを調査し、", "## 0. Preflight")


def bridge_root(root: Path) -> Path:
    return root / ".codex" / "local" / "chatgpt-research"


def request_dir(root: Path, request_id: str) -> Path:
    if not REQUEST_ID.fullmatch(request_id):
        raise ValueError("request-id must use lowercase letters, digits, and hyphens")
    return bridge_root(root) / request_id


def checked_bridge_path(root: Path, raw_path: str) -> Path:
    candidate = Path(raw_path)
    path = candidate.resolve() if candidate.is_absolute() else (root / candidate).resolve()
    allowed = bridge_root(root).resolve()
    try:
        relative = path.relative_to(allowed)
    except ValueError as exc:
        raise ValueError(f"bridge path must be below {allowed}") from exc
    if len(relative.parts) < 2:
        raise ValueError("bridge path must be inside one request-id directory")
    if not REQUEST_ID.fullmatch(relative.parts[0]):
        raise ValueError("the first bridge directory must be a valid request-id")
    return path


def command_init(root: Path, request_id: str) -> int:
    path = request_dir(root, request_id)
    if path.exists():
        print(f"ERROR request directory already exists: {path}")
        return 1
    path.mkdir(parents=True)
    print(path)
    return 0


def command_preflight(root: Path, raw_path: str) -> int:
    try:
        path = checked_bridge_path(root, raw_path)
    except ValueError as exc:
        print(f"ERROR {exc}")
        return 1
    if not path.parent.is_dir():
        print(f"ERROR request directory does not exist: {path.parent}")
        return 1
    print(f"Bridge path accepted: {path}")
    return 0


def command_gc(root: Path, request_id: str) -> int:
    try:
        path = request_dir(root, request_id)
    except ValueError as exc:
        print(f"ERROR {exc}")
        return 1
    if not path.is_dir():
        print(f"ERROR request directory does not exist: {path}")
        return 1
    shutil.rmtree(path)
    print(f"Garbage-collected ChatGPT research bridge: {request_id}")
    return 0


def audit_errors(root: Path) -> list[str]:
    errors: list[str] = []
    prompts = root / "prompts"
    if prompts.is_dir():
        unexpected = sorted(path.relative_to(root) for path in prompts.rglob("*") if path.is_file() and path.name != "README.md")
        for path in unexpected:
            errors.append(f"ERROR tracked ChatGPT bridge or prompt artifact is forbidden: {path}")
    ignored_bridge_root = bridge_root(root).resolve()
    for path in root.rglob("*.md"):
        resolved = path.resolve()
        if ignored_bridge_root in (resolved, *resolved.parents):
            continue
        content = path.read_text(encoding="utf-8")
        if sum(signal in content for signal in DIRECT_PROMPT_SIGNALS) >= 2:
            errors.append(f"ERROR possible direct ChatGPT research prompt outside the ignored bridge area: {path.relative_to(root)}")
    gitignore = root / ".gitignore"
    if not gitignore.is_file() or ".codex/local/" not in gitignore.read_text(encoding="utf-8"):
        errors.append("ERROR .gitignore must exclude .codex/local/")
    return errors


def command_audit(root: Path) -> int:
    errors = audit_errors(root)
    if errors:
        print("\n".join(errors))
        return 1
    print("ChatGPT research bridge audit passed.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    subparsers = parser.add_subparsers(dest="command", required=True)
    init = subparsers.add_parser("init", help="create one ignored request directory")
    init.add_argument("request_id")
    preflight = subparsers.add_parser("preflight", help="reject a bridge path outside the allowed request directory")
    preflight.add_argument("path")
    gc = subparsers.add_parser("gc", help="delete one completed request directory")
    gc.add_argument("request_id")
    subparsers.add_parser("audit", help="reject retired prompt files and common direct-prompt signatures")
    args = parser.parse_args()
    root = args.root.resolve()
    if args.command == "init":
        return command_init(root, args.request_id)
    if args.command == "preflight":
        return command_preflight(root, args.path)
    if args.command == "gc":
        return command_gc(root, args.request_id)
    return command_audit(root)


if __name__ == "__main__":
    sys.exit(main())
