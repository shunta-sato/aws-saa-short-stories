# プロット: network/05 世界の入り口に鍵を

| 項目 | 値 |
|---|---|
| 状態 | ready |
| family / episode | networking_and_application_security / 5 |
| terms | amazon_cloudfront, cloudfront_origin, cloudfront_cache_behavior, cloudfront_invalidation, cloudfront_origin_access_control, cloudfront_origin_access_identity, cloudfront_signed_url, cloudfront_signed_cookie, cloudfront_origin_shield, cloudfront_functions, lambda_at_edge, s3_static_website_hosting, aws_amplify(13語) |
| 時系列 | 夏の終わり。海外展開の配信フェーズ |
| 分量 | 5,000〜6,000字 |

## ねらい

CloudFrontを「世界中の入り口」として体系化し、同時に「入り口の鍵」(OAC・署名付きURL/Cookie)でアクセス制御する回。S1で散発的に登場したCloudFront知識(オリジンフェイルオーバー、エッジ)をここで一枚にまとめる。学校プランの「保護者だけが見られる配信」という、サービスの核心に関わる認可要件を扱う。

## あらすじ

海外挙式の映像配信が本格化し、毎回東京のS3まで取りに来る構成の限界が露呈。CloudFrontの設計を「ビヘイビア・オリジン・キャッシュキー」から作り直す。さらに学校プランで「URLを知っていれば誰でも見られる」状態が監査(風間)に指摘され、署名付きURL/Cookieによる本格的な認可へ移行する。

## ビート

1. **起**: 海外親族からの閲覧が遅い+転送コスト増。「全員が東京の倉庫まで写真を取りに来てる。各国の駅前に売店を出そう」(CDNの比喩)。**amazon_cloudfront**の基本(エッジ・TTL)を青柳に説明させる。
2. **承(配信の設計)**: **cloudfront_origin**(S3=静的、ALB=動的)+**cloudfront_cache_behavior**(/static/*は長TTL、/api/*はキャッシュ無効、パスごとの方針)。緊急差し替えに**cloudfront_invalidation**(1,000パス無料枠、定常運用はバージョン付きファイル名で)。海外式場のライブ需要スパイクでオリジン負荷→**cloudfront_origin_shield**(集約キャッシュ層、オリジンに近いリージョン)。
3. **転1(バケットを閉じる)**: 風間の監査指摘——「S3バケットが公開設定です。CloudFrontを経由しない直アクセスが可能。それを誰が、いつ取得したか、説明できますか」。**cloudfront_origin_access_control**(OAC)でバケットを非公開化しCloudFront専用に。旧方式**cloudfront_origin_access_identity**(OAI)は「レガシー。SSE-KMS非対応などの制約。新規はOAC」と歴史対比で。**s3_static_website_hosting**は「ウェブサイトエンドポイントはHTTPのみ・OAC不可」のため本番では棄却し、コーポレートサイト(完全公開)限定の選択肢として整理。コーポレートサイト自体はフロント刷新で**aws_amplify**(Gitプッシュでビルド・配信まで)へ、という小さな並行エピソード。
4. **転2(誰に見せるかの鍵)**: 学校プランの認可要件が山場。「URLを推測されたら他人の子の写真が見える」事態は許されない。**cloudfront_signed_url**(単一ファイル・期限付き——納品DLリンク向け)vs **cloudfront_signed_cookie**(アルバム一式・URL変更なし——保護者の閲覧セッション向け)の使い分け。S3 presigned URLとの層の違い(S3直 vs CDN経由)も一言(S3側はS3⑤/④で詳述)。キーグループと鍵ローテーションの存在に触れる。
5. **転3(エッジで動くコード)**: 保護者のデバイス別に画像サイズを出し分けたい+認可トークンの軽量検証をエッジでやりたい。**cloudfront_functions**(ミリ秒未満・JSのみ・ビューワーフックのみ・ネットワーク不可)vs **lambda_at_edge**(4フック・本文加工・外部呼び出し可・us-east-1で作成)。「軽い門番はFunctions、重い細工はLambda@Edge」。料金の桁差を城戸が一言で締める。
6. **結**: 海外配信のレイテンシとオリジン負荷の改善数値。風間の監査項目が「説明できる」状態に。締めの引き: 配信を固めた矢先、見知らぬIPレンジから学校プランへの異常な高頻度アクセスの兆候(net/06のWAF回へ)。

## 必須の対比(棄却理由込み)

- OAC vs OAI(新規はOAC、OAIはレガシー)
- ウェブサイトエンドポイント(HTTP のみ・OAC不可)vs RESTエンドポイント+CloudFront
- 署名付きURL(単一・URL個別)vs 署名付きCookie(複数・URL不変)vs S3 presigned(S3直)
- CloudFront Functions vs Lambda@Edge(フック・性能・料金・できること)
- Origin Shield(配信側の負荷集約)vs Transfer Acceleration(S1既出・アップロード側)

## 具体値の例

無効化の月1,000パス無料、Functionsのミリ秒未満/ビューワーフック限定、Lambda@Edgeのus-east-1制約、OACのSSE-KMS対応、TTLとキャッシュキー。

## 書いてはいけないこと

- WAF/Shieldの本格解説(net/06)。兆候の提示まで。
- 「CloudFrontを入れれば必ず速くなる」(キャッシュヒット率・動的コンテンツの限界に言及)。
