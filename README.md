# QCoder

QCoder で使う個人リポジトリ.

# QCoder について

URL: https://www.qcoder.jp/ja  

QCoder に参加した記録を残す.  
また, 実際にコーディングするときに使用する.

## ローカル環境のセットアップ
仮想環境を構築する.

```
python3 -m venv venv
source ./venv/bin/activate
```

`pip3` を使用する場合, リポジトリのターミナル上で以下のコマンドを実行する.

```
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

念の為, `qiskit[visualization]` も入れておく.

```
pip3 install 'qiskit[visualization]'
```

## Commit ルール

Commit の際は以下のルールに合わせて種類ごとにする.

🎉  初めてのコミット (Initial Commit)  
🔖  バージョンタグ (Version Tag)  
✨  新機能 (New Feature)  
🐛  バグ修正 (Bugfix)  
♻️  リファクタリング (Refactoring)  
📚  ドキュメント (Documentation)  
🎨  デザインUI/UX (Accessibility)  
🐎  パフォーマンス (Performance)  
🔧  ツール (Tooling)  
🚨  テスト (Tests)  
💩  非推奨追加 (Deprecation)  
🗑️  削除 (Removal)  
🚧  WIP (Work In Progress)
