# 下北・道南・胆振サイクリング 2026

## このrepoの役割

このリポジトリは「1旅行1repo」で運用します。YAMLが唯一の正本（SSoT）で、`plan/current.yaml` が現在のworking planです。過去のsnapshotにはファイルの複製ではなくGit履歴を使い、予約開始時や出発直前には `booking-start`、`pre-departure-final` などのtagを付けられます。`docs/*.md` はYAMLから作る生成物です。

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
- 変動情報・直前確認事項: `evidence/sources.yaml`
- `docs/*.md` は直接編集禁止
- 変更後は validate → render → test
