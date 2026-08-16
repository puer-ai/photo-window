# 在旧纸上保留照片窗口

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

这是一个智能体技能：自动识别照片的视觉核心，把主体及必要语境保留为可辨认的真实摄影，同时将外围场景转换为旧纸、墨线与淡彩水彩插画。

它保留的是一块有完整叙事语境的摄影“岛屿”，而不是紧贴主体的抠图；过渡边缘会经过低显著度区域，并在完成后把成品恢复到源照片的精确像素尺寸。

## 主要特点

- 自动选择视觉核心，不需要用户画圆、蒙版或轮廓。
- 主体与维持身份、尺度、姿态或氛围所需的语境一起保留。
- 插画可见面积默认目标约 60%，允许范围为 50–70%。
- 旧纸效果包含暖象牙色纸张、纤维、墨线或炭笔轮廓、干笔排线、蓝灰水洗和克制的褐色点染。
- 保持源图构图、宽高比、地标细节及外围物体的位置对应。
- 提供主体判断错误和覆盖比例不足时的定向修正提示。
- 提供 Python/Pillow 跨平台脚本和 Windows PowerShell 精确尺寸恢复脚本。

## 环境要求

- OpenAI Codex，或其他支持 `SKILL.md` 技能的智能体环境。
- 能够编辑附件图片的内置图片生成／编辑工具。
- 恢复精确尺寸时，任选一种：
  - Python 3.9+ 与 Pillow（跨平台）；
  - 带有 `System.Drawing` 的 Windows PowerShell。

本仓库不包含图片生成模型，也不包含任何 API 密钥。

## 安装

克隆仓库：

```bash
git clone https://github.com/puer-ai/preserve-photo-window-old-paper.git
cd preserve-photo-window-old-paper
```

### Windows PowerShell

```powershell
$codexRoot = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE ".codex" }
$skillsRoot = Join-Path $codexRoot "skills"
New-Item -ItemType Directory -Path $skillsRoot -Force | Out-Null
Copy-Item -Recurse -LiteralPath ".\skills\preserve-photo-window-old-paper" -Destination $skillsRoot
```

### macOS 或 Linux

```bash
codex_root="${CODEX_HOME:-$HOME/.codex}"
mkdir -p "$codex_root/skills"
cp -R skills/preserve-photo-window-old-paper "$codex_root/skills/"
```

安装后重启 Codex，使其重新发现技能。

## 使用方法

附上一张干净的源照片，然后调用技能：

```text
请用 $preserve-photo-window-old-paper 处理这张照片。
```

也可以明确指定要保留的摄影核心：

```text
请用 $preserve-photo-window-old-paper，把人物和自行车一起保留为摄影核心。
```

技能会依次：

1. 区分编辑目标图与可选的风格参考图；
2. 确定一个完整的视觉核心及必要语境；
3. 规划自然边界和插画覆盖比例；
4. 编译约束明确的混合媒介编辑提示；
5. 生成并检查一个候选结果，必要时进行一次定向重试；
6. 将选定结果恢复到源图尺寸；
7. 报告保留主体、插画区域、覆盖估算、最终尺寸和保真限制。

## 精确尺寸恢复

安装可选的 Python 依赖：

```bash
python -m pip install -r requirements.txt
```

运行跨平台脚本：

```bash
python skills/preserve-photo-window-old-paper/scripts/restore_source_size.py \
  --input generated.png \
  --source clean-source.jpg \
  --output final.png
```

Windows 也可以使用无需 Python 依赖的 PowerShell 脚本：

```powershell
powershell -NoProfile -File skills/preserve-photo-window-old-paper/scripts/restore_source_size.ps1 `
  -InputPath "generated.png" `
  -SourcePath "clean-source.jpg" `
  -OutputPath "final.png"
```

两个脚本默认都不会覆盖已有文件；只有明确传入 `--force` 或 `-Force` 才会覆盖。

## 仓库结构

```text
skills/preserve-photo-window-old-paper/
├── SKILL.md
├── agents/openai.yaml
├── references/prompt-template.md
└── scripts/
    ├── restore_source_size.py
    └── restore_source_size.ps1
```

面向用户的仓库说明放在可安装技能目录之外，避免增加智能体运行时的无关上下文。

## 隐私与保真说明

- 提交私人或保密照片前，请先检查你所选图片工具的隐私和数据处理条款。
- 技能会优先保护主体，但生成式图片编辑无法保证摄影核心与原图逐像素完全一致。
- 未取得再分发许可时，不要把第三方照片放进公开示例。

## 验证

```bash
python -m pip install -r requirements.txt
python tests/validate_repository.py
```

持续集成会在 Windows 和 Ubuntu 上执行相同检查。

## 参与贡献与安全

请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)、[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) 和 [SECURITY.md](SECURITY.md)。

## 许可证

本项目使用 [MIT License](LICENSE)。

这是一个独立的社区项目，与 OpenAI 无隶属或背书关系。
