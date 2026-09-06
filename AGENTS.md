# Repository rules

## Google Mapsレビュー情報

- `catalog/food.yaml` の飲食店候補と `catalog/places.yaml` の立ち寄りスポット候補には、取得できたGoogle Maps情報を `google_maps` に記録する。
- `google_maps.rating` はスター評価（0〜5）、`google_maps.review_count` はレビュー数、`google_maps.checked_at` は確認日（`YYYY-MM-DD`）とする。
- `google_maps` がない、または値が未取得の候補を見つけた場合、Codexは値を推測したりGoogle Mapsから直接取得したりせず、`prompts/google-maps-reviews.md` の形式でChatGPTへ貼り付ける依頼文をユーザに提示する。
- ユーザがChatGPTの回答を戻したら、対象名・地域の一致を確認してから候補YAMLへ反映する。不一致や複数候補は確認を求め、推測で埋めない。
