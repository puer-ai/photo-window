# Preserve Photo Window on Old Paper

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

An agent skill that identifies the visual core of a photograph, preserves that core as recognizable photography, and transforms the surrounding scene into an aged-paper ink-and-watercolor illustration.

The skill creates a broad photographic “island” rather than a tight cutout. It routes an organic torn-paper or rubbed-pigment transition through low-salience areas and restores the final image to the source photograph's exact pixel dimensions.

## Highlights

- Selects the visual core automatically; no circle, mask, or outline is required.
- Preserves the subject together with the context needed for identity, scale, pose, or atmosphere.
- Targets 50–70% illustrated coverage, with about 60% as the default.
- Uses warm aged paper, visible fibers, ink or charcoal contours, dry-brush hatching, blue-gray wash, and restrained sepia accents.
- Keeps source composition, aspect ratio, landmarks, and peripheral object alignment.
- Includes correction prompts for core-selection and coverage failures.
- Includes exact-size restoration helpers for Python/Pillow and Windows PowerShell.

## Requirements

- OpenAI Codex or another agent environment that supports `SKILL.md` skills.
- A built-in image-generation or image-editing tool that can edit an attached image.
- For exact-size restoration, choose one:
  - Python 3.9+ and Pillow (cross-platform), or
  - Windows PowerShell with `System.Drawing`.

This repository does not include an image-generation model or API credentials.

## Installation

Clone the repository:

```bash
git clone https://github.com/puer-ai/photo-window.git
cd photo-window
```

### Windows PowerShell

```powershell
$codexRoot = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE ".codex" }
$skillsRoot = Join-Path $codexRoot "skills"
New-Item -ItemType Directory -Path $skillsRoot -Force | Out-Null
Copy-Item -Recurse -LiteralPath ".\skills\preserve-photo-window-old-paper" -Destination $skillsRoot
```

### macOS or Linux

```bash
codex_root="${CODEX_HOME:-$HOME/.codex}"
mkdir -p "$codex_root/skills"
cp -R skills/preserve-photo-window-old-paper "$codex_root/skills/"
```

Restart Codex after installation so it can discover the skill.

## Usage

Attach a clean source photograph and invoke the skill:

```text
Use $preserve-photo-window-old-paper on this photograph.
```

You may override the automatically selected core:

```text
Use $preserve-photo-window-old-paper. Keep the person and the bicycle as the photographic core.
```

The skill will:

1. classify each input image as edit target or optional style reference;
2. identify one coherent visual core and its essential context;
3. plan an organic boundary and illustrated coverage;
4. compile a constrained mixed-media edit prompt;
5. generate and inspect one strong candidate, with one targeted retry when needed;
6. restore the selected result to the source dimensions; and
7. report the preserved core, illustrated regions, coverage estimate, dimensions, and fidelity limits.

## Exact-size restoration

Install the optional Python dependency:

```bash
python -m pip install -r requirements.txt
```

Then run:

```bash
python skills/preserve-photo-window-old-paper/scripts/restore_source_size.py \
  --input generated.png \
  --source clean-source.jpg \
  --output final.png
```

Windows users may use the dependency-free PowerShell helper instead:

```powershell
powershell -NoProfile -File skills/preserve-photo-window-old-paper/scripts/restore_source_size.ps1 `
  -InputPath "generated.png" `
  -SourcePath "clean-source.jpg" `
  -OutputPath "final.png"
```

Both helpers refuse to overwrite an existing output unless `--force` or `-Force` is explicitly supplied.

## Repository layout

```text
skills/preserve-photo-window-old-paper/
├── SKILL.md
├── agents/openai.yaml
├── references/prompt-template.md
└── scripts/
    ├── restore_source_size.py
    └── restore_source_size.ps1
```

Repository-level documentation remains outside the installable skill folder to keep the agent's runtime context focused.

## Privacy and fidelity

- Review the privacy and data-handling terms of the image tool you choose before submitting personal or confidential photographs.
- The skill prioritizes subject fidelity, but generative image editing cannot guarantee pixel-identical preservation of the photographic core.
- Do not include third-party photographs in public examples unless you have permission to redistribute them.

## Validation

```bash
python -m pip install -r requirements.txt
python tests/validate_repository.py
```

Continuous integration runs the same checks on Windows and Ubuntu.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), and [SECURITY.md](SECURITY.md).

## License

Released under the [MIT License](LICENSE).

This is an independent community project and is not affiliated with or endorsed by OpenAI.
