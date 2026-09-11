# 廃止済みの配置

`prompts/` はChatGPT調査ブリッジの保存先として廃止した。ChatGPTに渡す本文、自己完結資料、添付用アーカイブは、追跡せず `.codex/local/chatgpt-research/<request-id>/` にだけ置く。

作成、完了時のGC、保存先を判定できない場合の停止条件は [`.codex/CONSTITUTION.md`](../.codex/CONSTITUTION.md)、実行手順は [`AGENTS.md`](../AGENTS.md) に従う。このディレクトリへ新しい依頼文を追加してはならない。
