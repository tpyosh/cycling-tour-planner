#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
import tomllib
from pathlib import Path
from typing import Any

from ruamel.yaml import YAML
from ruamel.yaml.error import YAMLError


EXPECTED_SKILLS = {
    "cycling-trip-research",
    "cycling-itinerary-design",
    "cycling-trip-review",
    "travel-weather-refresh",
}
EXPECTED_AGENTS = {"trip-researcher.toml", "trip-critic.toml"}
DATE_PATTERN = re.compile(r"\b20\d{2}-\d{2}-\d{2}\b")
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def _load_yaml(path: Path) -> Any:
    yaml = YAML(typ="safe")
    with path.open(encoding="utf-8") as stream:
        return yaml.load(stream)


def _frontmatter(path: Path) -> tuple[dict[str, Any] | None, list[str]]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return None, [f"ERROR {path}: frontmatter must be delimited by ---"]
    yaml = YAML(typ="safe")
    try:
        value = yaml.load(match.group(1))
    except YAMLError as exc:
        return None, [f"ERROR {path}: invalid frontmatter: {exc}"]
    if not isinstance(value, dict):
        errors.append(f"ERROR {path}: frontmatter must be a mapping")
        return None, errors
    return value, errors


def _check_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return [f"ERROR {skill_file}: missing"]

    frontmatter, frontmatter_errors = _frontmatter(skill_file)
    errors.extend(frontmatter_errors)
    if frontmatter is None:
        return errors

    name = frontmatter.get("name")
    description = frontmatter.get("description")
    if name != skill_dir.name:
        errors.append(f"ERROR {skill_file}: name must match directory: {skill_dir.name}")
    if not isinstance(description, str) or not description.strip():
        errors.append(f"ERROR {skill_file}: description is required")
    elif "使わない" not in description:
        errors.append(f"ERROR {skill_file}: description must state a non-trigger boundary")

    text = skill_file.read_text(encoding="utf-8")
    for target in MARKDOWN_LINK_PATTERN.findall(text):
        if target.startswith(("http://", "https://", "#")):
            continue
        resolved = (skill_file.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"ERROR {skill_file}: linked resource does not exist: {target}")

    metadata_path = skill_dir / "agents" / "openai.yaml"
    if not metadata_path.is_file():
        errors.append(f"ERROR {metadata_path}: missing")
    else:
        try:
            metadata = _load_yaml(metadata_path)
        except (OSError, YAMLError) as exc:
            errors.append(f"ERROR {metadata_path}: invalid YAML: {exc}")
        else:
            interface = metadata.get("interface") if isinstance(metadata, dict) else None
            display_name = interface.get("display_name") if isinstance(interface, dict) else None
            short_description = interface.get("short_description") if isinstance(interface, dict) else None
            prompt = interface.get("default_prompt") if isinstance(interface, dict) else None
            if not isinstance(display_name, str) or not display_name.strip():
                errors.append(f"ERROR {metadata_path}: interface.display_name is required")
            if not isinstance(short_description, str) or not 25 <= len(short_description) <= 64:
                errors.append(f"ERROR {metadata_path}: interface.short_description must be 25-64 characters")
            if not isinstance(prompt, str) or f"${name}" not in prompt:
                errors.append(f"ERROR {metadata_path}: default_prompt must mention ${name}")
    return errors


def check_repository(root: Path) -> list[str]:
    errors: list[str] = []

    agents_md = root / "AGENTS.md"
    if not agents_md.is_file():
        errors.append("ERROR AGENTS.md: missing")
    elif agents_md.stat().st_size > 4096:
        errors.append(f"ERROR AGENTS.md: {agents_md.stat().st_size} bytes exceeds 4096-byte project limit")

    legacy_skills = root / ".codex" / "skills"
    if legacy_skills.exists() and any(legacy_skills.rglob("SKILL.md")):
        errors.append("ERROR .codex/skills: legacy repository skill location must not contain SKILL.md")

    skills_root = root / ".agents" / "skills"
    actual_skills = {path.name for path in skills_root.iterdir() if path.is_dir()} if skills_root.is_dir() else set()
    if actual_skills != EXPECTED_SKILLS:
        errors.append(f"ERROR .agents/skills: expected {sorted(EXPECTED_SKILLS)}, found {sorted(actual_skills)}")
    for skill_name in sorted(actual_skills):
        errors.extend(_check_skill(skills_root / skill_name))

    config_path = root / ".codex" / "config.toml"
    try:
        with config_path.open("rb") as stream:
            config = tomllib.load(stream)
    except (OSError, tomllib.TOMLDecodeError) as exc:
        errors.append(f"ERROR {config_path}: {exc}")
    else:
        agents = config.get("agents")
        if not isinstance(agents, dict) or agents.get("max_concurrent_threads_per_session") != 2:
            errors.append("ERROR .codex/config.toml: [agents].max_concurrent_threads_per_session must be 2")
        if config.get("web_search") != "live":
            errors.append('ERROR .codex/config.toml: web_search must be "live" for weather refresh')

    agent_root = root / ".codex" / "agents"
    actual_agents = {path.name for path in agent_root.glob("*.toml")} if agent_root.is_dir() else set()
    if actual_agents != EXPECTED_AGENTS:
        errors.append(f"ERROR .codex/agents: expected {sorted(EXPECTED_AGENTS)}, found {sorted(actual_agents)}")
    agent_names: set[str] = set()
    for path in sorted(agent_root.glob("*.toml")):
        try:
            with path.open("rb") as stream:
                agent = tomllib.load(stream)
        except tomllib.TOMLDecodeError as exc:
            errors.append(f"ERROR {path}: invalid TOML: {exc}")
            continue
        for field in ("name", "description", "developer_instructions"):
            if not isinstance(agent.get(field), str) or not agent[field].strip():
                errors.append(f"ERROR {path}: {field} is required")
        if agent.get("sandbox_mode") != "read-only":
            errors.append(f"ERROR {path}: custom travel agents must be read-only")
        name = agent.get("name")
        if isinstance(name, str):
            if name in agent_names:
                errors.append(f"ERROR {path}: duplicate agent name: {name}")
            agent_names.add(name)

    foundation_files = [agents_md, config_path, *skills_root.rglob("*"), *agent_root.glob("*.toml")]
    for path in foundation_files:
        if path.is_file() and DATE_PATTERN.search(path.read_text(encoding="utf-8")):
            errors.append(f"ERROR {path.relative_to(root)}: reusable Codex foundation contains a trip-specific ISO date")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate repository-local Codex customization")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = check_repository(args.root.resolve())
    if errors:
        print("\n".join(errors))
        return 1
    print("Codex customization validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
