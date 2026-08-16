# 古紙の上に写真の窓を残す

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

写真の視覚的な核を自動で見つけ、その主体と必要な文脈を写真として保ちながら、周辺を古紙・インク線・淡彩水彩のイラストへ変換するエージェントスキルです。

主体だけを切り抜くのではなく、物語やスケールが伝わる広い写真の「島」を残します。境界は目立たない領域を通る不規則な破れ紙／顔料の擦れとして構成し、完成画像を元写真と同じピクセル寸法へ戻します。

## 特長

- 円、マスク、輪郭指定なしで視覚的な核を自動選択します。
- 識別、スケール、姿勢、雰囲気に必要な文脈も写真として保持します。
- イラスト領域は表示面積の 50〜70%、標準目標は約 60% です。
- 温かい象牙色の古紙、紙繊維、インク／木炭の輪郭、ドライブラシ、青灰色のウォッシュ、控えめなセピアを用います。
- 元画像の構図、縦横比、ランドマーク、周辺物体の位置関係を維持します。
- 核の選択ミスとカバー率不足に対応する修正プロンプトを含みます。
- Python/Pillow と Windows PowerShell の原寸復元ヘルパーを含みます。

## 必要環境

- OpenAI Codex、または `SKILL.md` 形式のスキルに対応するエージェント環境。
- 添付画像を編集できる組み込み画像生成／編集ツール。
- 原寸復元には次のいずれか：
  - Python 3.9+ と Pillow（クロスプラットフォーム）、または
  - `System.Drawing` を利用できる Windows PowerShell。

このリポジトリには画像生成モデルや API キーは含まれていません。

## インストール

リポジトリをクローンします。

```bash
git clone https://github.com/1484509311/preserve-photo-window-old-paper.git
cd preserve-photo-window-old-paper
```

### Windows PowerShell

```powershell
$codexRoot = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE ".codex" }
$skillsRoot = Join-Path $codexRoot "skills"
New-Item -ItemType Directory -Path $skillsRoot -Force | Out-Null
Copy-Item -Recurse -LiteralPath ".\skills\preserve-photo-window-old-paper" -Destination $skillsRoot
```

### macOS または Linux

```bash
codex_root="${CODEX_HOME:-$HOME/.codex}"
mkdir -p "$codex_root/skills"
cp -R skills/preserve-photo-window-old-paper "$codex_root/skills/"
```

インストール後に Codex を再起動し、スキルを再検出させてください。

## 使い方

クリーンな元写真を添付してスキルを呼び出します。

```text
この写真に $preserve-photo-window-old-paper を使ってください。
```

残したい写真領域を明示することもできます。

```text
$preserve-photo-window-old-paper を使い、人物と自転車を写真の核として残してください。
```

スキルは次の順で処理します。

1. 編集対象と任意のスタイル参照画像を分類する。
2. 一つのまとまった視覚的な核と必要な文脈を決める。
3. 有機的な境界とイラストのカバー率を設計する。
4. 制約を明示したミクストメディア編集プロンプトを組み立てる。
5. 有力な候補を一つ生成・検査し、必要なら一度だけ狙いを絞って再試行する。
6. 選択した結果を元画像の寸法へ戻す。
7. 保持した核、イラスト領域、カバー率、寸法、忠実度の限界を報告する。

## 原寸復元

任意の Python 依存関係をインストールします。

```bash
python -m pip install -r requirements.txt
```

クロスプラットフォーム版を実行します。

```bash
python skills/preserve-photo-window-old-paper/scripts/restore_source_size.py \
  --input generated.png \
  --source clean-source.jpg \
  --output final.png
```

Windows では Python 依存関係のない PowerShell 版も使用できます。

```powershell
powershell -NoProfile -File skills/preserve-photo-window-old-paper/scripts/restore_source_size.ps1 `
  -InputPath "generated.png" `
  -SourcePath "clean-source.jpg" `
  -OutputPath "final.png"
```

どちらも既存ファイルを既定では上書きしません。上書きには `--force` または `-Force` の明示指定が必要です。

## リポジトリ構成

```text
skills/preserve-photo-window-old-paper/
├── SKILL.md
├── agents/openai.yaml
├── references/prompt-template.md
└── scripts/
    ├── restore_source_size.py
    └── restore_source_size.ps1
```

人向けの説明はインストール対象のスキルディレクトリ外に置き、エージェントの実行時コンテキストを簡潔に保ちます。

## プライバシーと忠実度

- 個人写真や機密写真を送信する前に、利用する画像ツールのプライバシーおよびデータ処理条件を確認してください。
- 主体の忠実度を優先しますが、生成画像編集で写真領域のピクセル単位の完全一致は保証できません。
- 再配布の許可がない第三者写真を公開サンプルに含めないでください。

## 検証

```bash
python -m pip install -r requirements.txt
python tests/validate_repository.py
```

CI は Windows と Ubuntu で同じ検証を実行します。

## コントリビューションとセキュリティ

[CONTRIBUTING.md](CONTRIBUTING.md)、[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)、[SECURITY.md](SECURITY.md) を参照してください。

## ライセンス

[MIT License](LICENSE) で公開します。

本プロジェクトは独立したコミュニティプロジェクトであり、OpenAI との提携や承認関係はありません。
