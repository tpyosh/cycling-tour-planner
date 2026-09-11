# 2026年9月 三陸旅行計画

このブランチは、2026年9月23日〜28日の三陸旅行について、検討中の候補、仮説案、参考タイムテーブル、宿泊構成、未確認事項を分離して記録します。交通・宿泊・施設はまだ予約・最終決定前です。

2026年9月6日までの候補評価と案A〜Dは `research/candidate-evaluation.md` が正本です。`plan/current.yaml` と生成済みの `docs/itinerary.md` は、2026年9月11日時点の current prime（現時点の最有力案）であり、予約済み・最終確定旅程ではありません。以前のworking planはGit履歴、比較案は調査文書に残し、上書きで検討履歴を失わない運用とします。未解決事項は `docs/issues.md`、宿泊確認の枠組みは `docs/lodging-calls.md` を参照してください。

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
  verification_status: confirmed
  acquisition_confidence: medium
  listing_name: 施設のGoogle Maps掲載名
  subject_match: exact
  source: {provider: Google Maps, retrieval_method: user_provided_chatgpt_research, url: null}
  evidence_scope: {rating_and_count: confirmed, review_text: partial, photos: not_checked}
  genre_context: {category: museum_and_exhibition, cautions: [展示施設は星が高く出やすいため、十分なレビュー件数がある4.0未満を警戒する。]}
  reassessment: {status: strong, plan_effect: maintain, rationale: [星、母数、ジャンル、ユーザー嗜好を合わせた再評価。]}
  review_notes: [展示内容そのものへの言及を一部確認。]
  audience_notes: [成人旅行者の具体的な評価傾向は未確認。]
  evidence_notes: [評価に使った要点を記録する。]
  limitations: [全レビュー本文を取得したわけではない。]
```

レビュー件数が複数の取得結果による幅で共有された場合は、`review_count` に共有値のうち最も具体的な件数を置き、`review_count_range: {min: ..., max: ...}` に幅を併記する。

Google Mapsのレビュー数・スターが未取得の候補について、Codexは値を推測・検索して補完しない。ユーザにChatGPTでの取得を依頼するプロンプトを提示し、ユーザがChatGPTの回答を戻した後に、対象候補の `google_maps` へ反映する。依頼文の雛形と回答の取り込みルールは `prompts/google-maps-reviews.md` に定める。

2026年9月10日のcurrent prime再監査は `research/google-maps-audit-20260910.md` に保存する。Google Mapsを旅程の自動ランキングには使わず、rating、review count、ジャンル、レビュー本文、施設の性質、ユーザー嗜好を組み合わせる。

2026年9月11日の9/25女川→気仙沼自走の成立性調査は `research/onagawa-kesennuma-feasibility-20260911.md` に保存する。約91kmは公式イベントの丸められたkm標を接続した概算であり、獲得標高を含む直接計算が完了するまで `estimates/distances.yaml` へ確定値として登録しない。

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python tools/validate.py
.venv/bin/python tools/render.py
.venv/bin/pytest -q
```

## 正本と生成物

- `PRINCIPLES.md`: 日程に依存しない、このリポジトリの設計原則。旅行の調査・評価・再設計ではこの文書を優先する
- `trip.yaml`: 旅行の基本情報
- `constraints.yaml`: ハード制約とソフト制約
- `catalog/`: 立ち寄り先、経路、宿泊地域、交通、食事の候補
- `plan/current.yaml`: 基準日付きのcurrent prime、変更理由、保留・除外、発動条件付き代替案。`status: current_prime`、`maturity: provisional`で、予約済み・確定旅程を意味しない
- `evidence/sources.yaml`: 主張、出典、確認日、変動性、再確認要否
- `issues.yaml`: 旅程を左右する未解決事項
- `estimates/distances.yaml`: 距離の元データと計算方法
- `research/lodging.yaml`: 宿候補と在庫確認の状態
- `research/candidate-evaluation.md`: 候補母集団、暫定評価、Google Maps調査の読み方、地域クラスター、仮説案A〜D、次回ブレスト事項
- `research/onagawa-kesennuma-feasibility-20260911.md`: 9/25女川→気仙沼の距離、時間予算、道路安全、削減基準、未解決事項の調査記録
- `docs/`: YAMLから生成する旅行者向け資料。直接編集しない

候補の調査状態と旅程への採用を混ぜません。採用は `plan/current.yaml` からの参照で表します。通常旅程と発動条件付きの代替案も分離します。

自転車の利用判断は [`PRINCIPLES.md`](PRINCIPLES.md) に従い、区間ごとに「走行体験」「候補束ね」「純粋移動」を評価します。再設計時にも `constraints.yaml` と `plan/current.yaml` の `mobility_strategy` を併せて更新してください。

## Codexスキル

`.codex/skills/travel-planner/` に、制約整理、情報の鮮度管理、実現可能性確認、宿泊調査、代替案作成、品質確認の汎用ノウハウがあります。
