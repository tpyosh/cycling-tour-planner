# ChatGPT調査依頼: 9/26気仙沼フルデイの訪問順と時間配分

このファイルは、ChatGPTへそのまま添付して使う自己完結型の調査指示書です。ChatGPTは別のローカルファイルを参照できなくても構いません。

ChatGPTには、このファイルを添付したうえで、次の一文だけ送ってください。

> 添付したMarkdownの指示に従ってWebを調査し、指定形式で回答してください。

ChatGPTの回答は編集や要約をせず、そのままリポジトリ管理を担当するCodexへ戻してください。予約、購入、電話、問い合わせ、メッセージ送信は依頼していません。

---

## ChatGPTへの実行指示

あなたは、個人旅行の実行可能性、施設の時間窓、自転車による市内移動を監査するリサーチャーです。Webを調査し、2026年9月26日（土）の `issue.kesennuma-full-day-feasibility` を、下記の解決条件に照らして解消してください。

最終回答は単なる調査レポートではなく、リポジトリ管理を担当するCodexへそのまま貼り付けられる、自己完結した「ドキュメンテーション依頼用のCodex向けプロンプト」にしてください。Codexがこの添付ファイルやChatGPTの会話履歴を参照できるとは仮定せず、調査結果、根拠、反映指示、検証条件を最終回答の中に収録してください。

### 0. Preflight（必須）

本調査を始める前に、次を短く出力してください。

1. 受信できた添付ファイル名を列挙する。
2. `chatgpt-resolve-kesennuma-full-day-feasibility.md` が読めることを確認する。
3. 同ファイル内の「ChatGPTへの実行指示」「引き渡しデータ」「リポジトリの反映条件」の3セクションが読めることを確認する。

このファイル、またはいずれかの必須セクションが見えない場合は、本調査を開始しないでください。不足しているファイル名またはセクション名だけを報告してください。

### 1. 調査目的、範囲、基準日

- 調査目的: 気仙沼魚市場、気仙沼「海の市」内の2施設、リアス・アーク美術館、朝・昼・夜の食事を、営業時間、移動、駐輪、待ち時間まで含めて1日に収められるか判断する。
- 対象Issue: `issue.kesennuma-full-day-feasibility`
- 対象日: 2026年9月26日（土）
- リポジトリ情報の基準日: 2026年9月11日
- Web情報の確認日: 実際に調査した日を記載する。
- 対象範囲: 9月26日の気仙沼市内だけ。旅行全体の作り直しはしない。

次の4条件をすべて満たす根拠が揃った場合だけ、Issueの `resolved` を提案してください。

1. 各施設の2026年9月26日に有効な利用可能時間と、妥当な必要滞在時間を確認している。
2. 移動、駐輪、入館待ちを含む訪問順と到着目標が決まっている。
3. 再監査中の気仙沼シャークミュージアムと氷の水族館を両方採用する案、両方外す案のどちらでも一日が成立する。
4. 魚市場で水揚げや入港船を確認できない場合の繰上げ先と食事時間が決まっている。

一部しか確認できなければ `in_progress`、重要な根拠が得られなければ `open` を提案してください。情報不足を推測で埋めて `resolved` にしないでください。

### 2. 動かしてはいけない前提

- 旅行日は2026年9月26日（土）。大人1名の一人旅である。
- 9月25日と26日は気仙沼に2連泊する予定だが、宿名と所在地は未確定である。
- 市内移動の基本は自転車。走行自体は目的ではなく、点在候補を束ねるために使う。
- レンタカーは使わない。市内で必要な場合に限り短距離タクシーを提案してよいが、自転車を載せられるとは仮定しない。
- 朝の気仙沼市魚市場では、荷捌き、水揚げ、入港船、市場前の物流・漁業動線を見ることが主目的である。
- `place.rias-ark-museum` は震災資料・地域文化への関心と合う採用候補である。公式情報が反証しない限り、標準案で守る。
- `place.kesennuma-shark-museum` と `place.kesennuma-ice-aquarium` は現行動線上にあるが、別Issueでレビュー本文の再監査中である。今回、施設品質の採否を確定してはならない。
- `food.tsurukame-dining-hall` は朝食の高優先度候補である。朝営業と魚市場動線が公式情報で確認できる場合は標準案へ置く。
- 昼食と夕食は `food.asahi-zushi-kesennuma`、`food.kitakatsu-maguroya` を中心に、旅行日固有の営業と動線を確認する。ただし、料理の総合ランキングやGoogle Mapsレビュー評価は別Issueの範囲である。
- 戻り鰹、メカジキ、フカヒレ、モウカの星、サンマ、ホヤ、地魚寿司を「海鮮」として一括評価しない。9月下旬は戻り鰹を特に重視し、メカジキは冬メカ最盛期より前として扱う。
- 魚市場前、港町、鹿折で見える冷蔵庫、加工工場、トラック、漁船は移動中の副次的価値とする。特定工場への立入りや一般見学は前提にしない。
- 予約、購入、電話、問い合わせ、メッセージ送信は行わない。

### 3. 隣接Issueとの境界

- `issue.kesennuma-fish-market`: 今回の訪問時刻を決めるため、見学可能時間、休場、入船・水揚げ情報の確認方法、魚市場が不発の場合を調べてよい。旬魚の実漁況を詳細に追い、このIssueまで解決済みにする必要はない。
- `issue.kesennuma-meal-selection`: 今回の時間割を成立させるため、候補店の旅行日固有の営業時間、予約要否、位置、標準的な食事時間を調べてよい。料理品質の総合比較や三食の最終選定は行わない。
- `issue.google-maps-review-text-reassessment`: シャークミュージアムと氷の水族館の採否は確定しない。Google Mapsのrating、review count、レビュー本文、写真を再取得・更新しない。
- `issue.lodging-endpoint-routes`: 宿名が未確定なので、宿から最初の候補、最後の候補から宿までのラストマイルは確定しない。別Issueとして残す。
- `issue.visit-status-and-cut-order`: 9月26日に限り削減順を提案してよい。全日程の候補分類は変更しない。

### 4. 必ず調べること

#### 4.1 旅行日固有の営業・利用可能時間

次の対象について、2026年9月26日の開館・営業可否、開始・終了時刻、最終入館・ラストオーダー、休館・臨時変更、予約要否を調べてください。

- 気仙沼市魚市場の一般見学エリア・見学デッキ
- 気仙沼「海の市」
- 気仙沼シャークミュージアム
- 氷の水族館
- リアス・アーク美術館
- 鶴亀食堂
- あさひ鮨
- 北かつまぐろ屋

公式サイト、公式営業カレンダー、運営者の公式SNS等を最優先してください。通常営業時間しか確認できない場合は、対象日固有の確認と区別してください。検索結果の抜粋だけを根拠にせず、根拠ページを開いて確認してください。

#### 4.2 魚市場の朝の成立性

- 一般旅行者が見学できる場所、入場方法、入口、見学可能時間、休場日・休日運用を確認する。
- 2026年9月26日の水揚げや入港船を事前または前夜に確認できる一次情報を探す。
- 水揚げの保証がない場合は、その限界を明記する。
- 前夜に確認する公式ページと、当日朝に現地で「不発」と判断する時刻を示す。
- 不発の場合に、鶴亀食堂、海の市、リアス・アーク美術館のどれを繰り上げられるか、各施設の開始時刻と合わせて判断する。

#### 4.3 必要滞在時間

各施設について、運営者が示す標準所要時間があれば採用してください。ない場合は、展示規模、展示構成、公式モデルコース等から推論し、`inference` と明示した幅で示してください。

少なくとも次を分けてください。

- 魚市場見学時間
- 海の市の売場・共用部を見る時間
- シャークミュージアム単体の時間
- 氷の水族館単体の時間
- リアス・アーク美術館の常設・震災関連展示と、開催確認できた企画の時間
- 朝・昼・夜それぞれの待ち時間と食事時間

#### 4.4 実走動線、距離、駐輪

- 魚市場の一般見学入口または駐輪地点を暫定起点にする。
- 魚市場、海の市、リアス・アーク美術館、昼食候補、夕食候補を結ぶ自転車向け動線を具体化する。
- 区間距離、累積距離、登りの影響、信号や市街地走行を含む所要時間を示す。
- 魚市場と海の市が同一または隣接施設である場合も、入口、駐輪、館内移動をゼロ分とみなさない。
- 各施設の駐輪場所、入口までの徒歩、施錠・再駐輪に必要な時間を確認する。公式情報がなければ `unknown` とし、推測で設備を断定しない。
- リアス・アーク美術館への登りを、平地と同じ自転車所要時間で計算しない。
- 再現可能な経由点列、利用した地図・ルーティングサービス、設定、共有URLまたは取得元を示す。
- 宿への往復は距離に含めず、宿確定後に再計算が必要だと明記する。

#### 4.5 2つの成立案と不発時案

最低限、次の3案を作ってください。

1. 標準案: シャークミュージアムと氷の水族館を両方含め、リアス・アーク美術館も守る。
2. 短縮案: 再監査中の2施設を両方外し、魚市場、海の市の売場・共用部、リアス・アーク美術館を中心にする。
3. 魚市場不発案: 水揚げや入港船を見込めない、または所定の時刻までに動きがない場合に、朝食と後続施設を繰り上げる。

各案で、移動、駐輪、入館待ち、施設滞在、朝食、昼食、夕食、予備時間を別々に積み上げてください。営業時間の端を狙わず、施設ごとに妥当な到着余裕を置いてください。

#### 4.6 企画展・臨時情報

既存根拠には、リアス・アーク美術館の「新方舟祭2026」が2026年9月25日から始まり、9月26日は会期内という未検証の計画シードがあります。名称、会期、開館、展示内容、通常展示への影響を公式情報で確認してください。確認できなければ、既存シードだけで開催中と断定しないでください。

施設・店舗の臨時休館、貸切、イベント、営業時間変更について、前日と当日朝に再確認すべき公式URLも示してください。

### 5. 情報源と判断のルール

- 営業、休館、最終入館、予約要否、一般見学可否は、施設または運営者の公式情報を最優先する。
- 距離・経路は、経由点と設定を示せるルーティング情報を使う。数値差がある場合は幅と理由を示す。
- 主要な主張ごとに、出典名、直接URL、確認日、対象日への有効性、変動性、旅行直前の再確認要否を記録する。
- 事実、出典からの推論、旅程上の提案を明確に分ける。
- 情報が見つからないことと、営業・利用上問題がないことを混同しない。
- 公式情報同士が矛盾する場合は、更新日と対象日を比較し、矛盾を隠さない。
- 料金、営業時間、展示、店舗営業は変動しうる。旅行直前に再確認すべきものを明記する。
- Google Mapsのrating、review count、レビュー本文、写真の調査・更新は行わない。
- 不明な値やIDを作らない。既存IDがない新規対象は、正本追加を提案せず `unresolved` に記載する。

### 6. 最終回答の形式

Preflight結果の後、最終回答は次の見出しを持つ1つのMarkdown文書にしてください。文書タイトルは `# Codexへの依頼: issue.kesennuma-full-day-feasibility の調査結果を反映する` とします。

#### 6.1 調査の要約

- 調査目的、対象範囲、対象日、リポジトリ基準日、Web確認日
- 結論: `resolved / in_progress / open` の提案
- 4つの解決条件が満たされたか
- 現行案への最小限の変更
- 最も影響の大きい未確認事項

#### 6.2 確認できた事実、推論、未確認事項

次の3区分を混ぜずに記載してください。

- `confirmed_fact`: 出典で直接確認できた事実
- `inference`: 出典から導いた所要時間や旅程上の判断
- `unverified`: 確認できなかったこと、旅行直前または宿確定後に確認すること

#### 6.3 旅行日固有の時間窓

| subject ID | 対象 | 2026-09-26に有効な時間・条件 | 最終入館等 | 必要滞在 | fact / inference | source title | direct URL | checked_at | volatility | recheck |
|---|---|---|---|---|---|---|---|---|---|---|

#### 6.4 魚市場の朝の判断

| 確認対象 | 確認方法 | 確認時刻 | 成功条件 | 不発条件 | 次の行動 | 直接URL |
|---|---|---|---|---|---|---|

#### 6.5 実走動線

| 区間 | 起点・終点 | 区間km | 累積km | 標高・登り | 純走行 | 駐輪・徒歩 | 経路条件 | source | confidence |
|---|---|---:|---:|---|---:|---:|---|---|---|

経路全体について、再現用の経由点列、利用サービス、設定、共有URLまたは取得元を記載してください。

#### 6.6 3つの時間割

標準案、短縮案、魚市場不発案を、それぞれ次の形式で示してください。

| 時刻 | 到着・出発 | 対象 | 移動 | 駐輪・徒歩・待ち | 滞在・食事 | 判断条件 | 根拠 |
|---|---|---|---:|---:|---:|---|---|

各案の末尾に、総走行距離、純走行時間、施設滞在、食事、待ち・駐輪、予備時間を集計してください。宿への往復を含まないことも明記してください。

#### 6.7 削減順と現地判断

| 判断地点・時刻 | 遅れ・不発の条件 | 削るもの | 守るもの | 次の行動 |
|---|---|---|---|---|

再監査中の2施設は採用確定扱いにせず、削減順を明記してください。リアス・アーク美術館を削る提案は、通常の削減と分け、公式時間窓上どうしても成立しない場合の例外として扱ってください。

#### 6.8 解決条件の判定

| 解決条件 | met / not_met / unknown | 根拠 | 残る作業 |
|---|---|---|---|

4条件すべてが `met` でない限り、`resolved` を提案しないでください。

#### 6.9 Codexへ反映を依頼するYAML候補

`evidence/sources.yaml` への追記候補を、次のスキーマに合うYAMLで示してください。1つの出典が複数の独立した主張を支える場合も、主張とsubjectの対応を追えるようにしてください。

```yaml
evidence_items:
  - id: evidence.kesennuma-example-20260911
    subject: place.kesennuma-fish-market
    checked_at: YYYY-MM-DD
    claims:
      - 確認できた事実だけを書く
    volatility: low | medium | high
    recheck_before_trip: true | false
    source:
      type: official | public_body | routing_service | other
      title: ページ名
      url: https://example.com/direct-page
    date_windows:  # 時間窓がある場合だけ。不要ならキーごと省略
      - date: 2026-09-26
        windows:
          - {start: "09:00", end: "17:00"}
```

`estimates/distances.yaml` への追記候補も示してください。`points[].distance_km` は起点からの累積距離です。再現できる経路数値が得られなければ、値を作らず `distance_update_status: not_ready` としてください。

```yaml
distance_update_status: ready | not_ready
distance_segments:
  - id: distance.kesennuma-city
    date: 2026-09-26
    origin:
      ref: place.kesennuma-fish-market
      label: 気仙沼市魚市場の一般見学入口または駐輪地点
    mode: bicycle
    route_variant: recommended
    display: true
    calculation:
      method: chatgpt_research
      provider: 使用したサービス名
      calculated_at: YYYY-MM-DD
      references:
        - https://example.com/reproducible-route
    points:
      - target: place.kesennuma-umi-no-ichi
        distance_km: 0.0
        confidence: high | medium | low
        note: 入口、駐輪、経由条件
      - target: place.rias-ark-museum
        distance_km: 0.0
        confidence: high | medium | low
        note: 登りと経由条件
```

Issueとcurrent primeへの更新案は、正本へ存在するフィールドだけで表現してください。

```yaml
issue_recommendation:
  existing_issue_id: issue.kesennuma-full-day-feasibility
  proposed_status: open | in_progress | resolved
  proposed_evidence: [evidence.kesennuma-example-20260911]
  proposed_next_action: 未解決作業。resolvedの場合も直前確認事項を記載する
  proposed_resolution: null または解決内容の簡潔な説明
  rationale: 判定理由

plan_day_update:
  date: 2026-09-26
  cycling_distance_km: {min: 0.0, max: 0.0}
  visits:
    - place.kesennuma-fish-market
    - place.kesennuma-umi-no-ichi
    - place.kesennuma-shark-museum
    - place.kesennuma-ice-aquarium
    - place.rias-ark-museum
  optional_visits: []
  food:
    - food.tsurukame-dining-hall
    - food.asahi-zushi-kesennuma
    - food.kitakatsu-maguroya
    - food.kesennuma-bonito-swordfish
  notes:
    - 標準案、短縮案、魚市場不発案の具体的な時刻と判断条件
```

再監査中の2施設は、今回の時間割調査だけを理由に `visits` から `optional_visits` へ移さないでください。標準案と短縮案の分岐は、まず `notes` と調査文書で表現します。公式な休館等で訪問不能と確認できた場合だけ、対象日への最小変更を別途提案してください。

必要なら、9月26日用contingencyの新設を提案してよいですが、既存スキーマの `id`, `name`, `trigger`, `date`, `transport`, `transport_alternatives`, `impacts`, `unresolved` だけを使ってください。`unresolved` は1件以上必要なので、解決後は直前再確認事項を入れてください。

#### 6.10 Codexへの変更指示

調査結果をどの正本へどう反映するか、次を明記してください。

- `evidence/sources.yaml`: 新しい根拠を追記する。既存IDと重複させない。
- `estimates/distances.yaml`: 再現可能な距離だけを追記する。
- `issues.yaml`: `issue.kesennuma-full-day-feasibility` のstatus、evidence、next_action、resolutionを条件に応じて更新する。
- `plan/current.yaml`: 2026-09-26のdayだけを最小限更新する。
- `catalog/routes.yaml`: `route.kesennuma-city` の距離やdescriptionを更新する必要がある場合だけ変更する。
- `research/kesennuma-full-day-feasibility-YYYYMMDD.md`: 調査判断、人が読む時間割、未確認事項、全出典を保存する新規文書として提案する。
- `docs/issues.md`, `docs/itinerary.md`, `docs/pins.md`: 手編集せず、正本YAML反映後に既存レンダラーで再生成する。

変更してはいけないものも明記してください。

- 9月26日以外の日別計画
- Google Mapsのrating、review count、review text、photos
- 別Issueのstatusやresolution
- 宿名未確定のままの宿ラストマイル
- 確認できなかった営業時間、所要時間、距離の推測値

#### 6.11 Codexが実行すべき検証

Codexへ、少なくとも次を依頼してください。

1. 変更した全YAMLがparseできること。
2. `.venv/bin/python tools/validate.py` が成功すること。
3. `.venv/bin/python tools/render.py` で派生文書を再生成し、続けて `.venv/bin/python -m pytest -q` が成功すること。
4. evidence、place、food、route、issueのID重複がないこと。
5. `issues.yaml` と `plan/current.yaml` から参照するIDが各catalogと `evidence/sources.yaml` に存在すること。
6. `date_windows` の時刻が `HH:MM`、日付が `YYYY-MM-DD` であること。
7. 距離台帳の累積距離が訪問順に非減少で、起点・targetのIDが既存正本に存在すること。
8. `resolved` を提案する場合、4つのresolution_conditionsすべてに根拠があること。
9. 既存の未コミット変更を上書きせず、今回の対象外差分を保持すること。

#### 6.12 Codexの完了報告に含める内容

Codexへ、作業終了時に次を報告するよう依頼してください。

- 変更ファイル一覧
- `issue.kesennuma-full-day-feasibility` の最終statusと根拠
- 2026年9月26日の標準案、短縮案、魚市場不発案の反映内容
- 事実、推論、未確認事項
- 旅行直前と宿確定後に残る確認
- YAML parse、schema validation、重複ID、参照整合性、render/testの結果

### 7. 最終セルフチェック

回答前に、次を確認してください。

- 旅行日を2026年9月26日（土）として調査した。
- 対象日固有の情報と通常情報を区別した。
- 魚市場、海の市、シャークミュージアム、氷の水族館、リアス・アーク美術館を別対象として扱った。
- 魚市場と海の市が近くても、駐輪、入口、館内移動をゼロ分にしていない。
- リアス・アーク美術館への登りを移動時間へ反映した。
- 標準案、短縮案、魚市場不発案を作った。
- 再監査中の2施設の採否を確定していない。
- 宿からのラストマイルを確定していない。
- Google Maps情報を再取得・更新していない。
- 事実、推論、未確認事項を分けた。
- 不明な値を推測していない。
- 主要な主張に出典名、直接URL、確認日、変動性、再確認要否がある。
- 4つの解決条件がすべて `met` でない限り `resolved` を提案していない。
- 最終回答が、添付を参照できないCodexへそのまま渡せる自己完結したプロンプトになっている。
- 予約、購入、電話、問い合わせ、メッセージ送信をしていない。

---

## 引き渡しデータ

以下は、ローカルリポジトリからこの依頼に必要な情報だけを抽出したスナップショットです。ChatGPTからローカルパスは参照できないため、調査判断にはこの内容を使ってください。

### Manifest

| 元ファイル | 安定ID・対象 | リポジトリ内の基準日・確認日 | このファイルへの収録範囲 |
|---|---|---|---|
| `trip.yaml` | `sanriku-2026` | 2026-09-11に抽出 | 日程、出発地、交通手段 |
| `constraints.yaml` | `travel-dates`, `solo-travel`, `no-rental-car`, `core-themes`, `bicycle-role` 等 | 2026-09-11に抽出 | 今回に関係する制約 |
| `issues.yaml` | `issue.kesennuma-full-day-feasibility` | identified 2026-09-11、2026-09-11に抽出 | 対象Issue全文 |
| `issues.yaml` | `issue.kesennuma-fish-market`, `issue.kesennuma-meal-selection`, `issue.google-maps-review-text-reassessment`, `issue.lodging-endpoint-routes`, `issue.visit-status-and-cut-order` | 2026-09-11に抽出 | 隣接Issueの境界 |
| `plan/current.yaml` | `plan.sanriku-current-prime-20260911` の2026-09-26 | as_of 2026-09-11 | 当日計画全文 |
| `catalog/routes.yaml` | `route.kesennuma-city` | 2026-09-11に抽出 | ルート候補全文 |
| `catalog/places.yaml` | 当日の5施設 | 2026-09-11に抽出 | 名称、役割、既知の注意 |
| `catalog/food.yaml` | 当日の4食候補・テーマ | 2026-09-11に抽出 | 名称、位置づけ、既知の注意 |
| `catalog/stay_areas.yaml` | `stay.kesennuma` | 2026-09-11に抽出 | 宿名未確定の事実 |
| `evidence/sources.yaml` | 対象と隣接Issueに関係する既存根拠 | 2026-09-03〜2026-09-10確認、2026-09-11に抽出 | 5件の要約 |
| `estimates/distances.yaml` | 全距離台帳 | 2026-09-11に抽出 | `segments: []` |
| `schema/evidence.schema.json`, `schema/distances.schema.json`, `schema/issues.schema.json`, `schema/itinerary.schema.json` | 関連フィールド | 2026-09-11に抽出 | 反映に必要な制約を本文へ転記 |

### 旅行と制約

```yaml
trip:
  id: sanriku-2026
  title: 2026年9月 三陸旅行
  start_date: 2026-09-23
  end_date: 2026-09-28
  origin: 名古屋
  modes: [bicycle, bus, train, ferry, taxi, mixed]
hard_constraints:
  - 2026年9月23日（水・祝）から9月28日（月）までの6日間
  - 大人1名の一人旅
  - レンタカーは使わず、JR、BRT、三陸鉄道、路線バス、船、自転車、必要時の短距離タクシーで組み立てる
  - 交通・宿泊・施設予約はいずれも未確定
soft_constraints:
  - 東日本大震災、津波、震災遺構、復興、被災後の交通再編を旅の主題とする
  - 震災遺構だけに偏らず、漁港、水産業、市場、地域史、生活文化、ローカルフード、珍スポットも探索する
  - 自転車は全区間自走の義務ではなく、点在候補を束ねる価値に応じて使う
```

### 対象Issue（全文）

```yaml
id: issue.kesennuma-full-day-feasibility
title: 9/26気仙沼フルデイの訪問順と時間配分を確定する
status: open
priority: high
category: schedule
identified_at: 2026-09-11
summary: 朝の魚市場、海の市内2施設、リアス・アーク美術館、三食を同日に置いているが、開館時刻、最終入館、標準滞在、移動、駐輪を含む時刻表がない。
impact: 魚市場の水揚げ時間を優先した結果、リアス・アーク美術館または海の市内施設の受付に間に合わないか、食事候補の営業時間と競合する可能性がある。
related_dates: [2026-09-26]
subjects:
  - route.kesennuma-city
  - place.kesennuma-fish-market
  - place.kesennuma-umi-no-ichi
  - place.kesennuma-shark-museum
  - place.kesennuma-ice-aquarium
  - place.rias-ark-museum
  - food.tsurukame-dining-hall
  - food.asahi-zushi-kesennuma
  - food.kitakatsu-maguroya
evidence: [evidence.rias-ark-event-2026]
next_action: 魚市場の目標時刻を起点に、各施設の旅行日固有の開館・最終入館、必要滞在、実走、駐輪、食事営業時間を並べ、通常案と魚市場が不発の場合の案を作る。
resolution_conditions:
  - 各施設の旅行日固有の利用可能時間と必要滞在時間を確認している
  - 移動、駐輪、待ち時間を含む訪問順と到着目標が決まっている
  - 再監査中の2施設を採用する場合と外す場合の両方で一日が成立する
  - 魚市場が不発の場合の繰上げ先と食事時間が決まっている
resolution: null
```

### 2026年9月26日のcurrent prime

```yaml
date: 2026-09-26
start: place.kesennuma
finish: place.kesennuma
cycling: {distance_km: {min: 10, max: 20}}
mobility_strategy:
  - segment: 気仙沼魚市場〜海の市〜リアス・アーク美術館
    preferred_mode: bicycle
    bicycle_value: candidate_linking
    rationale: 約10〜20kmで魚市場、海の市の具体施設、リアス・アーク美術館を束ねる。走行自体は目的にしない。
routes: [route.kesennuma-city]
transport: []
transport_alternatives: []
visits:
  - place.kesennuma-fish-market
  - place.kesennuma-umi-no-ichi
  - place.kesennuma-shark-museum
  - place.kesennuma-ice-aquarium
  - place.rias-ark-museum
optional_visits: []
food:
  - food.tsurukame-dining-hall
  - food.asahi-zushi-kesennuma
  - food.kitakatsu-maguroya
  - food.kesennuma-bonito-swordfish
candidate_decisions: []
stay: {preferred: [stay.kesennuma], fallback: []}
notes:
  - 朝の気仙沼魚市場では荷捌き、水揚げ、入港船、市場前の物流・漁業動線を具体的に確認する。
  - 海の市全体はGoogle Maps 3.8・レビュー約3,900件だが、複合施設の総合値で内部施設を一括評価しない。
  - 気仙沼シャークミュージアムは3.6・レビュー約2,156〜2,200件のためhigh_priority_recheck。氷の水族館は3.8・レビュー約286件のためrecheck_required。どちらも現行動線に残すが、レビュー本文確認まで採用確定扱いにしない。
  - 氷の水族館は施設品質の警戒と、マイナス20度、氷漬けの魚、製氷文化というB級・ローカル適合度を分けて評価する。
  - 魚市場前〜港町〜鹿折の移動中に見える冷蔵庫、加工工場、トラック、漁船は副次的価値とする。特定工場を一般公開施設として扱わない。
  - 鶴亀食堂は4.4・レビュー約454件で、市場前、地域性、朝営業を含め9/26朝食の高優先度候補を維持する。
  - 食は戻り鰹、メカジキ、フカヒレ、モウカの星、サンマ、ホヤ、地魚寿司を個別に評価する。9月下旬は戻り鰹を特に高く評価し、メカジキは冬メカ最盛期より前であることを踏まえる。
  - 朝・昼・夜の最終店選定、市場の最適時刻、2026年の実漁況は未検証。
```

### 現行ルート候補

```yaml
id: route.kesennuma-city
name: 気仙沼魚市場〜海の市〜リアス・アーク周遊
status: shortlisted
from: place.kesennuma
to: place.kesennuma
mode: bicycle
distance_km: {min: 10, max: 20}
route_value: main
tags: [fishery, earthquake, museum]
description: 気仙沼魚市場、海の市、シャークミュージアム、氷の水族館、リアス・アーク美術館を束ねる。魚市場前〜港町〜鹿折の移動中に冷蔵庫、加工工場、トラック、漁船が見えることは副次的価値とし、特定工場の一般公開を前提にしない。
```

### 施設候補

```yaml
- id: place.kesennuma-fish-market
  name: 気仙沼市魚市場
  status: shortlisted
  description: 朝に訪れ、荷捌き、水揚げ、入港船、市場前の物流・漁業動線を具体的に見る主軸。前夜に入船、水揚げ、休場情報を確認する。
- id: place.kesennuma-umi-no-ichi
  name: 気仙沼 海の市
  status: shortlisted
  description: シャークミュージアム、氷の水族館、水産物売場を束ねる具体的な施設。施設全体のGoogle Maps値を内部施設へ転用しない。
- id: place.kesennuma-shark-museum
  name: 気仙沼シャークミュージアム
  status: shortlisted
  description: サメ利用、気仙沼の漁業文化、サメ研究、大型標本等を扱う。Google Mapsは3.6・レビュー約2,156〜2,200件でhigh_priority_recheck。星だけでは削除しないが、今回も採用確定しない。
- id: place.kesennuma-ice-aquarium
  name: 氷の水族館
  status: shortlisted
  description: マイナス20度の空間、氷漬けの魚、製氷文化との接続を評価するB級・ローカル枠。Google Mapsは3.8・レビュー約286件でrecheck_required。今回も採用確定しない。
- id: place.rias-ark-museum
  name: リアス・アーク美術館
  status: shortlisted
  description: 震災資料・地域文化への関心と整合する採用候補。既存計画シードでは9月26日は「新方舟祭2026」の会期内だが、公式再確認が必要。
```

### 食事候補

```yaml
- id: food.tsurukame-dining-hall
  name: 鶴亀食堂
  status: shortlisted
  description: 市場前食堂として地域性と朝営業を評価する9月26日朝食の優先候補。Google Mapsは4.4・レビュー約454件。
- id: food.asahi-zushi-kesennuma
  name: あさひ鮨
  status: shortlisted
  description: ふかひれ寿司、モウカの星、鰹、さんま、ホヤを具体的に比較する有力候補。朝・昼・夜の最終配分は未確定。
- id: food.kitakatsu-maguroya
  name: 北かつまぐろ屋
  status: shortlisted
  description: 漁業者・組合直営系という性格を評価する有力候補。営業日と食事枠は未確定。
- id: food.kesennuma-bonito-swordfish
  name: 気仙沼の季節魚・郷土水産品
  status: shortlisted
  description: 戻り鰹、メカジキ、フカヒレ、モウカの星、サンマ、ホヤ、地魚寿司を料理ごとに評価する。9月下旬は戻り鰹を特に高く評価し、メカジキは冬メカ最盛期より前として扱う。
```

### 宿泊地域

```yaml
id: stay.kesennuma
name: 気仙沼
status: shortlisted
description: 9月25日・26日の2連泊候補。魚市場、旧向洋高校、リアス・アーク美術館を自転車で回る拠点。宿名、所在地、空室、価格は未確認。
```

### 既存根拠

```yaml
- id: evidence.rias-ark-event-2026
  subject: place.rias-ark-museum
  checked_at: 2026-09-03
  claims:
    - 計画シードでは「新方舟祭2026」は2026年9月25日から始まり、9月26日は開催期間内とされている
    - 開館・会期は旅行直前に公式情報で再確認する
  volatility: medium
  recheck_before_trip: true
  source:
    type: user_provided_planning_seed
    title: 2026年9月3日時点の三陸旅行検討結果
    url: null
- id: evidence.google-maps-tsurukame-20260910
  subject: food.tsurukame-dining-hall
  checked_at: 2026-09-10
  claims:
    - Google Mapsは4.4・レビュー約454件
    - 市場前、地域性、朝営業を含め9月26日朝食の高優先度候補を支持する
  volatility: medium
  recheck_before_trip: false
  source:
    type: user_provided_google_maps_reaudit
    title: 2026年9月10日 Google Maps評価・レビュー件数再監査
    url: null
- id: evidence.google-maps-shark-museum-20260910
  subject: place.kesennuma-shark-museum
  checked_at: 2026-09-10
  claims:
    - Google Mapsは3.6・レビュー約2,156〜2,200件
    - 大量レビューの低評価としてhigh_priority_recheckへ変更した
    - 水産業・珍施設への嗜好適合可能性があるため星だけで即削除しない
  volatility: medium
  recheck_before_trip: false
  source: {type: user_provided_google_maps_reaudit, title: 2026年9月10日 Google Maps評価・レビュー件数再監査, url: null}
- id: evidence.google-maps-ice-aquarium-20260910
  subject: place.kesennuma-ice-aquarium
  checked_at: 2026-09-10
  claims:
    - Google Mapsは3.8・レビュー約286件
    - 施設品質は警戒し、B級適合度を別途再評価するrecheck_requiredへ変更した
  volatility: medium
  recheck_before_trip: false
  source: {type: user_provided_google_maps_reaudit, title: 2026年9月10日 Google Maps評価・レビュー件数再監査, url: null}
```

### 隣接Issue

```yaml
- id: issue.kesennuma-fish-market
  priority: medium
  scope: 魚市場へ行く目標時刻、前夜の再確認方法、水揚げや入港船を確認できない場合の時間配分、2026年の実漁況を調べる。
- id: issue.kesennuma-meal-selection
  priority: medium
  scope: 朝・昼・夜それぞれの第一候補と代替候補、食材・料理、営業日、予約要否、current primeからの動線を最終選定する。
- id: issue.google-maps-review-text-reassessment
  priority: high
  scope: 気仙沼シャークミュージアム等のGoogle Mapsレビュー本文と写真を比較し、採用維持、短時間立寄り、保留、除外を再評価する。
- id: issue.lodging-endpoint-routes
  priority: medium
  scope: 宿名確定後に、宿の出入口と最初・最後の候補を結ぶ実走距離と所要時間を確認する。
- id: issue.visit-status-and-cut-order
  priority: high
  scope: 全日程の候補を分類し、遅延時の削減順と判断地点・時刻を決める。今回の対象は9月26日だけ。
```

### 現在の距離台帳

```yaml
schema_version: 1
segments: []
```

## リポジトリの反映条件

- 正本YAMLへ存在しないフィールドを追加しない。
- IDは既存命名規則の小文字英数字とハイフンを使い、既存IDと重複させない。
- `issues.yaml` のstatusは `open | in_progress | resolved | wont_fix`、priorityは `high | medium | low` のみ。
- `evidence/sources.yaml` の各項目は `id`, `subject`, `checked_at`, `claims`, `volatility`, `recheck_before_trip`, `source` が必須。sourceは少なくとも `type`, `url` を持つ。
- `date_windows` を使う場合、date、windows、start、endが必須で、時刻は `HH:MM`。
- `estimates/distances.yaml` のmodeは `bicycle | walk | car | mixed`。calculationは `method`, `provider`, `calculated_at`, `references` が必須。pointsは `target`, `distance_km`, `confidence`, `note` が必須。
- `plan/current.yaml` の日別データでは、`visits` と `optional_visits` に既存place ID、`food` に既存food IDだけを使う。
- `plan/current.yaml` のcontingencyは `unresolved` が1件以上必要。
- 確認できた事実だけをevidenceのclaimsへ入れる。推論と提案は調査文書またはplan notesへ分ける。
- 未確認事項を誤って解決済みにしない。4つの解決条件すべてに根拠がない限り、対象Issueを `resolved` にしない。
- ChatGPTはリポジトリを編集しない。最終回答は、Codexが編集・検証するための自己完結した依頼文として返す。
