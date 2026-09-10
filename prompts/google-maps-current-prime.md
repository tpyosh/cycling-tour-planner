# 2026-09-10再監査後のGoogle Maps未確認候補

2026-09-10の再監査でratingとreview countを確定できなかった11候補です。以下をChatGPTへ貼り付け、回答をCodexへ戻してください。Codexは名称・地域の一致を確認してから `catalog/places.yaml` または `catalog/food.yaml` へ反映します。

```text
以下の各候補について、Google Mapsで表示される店舗・施設を特定し、現在の「スター評価」と「クチコミ（レビュー）件数」を確認してください。

同名候補、広域地点、単一のGoogle Maps施設として特定できない対象は推測で統合せず、その対象の値を null または unknown にしてください。各対象について、下記のJSON形式を1件ずつ出力してください。

対象:
- 対象名: 石巻市震災遺構 門脇小学校 / 検索語: 石巻市震災遺構 門脇小学校 / 地域: 宮城県石巻市
- 対象名: 藤や食堂 / 検索語: 藤や食堂 石巻 / 地域: 宮城県石巻市
- 対象名: 大川小学校震災遺構 / 検索語: 大川小学校震災遺構 / 地域: 宮城県石巻市
- 対象名: 東日本大震災遺構 旧女川交番 / 検索語: 旧女川交番 / 地域: 宮城県女川町
- 対象名: 津波記憶石第28号 / 検索語: 津波記憶石 第28号 女川 / 地域: 宮城県女川町
- 対象名: 南三陸さんさん商店街 / 検索語: 南三陸さんさん商店街 / 地域: 宮城県南三陸町
- 対象名: 道の駅 大谷海岸 / 検索語: 道の駅 大谷海岸 / 地域: 宮城県気仙沼市
- 対象名: 神の倉の津波石 / 検索語: 神の倉 津波石 唐桑 / 地域: 宮城県気仙沼市唐桑町
- 対象名: 御崎神社 / 検索語: 御崎神社 唐桑 / 地域: 宮城県気仙沼市唐桑町
- 対象名: 鮪立集落・唐桑御殿型住宅 / 検索語: 鮪立 唐桑御殿 気仙沼 / 地域: 宮城県気仙沼市唐桑町
- 対象名: 旧気仙中学校 / 検索語: 旧気仙中学校 震災遺構 / 地域: 岩手県陸前高田市

出力形式:
{
  "name": "対象名",
  "matched_name": "Google Maps上の名称",
  "address_or_area": "住所または地域",
  "rating": 0.0,
  "review_count": 0,
  "review_count_range": null,
  "review_count_is_approximate": false,
  "checked_at": "YYYY-MM-DD",
  "verification_status": "confirmed | needs_recheck | unknown",
  "acquisition_confidence": "high | medium | low | unknown",
  "google_maps_url": "https://maps.google.com/...",
  "evidence_scope": {
    "rating_and_count": "confirmed | not_confirmed | unknown",
    "review_text": "not_checked | partial | extensive | unknown",
    "photos": "not_checked | partial | extensive | unknown"
  },
  "review_notes": ["レビュー本文から確認できた傾向"],
  "audience_notes": ["成人旅行者の評価傾向、子ども向けレビューへの偏り"],
  "evidence_notes": ["実物・展示内容・写真から確認できた比較材料"],
  "limitations": ["全レビュー本文は未取得"],
  "notes": "同名候補や確認できなかった点"
}
```
