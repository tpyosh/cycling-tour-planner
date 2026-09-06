# 2026年9月 三陸旅行計画

このブランチは、2026年9月23日〜28日の三陸旅行について、検討中の候補、仮説案、参考タイムテーブル、宿泊構成、未確認事項を分離して記録します。交通・宿泊・施設はまだ予約・最終決定前です。

2026年9月6日までの候補評価と案A〜Dは `research/candidate-evaluation.md` が正本です。`plan/current.yaml` と生成済みの `docs/itinerary.md` は、9月3日時点で時刻・宿泊を詳細化した working plan であり、案A〜Dを比較して確定した旅程ではありません。未解決事項は `docs/issues.md`、宿泊確認の枠組みは `docs/lodging-calls.md` を参照してください。

## 更新方法

1. 候補の追加・状態変更は `catalog/*.yaml` へ記録する。
2. 現行案への採用は `plan/current.yaml` からIDで参照する。
3. 調査結果は `evidence/sources.yaml`、旅程を左右する未解決事項は `issues.yaml` に記録する。
4. 宿名・在庫・価格の確認結果は `research/lodging.yaml` に記録する。
5. 検証後に旅行者向けMarkdownを再生成する。

候補探索の記録、暫定Tier、候補発見とRankingを分離する評価ルールは `research/candidate-evaluation.md` に記録する。ここは旅程確定文書ではなく、`catalog/` の候補母集団を維持するための調査記録である。

## Google Mapsのレビュー情報

飲食店（`catalog/food.yaml`）と立ち寄りスポット（`catalog/places.yaml`）には、取得できたGoogle Maps調査を `google_maps` に記録する。星と件数だけでなく、取得経路、本文・写真の確認範囲、成人旅行者や子ども向け偏り、実物・展示に関する評価材料、取得限界を分けて残す。未確認の観点を推測で補わない。

```yaml
google_maps:
  rating: 4.2
  review_count: 318
  review_count_is_approximate: false
  checked_at: 2026-09-05
  source: {provider: Google Maps, retrieval_method: user_provided_chatgpt_research, url: null}
  evidence_scope: {rating_and_count: confirmed, review_text: partial, photos: not_checked}
  review_notes: [展示内容そのものへの言及を一部確認。]
  audience_notes: [成人旅行者の具体的な評価傾向は未確認。]
  evidence_notes: [評価に使った要点を記録する。]
  limitations: [全レビュー本文を取得したわけではない。]
```

Google Mapsのレビュー数・スターが未取得の候補について、Codexは値を推測・検索して補完しない。ユーザにChatGPTでの取得を依頼するプロンプトを提示し、ユーザがChatGPTの回答を戻した後に、対象候補の `google_maps` へ反映する。依頼文の雛形と回答の取り込みルールは `prompts/google-maps-reviews.md` に定める。

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
- `plan/current.yaml`: 現在詳細化している working plan と発動条件付き代替案。予約済み・確定旅程を意味しない
- `evidence/sources.yaml`: 主張、出典、確認日、変動性、再確認要否
- `issues.yaml`: 旅程を左右する未解決事項
- `estimates/distances.yaml`: 距離の元データと計算方法
- `research/lodging.yaml`: 宿候補と在庫確認の状態
- `research/candidate-evaluation.md`: 候補母集団、暫定評価、Google Maps調査の読み方、地域クラスター、仮説案A〜D、次回ブレスト事項
- `docs/`: YAMLから生成する旅行者向け資料。直接編集しない

候補の調査状態と旅程への採用を混ぜません。採用は `plan/current.yaml` からの参照で表します。通常旅程と発動条件付きの代替案も分離します。

## Codexスキル

`.codex/skills/travel-planner/` に、制約整理、情報の鮮度管理、実現可能性確認、宿泊調査、代替案作成、品質確認の汎用ノウハウがあります。
