# シリーズ構成計画(全10シーズン・全35話)

このファイルはシリーズ全体の正典計画。各話の詳細プロットは `plots/` 配下の個別ファイル、世界観・人物は `universes/photorim/universe.md` を参照。**プロットは執筆前の設計図であり、執筆済み本文と矛盾した場合は本文と universe.md が優先する。**

## 分野の切り方(方針)

- カバレッジの管理単位は引き続き taxonomy_family(`tools/check_coverage.py` で機械検証)。
- 読書体験の単位は**シーズン**とする。1シーズン=1〜6話で、原則1ファミリーを担当するが、物語の時系列はシーズンを貫いて進行する。
- 各話の担当用語はfront matterの `terms` が正。既出用語の再登場(再掲)は自由だが、担当は1話のみ。
- 復習・物語推進に特化した話(terms: [])を各シーズン末に置いてよい(例: storage/06)。

## シーズン一覧と時系列

| S | シーズン | family | 話数 | 状態 | 物語上の時間 |
|---|---|---|---|---|---|
| 1 | ストレージとレジリエンス | storage_architecture + resilience_and_dr | 7(既刊6+新作1) | 既刊+plots/storage-06 | 1年目春〜冬 |
| 2 | 城の通りと門(ネットワーク) | networking_and_application_security | 6 | plots/network-01〜06 | 2年目春〜夏 |
| 3 | 鍵と名札(セキュリティ/ID) | security_identity_and_access | 5 | 構想(下記) | 2年目秋〜冬 |
| 4 | 記録の器(データベース) | database_architecture | 3 | 構想 | 3年目春 |
| 5 | 流れる記録(取り込み・分析) | data_ingestion_and_analytics | 3 | 構想 | 3年目夏 |
| 6 | 動かす力(コンピューティング) | compute_and_containers | 3 | 構想 | 3年目秋 |
| 7 | ほどよい距離(疎結合) | decoupling_and_integration | 2 | 構想 | 3年目冬 |
| 8 | 誰がいなくても(運用・ガバナンス) | management_governance_and_observability | 3 | 構想 | 4年目春 |
| 9 | 説明できる請求書(コスト) | cost_optimization | 2 | 構想 | 4年目夏 |
| 10 | 波の高さを知る日(完結) | performance_and_scaling + 総集 | 1 | 構想 | 4年目秋 |

## S2 ネットワーク編の用語割当(75語/6話)

| 話 | タイトル(案) | 担当用語(数) |
|---|---|---|
| net/01 | 一本の通り道 | amazon_vpc, vpc_cidr_block, vpc_route_table, public_subnet, private_subnet, internet_gateway, egress_only_internet_gateway, nat_gateway, nat_instance, elastic_ip, security_group, network_acl (12) |
| net/02 | 門は増やして、道は閉じる | vpc_endpoint, s3_gateway_endpoint, s3_interface_endpoint, interface_endpoint_private_dns, aws_privatelink, privatelink_endpoint_service, vpc_peering, aws_transit_gateway, aws_direct_connect, aws_site_to_site_vpn, aws_client_vpn, efs_mount_target (12) |
| net/03 | 行事の朝の受付戦争 | elastic_load_balancing_elb, application_load_balancer, alb_listener_rule, alb_path_based_routing, alb_host_based_routing, alb_target_group, alb_sticky_sessions, network_load_balancer, nlb_static_ip_elastic_ip, nlb_tls_listener, nlb_udp_support, elb_cross_zone_load_balancing, gateway_load_balancer, gateway_load_balancer_endpoint (14) |
| net/04 | 名前の見つけ方 | amazon_route_53, route53_alias_record, route53_health_check, route53_failover_routing, route53_weighted_routing, route53_latency_based_routing, route53_geolocation_routing, route53_geoproximity_routing, route53_multivalue_answer_routing, private_hosted_zone, aws_global_accelerator, global_accelerator_static_anycast_ip (12) |
| net/05 | 世界の入り口に鍵を | amazon_cloudfront, cloudfront_origin, cloudfront_cache_behavior, cloudfront_invalidation, cloudfront_origin_access_control, cloudfront_origin_access_identity, cloudfront_signed_url, cloudfront_signed_cookie, cloudfront_origin_shield, cloudfront_functions, lambda_at_edge, s3_static_website_hosting, aws_amplify (13) |
| net/06 | 攻める者、迎える者 | waf_web_acl, waf_managed_rule_group, waf_rate_based_rule, shield_standard_advanced, amazon_api_gateway, api_gateway_rest_api, api_gateway_http_api, api_gateway_websocket_api, api_gateway_endpoint_types, api_gateway_vpc_link, lambda_function_url, aws_device_farm (12) |

## S3以降の用語割当(シーズンレベル、話単位は各シーズン着手時に確定)

- **S3 セキュリティ/ID(67語/5話)**: ①IAM基礎(ポリシー評価・ロール・STS・MFA等14語) ②組織とクロスアカウント(SCP/OU/Identity Center/ABAC/Permissions Boundary等11語) ③暗号化(KMS一式/SSE3種/ACM/CloudHSM等16語) ④アプリと データのアクセス制御(S3系/Cognito/ALB認証/Secrets/Parameter Store等16語) ⑤脅威検知と監査(GuardDuty/Inspector/Macie/Security Hub/Detective等10語)。⑤で瀬名が父の入院で東京へ発つ「前震」を描く。
- **S4 データベース(41語/3話)**: ①RDS/Multi-AZ/レプリカ系 ②Aurora系+Global Database ③DynamoDB+ElastiCache。真鍋一花が本格合流。
- **S5 取り込み・分析(39語/3話)**: ①Kinesis/Firehose/MSK ②Glue/Athena/Lake Formation/Redshift ③AI系サービス+QuickSuite(写真の自動タグ付け文脈)。真鍋メイン。
- **S6 コンピューティング(39語/3話)**: ①EC2/ASG/起動テンプレート/スケーリングポリシー ②ECS/EKS/Fargate/Batch/Beanstalk ③Lambda詳説+Outposts/Wavelength。
- **S7 疎結合(31語/2話)**: ①SQS/SNS ②EventBridge/Step Functions/Streams。
- **S8 運用・ガバナンス(39語/3話)**: ①CloudWatch/X-Ray/Grafana ②CloudFormation/Organizations/Control Tower/Service Catalog ③SSM/Config/CloudTrail/Trusted Advisor/W-A。**③が「瀬名がいない日」本番回**(human SPOF、break-glass、守屋の伏線全回収)。
- **S9 コスト(33語/2話)**: ①購入オプション(RI/SP/Spot/キャパシティ予約) ②データ転送コスト/配賦/Budgets。城戸メイン。
- **S10 完結(7語+総集/1話)**: 南海トラフ臨時情報。performance_and_scaling 7語(horizontal/vertical/stateless/stateful/auto_scaling/transfer_acceleration/api_gateway_throttling_usage_plan)を総集的に担当。美咲のアルバム、滝本(自治体)、全キャラ集結。災害原則(universe.md)を厳守し、「備える人々」の話として締める。

## 伏線マップ(張る→回収)

| 伏線 | 張った場所 | 回収予定 |
|---|---|---|
| NAT 1AZ・踏み台1台・バッチ1台(SPOF赤丸) | S1 DR編 | **net/01** |
| 矢吹「どの単位で戻すんや」 | S1全体 | **storage/06**(本番障害でユーザー単位復元) |
| 狩野「止めないでください」→優先度を決める人へ | S1 DR編で種 | **storage/06**で中間到達、S10で完成 |
| 守屋「人が入れへんかったら」 | S1 DR編 | S8③(break-glass本番) |
| 瀬名のヘッドハント・東京の両親 | universe v2 | S3⑤で前震(数日不在)→S8③本番 |
| 美咲の波打ったアルバム | storage/05 | S10 |
| 青柳「検知して止めて戻せる仕組み」 | storage/05 | net/01で芽(監視自動化)→S8①② |
| 城戸「請求書で説明できますか」 | storage/01 | net/02(NAT処理料金)→S9 |
| 真鍋一花(東雲の若手、矢吹の元部下) | **net/02で初登場(カメオ)** | S4〜S5でメイン |
| 滝本早苗(高知の自治体防災担当) | **storage/06で初登場** | net/03、S10 |
| CloudFrontオリジンフェイルオーバー実発動 | S1 DR編(訓練) | **storage/06**(本番) |

## ストレージ編(既刊)Updateプラン

※出版前のためUpdate可。ただし**本文修正は今は実施しない**。実施時期は次の改稿バッチ(S2執筆前を推奨)。

1. **用語コラム形式のロールアウト**: storage/02〜05とresilience_and_dr/01の用語表を、storage/01と同じコラム形式(太字一行決め手+2〜4文)へ統一する。
2. **読書順ナビ**: READMEの目次をシーズン制に再編し、各編末尾に「次の話: 〜」リンクを追加。resilience_and_dr/01の「(完結)」表記を「シーズン1 第7話の前日譚」的位置付けに改める(storage/06がS1の最終話になるため)。
3. **接続線の微修正(数行)**: storage/05の風間初出にnet/06(WAF回)への含みを一行。storage/02のAWS Backup節にstorage/06で効く「復元訓練」への含みを一行。
4. **表記統一**: 既刊の「編」番号をシーズン表記(S1-01〜S1-07)に揃える(ファイル名は変更せずfront matterと冒頭表記のみ)。
5. 技術内容・用語割当・クイズは変更しない(コラム化は形式変換のみ)。

## 制作ワークフロー(確認)

プロット(本ファイル+個別プロット)→ Opus執筆 → 監督レビュー(物語+技術の二段階、writing-guide準拠)→ 修正ループ → コラム・カバレッジ機械検証 → PR。
