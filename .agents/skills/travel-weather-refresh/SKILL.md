---
name: travel-weather-refresh
description: 最新のweather、forecast、wind、rainを旅行のitineraryへ反映し、weather riskと再確認Actionを更新する。歴史天候の調査や、進行中の旅行に結び付かない一般的な気候質問には使わない。
---

# 旅行中の weather state refresh

現在の旅行について、最新の天気・風・降水・気温・警報と交通への影響可能性を、既存の正本へ更新する。これは外部可変状態のrefreshであり、Primeの自動変更ではない。

詳細は、作業開始時に [source-policy.md](references/source-policy.md) と [snapshot-contract.md](references/snapshot-contract.md) を読む。

## 開始時に読むもの

`README.md`、`trip.yaml`、`plan/current.yaml`、`catalog/routes.yaml`、`catalog/places.yaml`、`catalog/transport.yaml`、`evidence/sources.yaml`、`user_actions.yaml`、既存の`weather_climate`を読む。`docs/`は生成物であり直接編集しない。

日別の出発地・終着地・自走・経由地・宿泊・重要交通から、地点を抽出する。海岸、半島、橋、峠、高所、長い下り、フェリー、天候に弱い接続は、都市の代表地点だけで隠れないよう追加する。一方、無意味に細かな地点を列挙しない。

## Refresh workflow

1. `web_search = "live"`が有効であることを確認し、live Web検索だけで取得する。live dataが得られない場合、保存済み予報を最新として扱わず、refresh不能と明記して旅行判断・snapshot更新を止める。
2. 気象庁等の一次情報で警報・注意報・台風・気象概況を確認し、必要な地点・時間帯の予報は有力な天気サービスで補完する。フェリー・鉄道は天気と公式運航情報を別々に確認する。
3. 既存snapshotと比較し、降雨の有無・時間帯、風向/風速、最低気温、警報、台風・前線、フェリー影響可能性のうち、旅程に意味のある差分だけを抜き出す。ソース差は消さず、数値を平均しない。
4. 降水が自走時間と重なるか、風がroute方向・露出地形・上り/下りにどう関係するか、早朝/高所/風による体感温度、霧・雷・波浪・荒天を評価する。固定のgo/no-go閾値は作らない。
5. `plan/current.yaml`の`weather_climate.forecast_snapshot`を現在有効な内容へ**置換**する。`climate_baseline`は信頼できる既存値を保持し、refreshのたびに再取得しない。出典、絶対日付、`Retrieved: YYYY-MM-DD HH:mm TZ`に相当する取得日時、事実/推論/未確認を残す。
6. 現在残るweather riskと、previous snapshotからの重要差分を簡潔に反映する。今回のcurrent planで使われる、未完了かつ旅行者自身が確認できるweather recheckだけを`user_actions.yaml`へ残す。完了・期限経過・不要なweather Actionは削除し、別のTODO台帳を作らない。
7. YAMLを検証し、旅行者向け文書をrenderする。ユーザーへの報告は差分中心にする。意味のある変化がなければ「Forecast refreshed. No material weather change affecting the current itinerary.」と簡潔に伝える。

## 判断境界

予報だけからフェリー欠航や交通運休を推測しない。公式運航情報が未発表なら、その事実とweather riskを分けて記録する。

weather refreshだけを理由にPrime itinerary、アンカー、予約、交通を変更しない。route上の意味がある変化で経路変更・短縮・出発時刻変更・輪行化の判断が必要な場合は、確認済み事実、予報、既存Primeへの影響、選択肢、未確認事項を分けてユーザーへ返し、決定を待つ。
