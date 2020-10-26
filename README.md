# 使用方法

現状はファイル検索できないので，csvReader.py の`filepath`を書き換えることで対応

```python
    '''
    現状はfilepathを変更して対応
    '''
    filepath = '../data/test001.csv'
```

---

# venv

## 新しい環境作成

```zsh
$ cd [project dir]
$ python3 -m venv [newenvname]
# 名前はvenvにするのが無難
```

## Activate

```zsh
$ source [newenvname]/bin/activate
```

## 環境にインストールされているパッケージ確認

```zsh
$ pip freeze
```

## Deactivate

```zsh
$ deactivate
```

---

# Blueprints

[qiita-Flask のディレクトリ構成について考えてみたら Blueprints を試していた話](https://qiita.com/rarewin/items/8f252313db8ee7fa2de0)

## flask 起動

```zsh
$ export FLASK_APP=hoge
$ export FLASK_DEBUG=true
# vue-chartで実行
$ python3 -m flask run
```
