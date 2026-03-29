#!/usr/bin/env python3
"""Validate the repository's skill structure without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "skills"
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    sys.exit(1)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"Missing file: {path.relative_to(REPO_ROOT)}")
    except UnicodeDecodeError:
        fail(f"File is not valid UTF-8: {path.relative_to(REPO_ROOT)}")
    raise AssertionError("unreachable")


def extract_frontmatter(skill_md: Path) -> dict[str, str]:
    content = read_text(skill_md)
    match = FRONTMATTER_RE.match(content)
    if not match:
        fail(f"{skill_md.relative_to(REPO_ROOT)} has no valid YAML frontmatter")

    frontmatter = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key:
            frontmatter[key] = value
    return frontmatter


def validate_frontmatter(skill_dir: Path) -> None:
    skill_md = skill_dir / "SKILL.md"
    frontmatter = extract_frontmatter(skill_md)

    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")
    version = frontmatter.get("version", "")
    category = frontmatter.get("category", "")
    platforms = frontmatter.get("platforms")

    if not name:
        fail(f"{skill_md.relative_to(REPO_ROOT)} is missing 'name'")
    if not re.fullmatch(r"[a-z0-9-]+", name):
        fail(f"{skill_md.relative_to(REPO_ROOT)} has invalid skill name '{name}'")
    if not description:
        fail(f"{skill_md.relative_to(REPO_ROOT)} is missing 'description'")
    if not version:
        fail(f"{skill_md.relative_to(REPO_ROOT)} is missing 'version'")
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        fail(f"{skill_md.relative_to(REPO_ROOT)} has invalid semver '{version}'")
    if not category:
        fail(f"{skill_md.relative_to(REPO_ROOT)} is missing 'category'")
    if platforms is None:
        fail(f"{skill_md.relative_to(REPO_ROOT)} is missing 'platforms'")


def validate_openai_yaml(skill_dir: Path) -> None:
    path = skill_dir / "agents" / "openai.yaml"
    content = read_text(path)
    required_snippets = [
        "interface:",
        "display_name:",
        "short_description:",
        "default_prompt:",
    ]
    for snippet in required_snippets:
        if snippet not in content:
            fail(f"{path.relative_to(REPO_ROOT)} is missing '{snippet}'")


def validate_relative_links(markdown_path: Path) -> None:
    content = read_text(markdown_path)
    for target in LINK_RE.findall(content):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        linked = (markdown_path.parent / target).resolve()
        if not linked.exists():
            fail(
                f"{markdown_path.relative_to(REPO_ROOT)} has a broken relative link: {target}"
            )


def validate_skill_dir(skill_dir: Path) -> None:
    if not (skill_dir / "SKILL.md").exists():
        fail(f"Skill directory missing SKILL.md: {skill_dir.relative_to(REPO_ROOT)}")
    if not (skill_dir / "agents" / "openai.yaml").exists():
        fail(
            f"Skill directory missing agents/openai.yaml: {skill_dir.relative_to(REPO_ROOT)}"
        )

    validate_frontmatter(skill_dir)
    validate_openai_yaml(skill_dir)

    for path in [skill_dir / "SKILL.md", *skill_dir.rglob("*.md")]:
        validate_relative_links(path)


def main() -> None:
    if not SKILLS_DIR.exists():
        fail("Repository has no skills/ directory")

    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    if not skill_dirs:
        fail("No skill directories found under skills/")

    for skill_dir in skill_dirs:
        validate_skill_dir(skill_dir)

    print("[OK] Skill repository structure is valid.")


if __name__ == "__main__":
    main()
