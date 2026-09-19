# Codexカスタマイズは、常時原則・ワークフロー・機械検証を分けて保守する

この文書は、サイクリング旅行計画用のCodex基盤を変更するときの設計記録である。通常の旅行計画では通読せず、責務の置き場所、旧Skillの移行先、Codex機構の採否を確認したいときに参照する。

## 監査時点の構成は、旧Skillの配置と責務が標準仕様から外れていた

確認日は `2026-09-20`、インストール済みCLIは `codex-cli 0.155.1` である。監査時点のブランチは `main`、作業ツリーはクリーン、`origin/main` より2コミット先行していた。先行コミットは既存作業として保持した。

監査前のリポジトリには `AGENTS.md`、`.codex/config.toml`、hooks、rules、カスタムsubagentがなく、旅行計画の方針と手順は `.codex/skills/travel-planner/` に集中していた。リポジトリ内にCodex起動スクリプトや `CODEX_HOME` の指定はなく、シェル環境でも `CODEX_HOME` は未設定だった。

監査を実行したホスト環境は `.codex/skills/travel-planner` をSkill一覧へ注入していた。ただし、現行の公式仕様がリポジトリSkillとして探索する場所は、Gitルートから作業ディレクトリまでの `.agents/skills/` である。旧配置が見えていた事実は、`.codex/skills` が標準配置であることを意味しない。CLI、IDE、別のホストでも再現できる正本として `.agents/skills/` へ移行した。

ユーザー環境のSkillは `~/.codex/skills/.system/` と `~/.codex/skills/natural-japanese/` にあり、`~/.agents/skills/` と `/etc/codex/skills/` には該当ファイルがなかった。これはユーザー・system scopeの現状であり、リポジトリSkillの配置判断とは分けて扱った。インストール済みバイナリにも `.agents/skills`、`.codex/agents`、`agents.max_concurrent_threads_per_session` の実装文字列があり、公式資料と矛盾しないことを読み取り専用で確認した。

プロジェクトはユーザー設定で `trusted` として登録済みである。このため、リポジトリの `.codex/config.toml` と `.codex/agents/` は読み込める。信頼設定はマシン固有なので、リポジトリ側から変更しない。

監査時のユーザー設定は `approval_policy = "never"`、`sandbox_mode = "danger-full-access"` だった。ユーザーrulesにはGitを含む複数コマンドのallow設定があり、ユーザーhooksとsystem管理設定は確認されなかった。これらはマシン全体へ影響するため変更せず、リポジトリへも複製していない。権限が広くても、`AGENTS.md` とユーザー依頼による操作範囲は変わらない。

ユーザー設定のMCPは `node_repl`、`computer-use`、`openaiDeveloperDocs` だった。いずれも旅行計画専用ではなく、新しい認証や外部サービスを必要としないため、プロジェクト設定へ移していない。調査Skillは利用可能なWeb・ブラウザ・MCPを使えるが、特定のMCPへの依存は持たない。

参照した公式資料:

- [カスタマイズの概要](https://developers.openai.com/ja-JP/docs/customization/overview)
- [AGENTS.md](https://developers.openai.com/ja-JP/docs/agent-configuration/agents-md)
- [Skillsの作成と探索場所](https://developers.openai.com/ja-JP/docs/build-skills)
- [config.tomlの基本と優先順位](https://developers.openai.com/ja-JP/docs/config-file/config-basic)
- [config.tomlリファレンス](https://developers.openai.com/ja-JP/docs/config-file/config-reference)
- [subagentとカスタムagent](https://developers.openai.com/ja-JP/docs/agent-configuration/subagents)
- [hooks](https://developers.openai.com/ja-JP/docs/hooks)
- [rules](https://developers.openai.com/ja-JP/docs/agent-configuration/rules)
- [MCP](https://developers.openai.com/ja-JP/docs/extend/mcp)

## 各情報の正本を一箇所に定めた

| 責務 | 正本 | 配置理由 |
| --- | --- | --- |
| Skillが選ばれなくても守る姿勢 | `AGENTS.md` | Codexが作業開始前に読む、短く安定した指示だから |
| 候補・交通・営業・宿泊・自然条件の調査 | `$cycling-trip-research` | 明確な開始・終了条件を持つ反復ワークフローだから |
| 日別行程と代替案の設計 | `$cycling-itinerary-design` | 調査とは異なる、採否と全体構造の設計だから |
| 成立性・体験価値・旅全体の独立監査 | `$cycling-trip-review` | 現行案の作成から距離を置く批判的レビューだから |
| 詳細な評価基準 | 各Skillの `references/` | 該当作業でだけ読み、起動時コンテキストへ入れないため |
| データ構造と必須項目 | `schema/*.schema.json` | 自然言語で複製せず、機械検証できる正本だから |
| 参照整合性、日付、距離、Issue、宿泊調査の検査 | `tools/validate.py` | 決定的に判定できる処理だから |
| 旅行者向けMarkdown | `templates/` と `tools/render.py` | YAMLを正本に保ち、生成を再現可能にするため |
| Codexカスタマイズ自体の検査 | `tools/check_codex_customization.py` | Skill配置、TOML、frontmatter、参照を機械確認するため |
| 読み取り専用の並列調査・独立監査 | `.codex/agents/` | 中間出力のノイズと編集競合を主スレッドから分離するため |
| subagentの並列上限 | `.codex/config.toml` | Codexの動作設定であり、旅行方針ではないため |

Skillには `assets/` を置いていない。このリポジトリ自体が旅行計画のスターターであり、ルートのYAML、スキーマ、テンプレートが正本だからである。Skill内に雛形を複製すると、二つのスターターが別々に更新される。

## 旧Skillの各指示を追跡可能な形で移行した

| 旧ファイル・節 | 分類 | 新しい正本または判断 |
| --- | --- | --- |
| `SKILL.md`「旅行者が現地で判断できる計画」 | 常時適用する原則 | `AGENTS.md` の具体化原則と、行程設計Skillの成果条件 |
| 「最初に把握すること」 | 特定ワークフローの手順 | 行程設計Skillの開始条件。必須項目の正本は `trip.yaml`、`constraints.yaml` とschema |
| 「計画の組み立て方」1〜9 | 特定ワークフローの手順 | 調査Skill、行程設計Skill、レビューSkillへ作業の性質で分割 |
| 候補発見と順位付けの分離 | 常時原則とワークフロー | `AGENTS.md` の評価姿勢、調査Skillの終了条件、行程設計Skillの採用条件 |
| Actionability Gate | 参考知識・評価基準 | レビューSkillの `experience-and-structure.md` |
| `pass_through` | 参考知識・データ規則 | `experience-and-structure.md`。値の許容範囲は既存schemaを正本とする |
| 旅程全体を一本の線で評価 | 参考知識・評価基準 | 行程設計Skillの `itinerary-structure.md` とレビューの構造評価 |
| 宿泊地を翌朝の開始位置として評価 | 参考知識・評価基準 | `itinerary-structure.md` |
| 輪行・公共交通を総負担で比較 | 参考知識・評価基準 | 行程設計Skill本体と `itinerary-structure.md` |
| 日数を固定の充填枠にしない | 参考知識・評価基準 | `itinerary-structure.md` |
| 現行案を作成経緯から独立して再評価 | 常時原則とレビュー手順 | `AGENTS.md` とレビューSkill本体 |
| ユーザーの疑問を再監査の契機にする | レビュー手順 | `experience-and-structure.md` |
| `fact` / `inference` / `unverified` | 常時原則とデータ規則 | `AGENTS.md`、調査Skillの `evidence-and-risk.md`、`evidence.schema.json` |
| 情報源の優先順位と検索要約の扱い | 参考知識・評価基準 | `evidence-and-risk.md` |
| 変動性と旅行前再確認 | 参考知識・評価基準 | `evidence-and-risk.md`。フィールド定義はschemaを正本とする |
| 検索結果なしと満室・運休の区別 | 調査手順 | `evidence-and-risk.md` と `lodging.schema.json` |
| 外部状態を変える操作の制限 | 常時適用する原則 | `AGENTS.md` |
| `constraints`、`catalog`、`plan`、`evidence`、`issues` の分離 | ルーティングとデータ規則 | `README.md`、`tools/lib/data.py`、各schema |
| 候補状態と採用参照の分離 | データ規則 | 行程設計Skillと `tools/validate.py` |
| 日別の実現可能性項目 | 参考知識・評価基準 | レビューSkillの `feasibility-and-data.md` |
| 距離の区間分割と表示値の分離 | データ規則と自動処理 | `itinerary-structure.md`、`distances.schema.json`、`tools/validate.py` |
| 通常旅程と代替案の分離 | 設計手順とデータ規則 | 行程設計Skill、`itinerary.schema.json` |
| Issueの影響・次の確認・解決条件 | データ規則と自動処理 | `issues.schema.json`、`tools/validate.py`、行程設計reference |
| 最終旅程の状態区分 | 成果物要件 | 行程設計Skillと `templates/` |
| `quality-check.md` の決定的な項目 | 決定的に自動化できる処理 | `tools/validate.py` とテストを正本として維持 |
| `quality-check.md` の判断項目 | 参考知識・評価基準 | レビューSkillの二つのreferenceへ移行 |
| `experience-evaluation.md` | 参考知識・評価基準 | `experience-and-structure.md` へ集約 |
| `research-and-risk.md` | 参考知識・評価基準 | `evidence-and-risk.md` へ集約 |
| `data-model.md` の構成・ID・参照 | 重複 | `README.md`、schema、`tools/validate.py` を正本とし、Skillから削除 |
| `data-model.md` の評価・宿泊・距離の説明 | 参考知識 | 対応する調査・設計referenceへ移行 |
| `assets/starter/` | テンプレートだが重複 | 削除。ルートの空YAML、schema、templatesが再利用基盤の正本 |
| 旧 `agents/openai.yaml` | Skill UIメタデータ | 3 Skillの `agents/openai.yaml` へ役割別に移行 |
| `.codex/skills` という配置 | 現在は標準探索されない旧配置 | `.agents/skills` へ移行。`CODEX_HOME` 依存や起動ラッパーはなかった |

## 採用したCodex機構は、責務があるものだけに絞った

- `AGENTS.md`: 24行に抑え、常時必要な原則と読取り順だけを置いた。
- `.agents/skills`: 調査、設計、レビューの3つに分けた。各descriptionは発火対象と非対象を示す。
- Skillの `references/`: 詳細基準を作業時だけ読む。`assets/` と `scripts/` は、リポジトリ直下の正本と重複するため置かない。
- `.codex/agents`: `trip_researcher` と `trip_critic` は読み取り専用で、親だけがファイルを編集する。
- `[agents]`: 同時subagent数を2へ制限し、独立した二つの論点までを並列化できる。
- `.codex/config.toml`: `[agents]` 以外のプロジェクト固有設定は追加していない。
- 既存のschema、検証、生成、pytest: 自然言語の注意書きより確実な処理を引き続き担当する。

## 今回は使わないCodex機構にも理由がある

| 機構 | 不採用理由 |
| --- | --- |
| hooks | 毎ターンやツール実行ごとに旅行データ検証を走らせると頻度と誤検出の負担が大きい。手動コマンドとpytestで十分に決定的で、未信頼hookのレビューも不要にできる |
| rules | rulesはsandbox外コマンドの許可・確認・禁止を扱う。旅行方針の置き場所ではなく、このリポジトリ固有の恒久的なコマンド境界も確認できなかった |
| MCPの追加 | 現在利用可能なWeb・ブラウザ・ドキュメント機能で調査できる。新しいサービス、認証、プロジェクト固有サーバーを必要とする反復処理はない |
| 権限・sandboxの上書き | ユーザーの実行環境と組織ポリシーが決める領域であり、旅行リポジトリが権限を拡大・縮小する根拠がない。custom agentだけは編集競合防止のため `read-only` とした |
| `requirements.toml` | 管理者が強制する設定であり、リポジトリ利用者の権限をこのプロジェクトから強制する要件がない |
| project root markers | Gitルートが正しく検出されており、独自markerは不要 |
| plugins | このリポジトリ内で共同保守するSkillで足りる。外部配布やMCP同梱が必要になった時点で検討する |
| memories | 個別旅行の一時情報を再利用基盤へ混ぜる危険がある。永続化すべき知見はレビューを経たファイル変更として残す |
| automations | 定期実行する監視要件がなく、旅行ごとの再確認日はIssueと `recheck_before_trip` で管理できる |
| profiles、model指定 | 個人の速度・価格・品質選択であり、プロジェクト共通の正本にしない |
| `model_instructions_file` | 組込み指示の置換用途であり、短い `AGENTS.md` とSkillによる段階読込みより影響範囲が大きい |

旧式・非推奨として確認した項目は、新規設定へ持ち込んでいない。CLI 0.155.1では `agents.max_threads` は `agents.max_concurrent_threads_per_session` の旧alias、`features.codex_hooks` は `features.hooks` の非推奨alias、`experimental_instructions_file` は `model_instructions_file` へ改名済み、`approval_policy = "untrusted"` は廃止済みである。今回のリポジトリには、これらの旧キー自体が存在しなかった。

## 将来の知見は、個別事例を残さず一般化して戻す

基盤へ変更を戻す前に、複数旅行へ適用できるか、既存の正本へ追記できるか、機械検証へ落とせるかを確認する。特定の日付、地域、施設、便、予約、current plan、候補順位、未解決Issue、調査時点の価格・営業時間は、個別旅行のYAML、Issue、ブランチへ残す。

一般化した変更は、該当するSkillまたはreferenceを一箇所だけ更新する。構造や整合性として判定できる場合はschemaまたは検証スクリプトへ移し、回帰テストを追加する。失敗事例そのものは恒久ルールにせず、現在必要な肯定形の原則へ蒸留する。

## 検証は一つのコマンドで再実行できる

```bash
.venv/bin/python tools/check_codex_customization.py
.venv/bin/python tools/validate.py
.venv/bin/python tools/render.py
.venv/bin/python -m pytest -q
```

`check_codex_customization.py` は、`AGENTS.md` のサイズ、正規Skill配置、frontmatter、referenceリンク、`agents/openai.yaml`、TOML、read-only agent、旧Skillの残存、共通基盤へのISO日付混入を検査する。旅行固有の地名や一時的な候補の意味までは機械判定できないため、変更レビューでも確認する。

公式が案内する別Codexプロセスによる発見確認は、このリポジトリの既存テスト手順ではないため自動実行しない。新しいCodexセッションで確認する場合は、リポジトリを信頼済みにしたうえで、Skill一覧に3 Skill、custom agent一覧に2 agentが現れることを確認する。
