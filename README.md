# 旅行計画スケルトン

このリポジトリは「1旅行1ブランチまたは1コピー」で使う、旅行計画の汎用スケルトンです。行き先、日付、候補、予約情報は未設定です。

## 始め方

1. `trip.yaml` に旅行名、日付、出発地、交通手段を記入する。
2. `constraints.yaml` で変更できない条件と希望を分ける。
3. `catalog/*.yaml` に候補を追加する。
4. `plan/current.yaml` から採用する候補をIDで参照する。
5. 調査結果は `evidence/sources.yaml`、計画上の未解決事項は `issues.yaml` に記録する。
6. 検証後に旅行者向けMarkdownを生成する。

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python tools/validate.py
.venv/bin/python tools/check_terminology.py
.venv/bin/python tools/check_codex_customization.py
.venv/bin/python tools/render.py
.venv/bin/python -m pytest -q
```

## 正本と生成物

- `trip.yaml`: 旅行の基本情報
- `constraints.yaml`: ハード制約とソフト制約
- `catalog/`: 立ち寄り先、経路、宿泊地域、交通、食事の候補
- `plan/current.yaml`: 現在採用している日別計画と代替案
- `evidence/sources.yaml`: 主張、出典、確認日、変動性、再確認要否
- `issues.yaml`: 旅程を左右する未解決事項
- `estimates/distances.yaml`: 距離の元データと計算方法
- `research/lodging.yaml`: 宿候補と在庫確認の状態
- `docs/`: YAMLから生成する旅行者向け資料。直接編集しない

候補の調査状態と旅程への採用を混ぜません。採用は `plan/current.yaml` からの参照で表します。通常旅程と発動条件付きの代替案も分離します。

計画履歴は同じYAMLの複製ではなくGitで残します。予約開始、主要予約完了、出発直前など、後から戻る意味がある時点だけタグまたは明示的なスナップショットを使います。

## Codexカスタマイズ

- `AGENTS.md`: Skillの選択に依存せず守る、短い共通原則と読取り順
- `.agents/skills/`: 調査、行程設計、批判的レビューの反復可能なワークフロー
- `.codex/agents/`: 調査と独立監査を主スレッドから分離する、読み取り専用subagent
- `.codex/config.toml`: subagentの同時実行数だけを定めるプロジェクト設定
- `tools/check_codex_customization.py`: 配置、構文、参照、個別日付の混入を検査するスクリプト

設計判断、旧Skillからの移行先、採用しなかったCodex機構は [docs/codex-customization.md](docs/codex-customization.md) に記録しています。リポジトリSkillの正本は `.agents/skills/` です。
