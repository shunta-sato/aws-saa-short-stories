# プロット: network/06 攻める者、迎える者

| 項目 | 値 |
|---|---|
| 状態 | ready |
| family / episode | networking_and_application_security / 6(S2最終話) |
| terms | waf_web_acl, waf_managed_rule_group, waf_rate_based_rule, shield_standard_advanced, amazon_api_gateway, api_gateway_rest_api, api_gateway_http_api, api_gateway_websocket_api, api_gateway_endpoint_types, api_gateway_vpc_link, lambda_function_url, aws_device_farm(12語) |
| 時系列 | 秋。net/05の引き(異常アクセスの兆候)の直後 |
| 分量 | 5,500〜6,500字 |

## ねらい

S2の総決算。net/05の引きを受けた攻撃対応(WAF/Shield)と、パートナー向けAPI公開(API Gateway)の二本柱で「迎えたい客と、迎えたくない客」を分ける設計を描く。風間が東京から本格介入し、S3(セキュリティ編)への橋渡しを行う。

## あらすじ

学校プランへのスクレイピング・ログイン総当たりが本格化。風間が東京から飛んできて、L7防御(WAF)とDDoS対応(Shield)の体系を整える。並行して、印刷パートナー(net/02のPrivateLink)向けに正式なAPIを公開する案件が走り、API Gatewayの設計判断を通る。最後にネットワーク編全体を「城の地図」として総括し、S3(鍵と名札)へ繋ぐ。

## ビート

1. **起**: net/05の兆候が本格化。特定IPレンジから保護者ログインへの総当たり+画像の機械的収集。署名付きCookieで中身は守られているが、ログイン画面とAPIが叩かれ続けレイテンシ悪化。風間が新神戸に降り立つ(東京拠点から初の現地参戦)。
2. **承(層の整理)**: 風間が防御の層を板書——「L3/L4の洪水は**shield_standard_advanced**(Standardは全員に自動・無償、AdvancedはSRT支援・コスト保護・年間コミット)。L7のリクエスト内容は**waf_web_acl**。VPC内部はNetwork Firewall(S3シーズン担当)」。WAFをCloudFrontとALBに関連付け(CloudFront用はus-east-1という細部)。**waf_managed_rule_group**(OWASP系を即適用・まずカウントモードで誤検知確認)+**waf_rate_based_rule**(ログインパスに厳しめのしきい値・NAT配下の巻き込みリスクに注意)。攻撃は止むが、堂島が一言「止めたことと、説明できることは別だぞ」→風間「では、その話は次の季節に」(S3への引き)。
3. **転1(パートナーAPI)**: 印刷パートナー向け注文API の正式公開。**amazon_api_gateway**の選定階段: 機能要件(APIキーで取引先ごとのクォータ、リクエスト検証、WAF適用)→**api_gateway_rest_api**。「軽くて安い**api_gateway_http_api**はJWT認可とプロキシには最適だが、使用量プラン・キャッシュ・WAF直結がない」という棄却理由を明示。注文ステータスのリアルタイム通知の話が出て**api_gateway_websocket_api**(双方向・接続ID管理)を別系統として整理。社内バッチの簡易フックは**lambda_function_url**(AuthType=AWS_IAM、API GW機能不要の最小口)で済ませる対比。
4. **転2(入り口の場所)**: **api_gateway_endpoint_types**——パートナーは国内固定なのでリージョン型(エッジ最適化は自前CloudFrontと二重になるため棄却)、社内管理APIはプライベート型+VPCエンドポイント。バックエンドのECSはプライベートサブネットのまま**api_gateway_vpc_link**(REST=NLB前提という細部、net/02のPrivateLink知識と接続)。
5. **転3(モバイルの検証)**: 保護者アプリの新ログインフロー(WAF・署名Cookie対応)を多端末で検証する必要→**aws_device_farm**(実機ファーム・自動/手動テスト)を青柳が回す。「手元に端末を並べる時代やないんやな」と矢吹。軽い幕間として扱い、デバイス互換の不具合を1件検出して価値を示す。
6. **結(S2総括とS3への橋)**: 美咲がネットワーク編の全成果を「城の地図」として一枚に描く——通り(VPC/ルート)、門(IGW/NAT/エンドポイント)、受付(ELB)、案内板(Route 53)、売店と鍵(CloudFront/署名)、検問(WAF)。堂島「地図はできた。次は、**名札と鍵束**の話だ。誰が、どの部屋に、どの鍵で入れるのか」。風間が東京へ戻る新幹線のホームで美咲に「次の季節は、私の番ですね」(S3主役格の宣言)。

## 必須の対比(棄却理由込み)

- WAF(L7内容)vs Shield(L3/L4・Standard自動/Advanced有償)vs レートベースルール(頻度)
- REST API vs HTTP API(使用量プラン・キャッシュ・WAF・コストの差)
- エンドポイントタイプ3種(エッジ最適化/リージョン/プライベート)の要件対応
- API Gateway vs Lambda Function URL(フル機能の入口 vs 最小の口)
- VPCリンク(API→VPC方向)とプライベートAPI(VPC→API方向)の混同注意

## 具体値の例

CloudFront用WAFのus-east-1、レートベースの時間窓としきい値、429 Too Many Requests、REST=NLB前提のVPCリンク、Shield Advancedの年間コミット・SRT。

## 書いてはいけないこと

- IAM/KMS/GuardDuty等の本格解説(S3担当)。風間は「層の整理」と「次の季節」の予告まで。
- 攻撃者の手口の具体的な再現手順(学習コンテンツとして攻撃のチュートリアル化はしない)。
