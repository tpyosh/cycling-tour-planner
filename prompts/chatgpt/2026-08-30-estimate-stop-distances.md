# 自転車旅程の立ち寄り地点までの概算距離を調べてください

2026年9月に自転車旅行を計画しています。各立ち寄り場所について、その日のスタート地点から予定ルートに沿って自転車で走った場合の累計距離を概算してください。

Web検索、公開されている地図・道路情報、施設の所在地情報などを使ってください。直線距離ではなく、実際に通行可能と思われる道路に沿った距離を優先します。厳密なルート計算ができない場合は、周辺道路や区間距離から推定し、推定箇所を明記してください。距離は1 km単位に丸めます。

## 計算条件

- 基本的に自転車で走行する
- 各日の立ち寄り場所は記載順に訪問する
- 各日のスタート地点を0 kmとした累計距離を求める
- フェリーと鉄道の移動距離は自転車累計に含めない
- フェリーや鉄道で移動した後は、到着地点を0 kmとして自転車累計を再開する
- 登山道や施設内の徒歩距離は含めない
- 「市街」「中心部」は、代表的な駅または市街中心を基準点とし、採用地点を明記する
- 立ち寄り場所が広い場合は、一般的な入口、駐車場、ビジターセンターなどを到着点とする
- 通行できるか不明な道路を、根拠なく経路へ含めない

## 調査対象

### 9月22日：むつ市街から下風呂温泉

予定経路は「むつ市街→恐山→薬研→下風呂温泉」です。

1. 恐山菩提寺
2. 三途の川 太鼓橋
3. 奥薬研修景公園
4. 元祖かっぱの湯
5. 下風呂温泉

### 9月23日：下風呂温泉から大間、函館

第1区間は「下風呂温泉→大間崎→大間フェリーターミナル」です。

1. 大間崎

その後、大間から函館へフェリーで移動します。第2区間は函館フェリーターミナルを0 kmとして計算してください。

1. 函館市北方民族資料館
2. シゲちゃんすし

### 9月24日：函館市街から鹿部

予定経路は「函館市街→戸井→恵山→水無海浜温泉→南茅部→鹿部」です。

通常の立ち寄り場所：

1. 旧戸井線アーチ橋
2. 恵山
3. 水無海浜温泉

任意の立ち寄り場所：

4. 函館市縄文文化交流センター
5. 垣ノ島遺跡
6. 鹿部間歇泉公園

任意の立ち寄り場所は、記載順にすべて訪問した場合の累計距離を求めてください。可能であれば、基本ルートに対する追加距離も示してください。

### 9月25日：鹿部から八雲、盤石温泉

予定経路は「鹿部→森町→八雲町中心部→盤石温泉→八雲町中心部」です。

1. 八雲町郷土資料館
2. 八雲町木彫り熊資料館
3. 盤石温泉

八雲町郷土資料館と八雲町木彫り熊資料館が同一または隣接施設であれば、その旨も示してください。

### 9月26日：洞爺方面から登別温泉

八雲町中心部から洞爺方面までは鉄道輪行します。鉄道距離は自転車累計に含めません。

自転車区間は、ひとまず洞爺駅を0 kmとします。予定経路は「洞爺駅→有珠山噴火遺構→オサル湯→オロフレ峠→登別温泉」です。

1. 西山山麓火口散策路
2. 金比羅火口災害遺構散策路
3. オサル湯
4. オロフレ峠
5. 登別地獄谷

洞爺駅より適切な輪行終了地点があれば、理由とともに提案してください。ただし、提案ルートと洞爺駅起点の距離は混ぜず、別々に示してください。

### 9月27日：登別温泉から苫小牧西港

予定経路は「登別温泉→白老→苫小牧西港フェリーターミナル」です。

1. ウポポイ
2. 国立アイヌ民族博物館
3. 仙台藩白老元陣屋資料館
4. 白老仙台藩陣屋跡

同一敷地内にある施設間の自転車移動は加算せず、その旨を示してください。

## 回答形式

最初に、基準点として採用した場所と、重要な経路上の仮定を箇条書きで示してください。その後、次のYAMLを埋めてください。キー名とIDは変更しないでください。距離を特定できない地点は`points`から省き、YAMLの後に理由を書いてください。

```yaml
schema_version: 1
segments:
  - id: distance.20260922-mutsu-shimofuro
    date: "2026-09-22"
    origin: {ref: stay.mutsu, label: "採用したスタート地点"}
    mode: bicycle
    route_variant: main
    display: true
    calculation:
      method: chatgpt_research
      provider: "ChatGPT Web調査"
      calculated_at: "2026-08-30"
      references: []
    points:
      - {target: place.osorezan, distance_km: 0, confidence: high, note: ""}
      - {target: place.sanzu-river, distance_km: 0, confidence: medium, note: ""}
      - {target: place.okuyagen, distance_km: 0, confidence: medium, note: ""}
      - {target: place.ganso-kappa-no-yu, distance_km: 0, confidence: medium, note: ""}
      - {target: place.shimofuro-onsen, distance_km: 0, confidence: medium, note: ""}

  - id: distance.20260923-shimofuro-oma
    date: "2026-09-23"
    origin: {ref: stay.shimofuro, label: "採用した下風呂温泉の基準点"}
    mode: bicycle
    route_variant: main
    display: true
    calculation: {method: chatgpt_research, provider: "ChatGPT Web調査", calculated_at: "2026-08-30", references: []}
    points:
      - {target: place.oma-cape, distance_km: 0, confidence: medium, note: ""}

  - id: distance.20260923-hakodate
    date: "2026-09-23"
    origin: {label: "採用した函館側の基準点"}
    mode: bicycle
    route_variant: main
    display: true
    calculation: {method: chatgpt_research, provider: "ChatGPT Web調査", calculated_at: "2026-08-30", references: []}
    points:
      - {target: place.hakodate-northern-peoples-museum, distance_km: 0, confidence: medium, note: ""}
      - {target: food.shigechan-sushi, distance_km: 0, confidence: medium, note: ""}

  - id: distance.20260924-hakodate-shikabe
    date: "2026-09-24"
    origin: {ref: stay.hakodate, label: "採用したスタート地点"}
    mode: bicycle
    route_variant: all-optional
    display: true
    calculation: {method: chatgpt_research, provider: "ChatGPT Web調査", calculated_at: "2026-08-30", references: []}
    points:
      - {target: place.toi-line-arch, distance_km: 0, confidence: medium, note: ""}
      - {target: place.esan, distance_km: 0, confidence: medium, note: ""}
      - {target: place.mizunashi-kaihin-onsen, distance_km: 0, confidence: medium, note: ""}
      - {target: place.jomon-center, distance_km: 0, additional_distance_km: 0, confidence: medium, note: ""}
      - {target: place.kakinoshima, distance_km: 0, additional_distance_km: 0, confidence: medium, note: ""}
      - {target: place.shikabe-geyser, distance_km: 0, additional_distance_km: 0, confidence: medium, note: ""}

  - id: distance.20260925-shikabe-banjaku
    date: "2026-09-25"
    origin: {ref: stay.shikabe, label: "採用したスタート地点"}
    mode: bicycle
    route_variant: main
    display: true
    calculation: {method: chatgpt_research, provider: "ChatGPT Web調査", calculated_at: "2026-08-30", references: []}
    points:
      - {target: place.yakumo-local-museum, distance_km: 0, confidence: medium, note: ""}
      - {target: place.yakumo-bear-museum, distance_km: 0, confidence: medium, note: ""}
      - {target: place.banjaku-onsen, distance_km: 0, confidence: low, note: ""}

  - id: distance.20260926-toya-noboribetsu
    date: "2026-09-26"
    origin: {label: "採用した輪行終了地点"}
    mode: bicycle
    route_variant: main
    display: true
    calculation: {method: chatgpt_research, provider: "ChatGPT Web調査", calculated_at: "2026-08-30", references: []}
    points:
      - {target: place.nishiyama-crater, distance_km: 0, confidence: medium, note: ""}
      - {target: place.kompira-eruption-ruins, distance_km: 0, confidence: medium, note: ""}
      - {target: place.osaru-yu, distance_km: 0, confidence: low, note: ""}
      - {target: place.orofure-pass, distance_km: 0, confidence: medium, note: ""}
      - {target: place.noboribetsu-jigokudani, distance_km: 0, confidence: medium, note: ""}

  - id: distance.20260927-noboribetsu-tomakomai
    date: "2026-09-27"
    origin: {ref: stay.noboribetsu-onsen, label: "採用したスタート地点"}
    mode: bicycle
    route_variant: main
    display: true
    calculation: {method: chatgpt_research, provider: "ChatGPT Web調査", calculated_at: "2026-08-30", references: []}
    points:
      - {target: place.upopoy, distance_km: 0, confidence: high, note: ""}
      - {target: place.national-ainu-museum, distance_km: 0, confidence: high, note: ""}
      - {target: place.shiraoi-jinya-museum, distance_km: 0, confidence: high, note: ""}
      - {target: place.shiraoi-jinya, distance_km: 0, confidence: high, note: ""}
```

`confidence`は次の基準で指定してください。

- `high`: 地図や公式所在地から道路距離をかなり確実に判断できる
- `medium`: 経路や基準点に多少の幅がある
- `low`: 通行経路、進入路、到着点などに大きな不確実性がある

参照したWebページのURLは、対応する区間の`calculation.references`へ入れてください。YAMLの後に、距離を特定できなかった地点と理由を列挙してください。計算結果と現在の予定走行距離に大きな矛盾があれば、その点も指摘してください。

# Answer

以下では、**自転車で到達できる地点まで**を距離に含め、散策路・登山道・温泉までの徒歩区間は除外しています。特に基準点・到着点は次のように置きました。

* 9/22の「むつ市街」は**むつ市役所本庁舎（中央1丁目8-1）**を0 kmとしました。恐山―薬研間は県道4号を使用します。国道279号側へ抜ける**正津川林道は一般車両通行止め**で、ナビに表示されても通り抜け不可です。実走記録では下風呂―薬研23 km、薬研―恐山15 km程度で、公式案内でも薬研―奥薬研は約2 kmです。 ([むつ市公式サイト][1])
* 恐山菩提寺→三途の川太鼓橋は約0.5 km。訪問順が「菩提寺→三途の川」なので、この短い戻りも累計に入れています。 ([じゃらん][2])
* 9/23の下風呂は**海峡の湯前**を温泉街中心として採用。大間崎まで約19 km、大間崎からフェリーターミナルまでさらに約4 kmなので、乗船時点では約23 kmです。
* 函館側は**津軽海峡フェリー函館フェリーターミナル（港町3-19-2）**で0 kmにリセットします。北方民族資料館は末広町21-7、シゲちゃんすしは中島町14-10です。 ([津軽海峡フェリー株式会社 |][3])
* 9/24の「函館市街」は**JR函館駅**を0 kmとしました。「恵山」は**恵山火口原駐車場**への到着として扱い、そこから山頂への登山は含めません。旧戸井線アーチ橋は立入禁止・周辺私有地のため、**国道278号側から見られる地点**を到着点とします。水無海浜温泉へは海岸をショートカットせず、公道を迂回します。 ([函館市公式サイト][4])
* 函館市縄文文化交流センターと垣ノ島遺跡は**駐車場を共用し、遺跡入口が駐車場横**なので、自転車移動は0 km扱いです。 ([函館市公式サイト][5])
* 9/25は**道の駅しかべ間歇泉公園**を鹿部の基準点としました。八雲町郷土資料館と木彫り熊資料館は**入口共通の隣接施設**なので同一距離です。盤石温泉は、直近のアクセス情報で車両進入実績のある**小橋手前の駐車可能地点**までとし、その先の徒歩を除外しています。ここは未舗装区間と道路状況の変動があるためlowです。 ([八雲町公式サイト][6])
* 9/26は**JR洞爺駅**をそのまま0 kmにするのが妥当と判断しました。有珠駅などへ乗り越しても西山火口へのアクセスが改善せず、予定ルートに対する明確な利点がありません。西山は北口側駐車地点、金比羅は洞爺湖ビジターセンター周辺、オサル湯は国道453号沿いの道路側到着地点まで、オロフレ峠は**旧オロフレ峠側の展望・駐車地点**までです。盤渓付近の閉鎖された近道は使わず、国道453号→道道2号を使う前提です。 ([洞爺湖温泉観光協会][7])
* 9/27は**登別温泉バスターミナル付近**を温泉街中心として採用。国立アイヌ民族博物館はウポポイ園内なので0 km加算、仙台藩白老元陣屋資料館と陣屋跡も同一史跡内なので0 km加算です。 ([ウポポイ][8])

9/24の位置関係はこの地図で確認できます。

なお、ChatGPTの出力UIでは生URLをコードブロックへ直接埋め込めないため、`calculation.references` には機械可読な参照IDを入れ、**YAML直後に各IDと実際のWebページへのクリック可能なリンクを対応付けています**。

```yaml
schema_version: 1

segments:

  - id: distance.20260922-mutsu-shimofuro
    date: "2026-09-22"
    origin: {ref: stay.mutsu, label: "むつ市役所本庁舎（むつ市街中心）"}
    mode: bicycle
    route_variant: main
    display: true
    calculation:
      method: chatgpt_research
      provider: "ChatGPT Web調査"
      calculated_at: "2026-08-30"
      references:
        - source:mutsu-osore
        - source:osore-sanzu
        - source:shimokita-road-distances
        - source:mutsu-yagen
        - source:shozugawa-closure
    points:
      - {target: place.osorezan, distance_km: 15, confidence: high, note: "恐山菩提寺の一般参拝入口まで。県道4号で概算。"}
      - {target: place.sanzu-river, distance_km: 16, confidence: medium, note: "菩提寺から約0.5 km戻る訪問順を反映。太鼓橋付近まで。"}
      - {target: place.okuyagen, distance_km: 32, confidence: medium, note: "県道4号経由。恐山―薬研約15 km、薬研―奥薬研約2 kmを基礎に推定。"}
      - {target: place.ganso-kappa-no-yu, distance_km: 32, confidence: medium, note: "奥薬研の自転車到達地点から先は徒歩扱い。徒歩距離は加算しない。"}
      - {target: place.shimofuro-onsen, distance_km: 57, confidence: medium, note: "奥薬研から薬研へ約2 km戻り、実走記録の薬研―下風呂約23 kmを加算。正津川林道は不使用。"}

  - id: distance.20260923-shimofuro-oma
    date: "2026-09-23"
    origin: {ref: stay.shimofuro, label: "下風呂温泉 海峡の湯前"}
    mode: bicycle
    route_variant: main
    display: true
    calculation: {method: chatgpt_research, provider: "ChatGPT Web調査", calculated_at: "2026-08-30", references: [source:shimofuro-oma-road, source:oma-terminal]}
    points:
      - {target: place.oma-cape, distance_km: 19, confidence: high, note: "海峡の湯付近から国道279号系統。大間崎からフェリーターミナルへはさらに約4 km、乗船時点で約23 km。"}

  - id: distance.20260923-hakodate
    date: "2026-09-23"
    origin: {label: "津軽海峡フェリー函館フェリーターミナル（港町3-19-2）"}
    mode: bicycle
    route_variant: main
    display: true
    calculation: {method: chatgpt_research, provider: "ChatGPT Web調査", calculated_at: "2026-08-30", references: [source:hakodate-ferry-terminal, source:hakodate-northern-peoples, source:shigechan]}
    points:
      - {target: place.hakodate-northern-peoples-museum, distance_km: 6, confidence: medium, note: "港町のフェリーターミナルから一般道で末広町21-7へ。所在地と市街道路から推定。"}
      - {target: food.shigechan-sushi, distance_km: 10, confidence: medium, note: "北方民族資料館から中島町14-10へ約4 kmと推定。累計約10 km。"}

  - id: distance.20260924-hakodate-shikabe
    date: "2026-09-24"
    origin: {ref: stay.hakodate, label: "JR函館駅"}
    mode: bicycle
    route_variant: all-optional
    display: true
    calculation: {method: chatgpt_research, provider: "ChatGPT Web調査", calculated_at: "2026-08-30", references: [source:toi-arch, source:esan-access, source:mizunashi, source:jomon-center, source:kakinoshima, source:donan-cycle-route]}
    points:
      - {target: place.toi-line-arch, distance_km: 25, confidence: medium, note: "汐首町441番地先。橋梁への立入りはせず、国道278号側の見学可能地点まで。"}
      - {target: place.esan, distance_km: 45, confidence: high, note: "恵山火口原駐車場まで。山頂までの登山距離は含めない。"}
      - {target: place.mizunashi-kaihin-onsen, distance_km: 68, confidence: medium, note: "火口原から国道278号側へ戻り、恵山岬町へ公道迂回。直線的な海岸ショートカットは使用しない。"}
      - {target: place.jomon-center, distance_km: 95, additional_distance_km: 0, confidence: medium, note: "臼尻町551-1。南茅部を通る基本ルート沿いで、1 km丸めでは追加距離0。"}
      - {target: place.kakinoshima, distance_km: 95, additional_distance_km: 0, confidence: high, note: "縄文文化交流センターと駐車場共用。自転車移動を加算しない。"}
      - {target: place.shikabe-geyser, distance_km: 110, additional_distance_km: 0, confidence: medium, note: "鹿部側の基準終点として採用。基本ルートの終点自体なので追加距離0。"}

  - id: distance.20260925-shikabe-banjaku
    date: "2026-09-25"
    origin: {ref: stay.shikabe, label: "道の駅しかべ間歇泉公園"}
    mode: bicycle
    route_variant: main
    display: true
    calculation: {method: chatgpt_research, provider: "ChatGPT Web調査", calculated_at: "2026-08-30", references: [source:shikabe-yakumo, source:yakumo-museums, source:banjaku-access]}
    points:
      - {target: place.yakumo-local-museum, distance_km: 67, confidence: medium, note: "鹿部→森町→八雲中心部。末広町154の資料館まで。"}
      - {target: place.yakumo-bear-museum, distance_km: 67, confidence: high, note: "郷土資料館と隣接し入口共通。同一地点として自転車移動0 km。"}
      - {target: place.banjaku-onsen, distance_km: 92, confidence: low, note: "八雲中心部から約25 km。直近のアクセス記録で車両進入実績のある小橋手前の駐車可能地点まで。未舗装区間・道路状態に不確実性あり。"}

  - id: distance.20260926-toya-noboribetsu
    date: "2026-09-26"
    origin: {label: "JR洞爺駅"}
    mode: bicycle
    route_variant: main
    display: true
    calculation: {method: chatgpt_research, provider: "ChatGPT Web調査", calculated_at: "2026-08-30", references: [source:toya-eruption-ruins, source:osaruyu, source:orofure-route, source:orofure-pass]}
    points:
      - {target: place.nishiyama-crater, distance_km: 6, confidence: medium, note: "西山山麓火口散策路の北口側駐車地点まで。散策路の徒歩距離は除外。"}
      - {target: place.kompira-eruption-ruins, distance_km: 9, confidence: medium, note: "洞爺湖ビジターセンター・火山科学館周辺を自転車到着点とし、金比羅火口散策路の徒歩距離は除外。"}
      - {target: place.osaru-yu, distance_km: 35, confidence: low, note: "国道453号沿いのオサル湯アクセス地点まで。河原の湯までの徒歩は除外。正式な温泉施設ではなく到着点にも幅がある。"}
      - {target: place.orofure-pass, distance_km: 54, confidence: medium, note: "盤渓付近の閉鎖された近道は使わず国道453号→道道2号。壮瞥側から旧オロフレ峠の展望・駐車地点へ。"}
      - {target: place.noboribetsu-jigokudani, distance_km: 74, confidence: medium, note: "オロフレ峠立寄り後、道道2号系統で登別温泉へ。地獄谷入口付近まで。"}

  - id: distance.20260927-noboribetsu-tomakomai
    date: "2026-09-27"
    origin: {ref: stay.noboribetsu-onsen, label: "登別温泉バスターミナル付近"}
    mode: bicycle
    route_variant: main
    display: true
    calculation: {method: chatgpt_research, provider: "ChatGPT Web調査", calculated_at: "2026-08-30", references: [source:upopoy, source:shiraoi-jinya, source:shiraoi-tomakomai]}
    points:
      - {target: place.upopoy, distance_km: 30, confidence: medium, note: "登別温泉から一般道で白老若草町2-3のウポポイ入口まで。"}
      - {target: place.national-ainu-museum, distance_km: 30, confidence: high, note: "ウポポイ園内。同一敷地内の施設間移動は自転車距離に加算しない。"}
      - {target: place.shiraoi-jinya-museum, distance_km: 33, confidence: medium, note: "ウポポイから仙台藩白老元陣屋資料館まで約3 km。"}
      - {target: place.shiraoi-jinya, distance_km: 33, confidence: high, note: "資料館は史跡白老仙台藩陣屋跡内。同一敷地のため自転車距離を加算しない。"}
```

### 参照リンク対応

`source:mutsu-osore` は、むつ市―恐山の道路距離が約14.3 kmとされる資料と、むつ市公式の恐山案内です。 [むつ市から恐山への道路距離](https://www.rome2rio.com/ja/s/%E3%82%80%E3%81%A4%E5%B8%82/%E6%81%90%E5%B1%B1?utm_source=chatgpt.com) [むつ市「霊場恐山」](https://www.city.mutsu.lg.jp/bunka/spot/reijyouosorezann.html?utm_source=chatgpt.com)
`source:osore-sanzu` は、恐山菩提寺から三途の川が約500～550 mである資料です。 [三途の川 基本情報](https://www.jalan.net/kankou/spt_guide000000191912/?utm_source=chatgpt.com) [恐山菩提寺周辺距離](https://www.jalan.net/kankou/spt_02208ag2130012244/spot/?utm_source=chatgpt.com)
`source:shimokita-road-distances` は、下風呂―薬研―恐山を実際に自転車で走った区間距離です。
`source:mutsu-yagen` は奥薬研が薬研温泉から約2 kmであるむつ市の案内です。
`source:shozugawa-closure` は正津川林道の一般車両通行止めです。 [下北森林管理署 通行規制のお知らせ](https://www.rinya.maff.go.jp/tohoku/syo/simokita/attach/pdf/index-20.pdf)

`source:shimofuro-oma-road` は下風呂―大間崎の道路距離、`source:oma-terminal` は大間フェリーターミナルの所在地確認に使用しました。  [津軽海峡フェリー 大間ターミナル案内](https://www.tsugarukaikyo.co.jp/guide/terminal/?utm_source=chatgpt.com)

`source:hakodate-ferry-terminal` は函館FTの所在地、`source:hakodate-northern-peoples` は北方民族資料館、`source:shigechan` はシゲちゃんすしの所在地確認です。 [函館フェリーターミナル](https://www.tsugarukaikyo.co.jp/guide/terminal/hakodate/?utm_source=chatgpt.com) [函館市北方民族資料館](https://www.city.hakodate.hokkaido.jp/docs/2015121000103/?utm_source=chatgpt.com) [シゲちゃんすし所在地](https://map.yahoo.co.jp/v3/place/PiplkYadkKs?utm_source=chatgpt.com)

`source:toi-arch` は旧戸井線アーチ橋の所在地・立入条件、`source:esan-access` は恵山火口原への車道アクセス、`source:mizunashi` は水無海浜温泉、`source:jomon-center` と `source:kakinoshima` は縄文施設の所在地・共用駐車場、`source:donan-cycle-route` は函館―鹿部のサイクリング基準距離です。      [北海道開発局 どうなん海道サイクルルート資料](https://www.hkd.mlit.go.jp/ky/kn/dou_kei/k5m5qg000000324h-att/k5m5qg00000032ch.pdf)

`source:shikabe-yakumo` は鹿部―八雲側の区間距離、`source:yakumo-museums` は両資料館の位置関係、`source:banjaku-access` は盤石温泉への直近アクセス情報です。 [鹿部―八雲方面の道路距離資料](https://no-1-travel.com/around-hokkaido-drive/?PageSpeed=noscript&utm_source=chatgpt.com) [八雲町郷土資料館・木彫り熊資料館](https://www.town.yakumo.lg.jp/site/museum/kyoudo001.html?utm_source=chatgpt.com) [盤石温泉へのアクセス情報](https://t2412.livedoor.blog/archives/1069357.html?utm_source=chatgpt.com)

`source:toya-eruption-ruins` は西山・金比羅火口、`source:osaruyu` はオサル湯、`source:orofure-route` と `source:orofure-pass` は盤渓―オロフレ峠の公道路線確認です。

`source:upopoy` はウポポイと国立アイヌ民族博物館の位置関係、`source:shiraoi-jinya` は資料館と史跡が同一敷地であること、`source:shiraoi-tomakomai` は苫小牧方向の道路距離の検算に使用しました。

### 距離を特定できなかった地点

`points` から省いた地点は**ありません**。ただし、**盤石温泉とオサル湯だけは「湯そのもの」まで自転車で入る距離ではありません**。盤石温泉は小橋手前の車両到達地点、オサル湯は国道453号沿いのアクセス地点を終点としており、それぞれ最後の徒歩区間を除外しています。そのため両者を `low` としました。オサル湯については壮瞥町自身が、正式な温泉施設ではなく衛生・安全面から積極的には案内していない場所と説明しています。 ([そうべつ観光協会][9])

### 全体の距離感のチェック

かなり重要なのは**9月24日と25日**です。9/24は今回の指定順で約**110 km**です。北海道開発局の「どうなん海道サイクルルート」は函館―鹿部を87 kmの上級者向けステージとして設定していますが、これは基幹ルートの距離で、今回のように**恵山火口原まで登り、水無海浜温泉まで恵山岬側へ入る**ルートとは一致しません。したがって110 kmは異常値ではありません。公式資料の87 kmだけを予定距離としていた場合は、今回の行程では**20 km強不足**すると見た方がよいです。

9/25は盤石温泉到着時点で約**92 km**ですが、予定経路はその後**八雲町中心部へ戻る**ので、実際の日間走行距離は約**117 km**になります。YAMLの最後のpointが盤石温泉なので、この25 kmの戻りを見落としやすいです。

9/26は地獄谷到着で約**74 km**。距離だけなら短めですが、オロフレ峠を含むため走行負荷は距離以上です。9/27も最後の登録pointは白老で33 kmですが、そこから苫小牧西港までさらに約30 kmあり、**一日の総走行はおよそ63 km**です。9/23も同様に、大間崎19 kmのあとフェリーターミナルまで約4 kmあるため、第1区間の総走行は約23 kmです。

道路規制、とくに**正津川林道・盤石温泉進入路・オロフレ峠周辺**は9月下旬までに状況が変わる可能性があります。出発直前に道路規制だけ再チェックする運用が有効です。

[1]: https://www.city.mutsu.lg.jp/bunka/spot/reijyouosorezann.html?utm_source=chatgpt.com "霊場恐山｜観光・文化・スポーツ｜むつ市"
[2]: https://www.jalan.net/kankou/spt_guide000000191912/?utm_source=chatgpt.com "〖三途の川〗アクセス・営業時間・料金情報 - じゃらんnet"
[3]: https://www.tsugarukaikyo.co.jp/guide/terminal/hakodate/?utm_source=chatgpt.com "函館フェリーターミナル | 津軽海峡フェリー株式会社"
[4]: https://www.city.hakodate.hokkaido.jp/docs/2024030500093/ "https://www.city.hakodate.hokkaido.jp/docs/2024030500093/"
[5]: https://www.city.hakodate.hokkaido.jp/docs/2022012400119/ "https://www.city.hakodate.hokkaido.jp/docs/2022012400119/"
[6]: https://www.town.yakumo.lg.jp/site/museum/kyoudo001.html?utm_source=chatgpt.com "八雲町郷土資料館利用案内 - 八雲町公式サイト｜太平洋と日本海、二つの海をもつ町"
[7]: https://www.laketoya.com/leisure/ "https://www.laketoya.com/leisure/"
[8]: https://ainu-upopoy.go.jp/facility/upopoy/ "https://ainu-upopoy.go.jp/facility/upopoy/"
[9]: https://sobetsu-kanko.com/qa "https://sobetsu-kanko.com/qa"
