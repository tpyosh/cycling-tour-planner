# 2026年9月 三陸旅行計画

このブランチは、2026年9月23日〜28日の三陸旅行について、2026年9月3日時点の検討結果を記録した working plan です。現時点の最有力案、候補、代替案、参考タイムテーブル、宿泊構成、未確認事項を分離して管理しています。交通・宿泊・施設はまだ予約・最終決定前です。

旅行者向けの現在の旅程は `docs/itinerary.md`、未解決事項は `docs/issues.md`、宿泊確認の枠組みは `docs/lodging-calls.md` を参照してください。

## 更新方法

1. 候補の追加・状態変更は `catalog/*.yaml` へ記録する。
2. 現行案への採用は `plan/current.yaml` からIDで参照する。
3. 調査結果は `evidence/sources.yaml`、旅程を左右する未解決事項は `issues.yaml` に記録する。
4. 宿名・在庫・価格の確認結果は `research/lodging.yaml` に記録する。
5. 検証後に旅行者向けMarkdownを再生成する。

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python tools/validate.py
.venv/bin/python tools/render.py
.venv/bin/pytest -q
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

## Codexスキル

`.codex/skills/travel-planner/` に、制約整理、情報の鮮度管理、実現可能性確認、宿泊調査、代替案作成、品質確認の汎用ノウハウがあります。
