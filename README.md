# cli_twitter_client
## 準備
```
pip install twitter
```

+ `auth.py`に取得したKEYを記述

```python
CONSUMER_KEY = "xxxxxxxxxx"
CONSUMER_SECRET_KEY = "xxxxxxxxxx"
ACCESS_TOKEN = "xxxxxxxxxx"
ACCESS_TOKEN_SECRET = "xxxxxxxxxx"
```
***
## 実行方法
+ `main.py`を実行してください。
***
## 機能
```
[h] / [home]       = show timeline.(non stream)
                     [OPTION] [COUNT(DEFAULT 10)]
[p] / [post]       = post tweet.
                     [OPTIONS] [*POSTTEXT] [REPLYID]
[r] / [retweet]    = retweet.
                     [OPTION] [*ID]
[s] / [search]     = search tweets.
                     [OPTIONS] [*KEYWORD] [COUNT(DEFAULT 10)]
[m] / [mydata]     = show mydata.

* is Required

***************************************************************

[q] / [e] / [exit] = exit.
[help]             = show help.
[c] / [clear]      = claer console.
```

+ `[h] / [home]`
    + タイムラインを取得します
    + オプション
        + 取得件数

```
$ home 100
```

+ `[p] / [post]`
    + ツイートします。
    + オプション
        + ツイートするテキスト(必須)
        + リプライ対象のID

```
@xxxxx / test
[20xx/xx/xx xx:xx:xx] [id=10]
Hello World!!

$ post "test tweet" 10
```

+ `[r] / [retweet]`
    + リツイートします。
    + オプション
        + リツイート対象のID

```
@xxxxx / test
[20xx/xx/xx xx:xx:xx] [id=10]
Hello World!!

$ retweet 10
```

+ `[s] / [search] `
    + キーワードでツイートを検索します。
    + オプション
        + 検索キーワード(必須)
        + 取得件数

```
$ search "key word" 100
```

+ `[m] / [mydata]`
    + 自分のアカウント情報を参照します。

```
$ mydata
```

+ `[q] / [e] / [exit]`
    + 終了します。

```
$ exit
```

+ `[help]`
    + ヘルプを表示します。

```
$ help
```

+ `[c] / [clear]`
    + コンソールをクリアします。

```
$ clear
```
