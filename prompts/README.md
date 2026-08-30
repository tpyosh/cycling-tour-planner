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

### ChatGPTへの質問は`prompts/chatgpt/`へ保存する

CodexがChatGPTへ調査や検討を依頼するときは、回答文にプロンプトを直接展開せず、`prompts/chatgpt/`にMarkdownファイルを作ります。ユーザーはそのファイルの内容をChatGPTへ貼り付け、得られた回答をCodexとの会話へ貼り戻します。

ファイル名は`YYYY-MM-DD-topic.md`とします。`topic`には、依頼内容が分かる短い英小文字のkebab-caseを使います。同じ日に同じテーマを再依頼する場合は、末尾に`-02`のような連番を付けます。

質問ファイルは、次の条件を満たすように作ります。

- ファイル全体をそのままChatGPTへ貼り付けられる
- 調査目的、前提、対象、期待する出力形式を含む
- repository全体を転載せず、回答に必要な情報だけを含む
- 機械的に反映したい回答には、既存IDを使ったYAMLなどの構造化出力を求める
- Web調査が必要な場合は、参照URLと推定箇所の明記を求める

Codexはファイルを作成したら、そのパスとユーザーが次に行う操作を伝えます。ChatGPTからの回答は質問ファイルへ追記せず、ユーザーがCodexとの会話へ貼り付けます。Codexは回答を現行schemaに合わせて正規化し、validation、Markdown生成、diff確認まで行います。距離調査の回答は、旅程データへ直接書かず、`estimates/distances.yaml`へ反映します。
