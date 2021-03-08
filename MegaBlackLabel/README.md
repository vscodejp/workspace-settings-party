# VS Code Meetup #10 お隣の.vscode を覗いてみよう！

https://vscode.connpass.com/event/204791

VS Code Meetup のイベントの参加者リポジトリです。
参加される方には、ここにご自身の設定をコミットしてください。
なお、紹介いただいたソースコードの秘匿情報を含まないようにお気をつけください。

```md
# このワークスペースの目的
AmpfyでLambdaを使ってPDF変換を実装


# どんなことをしたくて設定を入れているか

- localstackの起動
- dind-ubuntuでDocker内部にあるdocker-composeの起動処理
- samコマンドの実行テスト

# 相談したい、話したいこと（任意）

AWSの@aws-amplify/cliを使いつつlocalstackの開発をDockerでやろうとすると、Dockerの中でさらにDockerを起動して、その中でlocalstack立ち上げるのですが、手順が面倒だったのでtasks.jsonに書きました。

同梱されているdocker-composeファイルがlocalstack立ち上げるやつなのですが、1プロジェクトに2つのdocker-composeファイルがあるんだぜ。頭おかしいでしょ。

なお、このサンプルプロジェクトですが、検証中にAWSから発表されたコンテナイメージのサポートによってこんなことやらなくて済むようになったのでお役御免となりました。

https://aws.amazon.com/jp/blogs/news/new-for-aws-lambda-container-image-support/


```
