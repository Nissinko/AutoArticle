# AutoArticle
記事構成案自動化

## 0. gitリポジトリのクローン
```
git clone https://github.com/Nissinko/AutoArticle.git
```

## 1.パスワードを変更する
mieruca.pyのhogeの部分を適切なパスワードに変更して下さい

## 2.ダウンロードディレクトリの修正
mieruca.pyのdownload_directoryを、ブラウザからファイルをダウンロードした際の標準格納フォルダへのパスに変更して下さい。

## 3.実行
```
python mieruca.py
```
上記のコマンドを実行すると、./data/<検索キーワード>/に共起語のxlsxファイル、キーワード及び検索結果のdocxファイルが作成されます。

## 4.Windows対応（編集中）
