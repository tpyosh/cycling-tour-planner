# Snapshot contract

正本は`plan/current.yaml`の`weather_climate`である。`docs/itinerary.md`はrendererが生成する。

## Current state

- `forecast_snapshot.retrieved_at`: 絶対日時とTZ。表示は`Retrieved: YYYY-MM-DD HH:mm TZ`相当とする。
- `forecast_snapshot.sources`: live sourceの題名、URL、確認日、変動性。
- `synoptic_context`: `fact` / `inference` / `unverified`を分け、警報、台風、前線、概況を置く。
- `days`: 絶対日付、route segment、意味のある地点の降水・気温・風・警報、route relevance、直前確認を置く。0〜2日、3〜4日、5〜7日、それより先で確実性が異なることを、気象機関のconfidenceがあればそれを優先して表す。
- `climate_baseline`: 平年値・季節特性だけを置き、forecast refreshでは置換しない。
- `seasonal_outlook`: 期間平均の傾向であり、日別forecastの代用にしない。
- `operational_summary`: 現在のweather riskと、Primeを維持するかユーザー判断が必要かを簡潔に記録する。

## Refresh and actions

前回snapshotとの差分は、現在の判断に意味がある場合だけ`operational_summary`または日別の`interpretation`へ短く残す。古いforecast本文を履歴として追加しない。Git historyが履歴である。

Open recheckは`user_actions.yaml`が正本である。翌日の時間帯別風、フェリーの公式運航、警報、雨の時間帯など、旅行者自身の次の確認が必要なものだけを残す。単なる予報値、期限経過、確認済み、不要なActionは削除する。

警報、台風接近、暴風、波浪、大雨、雷、通行止めにつながる状況、重大交通影響は、**Observed fact / Forecast / Official warning or operation / Potential itinerary impact / Decision needed**を区別する。Decision neededがroute変更なら、Primeを編集せずユーザーの判断を待つ。
