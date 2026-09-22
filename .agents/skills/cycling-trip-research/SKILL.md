---
name: cycling-trip-research
description: 国内サイクリング旅行の候補、交通、営業、通行、宿泊、自然条件を調査し、出典付きの根拠と未確認事項を旅行データへ整理する。行程の採否決定や全体設計だけを行う依頼には使わない。
---

# サイクリング旅行の調査

候補の発見や成立条件の確認を、行程への採用判断から分離して進める。成果は、再確認可能な根拠と、次の調査行動が分かる未確認事項である。

## 開始条件

調査論点、対象範囲、基準日を確認する。個別旅行を扱う場合は、`trip.yaml`、`constraints.yaml`、関連する `catalog/*.yaml`、`evidence/sources.yaml`、`issues.yaml` を読む。

情報源の選び方、記録単位、変動性、宿泊在庫、自然条件の扱いは [references/evidence-and-risk.md](references/evidence-and-risk.md) を読む。スポット、博物館、イベント、産業施設、食候補を評価または `shortlisted` へ昇格させるときは、必ず [references/candidate-promotion.md](references/candidate-promotion.md) を読む。

## ワークフロー

1. 調査によって変わる判断と、必要な証拠を定義する。
2. Discoverでは広く集めるが、発見を採用根拠にしない。Verifyでは実行可否に関わる事実を運営者、交通事業者、自治体、道路管理者などの一次情報へ戻って確認する。
3. Evaluateでは、候補地で成人一人が行うこと、観察地点または自走範囲、実際に見えるもの、必要時間、アクセス条件と対象来場者を調べる。候補種別ごとのGate、レビューの使い方、例外、回帰例は `candidate-promotion.md` に従う。
4. 時刻、営業、運賃、予約、通行、持込条件は、旅行日に有効な情報かを確認する。確認できない値を推測で埋めない。
5. `evidence/sources.yaml` へ主張単位で記録する。Promotion Gateを通った候補だけを `shortlisted` にし、通らない候補は `discovered` / `researching` のまま、または理由を残して `deferred` / `rejected` にする。Scheduleは行程設計の責務であり、ここで決めない。
6. 計画を左右する未確認事項だけを `issues.yaml` に残し、影響、次の確認、解決条件を記す。
7. 調査で予約・購入・最終判断・直前確認・出発準備に必要な情報がそろい、旅行者自身の実行だけが残った場合は `user_actions.yaml` に移す。未確認事項をUser Actionとして水増ししない。

独立した論点が複数あり、出典探索の中間出力を主スレッドから分離する価値がある場合は、読み取り専用の `trip_researcher` に論点ごとに委任してよい。親エージェントだけが結果を照合し、正本YAMLへ反映する。

## 終了条件

- 採否に使う主張に、認識状態、出典、確認日、変動性がある。
- 見つからない情報と、利用不可・満室・運休を区別している。
- 未確認事項に次の確認行動と解決条件がある。
- YAMLを変更した場合、`tools/validate.py` が成功する。
