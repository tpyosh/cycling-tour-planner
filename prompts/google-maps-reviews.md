# Google Mapsレビュー情報の取得依頼

## 運用

1. Codexは `catalog/food.yaml` または `catalog/places.yaml` の `name` と `map_query` を使い、未取得の候補を列挙する。
2. Codexは以下の依頼文を候補ごとに埋めてユーザへ提示する。Codex自身はGoogle Mapsを検索しない。
3. ユーザは依頼文をChatGPTに貼り付ける。
4. ユーザはChatGPTの回答をCodexへ戻す。
5. Codexは対象名・場所が一致することを確認し、回答を `google_maps` に反映する。不一致、複数候補、取得不能は推測で埋めず、ユーザへ確認する。

## ChatGPTへ貼り付ける依頼文

```text
以下の候補について、Google Mapsで表示される店舗・施設を特定し、現在の「スター評価」と「クチコミ（レビュー）件数」を確認してください。

対象名: {name}
Google Maps検索語: {map_query}
地域・補足: {area_or_context}

出力は次のJSONだけにしてください。確認できない項目は null または `unknown` にし、推測で補完しないでください。レビュー本文や写真は、実際に確認した範囲だけを要約してください。
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

## YAMLへの反映

回答を候補の `google_maps` に転記する。レビュー件数が概数なら `review_count_is_approximate: true` とする。URLと取得方法は `source`、本文・写真をどこまで見たかは `evidence_scope`、本文傾向は `review_notes`、成人旅行者と子ども向け偏りは `audience_notes`、展示や実物に関する比較材料は `evidence_notes`、取得できなかった範囲は `limitations` に記録する。

確認していない観点を推測で埋めない。星と件数しか確認できなかった場合も、`review_text: not_checked`、`photos: not_checked` と明記すれば調査結果として保存できる。対象を特定できなかった場合は、候補マスターに `rating: null`、`review_count: null`、`verification_status: needs_recheck` を記録し、次回も取得対象として扱う。
