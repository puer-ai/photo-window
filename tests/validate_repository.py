#!/usr/bin/env python3
"""Validate the published skill package and smoke-test resize helpers."""

from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "preserve-photo-window-old-paper"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validate_skill() -> None:
    skill_md = SKILL / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.DOTALL)
    require(match is not None, "SKILL.md must start with YAML frontmatter")

    frontmatter = match.group(1)
    require(
        re.search(r"^name:\s*preserve-photo-window-old-paper\s*$", frontmatter, re.MULTILINE)
        is not None,
        "Skill name must match its directory",
    )
    require(
        re.search(r"^description:\s*\S.+$", frontmatter, re.MULTILINE) is not None,
        "Skill description must be non-empty",
    )
    require(len(text.splitlines()) < 500, "SKILL.md should stay below 500 lines")

    required = [
        SKILL / "agents" / "openai.yaml",
        SKILL / "references" / "prompt-template.md",
        SKILL / "scripts" / "restore_source_size.py",
        SKILL / "scripts" / "restore_source_size.ps1",
        ROOT / "README.md",
        ROOT / "README.zh-CN.md",
        ROOT / "README.ja.md",
        ROOT / "LICENSE",
        ROOT / "CONTRIBUTING.md",
        ROOT / "SECURITY.md",
        ROOT / "CODE_OF_CONDUCT.md",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
    require(not missing, f"Missing required files: {missing}")

    openai_yaml = (SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8")
    require(
        "$preserve-photo-window-old-paper" in openai_yaml,
        "agents/openai.yaml default prompt must name the skill",
    )


def smoke_test_resize_helpers() -> None:
    python_helper = SKILL / "scripts" / "restore_source_size.py"
    powershell_helper = SKILL / "scripts" / "restore_source_size.ps1"

    with tempfile.TemporaryDirectory() as temp_dir:
        temp = Path(temp_dir)
        source = temp / "source.png"
        generated = temp / "generated.png"
        python_output = temp / "python-output.png"

        Image.new("RGB", (37, 61), "white").save(source)
        Image.new("RGB", (80, 40), "navy").save(generated)

        subprocess.run(
            [
                sys.executable,
                str(python_helper),
                "--input",
                str(generated),
                "--source",
                str(source),
                "--output",
                str(python_output),
            ],
            check=True,
        )
        with Image.open(python_output) as result:
            require(result.size == (37, 61), "Python helper returned the wrong size")

        if os.name == "nt":
            powershell_output = temp / "powershell-output.png"
            subprocess.run(
                [
                    "powershell",
                    "-NoProfile",
                    "-ExecutionPolicy",
                    "Bypass",
                    "-File",
                    str(powershell_helper),
                    "-InputPath",
                    str(generated),
                    "-SourcePath",
                    str(source),
                    "-OutputPath",
                    str(powershell_output),
                ],
                check=True,
            )
            with Image.open(powershell_output) as result:
                require(result.size == (37, 61), "PowerShell helper returned the wrong size")


def main() -> None:
    validate_skill()
    smoke_test_resize_helpers()
    print("Repository validation passed.")


if __name__ == "__main__":
    main()
