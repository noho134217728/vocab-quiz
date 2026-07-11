# 英単語小テスト生成器

このリポジトリは中山の作成した、英単語小テストを自動生成するためのWebアプリです。

指定した単語範囲から、指定した問題数だけランダムに出題できます。
問題用紙と模範解答をワンボタンで切り替えられ、印刷にも対応しています。

## 公開ページ

以下のURLから使用できます。

```text
https://ユーザー名.github.io/リポジトリ名/
```

実際のURLに置き換えてください。

## 注意

この教材は関係者向けです。
URLやファイルを外部に共有しないでください。

GitHub Pagesで公開しているため、URLを知っている人はアクセスできます。
本格運用時には、認証付きの公開方法へ移行する予定です。

---

# 使うだけの人向け

## 1. サイトを開く

Slackなどで共有されたURLを開いてください。

## 2. 小テストを作成する

画面上部で以下を指定します。

* 開始ID
* 終了ID
* 問題数
* タイトル

例：

```text
開始ID: 1
終了ID: 100
問題数: 20
タイトル: 英単語小テスト 第1回
```

この場合、ID 1〜100 の単語からランダムに20問が出題されます。

## 3. 表示を切り替える

以下のボタンで表示を切り替えられます。

* 問題用紙
* 模範解答
* 両方表示

## 4. 印刷する

以下のボタンから印刷できます。

* 問題を印刷
* 解答を印刷
* 問題＋解答を印刷

ブラウザの印刷画面が開いたら、必要に応じて以下を設定してください。

```text
用紙サイズ: A4
向き: 縦
倍率: 100% または 用紙に合わせる
背景グラフィック: 必要に応じてON
```

---

# 編集する人向け

小テストの内容は `words.csv` で管理しています。

基本的に編集するのは `words.csv` だけです。
`words.json` は自動生成されるため、通常は編集しません。

## ファイル構成

```text
vocab-quiz/
  index.html
  words.csv
  csv_to_json.py
  robots.txt
  README.md
  .github/
    workflows/
      deploy.yml
```

## 各ファイルの意味

| ファイル                           | 役割                                    |
| ------------------------------ | ------------------------------------- |
| `index.html`                   | 小テスト生成器本体                             |
| `words.csv`                    | 単語データの編集元                             |
| `csv_to_json.py`               | `words.csv` を `words.json` に変換するプログラム |
| `words.json`                   | アプリが読み込む単語データ                         |
| `README.md`                    | この説明書                                 |
| `.github/workflows/deploy.yml` | GitHub Pagesに自動公開する設定                 |

---

# 単語を追加する方法

## GitHub上で直接編集する場合

1. GitHubのリポジトリを開く
2. `words.csv` を開く
3. 右上の鉛筆マークを押して編集する
4. 一番下に新しい単語を追加する
5. `Commit changes` を押す
6. GitHub Actions が自動で実行される
7. サイトに反映される

## 追加する行の例

```csv
consequence,結果・帰結,noun,result;outcome,co_________,This decision may have serious consequences.
significant,重要な・かなりの,adjective,important;considerable,si_________,There is a significant difference between the two results.
evaluate,〜を評価する,verb,assess;judge,ev______,Students should evaluate the writer's opinion carefully.
```

---

# words.csv の列

`words.csv` は以下の6列で構成されています。

```csv
answer,ja_prompt,pos,aliases,hint,example
```

## 各列の意味

| 列名          | 意味            | 例                                      |
| ----------- | ------------- | -------------------------------------- |
| `answer`    | 正解の英単語        | `influence`                            |
| `ja_prompt` | 問題として表示される日本語 | `影響を及ぼす`                               |
| `pos`       | 品詞            | `verb`, `noun`, `adjective`, `adverb`  |
| `aliases`   | 別解            | `affect;impact`                        |
| `hint`      | ヒント           | `in_______`                            |
| `example`   | 例文            | `Her speech influenced many students.` |

## 品詞の書き方

基本的には以下を使います。

```text
verb        動詞
noun        名詞
adjective   形容詞
adverb      副詞
phrase      熟語・表現
```

## aliases の書き方

別解がない場合は空欄にします。

```csv
derive,導出する・由来する,verb,,de____,We derive the answer from the data.
```

別解が1つある場合：

```csv
influence,〜に影響を与える,verb,affect,in_______,The book influenced many young readers.
```

別解が複数ある場合は、セミコロン `;` で区切ります。

```csv
result,結果,noun,outcome;consequence,re____,The result was surprising.
```

カンマ `,` で区切るとCSVの列が崩れるので、別解の区切りには必ず `;` を使ってください。

---

# CSV編集時の注意

## 1. 列名を変更しない

1行目は必ずこのままにしてください。

```csv
answer,ja_prompt,pos,aliases,hint,example
```

この行を変更すると、変換プログラムが正しく動きません。

## 2. 例文にカンマを入れる場合は引用符で囲む

例文にカンマ `,` が入る場合は、その例文全体を `"` で囲んでください。

```csv
however,しかしながら,adverb,nevertheless,ho_____,"However, this idea is not always correct."
```

## 3. 問題文は一意に答えやすくする

日本語だけだと複数の英単語が正解になりやすいです。

あまり良くない例：

```csv
effect,影響,noun,impact;influence,ef____,The effect was clear.
```

改善例：

```csv
effect,結果として生じる影響・効果,noun,result;impact,ef____,The effect of the new rule was clear.
influence,人や物事に及ぼす影響,noun,impact,in_______,His influence on the students was great.
```

## 4. 受験生が解ける日本語にする

専門的すぎる訳語だけにすると、受験生が答えにくくなります。

例：

```csv
consequence,結果・帰結,noun,result;outcome,co_________,This decision may have serious consequences.
```

## 5. 例文は短くする

例文は小テストの模範解答に表示されます。
長すぎると印刷時に見づらくなります。

目安：

```text
8語〜15語程度
```

---

# GitHub Actionsによる自動反映

このリポジトリでは、`words.csv` を編集してCommitすると、自動で次の処理が行われます。

```text
words.csv を更新
↓
csv_to_json.py が実行される
↓
words.json が生成される
↓
index.html と words.json が GitHub Pages に公開される
```

そのため、編集者は基本的に `words.csv` だけを編集すれば大丈夫です。

## 反映を確認する方法

1. GitHubのリポジトリを開く
2. `Actions` タブを開く
3. 一番上のワークフローが成功しているか確認する
4. 成功していれば、公開ページを再読み込みする

ブラウザに古い内容が残っている場合があります。
その場合は、ページを再読み込みしてください。

```text
Mac: Command + Shift + R
Windows: Ctrl + F5
```

---

# ローカルで確認する方法

自分のパソコンで動作確認したい場合は、以下の手順を使います。

## 1. words.json を生成する

```bash
python3 csv_to_json.py
```

## 2. ローカルサーバーを起動する

```bash
python3 -m http.server 8000
```

## 3. ブラウザで開く

```text
http://localhost:8000
```

---

# よくあるエラー

## サイトに変更が反映されない

以下を確認してください。

* `words.csv` をCommitしたか
* `Actions` が成功しているか
* ブラウザを強制再読み込みしたか
* 編集した行のCSV形式が崩れていないか

## GitHub Actionsが失敗する

多くの場合、`words.csv` の書き方に原因があります。

特に以下を確認してください。

* 1行目の列名が変わっていないか
* 例文中のカンマを `"` で囲んでいるか
* 必要な列が不足していないか
* `aliases` をカンマではなくセミコロンで区切っているか

## 問題数が指定より少ない

指定した範囲にある単語数より多い問題数を指定すると、存在する単語数までしか出題されません。

例：

```text
ID 1〜10 の範囲に10語しかない
問題数を20にする
→ 実際には10問だけ出題
```

---

# 運用ルール案

## 通常利用者

* Slackに貼られたURLから使う
* URLを外部共有しない
* 問題や解答を必要に応じて印刷する

## 編集者

* `words.csv` だけを編集する
* `words.json` は直接編集しない
* 例文や日本語訳が長くなりすぎないようにする
* 変更後は `Actions` の成功を確認する

## 管理者

* `index.html` の仕様を管理する
* `deploy.yml` を管理する
* 本格運用時には認証付き公開方法を検討する

---

# 単語データ作成の方針

この教材は、大学受験生向けの英単語小テストを想定しています。

対象レベルの目安：

```text
地方国公立大学
旧帝大レベル
TOEIC 600点以上
TOEFL 50〜90点程度
```

出題語彙は以下を中心にします。

* 大学受験の長文で頻出する語
* 論説文でよく使われる抽象語
* 英作文で使いやすい動詞
* 文脈判断に必要な形容詞・副詞
* TOEICやTOEFLにも接続しやすい語

例文は、受験生が読める標準的な長さにします。
専門的すぎる例文や、大学院・研究者向けの例文は避けます。

---

# 更新履歴

## v0.1

* 英単語小テスト生成器を作成
* `words.csv` から `words.json` を自動生成
* GitHub Pagesで公開
* 問題用紙・模範解答・印刷機能に対応
