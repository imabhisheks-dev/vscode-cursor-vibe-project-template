#!/usr/bin/env python3
"""Inventory and soft-compare VS Code / Cursor / Claude template pairs."""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

# Logical pairs: (label, vscode_rel, cursor_rel, claude_rel_or_None)
PAIRS: list[tuple[str, str | None, str | None, str | None]] = [
    (
        "always-on/repo-instructions",
        ".github/copilot-instructions.md",
        ".cursor/rules/copilot-instructions.mdc",
        "CLAUDE.md",
    ),
    (
        "rules/general",
        ".github/instructions/general-coding.instructions.md",
        ".cursor/rules/general-coding.mdc",
        ".claude/rules/general.md",
    ),
    (
        "rules/typescript",
        ".github/instructions/typescript.instructions.md",
        ".cursor/rules/typescript.mdc",
        ".claude/rules/typescript.md",
    ),
    (
        "rules/python",
        ".github/instructions/python.instructions.md",
        ".cursor/rules/python.mdc",
        None,
    ),
    (
        "rules/documentation",
        ".github/instructions/documentation.instructions.md",
        ".cursor/rules/documentation.mdc",
        None,
    ),
    (
        "agents/planner",
        ".github/agents/planner.agent.md",
        ".cursor/agents/planner.md",
        None,
    ),
    (
        "agents/implementer",
        ".github/agents/implementer.agent.md",
        ".cursor/agents/implementer.md",
        ".claude/agents/implementer.md",
    ),
    (
        "agents/reviewer",
        ".github/agents/reviewer.agent.md",
        ".cursor/agents/reviewer.md",
        None,
    ),
    (
        "agents/feature-builder",
        ".github/agents/feature-builder.agent.md",
        ".cursor/agents/feature-builder.md",
        None,
    ),
    (
        "agents/strict-formatter",
        ".github/agents/strict-formatter.agent.md",
        ".cursor/agents/strict-formatter.md",
        None,
    ),
    (
        "agents/researcher",
        None,
        None,
        ".claude/agents/researcher.md",
    ),
    (
        "commands/create-component",
        ".github/prompts/create-component.prompt.md",
        ".cursor/commands/create-component.md",
        None,
    ),
    (
        "commands/security-review",
        ".github/prompts/security-review.prompt.md",
        ".cursor/commands/security-review.md",
        None,
    ),
    (
        "commands/write-tests",
        ".github/prompts/write-tests.prompt.md",
        ".cursor/commands/write-tests.md",
        None,
    ),
    (
        "commands/compare-ide-setup",
        ".github/prompts/compare-ide-setup.prompt.md",
        ".cursor/commands/compare-ide-setup.md",
        None,
    ),
    (
        "skills/webapp-testing",
        ".github/skills/webapp-testing/SKILL.md",
        ".cursor/skills/webapp-testing/SKILL.md",
        ".claude/skills/webapp-testing/SKILL.md",
    ),
    (
        "skills/github-actions-debugging",
        ".github/skills/github-actions-debugging/SKILL.md",
        ".cursor/skills/github-actions-debugging/SKILL.md",
        None,
    ),
    (
        "skills/compare-ide-setup",
        None,
        ".cursor/skills/compare-ide-setup/SKILL.md",
        None,
    ),
    (
        "hooks/formatting",
        ".github/hooks/formatting.json",
        ".cursor/hooks.json",
        ".claude/settings.json",
    ),
    (
        "hooks/security",
        ".github/hooks/security.json",
        ".cursor/hooks.json",
        ".claude/settings.json",
    ),
    (
        "hooks/audit",
        ".github/hooks/audit.json",
        ".cursor/hooks.json",
        ".claude/settings.json",
    ),
    (
        "hooks/script-block-dangerous",
        "scripts/block-dangerous.sh",
        ".cursor/hooks/block-dangerous.sh",
        "scripts/block-dangerous.sh",
    ),
    (
        "hooks/script-log-tool-use",
        "scripts/log-tool-use.sh",
        ".cursor/hooks/log-tool-use.sh",
        "scripts/log-tool-use.sh",
    ),
    (
        "hooks/script-format",
        "scripts/format-changed-files.sh",
        ".cursor/hooks/format-changed-files.sh",
        "scripts/format-changed-files.sh",
    ),
    (
        "shared/agents-md",
        "AGENTS.md",
        "AGENTS.md",
        "AGENTS.md",
    ),
]


FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n?", re.DOTALL)
BULLET_RE = re.compile(r"^\s*[-*]\s+", re.MULTILINE)
HEADING_RE = re.compile(r"^#+\s*", re.MULTILINE)
SPACE_RE = re.compile(r"\s+")


def normalize_body(text: str) -> str:
    body = FRONTMATTER_RE.sub("", text)
    body = BULLET_RE.sub("", body)
    body = HEADING_RE.sub("", body)
    body = SPACE_RE.sub(" ", body).strip().lower()
    return body


def fingerprint(text: str) -> str:
    return hashlib.sha1(normalize_body(text).encode("utf-8")).hexdigest()[:12]


def status_for(path: str | None) -> tuple[str, str | None, float | None]:
    if path is None:
        return ("n/a", None, None)
    full = ROOT / path
    if not full.exists():
        return ("missing", path, None)
    try:
        data = full.read_text(encoding="utf-8")
    except OSError:
        return ("unreadable", path, None)
    mtime = full.stat().st_mtime
    return ("present", fingerprint(data), mtime)


def newest_side(mtimes: dict[str, float | None]) -> str | None:
    present = {k: v for k, v in mtimes.items() if v is not None}
    if not present:
        return None
    return max(present.items(), key=lambda item: item[1])[0]


def main() -> int:
    print(f"ROOT={ROOT}")
    print("PAIR\tVSCODE\tCURSOR\tCLAUDE\tBODY_SYNC\tNEWEST\tNOTES")

    drift = 0
    missing = 0

    for label, vscode, cursor, claude in PAIRS:
        vs_st, vs_fp, vs_mt = status_for(vscode)
        cu_st, cu_fp, cu_mt = status_for(cursor)
        cl_st, cl_fp, cl_mt = status_for(claude)

        notes: list[str] = []
        body_sync = "n/a"

        active_fps = []
        if vs_st == "present":
            active_fps.append(("vscode", vs_fp))
        if cu_st == "present":
            active_fps.append(("cursor", cu_fp))
        if cl_st == "present" and claude not in {vscode, cursor}:
            active_fps.append(("claude", cl_fp))

        if any(st == "missing" for st in (vs_st, cu_st, cl_st) if st != "n/a"):
            missing += 1
            for side, st, path in (
                ("vscode", vs_st, vscode),
                ("cursor", cu_st, cursor),
                ("claude", cl_st, claude),
            ):
                if st == "missing":
                    notes.append(f"missing:{side}:{path}")

        if len({fp for _, fp in active_fps}) <= 1 and len(active_fps) >= 2:
            body_sync = "aligned"
        elif len(active_fps) >= 2:
            body_sync = "diverged"
            drift += 1
            notes.append("recommend:compare-bodies-and-merge")
        elif len(active_fps) == 1:
            body_sync = "single-side"
            notes.append("recommend:add-missing-counterparts")

        # Hook configs intentionally share one Cursor/Claude file across multiple logical hooks.
        if label.startswith("hooks/") and not label.startswith("hooks/script-"):
            notes.append("format-diff-expected:adapt-behavior-not-paste")

        newest = newest_side({"vscode": vs_mt, "cursor": cu_mt, "claude": cl_mt}) or "-"
        note = ";".join(notes) if notes else "-"
        print(
            f"{label}\t{vs_st}\t{cu_st}\t{cl_st}\t{body_sync}\t{newest}\t{note}"
        )

    print()
    print(f"SUMMARY\tmissing_pairs={missing}\tbody_divergences={drift}")
    print(
        "HINT\tUse the compare-ide-setup skill to recommend concrete append/port edits per diverged pair."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
