# ChatGPT調査依頼: 9/25女川→気仙沼の自走成立性

このファイルは、ChatGPTへそのまま添付して使う自己完結型の調査指示書です。別のローカルファイルは参照できなくても構いません。

ChatGPTには、このファイルを添付したうえで、次の一文だけ送ってください。

> 添付したMarkdownの指示に従って調査し、指定形式で回答してください。

ChatGPTの回答は編集せず、そのままCodexへ戻してください。予約、購入、電話、問い合わせ、メッセージ送信は依頼していません。

---

## ChatGPTへの実行指示

あなたは、長距離サイクリングを含む個人旅行の実行可能性と道路安全を監査するリサーチャーです。Webを調査し、2026年9月25日（金）の `issue.onagawa-kesennuma-feasibility` を、下記の解決条件に照らして解消してください。

目的は旅程全体の作り直しではありません。女川から気仙沼市東日本大震災遺構・伝承館までの1日だけを対象に、現行案を維持できるか、条件付きなら何が必要か、成立しないなら最小限の変更は何かを判断してください。

### 0. Preflight（必須）

本調査を始める前に、次を短く出力してください。

1. 受信できた添付ファイル名を列挙する。
2. `chatgpt-resolve-onagawa-kesennuma-feasibility.md` が読めることを確認する。
3. 同ファイル内の「ChatGPTへの実行指示」と「引き渡しデータ」の両方が読めることを確認する。

このファイル、またはいずれかの必須セクションが見えない場合は、本調査を開始しないでください。不足しているファイル名またはセクション名だけを報告してください。

### 1. 対象Issueと完了条件

- Issue ID: `issue.onagawa-kesennuma-feasibility`
- 対象日: 2026-09-25（金）
- 現在の状態: `open`
- 現在の優先度: `high`
- 主なリスク: 約90〜100kmとされる自走区間の距離、標高、道路安全、トンネル、休憩込み所要時間が未検証で、当日の最優先施設の最終受付に間に合わない可能性がある。

次の4条件をすべて満たす根拠が揃った場合だけ、`resolved` を提案してください。

1. 実走経路、距離、獲得標高、休憩・立寄り込みの所要時間が分かる。
2. 危険区間とトンネルについて、許容可否と回避策が分かる。
3. 気仙沼市東日本大震災遺構・伝承館へ、受付締切の端ではない到着目標がある。
4. 遅延時に切る候補の順序と、判断地点・判断時刻が決まっている。

一部しか確認できなければ `partially_resolved`、重要な根拠が得られなければ `still_open` としてください。情報不足を推測で埋めて `resolved` にしないでください。

### 2. 動かしてはいけない前提

- 旅行日は2026年9月25日（金）。
- 大人1名の一人旅で、荷物を積んだ自転車を使う。
- レンタカーは使わない。短距離タクシーは必要時のみ許容するが、自転車を載せられるとは仮定しない。
- 自転車の能力上限は1日100km程度。長い登り、グラベル、林道、押し歩き、担ぎには対応できる。
- ただし、巡航速度、車種、荷物重量、朝の宿、気仙沼の宿は未確定である。
- 当日の最優先は `place.kesennuma-memorial-museum`（気仙沼市東日本大震災遺構・伝承館、旧向洋高校）。途中候補より優先する。
- 志津川の `place.minamisanriku-disaster-office`（旧防災対策庁舎・南三陸町震災復興祈念公園）は採用中の主軸候補である。
- `place.sansan-shopping-village`、`place.hama-re-utatsu`、`place.oya-coast` は任意候補で、遅延時には削ってよい。
- 南三陸311メモリアルと歌津魚竜化石展示は現行案で保留中。今回の標準行程には追加しない。
- 全線自走そのものは目的ではない。安全や最優先施設の時間窓を守れない場合は、自走短縮や別経路を提案してよい。
- 予約、購入、電話、問い合わせ、メッセージ送信は行わない。

### 3. 起終点と計算上の仮定

宿が未確定なので、コア区間の暫定起点は「女川駅の一般利用者が出入りする地点」としてください。終点は「気仙沼市東日本大震災遺構・伝承館の一般来館者入口または駐輪地点」とし、気仙沼駅や市中心部を終点にしないでください。

宿から女川駅、施設から気仙沼の宿までの距離は、別Issue `issue.lodging-endpoint-routes` の対象です。今回のIssueを `resolved` とする場合も、宿確定後にラストマイルを再計算する必要があることを明記してください。

巡航速度が未確定なので、少なくとも移動平均速度15km/h、18km/h、20km/hの3ケースで計算してください。下りや平地だけの瞬間速度ではなく、走行中の平均速度として扱います。登坂、信号、路面、荷物の影響を別途加味し、停止時間と混ぜないでください。

15km/hケースで成立しないことだけを理由に全案を `no` とせず、どの速度・出発時刻・削減条件なら成立するかを示してください。ただし、実績のない速度を前提に「成立」と断定しないでください。

### 4. 必ず調べること

#### 4.1 施設の時間窓

- 2026年9月25日の開館可否、開館時間、最終受付・最終入館、休館・臨時休館、見学に必要な標準時間、駐輪から受付までの導線を、施設公式情報で確認する。
- 現行案の「16:00最終受付」が正しいか、通常情報ではなく旅行日に有効な情報として検証する。
- 受付締切より30分以上前を基本に、安全な到着目標を提案する。30分では不足または過剰なら理由を示す。

#### 4.2 実走経路と数値

- 女川駅から、旧防災対策庁舎・南三陸町震災復興祈念公園を経由し、必要に応じて歌津、本吉、道の駅大谷海岸付近を通って、気仙沼市東日本大震災遺構・伝承館へ至る自転車向け経路を具体化する。
- 経路を区間に分け、道路番号、主要交差点・橋・峠・トンネル、距離、累積距離、獲得標高、想定走行時間を示す。
- 自動車向け最短経路をそのまま自転車経路とみなさない。自転車通行禁止、歩道通行の可否、迂回、側道、復興道路や自動車専用道路への誤進入を確認する。
- ルート計算結果は、利用した地図・ルーティングサービス、計算日、経由点、ルート設定を示し、再現できるようにする。可能なら共有可能なルートURLまたはGPX取得元を示す。
- ルーティングサービス間で数値が異なる場合は幅と理由を示す。1つのサービスだけの値を高精度な確定値として扱わない。

#### 4.3 道路安全と通行可否

- 国、宮城県、市町、道路管理者、警察等の一次情報を優先し、2026年9月25日に影響する工事、通行止め、片側交互通行、災害規制、自転車通行規制を確認する。
- トンネルごとに名称、延長、照明、路肩・歩道、自転車通行可否、代替経路を確認する。確認できない項目は `unknown` とする。
- 交通量、大型車、路肩の狭さ、舗装、落石・冠水等の現場状況は、一次情報で分からない範囲だけ、できるだけ新しい実走記録や道路映像で補う。
- 地図画像やStreet Viewの撮影年月が古い場合は、その限界を明記する。
- 自転車用前後ライト、反射材等の一般論だけで危険区間を「問題なし」と判定しない。

#### 4.4 時間予算

次を別々に積み上げてください。

- 純走行時間
- 旧防災対策庁舎・南三陸町震災復興祈念公園の滞在
- 補給、昼食、給水、トイレ
- 任意候補の滞在
- 写真、駐輪、道迷い、短い機材調整
- パンク等の軽微な遅延バッファ
- 施設到着後、受付までのバッファ

標準案に加えて、任意候補をすべて切った最小案を作ってください。出発時刻を勝手に1つへ固定せず、各速度ケースについて必要な出発時刻または最終出発時刻を逆算してください。

#### 4.5 チェックポイントと削減規則

少なくとも次の地点について、標準案の目標通過時刻と「これを過ぎたら何を切るか」を示してください。

- 女川駅出発
- 志津川到着・出発
- 歌津付近
- 本吉または道の駅大谷海岸付近
- 気仙沼市東日本大震災遺構・伝承館到着

任意候補の基本削減順は、現行案の位置づけに反しない範囲で提案してください。旧防災対策庁舎・南三陸町震災復興祈念公園を削る必要がある場合は、それを通常の削減ではなく、最優先施設を守るための例外的判断として分けてください。

#### 4.6 回避策・離脱策

- 危険区間の自転車向け迂回路と、その追加距離・時間を確認する。
- 公共交通への切替を提案する場合は、2026年9月25日に有効な便、乗降地点、輪行準備時間、輪行袋入り自転車の持込み条件を公式情報で確認する。
- 輪行可否が未確認なら、公共交通を確実なfallbackとして扱わない。これは別Issue `issue.brt-bicycle-carriage` が未解決であるため。
- 自転車を伴うタクシー利用も、車種や事業者確認なしに確実なfallbackとしない。
- 確実な離脱策が存在しない区間は、その事実自体を安全判断へ反映する。

#### 4.7 日照と直前再確認

- 2026年9月25日の女川・気仙沼周辺の日の出・日没を、公的または天文機関の情報で確認する。
- 通行規制、施設の臨時休館、天候・警報について、前日と当日朝に見るべき公式ページを特定する。
- 天候そのものを長期予報から断定しない。風雨等により発動する中止・短縮条件を提案する。

### 5. 情報源と判断のルール

- 営業、受付、通行規制、自転車通行可否、公共交通の持込み条件は、施設、道路管理者、自治体、警察、交通事業者等の公式情報を最優先する。
- 距離・標高・経路は、経由点と設定を示せるルーティング情報を使う。現場の快適性は最近の実走記録等で補助する。
- 検索結果の抜粋だけを根拠にしない。根拠ページを開いて確認する。
- 主要な主張ごとに、ページ名、直接URL、確認日、情報が対象日に有効かを記録する。
- 事実、情報源からの推論、あなたの提案を明確に分ける。
- 情報が見つからないことと、安全・営業上問題ないことを混同しない。
- 数値の精度を誇張せず、幅、計算条件、確信度を示す。
- 古いブログや古い地図画像を、2026年当日の通行可否の根拠にしない。
- Google Mapsのratingやreview countの再取得は今回の対象外とする。

### 6. 出力形式

日本語で、次の順に出力してください。

#### A. Preflight結果

冒頭で指定した受信確認を記載してください。

#### B. 結論

- Issue判定: `resolved / partially_resolved / still_open`
- 現行の全線自走案: `go / conditional / no-go / unknown`
- 15km/h、18km/h、20km/hの各ケース: `go / conditional / no-go / unknown`
- 推奨する到着目標と、その余裕
- 推奨する出発時刻または最終出発時刻
- 最大の安全・時間リスク3件以内
- 現行案を変える場合の最小変更

#### C. 公式に確認できた時間窓

| subject | 2026-09-25に有効な事実 | source title | direct URL | checked_at | volatility | 再確認要否 |
|---|---|---|---|---|---|---|

対象日固有の情報がない場合は、通常情報と未確認部分を分けてください。

#### D. 実走経路

| 区間 | 経由道路・地点 | 区間km | 累積km | 区間獲得標高 | 累積獲得標高 | トンネル・危険 | 回避策 | 数値の出典 | confidence |
|---|---|---:|---:|---:|---:|---|---|---|---|

経路全体について、再現用の経由点列、利用サービス、設定、共有URLまたはGPX取得元も記載してください。

#### E. トンネル・危険区間台帳

| 名称・区間 | 道路 | 延長 | 照明 | 路肩・歩道 | 自転車通行可否 | 交通・現場状況 | 代替 | 根拠 | 判定 |
|---|---|---:|---|---|---|---|---|---|---|

#### F. 時間予算と速度別成立性

標準案と、任意候補をすべて切った最小案を分けてください。

| ケース | 移動平均速度 | 純走行 | 必須滞在 | 補給・昼食 | 任意滞在 | 小休止等 | 遅延buffer | 受付前buffer | 合計 | 必要出発時刻 | 到着見込 | 判定 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|

#### G. 現地運用表

| チェックポイント | 目標時刻 | 打切り時刻 | 遅れた場合に切るもの | 次の判断 | 根拠 |
|---|---|---|---|---|---|

この表だけを現地で見ても判断できる粒度にしてください。任意候補の最終的な削減順を明記してください。

#### H. 回避策・離脱策

| 発動条件 | 手段 | 追加距離・時間 | 自転車の扱い | 対象日に利用可能か | 確信度 | 残る確認 |
|---|---|---:|---|---|---|---|

#### I. Issue解決条件の充足判定

| 解決条件 | met / not_met / unknown | 根拠 | 残る作業 |
|---|---|---|---|

4条件すべてが `met` でない限り、`resolved` を提案しないでください。

#### J. レポジトリへ反映できるデータ

まず `evidence/sources.yaml` 用候補を、以下のスキーマに合うYAMLで出してください。1つの出典が複数の独立した主張を支える場合は、主張単位が追えるように分けてください。

```yaml
evidence_items:
  - id: evidence.onagawa-kesennuma-example-20260911
    subject: route.onagawa-kesennuma-coast
    checked_at: 2026-09-11
    claims:
      - 確認できた事実
    volatility: low | medium | high
    recheck_before_trip: true | false
    source:
      type: official | public_body | routing_service | recent_user_report | other
      title: ページ名
      url: https://example.com/direct-page
    date_windows:  # 時間窓がある場合だけ。なければキーごと省略
      - date: 2026-09-25
        windows:
          - {start: "09:00", end: "16:00"}
```

次に `estimates/distances.yaml` 用候補を出してください。`points` の `distance_km` は起点からの累積距離です。正確に算出できない値は作らず、このブロック自体を `not_ready` としてください。

```yaml
distance_update_status: ready | not_ready
distance_segments:
  - id: distance.onagawa-kesennuma-coast
    date: 2026-09-25
    origin:
      ref: place.onagawa
      label: 女川駅
    mode: bicycle
    route_variant: recommended
    display: true
    calculation:
      method: chatgpt_research
      provider: 使用したサービス名
      calculated_at: 2026-09-11
      references:
        - https://example.com/reproducible-route
    points:
      - target: place.minamisanriku-disaster-office
        distance_km: 0.0
        confidence: high | medium | low
        note: 経由条件と注意
      - target: place.kesennuma-memorial-museum
        distance_km: 0.0
        confidence: high | medium | low
        note: 経由条件と注意
```

最後にIssueとcurrent primeへの更新提案を出してください。スキーマにないフィールドを既存YAMLへ追加しないでください。

```yaml
issue_recommendation:
  existing_issue_id: issue.onagawa-kesennuma-feasibility
  proposed_status: open | in_progress | resolved
  proposed_evidence: [evidence.onagawa-kesennuma-example-20260911]
  proposed_next_action: 残作業。解決済みなら直前再確認だけを記載
  proposed_resolution: null
  rationale: 判定理由

plan_update:
  date: 2026-09-25
  cycling_distance_km: {min: 0.0, max: 0.0}
  mobility_strategy_recommendation: bicycle | mixed | public_transport
  visits: [place.minamisanriku-disaster-office, place.kesennuma-memorial-museum]
  optional_visits: [削減順を反映したID]
  notes:
    - スキーマ上notesへ追加できる具体的な到着目標、出発時刻、チェックポイント

contingency_update:
  id: contingency.kesennuma-memorial-deadline
  trigger: 数値化した発動条件
  impacts: [発動時に行うこと]
  unresolved: [未解決事項。なければ空配列ではなく「直前に再確認する事項」を記載]
```

#### K. 未確認事項と直前チェック

未確認の理由、確認手段、確認する日、現行案への影響を表にしてください。前日と当日朝に開く公式URLをまとめてください。

#### L. 出典一覧

重複を除き、公式・公的情報、ルーティング・地図、最近の実走報告の順にまとめてください。各出典には直接URLと確認日を付けてください。

### 7. 最終セルフチェック

回答前に、次を確認してください。

- 旅行日を2026年9月25日として調査した。
- 終点を気仙沼市中心部ではなく、震災遺構・伝承館の入口または駐輪地点にした。
- 自動車専用道路を自転車経路へ含めていない。
- 距離、標高、走行時間の計算条件と出典を示した。
- 走行時間と停止時間を分けた。
- 最終受付時刻の端ではなく到着余裕を置いた。
- 任意候補の削減順とチェックポイント時刻を数値化した。
- 公共交通やタクシーを、輪行・積載条件未確認のまま確実なfallbackにしていない。
- 事実、推論、提案を分けた。
- 不明な値を推測していない。
- 主要な主張に直接URL、確認日、変動性、再確認要否がある。
- 4つの解決条件がすべて `met` でない限り `resolved` にしていない。
- 予約、購入、電話、問い合わせ、メッセージ送信をしていない。

---

## 引き渡しデータ

以下は、ローカルリポジトリからこの依頼に必要な情報だけを抽出したスナップショットです。ChatGPTからローカルパスは参照できないため、調査判断にはこの内容を使ってください。

### Manifest

| 元ファイル | 安定ID・対象 | リポジトリ内の基準日・確認日 | このファイルへの収録範囲 |
|---|---|---|---|
| `trip.yaml` | `sanriku-2026` | 2026-09-11に抽出 | 日程、出発地、交通手段 |
| `constraints.yaml` | `travel-dates`, `solo-travel`, `no-rental-car`, `bicycle-role`, `cycling-capability` 等 | 2026-09-11に抽出 | 関連するハード・ソフト制約 |
| `issues.yaml` | `issue.onagawa-kesennuma-feasibility` | identified 2026-09-09、2026-09-11に抽出 | Issue全文 |
| `issues.yaml` | `issue.onagawa-kesennuma-route-value`, `issue.brt-bicycle-carriage`, `issue.lodging-endpoint-routes` | 2026-09-11に抽出 | 境界条件の要約 |
| `plan/current.yaml` | `plan.sanriku-current-prime-20260910` の2026-09-25 | as_of 2026-09-10、2026-09-11に抽出 | 当日計画とcontingency |
| `catalog/routes.yaml` | `route.onagawa-kesennuma-coast` | 2026-09-11に抽出 | 経路候補全文 |
| `catalog/places.yaml` | 当日の訪問・任意候補 | 2026-09-11に抽出 | 名称、位置づけ、既知の注意 |
| `catalog/stay_areas.yaml` | `stay.onagawa`, `stay.kesennuma` | 2026-09-11に抽出 | 宿泊地域と宿未確定の事実 |
| `evidence/sources.yaml` | 対象Issueの根拠 | 2026-09-11に抽出 | 対象Issueに紐づく根拠が空である事実 |
| `estimates/distances.yaml` | 全距離台帳 | 2026-09-11に抽出 | `segments: []` |

### 旅行の基本情報

```yaml
id: sanriku-2026
title: 2026年9月 三陸旅行
start_date: 2026-09-23
end_date: 2026-09-28
origin: 名古屋
modes: [bicycle, bus, train, ferry, taxi, mixed]
```

### 関連制約

```yaml
hard:
  - id: travel-dates
    description: 2026年9月23日（水・祝）から9月28日（月）までの6日間とする
  - id: solo-travel
    description: 大人1名の一人旅として交通・宿泊を組み立てる
  - id: no-rental-car
    description: レンタカーは使わず、JR、BRT、三陸鉄道、路線バス、船、自転車、必要時の短距離タクシーで組み立てる
  - id: no-bookings-yet
    description: 現時点では交通・宿泊・施設予約のいずれも確定扱いにしない
soft:
  - id: core-themes
    description: 東日本大震災、津波、震災遺構、復興、被災後の交通再編を旅の主題とする
  - id: bicycle-role
    description: 自転車旅行だから全区間を自走するという思想は採用せず、走行自体の価値、点在候補を束ねる価値、純粋移動の3類型を区間ごとに判定して使う
  - id: avoid-low-value-roads
    description: 自転車で得られる付加価値が低い純粋移動区間は、全線接続にこだわらず公共交通・輪行へ切り替える
  - id: cycling-capability
    description: 自転車は1日100km程度までを許容し、長い登り、グラベル、林道、押し歩き、担ぎにも対応できる
```

### 対象Issue（全文）

```yaml
id: issue.onagawa-kesennuma-feasibility
title: 9/25女川→気仙沼の自走と16:00最終受付を成立させる
status: open
priority: high
category: safety
identified_at: 2026-09-09
summary: 実走距離、道路の快適性、危険区間、トンネル、途中候補の所要時間が未検証で、気仙沼震災遺構へ16:00までに着ける保証がない。
impact: この日の最優先である気仙沼震災遺構を見られず、翌日の気仙沼フルデイにも影響する。
related_dates: [2026-09-25]
subjects: [route.onagawa-kesennuma-coast, place.minamisanriku-disaster-office, place.sansan-shopping-village, place.hama-re-utatsu, place.oya-coast, place.kesennuma-memorial-museum]
evidence: []
next_action: 自転車ルーティング、実走記録、道路管理者の情報から区間別所要、危険、トンネルを確認し、途中候補の優先順位と通過期限を決める。
resolution_conditions:
  - 実走距離、標高、休憩込み所要時間が分かっている
  - 危険区間とトンネルの許容可否、回避策を確認している
  - 気仙沼震災遺構へ十分な余裕を持つ到着目標がある
  - 遅延時に切る途中候補の順序と判断地点・時刻が決まっている
resolution: null
```

### 隣接Issueとの境界

```yaml
- id: issue.onagawa-kesennuma-route-value
  priority: medium
  scope: 道路区間ごとの景観・観察対象と、全線自走そのものの付加価値を再評価する。今回の安全・締切判断に必要な範囲だけ触れ、満足度の総合再評価までは行わない。
- id: issue.brt-bicycle-carriage
  priority: high
  scope: 気仙沼線BRT・大船渡線BRTの輪行袋入り自転車の持込みを正式確認する。未解決なので、公式な持込み条件を確認できないBRTを確実なfallbackにしない。
- id: issue.lodging-endpoint-routes
  priority: medium
  scope: 宿名確定後に、宿と最初・最後の候補を結ぶ実走動線を確認する。今回は女川駅を暫定起点とする。
```

### 2026-09-25のcurrent prime

```yaml
date: 2026-09-25
start: place.onagawa
finish: place.kesennuma
cycling: {distance_km: {min: 90, max: 100}}
mobility_strategy:
  - segment: 女川→志津川→歌津→本吉→大谷海岸→気仙沼
    preferred_mode: bicycle
    bicycle_value: intercity_mobility
    rationale: current primeで最も都市間移動色が強い区間。原則全線自走とするが、走行自体の価値を沿岸という理由だけで過大評価しない。
routes: [route.onagawa-kesennuma-coast]
transport: []
transport_alternatives: []
visits:
  - place.minamisanriku-disaster-office
  - place.kesennuma-memorial-museum
optional_visits:
  - place.sansan-shopping-village
  - place.hama-re-utatsu
  - place.oya-coast
food: []
candidate_decisions:
  - subject: place.minamisanriku-311-memorial
    decision: on_hold
    rationale: 開館日ではあるが時間コストが大きく、気仙沼震災遺構の16:00最終受付を優先するため保留する。
  - subject: place.utatsu-ichthyosaur-display
    decision: on_hold
    rationale: 歌津魚竜は地域テーマとして認識するが、通常旅行者が短時間で強く回収できる対象としては弱く、current primeでは優先度を下げる。
stay: {preferred: [stay.kesennuma], fallback: []}
notes:
  - 気仙沼市東日本大震災遺構・伝承館の最終受付16:00をこの日の最優先とし、遅れた場合は途中候補を切る。
  - 志津川では南三陸町震災復興祈念公園と旧防災対策庁舎を主軸にし、さんさん商店街は動線上で時間が許せば立ち寄る。
  - ハマーレ歌津はローカル商業とかもめ館等を15分程度で確認する候補。道の駅大谷海岸は補給と短時間休憩に使い、主目的にしない。
  - Google Maps再監査後も歌津に「絶対に止まるべき強い対象」は未確保。
  - 食事は9/26と独立に、その土地で一食を使う価値、季節性、動線コスト、16:00締切との両立で評価する。この食事枠では現時点で強い候補を発見できていない。
  - 実走距離、道路の快適性、危険区間、トンネル、走行自体に特別な価値がある区間、16:00到達余裕は未検証。
```

### 現行contingency

```yaml
id: contingency.kesennuma-memorial-deadline
name: 9/25気仙沼震災遺構の締切優先
trigger: 16:00最終受付への到着余裕が計画値を下回る
date: 2026-09-25
transport: []
transport_alternatives: []
impacts:
  - 途中候補を下位から削り、気仙沼震災遺構を守る
  - 南三陸311メモリアル、歌津魚竜関連、道の駅大谷海岸等の滞在を追加しないか短縮する
unresolved:
  - 途中候補の最終優先順位と各チェックポイントの通過期限を決める
```

### 現行ルート候補

```yaml
id: route.onagawa-kesennuma-coast
name: 女川→南三陸→歌津→大谷海岸→気仙沼
status: researching
from: place.onagawa
to: place.kesennuma
mode: bicycle
distance_km: {min: 90, max: 100}
route_value: main
tags: [current-prime, intercity, deadline-sensitive]
description: current primeで最も都市間移動色が強い約90〜100kmの全線自走区間。志津川、歌津、道の駅大谷海岸の停止候補を通り、16:00最終受付の気仙沼震災遺構を最優先する。走行自体に特別な価値がある道路区間は未確認であり、沿岸という理由だけで価値を水増ししない。
```

### 立寄り候補の位置づけ

```yaml
- id: place.minamisanriku-disaster-office
  name: 旧防災対策庁舎・南三陸町震災復興祈念公園
  status: shortlisted
  role: required
  description: 9/25志津川の主軸。旧防災対策庁舎と南三陸町震災復興祈念公園を具体対象として訪ねる。南三陸311メモリアルは別の保留候補として扱う。
- id: place.sansan-shopping-village
  name: 南三陸さんさん商店街
  status: shortlisted
  role: optional
  description: 志津川の動線上で立ち寄る商業施設。
- id: place.hama-re-utatsu
  name: 南三陸ハマーレ歌津
  status: researching
  role: optional
  description: ローカル商業とかもめ館等を15分程度で確認する候補。9/25の進行と気仙沼震災遺構の最終受付を優先する。
- id: place.oya-coast
  name: 道の駅 大谷海岸
  status: researching
  role: optional_rest
  description: 9/25の補給・短時間休憩候補。主目的にはしない。
- id: place.kesennuma-memorial-museum
  name: 気仙沼市東日本大震災遺構・伝承館（旧向洋高校）
  status: shortlisted
  role: highest_priority
  description: 9/25の最優先。門脇小学校とは異なる大型実物遺構で、現行計画では最終受付16:00を守る。旅行日直前に公式情報を再確認する。
```

### 宿泊地域と起終点の限界

```yaml
- id: stay.onagawa
  name: 女川
  description: 9/24の1泊候補。宿名・空室・価格は未確認。
- id: stay.kesennuma
  name: 気仙沼
  description: 9/25・9/26の2連泊候補。宿名・空室・価格は未確認。
```

### 現在の根拠・距離台帳

```yaml
issue_evidence: []
distance_estimates:
  schema_version: 1
  segments: []
```

したがって、現行の90〜100km、16:00最終受付、道路安全、標高、所要時間、チェックポイント時刻はいずれも、今回あらためて外部根拠で検証する必要があります。
