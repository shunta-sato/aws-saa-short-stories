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

### S2設計原則「後手のシーズン」

S2の各話の火種は、前話の応急処置が生んだ歪みから連鎖させる(01: 放置した赤丸が計画メンテ通知で締切付きに→急造のNAT3台→02: データ処理コストとCIDR事故→…)。シーズン主題は「先送りの利子」。S1の大火の籠城戦に対し、S2は小さい火が連鎖する遭遇戦として運ぶ。

### S2幕間(ショートショート)

用語集441語に立項されていないがSAA頻出・難解のトピックを、本編より短い幕間(目安1,500〜2,500字。人間模様を十分に描くためなら4,000字程度まで延ばしてよい。terms: []、coverage対象外)で補強する。プロットは plots/network-ex01〜04。**幕間は技術補強と同時に、本編では描かれない登場人物の人となり・人間模様を主役にするエンタメ回とする**(技術は1トピックに絞り、謎解き・役割逆転・照れ・賭けなどの仕掛けで人間を前に出す。字数より人間を優先する)。

| 幕間 | 主題 | 配置 |
|---|---|---|
| ex01 通らなかった記録 | VPC Flow Logs | net/01の直後 |
| ex02 トンネルの両端 | VGW / Customer Gateway(S2S VPNの構成要素) | net/02の直後 |
| ex03 一本足の専用線 | Direct Connect Gateway / DX冗長化(DX+VPNフェイルオーバー) | net/02の直後(ex02の後) |
| ex04 名前が届かない日 | Route 53 Resolver(ハイブリッドDNS) | net/04の直後 |

## S3 鍵と名札編の話単位割当(67語/5話+幕間4本)

**シーズンアーク「静かな侵入者」**: 5話貫通の潜入戦。各話の冒頭にタイムスタンプ付きの無機質なログ断片を1行置く(手口は描かない)。侵入者は最後まで捕まらない(現実路線)——勝利条件は「叩かれても倒れない・気づける・説明できる」。風間がシーズン主役格。⑤で瀬名の父入院の前震(正典)。プロットは plots/security-01〜05、security-ex01〜04。

| 話 | タイトル(案) | 担当用語(数) |
|---|---|---|
| sec/01 | 名札の棚卸し | iam, iam_user, iam_group, iam_role, iam_policy, iam_identity_policy, iam_root_user, iam_access_key, multi_factor_authentication_mfa, sts_assume_role, iam_trust_policy, iam_policy_evaluation_logic, iam_explicit_deny, shared_responsibility_model (14) |
| sec/02 | 誰も住んでいないはずの家 | organizations_organizational_unit, service_control_policy, aws_iam_identity_center, iam_identity_center_permission_set, iam_cross_account_access, iam_permissions_boundary, iam_session_policy, iam_abac, resource_based_policy, aws_resource_access_manager_aws_ram, aws_directory_service (11) |
| sec/03 | 鍵の鍵 | aws_kms, kms_key_policy, kms_aws_managed_key, kms_customer_managed_key, kms_data_key, kms_envelope_encryption, kms_grant, kms_key_rotation, kms_multi_region_key, aws_cloudhsm, aws_certificate_manager_acm, acm_dns_validation, ebs_volume_encryption, s3_sse_s3, s3_sse_kms, s3_sse_c (16) |
| sec/04 | 一晩の鍵交換 | s3_bucket_policy, s3_acl, s3_block_public_access, s3_object_ownership_bucket_owner_enforced, s3_presigned_url, s3_access_points, efs_access_points, vpc_endpoint_policy, amazon_cognito, alb_authentication_oidc_cognito, api_gateway_authorizers, aws_secrets_manager, secrets_manager_rotation, systems_manager_parameter_store, parameter_store_secure_string (15) |
| sec/05 | 検知して、止まって、戻せる | amazon_guardduty, amazon_inspector, amazon_macie, amazon_detective, aws_security_hub, aws_artifact, aws_audit_manager, aws_shield, aws_waf, aws_network_firewall, aws_firewall_manager (11) |

### S3幕間(ショートショート)

問題データに登場するが用語集441語に立項されていない頻出・難解トピックの補強(terms: []、目安1,500〜2,500字・人間模様を描くためなら4,000字程度まで可、エンタメ方針適用)。

| 幕間 | 主題 | 配置 | エンタメの核 |
|---|---|---|---|
| ex01 外から見える鍵穴 | IAM Access Analyzer | sec/01の直後 | 風間のノートの正の字と花丸 |
| ex02 又貸しの合言葉 | 外部ID(混乱した代理人) | sec/02の直後 | 狩野×風間の東京コンビ、契約書が設定に翻訳できる |
| ex03 名札を拾う者 | IMDSv2の強制 | sec/04の直後 | 矢吹のテプラ剥がし行脚の思い出 |
| ex04 使われていない鍵 | 認証情報レポート/最終アクセス情報 | sec/05の直後(エピローグ) | 瀬名の鍵束が一番膨らんでいた(人間SPOFの数値化、S8布石) |

## S4 記録の器編の話単位割当(41語/3話+幕間2本)

**シーズンアーク「数える人」**: 3年目春。真鍋一花が神戸へ正式合流し、矢吹の「復元単位」の思想がデータモデリングの言葉に翻訳されるシーズン。火種は成長の利子——動画GA後のユーザー増と新商品「思い出検索」で、S1-02でgp3化して以来だましだまし育ててきたメタデータDB(RDS)が天井に触れる。各話の主題は「器を選ぶ前に、中身と読まれ方を数える」。真鍋の「で、1日何件です?」がシーズンの背骨。瀬名は東京との行き来が増える(数日単位の不在。理由は説明しない——S8への継続前震)。

| 話 | タイトル(案) | 担当用語(数) |
|---|---|---|
| db/01 | 行列は窓口で分ける | amazon_rds, rds_multi_az_deployment, rds_multi_az_db_cluster, read_replica, rds_read_replica_promotion, rds_cross_region_read_replica, rds_proxy, rds_snapshot, rds_automated_backup, rds_point_in_time_recovery, rds_storage_autoscaling, amazon_elasticache, elasticache_redis_memcached_choice, elasticache_cluster_mode, elasticache_lazy_loading, elasticache_write_through (16) |
| db/02 | 六つの写し、一つの器 | amazon_aurora, aurora_cluster_volume, aurora_replica, aurora_writer_reader_endpoint, amazon_aurora_serverless, aurora_serverless_v2_capacity, aurora_global_database, amazon_redshift, amazon_documentdb, amazon_neptune, amazon_keyspaces (11) |
| db/03 | 数えてから、建てる | amazon_dynamodb, dynamodb_partition_key, dynamodb_sort_key, dynamodb_gsi, dynamodb_lsi, dynamodb_rcu_wcu, dynamodb_provisioned_capacity, dynamodb_on_demand_capacity, dynamodb_autoscaling, dynamodb_consistency_models, dynamodb_ttl, dynamodb_pitr, dynamodb_global_tables, dynamodb_dax (14) |

### S4幕間(ショートショート)

問題データに登場するが用語集441語に立項されていない頻出・難解トピックの補強(terms: []、1,500〜2,500字、エンタメ方針適用)。DMS・DynamoDB Streamsは用語集に立項済みのため幕間では扱わない(それぞれS5・S7系の本編担当)。

| 幕間 | 主題 | 配置 | エンタメの核 |
|---|---|---|---|
| ex01 パスワードのない扉 | IAMデータベース認証(RDS/Aurora) | db/01の直後 | 風間の月次訪問、合鍵台帳の「回さなくていい扉」。青柳の例外台帳当番が実を結ぶ |
| ex02 巻き戻しの作法 | Aurora Backtrack(PITRとの対比) | db/02の直後 | 真鍋の検証事故と矢吹のテープ巻き戻しの記憶。青柳×真鍋の初共同作業 |

## S3以降の用語割当(シーズンレベル、話単位は各シーズン着手時に確定)

- **S3 セキュリティ/ID(67語/5話+幕間4本)**: 話単位の割当・シーズンアーク・幕間は上の「S3 鍵と名札編」節を正典とする。
- **S4 データベース(41語/3話+幕間2本)**: 話単位の割当・シーズンアーク・幕間は上の「S4 記録の器編」節を正典とする。
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
| 赤丸の半年放置(既知リスクの先送り構造) | **net/01** | **S8③**(人間SPOFの同型。「赤丸は構成図の中だけやなかった」) |
| 安全は売上を生まない工事(先送りの利子と予算) | net/01(城戸の電話一本・臨時コスト) | **S9**(安全予算の言語化・城戸メイン) |
| 赤丸にオーナーと期限がなかった(気づきを仕組みに載せる) | net/01(日付と持ち主の運用開始) | **S8**(Config等の検知自動化・青柳) |
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
