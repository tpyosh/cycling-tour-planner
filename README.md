# 下北・道南・胆振サイクリング 2026

## 旅行者向けドキュメント

- [旅程を見る](docs/itinerary.md)
- [Google Mapsに登録するピンを見る](docs/pins.md)

## このrepoの役割

このリポジトリは「1旅行1repo」で運用します。YAMLが唯一の正本（SSoT）で、`plan/current.yaml` が現在のworking planです。通常旅程は `days`、出発日を切り替える予備計画は `contingencies`、準備事項は `pre_trip_todos` に記録します。過去のsnapshotにはファイルの複製ではなくGit履歴を使い、予約開始時や出発直前には `booking-start`、`pre-departure-final` などのtagを付けられます。`docs/*.md` はYAMLから作る生成物です。

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
- `docs/*.md` は直接編集禁止
- 変更後は validate → render → test
