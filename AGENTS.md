# Repository rules

## ChatGPT調査ブリッジ（必須ゲート）

ユーザーの依頼に「ChatGPTに調べさせる」「ChatGPT向けプロンプト」「引き渡し資料」「添付用アーカイブ」のいずれかが含まれる場合、これは**一時ブリッジ作業**である。通常の文書作成や `prompts/` の更新として扱ってはならない。

本文を書き始める前に、必ず `.codex/CONSTITUTION.md` を読み、次の決定表に従う。

| 条件 | 必須行動 | 禁止行動 |
| --- | --- | --- |
| ChatGPTへ渡す本文・添付・アーカイブを新規作成または更新する | `python3 tools/chatgpt_research.py init <request-id>` で作った `.codex/local/chatgpt-research/<request-id>/` にだけ置く。作成前と作成後に `python3 tools/chatgpt_research.py preflight <対象パス>` を成功させる。 | `prompts/`、`docs/`、`research/`、リポジトリ直下、その他の追跡領域に置く。 |
| 依頼の回答を受領した、依頼を中止した、または別依頼に置き換えた | 必要な恒久データだけを正本へ反映した後、`python3 tools/chatgpt_research.py gc <request-id>` を実行する。 | ブリッジ本文・添付を追跡領域へ移して保存する。 |
| 恒久的な運用規則や入力要件を残す | ChatGPTへそのまま送る命令文ではなく、`AGENTS.md`、`.codex/CONSTITUTION.md`、または正本の仕様として記述する。 | 再利用目的を理由にChatGPT向け完成プロンプトを追跡する。 |
| 保存先、依頼の完了状態、または恒久物／一時物の区別が決められない | ブリッジの作成・移動・削除を停止し、ユーザーに判断を求める。 | 仮に `prompts/` へ置いて作業を続ける。 |

`tools/chatgpt_research.py audit` が廃止済みの `prompts/`、または追跡領域にある典型的な直接依頼文を検出した場合は、当該ブリッジを使わず、移行または削除方針を決めるまで作業を停止する。通常のリポジトリ検証ではこの監査も実行する。

## Google Mapsレビュー情報

- `catalog/food.yaml` の飲食店候補と `catalog/places.yaml` の立ち寄りスポット候補には、取得できたGoogle Maps情報を `google_maps` に記録する。
- `google_maps.rating` はスター評価（0〜5）、`google_maps.review_count` はレビュー数、`google_maps.checked_at` は確認日（`YYYY-MM-DD`）とする。
- `google_maps` がない、または値が未取得の候補を見つけた場合、Codexは値を推測したりGoogle Mapsから直接取得したりしない。ChatGPTへ依頼する本文が必要なら、上記のChatGPT調査ブリッジとして作成する。
- ユーザがChatGPTの回答を戻したら、対象名・地域の一致を確認してから候補YAMLへ反映する。不一致や複数候補は確認を求め、推測で埋めない。
