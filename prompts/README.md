# 外部調査プロンプト

外部サービスへ調査を依頼するためのプロンプトを保存する場合は `prompts/` 配下に置きます。ファイルには、調査目的、前提、対象、期待する出力形式、必要な出典を含めます。

回答はプロンプトへ追記せず、内容を確認してから対応する正本YAMLへ反映します。距離調査は `estimates/distances.yaml`、時刻・営業・規制などの根拠は `evidence/sources.yaml` に記録します。

Google Mapsのレビュー数・スターは `google-maps-reviews.md` の運用に従います。CodexはGoogle Mapsから直接取得せず、対象候補ごとの依頼文を作成してユーザに提示します。

2026-09-10再監査で値を確定できなかった11候補の一括依頼文は `google-maps-current-prime.md` にあります。

current primeの成立性、日別の時間配分、営業・交通・道路・宿泊・食事、既存issueの不足をまとめて外部調査する場合は `current-prime-gap-audit.md` を使います。

9/25の女川→気仙沼自走と気仙沼市東日本大震災遺構・伝承館の最終受付を単独で検証し、`issue.onagawa-kesennuma-feasibility` の解消材料を得る場合は、自己完結型の `chatgpt-resolve-onagawa-kesennuma-feasibility.md` を1ファイルだけChatGPTへ添付して使います。
