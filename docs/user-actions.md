<!-- GENERATED FILE. DO NOT EDIT DIRECTLY. -->

# User Action Dashboard

いま旅行者自身が行う必要のある、未完了の実務だけを表示します。調査・比較・検証は [Issue一覧](issues.md) で管理します。完了したActionはここで完了表示にせず削除し、予約・利用内容などの現在状態を該当する正本へ反映します。

## 今すぐ行う

| Action | 期限・推奨時期 | なぜ必要か | 関連 |
| --- | --- | --- | --- |

| 青函トンネル記念館の体験坑道（9/25朝一候補）を予約し、始発便の扱いを電話で確認する | 期限未設定（今すぐ行う） | 旅程の主役であり、奥津軽いまべつ13:35発へ輪行で接続する前提になる。朝一便の乗車保証は未確認である。 | 青函トンネル記念館 / はやぶさ24号 |

| 9/27 13:40 大間→函館フェリーを、輪行を含めて予約する | 期限未設定（今すぐ行う） | 函館泊と9/28の帰路に直結する便で、輪行料金も旅客運賃とは別に必要である。 | 津軽海峡フェリー 大間→函館 9便 / 函館 |

### 青函トンネル記念館の体験坑道（9/25朝一候補）を予約し、始発便の扱いを電話で確認する

- **ID:** `action.tappi-museum-booking`
- **関連Issue:** issue.tappi-museum-okutsugaru-connection
- **根拠:** [じゃらん 青函トンネル記念館 体験坑道プラン](https://www.jalan.net/kankou/spt_02306cc3290032412/activity/l00005CBA0/) / [Amazing AOMORI 青函トンネル記念館](https://aomori-tourism.com/spot/detail_68.html)
- **メモ:** 予約前または予約時に、集合8:50・体験9:00〜9:50の予約で9:00始発便に乗れるか、保証されない場合の割当方法と受付期限を青函トンネル記念館（0174-38-2301）へ確認する。

### 9/27 13:40 大間→函館フェリーを、輪行を含めて予約する

- **ID:** `action.oma-ferry-booking`
- **関連Issue:** issue.oma-ferry-operation
- **根拠:** [津軽海峡フェリー 函館〜大間航路 時刻表](https://www.tsugarukaikyo.co.jp/service/timetable/hakodate-oma/)
- **メモ:** 予約・決済後も、当日は出航20分前までにチェックインできるようにする。運航状況の確認は9/27当日の別Actionで行う。

## 前日まで／出発前に行う

| Action | 期限・推奨時期 | なぜ必要か | 関連 |
| --- | --- | --- | --- |

| 龍泊ラインの道路規制・災害状況を確認する | 9/23まで | 9/24の主な自走区間を安全に通行できるかを左右する。 | 小泊→龍泊ライン→竜飛 |

### 龍泊ラインの道路規制・災害状況を確認する

- **ID:** `action.ryuhyo-road-preflight`
- **関連Issue:** issue.ryuhyo-day-operation
- **根拠:** [青森県 道路情報（青森みち情報）](https://www.pref.aomori.lg.jp/soshiki/kendo/doro/)
- **メモ:** 9/23夜または9/24出発前に青森県「青森みち情報」を確認する。通行止め、豪雨、雷、崩落、土砂災害、明確に危険な道路状態なら再判断する。

## 当日に行う

| Action | 期限・推奨時期 | なぜ必要か | 関連 |
| --- | --- | --- | --- |

| 奥津軽いまべつ→八戸→下北の運休・大幅遅延を確認する | 9/25まで | 9/25に下北へ輪行転場し、むつ泊へ到達するために必要である。 | はやぶさ24号 / 快速しもきた（3233D） |

| 大間→函館フェリーの運航状況を確認する | 9/27まで | 欠航・遅延は函館泊と帰路を変えるため、当日判断が必要である。 | 津軽海峡フェリー 大間→函館 9便 |

### 奥津軽いまべつ→八戸→下北の運休・大幅遅延を確認する

- **ID:** `action.okutsugaru-rail-preflight`
- **関連Issue:** issue.okutsugaru-rail-operation
- **根拠:** [JR東日本 時刻表 はやぶさ24号](https://timetables.jreast.co.jp/2609/train/030/033862.html) / [JR東日本 時刻表 快速しもきた](https://timetables.jreast.co.jp/2609/train/055/055641.html)
- **メモ:** 当日朝にJRの運行情報で確認する。

### 大間→函館フェリーの運航状況を確認する

- **ID:** `action.oma-ferry-preflight`
- **関連Issue:** issue.oma-ferry-operation
- **根拠:** [津軽海峡フェリー 函館〜大間航路 時刻表](https://www.tsugarukaikyo.co.jp/service/timetable/hakodate-oma/)
- **メモ:** 9/27当日に津軽海峡フェリーの運航状況を確認する。欠航時は current plan の contingency.oma-ferry-cancellation を使う。
