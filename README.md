# Lambdaをローカル環境でテストする方法(RIE) 
## Lambda Runtime Interface Emulator (RIE)とは
https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/runtimes-images.html#runtimes-test-emulator
```
実際の AWS Lambda サービスで提供されているランタイム API をローカル環境でエミュレートする代替機能 (プロキシ) として動作します。
これによりコンテナイメージとしてパッケージ化された Lambda 関数をローカルでテストすることが可能になります。
```
## 構築手順
1. lambdaのイメージを作成する
```
# Dockerfileの中身は下記URL参照
$ touch Dockerfile

$ docker build -t {image名}:{TAG} 
```
* イメージにはRIEをインストールしておく必要あり。
* AWSのベースイメージを利用する場合はデフォルトで利用可能。
* AWSコンテナイメージ
    * https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/python-image.html

2. コンテナを起動する
`docker run -p 9000:8080 {image名}:{TAG} ` 
* RIEは 8080 ポートでリスニングしているのでローカルの適当なポートとマッピングする

3. テスト実行
　`$ curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'`
* curlコマンドやAPI Testerなどのツールなどを利用し実際のlambdaを利用する形式で実行可能

## 注意点
* RIEは、Lambdaのオーケストレーターやセキュリティおよび認証の機能はエミュレートしない
* AWS提供以外のカスタムイメージの場合、RIEを直接イメージに含めるより、実行時に--entrypointでRIEを差し込む方が、商用環境に不要なRIEを持ち込まないので良い

## 参考
* https://aws.amazon.com/jp/builders-flash/202104/new-lambda-container-development-2/?awsf.filter-name=*all