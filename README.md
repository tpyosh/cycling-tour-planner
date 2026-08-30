# 下北・道南・胆振サイクリング 2026

## 旅行者向けドキュメント

- [旅程を見る](docs/itinerary.md)
- [Google Mapsに登録するピンを見る](docs/pins.md)
- [未解決事項を見る](docs/issues.md)

## このrepoの役割

このリポジトリは「1旅行1repo」で運用します。YAMLが唯一の正本（SSoT）で、`plan/current.yaml` が現在のworking planです。通常旅程は `days`、出発日を切り替える予備計画は `contingencies`、準備事項は `pre_trip_todos`、未解決事項は `issues.yaml` に記録します。過去のsnapshotにはファイルの複製ではなくGit履歴を使い、予約開始時や出発直前には `booking-start`、`pre-departure-final` などのtagを付けられます。`docs/*.md` はYAMLから作る生成物です。

## `itinerary.md` は現行計画のスナップショット

`docs/itinerary.md` には、現在採用している日程・ルート・立ち寄り先と、その日の実行判断に必要な制約だけを載せます。施設の基本情報、複数日にまたがる営業時間表、調査過程、出典一覧などの詳細資料は載せません。

現行旅程に時間・安全・接続上の未解決リスクがある場合は、該当日の節に短い要約を置き、`docs/issues.md` の該当Issueへリンクします。問題の根拠、影響、次の確認事項、解決条件は `issues.yaml` で管理します。調査済みの事実と出典は `evidence/sources.yaml` に残します。

## 日常操作

```bash
python -m pip install -r requirements.txt
python tools/validate.py
python tools/render.py
pytest
```

## 編集ルール

- 候補追加: `catalog/*.yaml`
- 現行旅程変更: `plan/current.yaml`
- 出発日変更などの予備計画: `plan/current.yaml` の `contingencies`（通常旅程の `days` へ混ぜない）
- 旅行前の準備事項: `plan/current.yaml` の `pre_trip_todos`
- 変動情報・直前確認事項: `evidence/sources.yaml`
- 旅程上の未確認事項・判断待ち: `issues.yaml`
- 旅程スナップショット: `docs/itinerary.md`（詳細調査を転載せず、該当日の制約とIssueリンクに限定）
- `docs/*.md` は直接編集禁止
- 変更後は validate → render → test
