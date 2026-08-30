# ChatGPTとCodexの役割分担

## ChatGPT

Web調査、候補発見、比較、ブレスト、ユーザーとの意思決定支援を担当します。repositoryのSSoTは直接管理しません。

## Codex

repositoryの現在状態の読取り、ブレスト用プロンプト作成、結果の反映、YAML正規化、validation、Markdown生成、diff確認を担当します。

## ChatGPT → Codex

可能なら自然言語に加えて構造化change setを渡します。v1では自動適用せず、Codexが現行schemaへ反映します。

```yaml
changes:
  - operation: add_candidate
    id: place.example
  - operation: modify_day
    date: 2026-09-24
    add_visit: [place.example]
```

## Codex → ChatGPT

repository全体ではなく、関連するhard/soft constraints、current planの日、候補、deferred/rejectedの理由、要再確認事項、今回の依頼だけを抽出します。
