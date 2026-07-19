# シリーズ構成計画(全10シーズン・全37話)

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
| 4 | 記録の器(データベース) | database_architecture | 4 | plots/database-01〜04 | 3年目春〜夏 |
| 5 | 流れる記録(取り込み・分析) | data_ingestion_and_analytics | 3 | plots/analytics-01〜03 | 3年目夏〜秋 |
| 6 | 動かす力(コンピューティング) | compute_and_containers | 3 | plots/compute-01〜03 | 3年目冬(11月〜2月上旬) |
| 7 | ほどよい距離(疎結合) | decoupling_and_integration | 2 | plots/decoupling-01〜02 | 4年目2月〜3月 |
| 8 | 誰がいなくても(運用・ガバナンス) | management_governance_and_observability | 3 | plots/governance-01〜03 | 4年目4月〜6月 |
| 9 | 説明できる請求書(コスト) | cost_optimization | 2 | plots/cost-01〜02 | 4年目7月〜8月 |
| 10 | 波の高さを知る日(完結・劇場版前後編) | performance_and_scaling + 総集 | 2 | plots/performance-01〜02 | 4年目9月〜10月 |

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

## S4 記録の器編の話単位割当(41語/4話+幕間3本)

**シーズンアーク「数える人」**: 3年目春。真鍋一花が神戸へ正式合流し、矢吹の「復元単位」の思想がデータモデリングの言葉に翻訳されるシーズン。火種は成長の利子——動画GA後のユーザー増と新商品「思い出検索」で、S1-02でgp3化して以来だましだまし育ててきたメタデータDB(RDS)が天井に触れる。各話の主題は「器を選ぶ前に、中身と読まれ方を数える」。真鍋の「で、1日何件です?」がシーズンの背骨。瀬名は東京との行き来が増える(数日単位の不在。理由は説明しない——S8への継続前震)。

**シーズンの人間側の主題(db/03を軸に)**: フォトリムには頼れるシニアDB人材がいない——美咲も瀬名もインフラ寄り、真鍋は26歳で大規模データは未経験。検証1万件で出ない問題が本番100万件で顔を出し、クラウドの馬力(スケールアップ)で殴れば請求書が跳ねる。その袋小路で「データ設計に立ち返る」導き手として、東雲アーカイブズの元DBA・戸倉重雄(引退・一話限りの客演)を立てる。矢吹=復元単位(運用の系譜)と戸倉=形と分布(設計の系譜)が真鍋の中で合流し、「設計レビューの型」の制度化でシニア不在を型と帳面で埋める——真鍋の成長がそのままチームに「データの層」を増やし、S5(分析)で真鍋がメインを張る土台になる。

| 話 | タイトル(案) | 担当用語(数) |
|---|---|---|
| db/01 | 行列は窓口で分ける | amazon_rds, rds_multi_az_deployment, rds_multi_az_db_cluster, read_replica, rds_read_replica_promotion, rds_cross_region_read_replica, rds_proxy, rds_snapshot, rds_automated_backup, rds_point_in_time_recovery, rds_storage_autoscaling, amazon_elasticache, elasticache_redis_memcached_choice, elasticache_cluster_mode, elasticache_lazy_loading, elasticache_write_through (16) |
| db/02 | 六つの写し、一つの器 | amazon_aurora, aurora_cluster_volume, aurora_replica, aurora_writer_reader_endpoint, amazon_aurora_serverless, aurora_serverless_v2_capacity, aurora_global_database, amazon_redshift, amazon_documentdb, amazon_neptune, amazon_keyspaces (11) |
| db/03 | 一万件は嘘をつく | [](物語推進+データ設計基礎回。S1-01「請求書は嘘をつかない」との対題。戸倉客演、設計レビュー制度化) |
| db/04 | 数えてから、建てる | amazon_dynamodb, dynamodb_partition_key, dynamodb_sort_key, dynamodb_gsi, dynamodb_lsi, dynamodb_rcu_wcu, dynamodb_provisioned_capacity, dynamodb_on_demand_capacity, dynamodb_autoscaling, dynamodb_consistency_models, dynamodb_ttl, dynamodb_pitr, dynamodb_global_tables, dynamodb_dax (14) |

### S4幕間(ショートショート)

問題データに登場するが用語集441語に立項されていない頻出・難解トピックの補強(terms: []、1,500〜2,500字、エンタメ方針適用)。DMS・DynamoDB Streamsは用語集に立項済みのため幕間では扱わない(それぞれS5・S7系の本編担当)。

| 幕間 | 主題 | 配置 | エンタメの核 |
|---|---|---|---|
| ex01 パスワードのない扉 | IAMデータベース認証(RDS/Aurora) | db/01の直後 | 風間の月次訪問、合鍵台帳の「回さなくていい扉」。青柳の例外台帳当番が実を結ぶ |
| ex02 巻き戻しの作法 | Aurora Backtrack(PITRとの対比) | db/02の直後(db/03の前) | 真鍋の検証事故と矢吹のテープ巻き戻しの記憶。青柳×真鍋の初共同作業 |
| ex03 豆の帳面 | (人物回・技術新出なし)戸倉重雄の29年と「記録を付ける人」 | db/03の直後(db/04の前) | 帳面を返しに行く真鍋+美咲。豆の台帳=人間版アクセスパターン。「引けん記録は、無いのと同じや」 |

## S5 流れる記録編の話単位割当(39語/3話+幕間2本)

**シーズンアーク「数えながら、流す」**: 3年目夏〜秋。秋β公開を跨ぎ、真鍋がメインを張る。S4で数え切った中身を、今度はリアルタイムに流し(川)、湖に貯め(台帳)、機械に読ませる(裏書き)。人間側の主題は二つ——①戸倉の系譜の制度化(帳面→カタログ→設計レビューの型の運用)と"何か"のジャブ(S5-02)、②「機械が書く裏書き」の責任(自動で書く・人が承る)。瀬名の東京行き来は続く(理由は書かない——S8前震)。

| 話 | タイトル(案) | 担当用語(数) |
|---|---|---|
| an/01 | 数えながら、流す | amazon_kinesis, kinesis_data_streams, kinesis_shard, kinesis_partition_key, kinesis_retention_period, kinesis_enhanced_fan_out, amazon_data_firehose, firehose_delivery_stream, firehose_buffering_hint, firehose_record_transformation, amazon_managed_streaming_for_apache_kafka_amazon_msk, amazon_kinesis_video_streams (12) |
| an/02 | 湖の底の台帳 | data_lake, aws_glue, glue_crawler, glue_data_catalog, glue_etl_job, parquet_columnar_format, amazon_athena, athena_partitioning, athena_workgroup, athena_federated_query, aws_lake_formation, amazon_opensearch_service, amazon_emr, redshift_spectrum, redshift_copy_unload (15) |
| an/03 | 写真が言葉になる日 | amazon_rekognition, amazon_transcribe, amazon_translate, amazon_comprehend, amazon_textract, amazon_polly, amazon_lex, amazon_kendra, amazon_sagemaker_ai, amazon_quicksuite, amazon_elastic_transcoder, aws_data_exchange (12) |

### S5幕間(ショートショート)

| 幕間 | 主題 | 配置 | エンタメの核 |
|---|---|---|---|
| ex01 流れの中の算盤 | Managed Service for Apache Flink(ウィンドウ集計) | an/01の直後 | 城戸×青柳。「締めのない数字を信じてええんですか」→速報と確定の二本立て |
| ex02 借りない倉庫 | Redshift Serverless(RPU従量) | an/02の直後 | 城戸の倹約回。「使うた分だけ借りる、いう借り方」。削った金は消すな、移せ(S8/S9への種) |

## S6 動かす力編の話単位割当(39語/3話+幕間2本)

**シーズンアーク「先に起きる機械」**: 3年目11月下旬〜4年目2月上旬。主題は「**人が機械より早く起きる会社をやめる**」——行事の朝の手動増員(手動27回・休出9回)とS5の推論ピーク(平常の20倍)を、波の設計で解く。青柳がスケーリング設計の主担当に立ち、美咲は任せる側へ。矢吹の港のコンテナ比喩(神戸)がコンテナ編を導く。S6-03の「クラウドを外へ持ち出す棚」でS10への種(Snowball Edgeの防災訓練・滝本の名前を一度)を置く。

| 話 | タイトル(案) | 担当用語(数) |
|---|---|---|
| cp/01 | 先に起きる機械 | amazon_ec2, ec2_instance_families, ec2_burstable_instances, ec2_graviton, ec2_hibernation, launch_template, amazon_ec2_auto_scaling, auto_scaling_group, target_tracking_scaling_policy, step_scaling_policy, scheduled_scaling, auto_scaling_elb_health_check, auto_scaling_lifecycle_hook, ec2_placement_group_cluster, ec2_placement_group_partition, ec2_placement_group_spread (16) |
| cp/02 | 箱を運ぶ船団 | amazon_ecs, ecs_task_definition, ecs_service, ecs_capacity_provider, amazon_ecr, aws_fargate, amazon_eks, amazon_eks_anywhere, amazon_eks_distro, amazon_ecs_anywhere, aws_batch, aws_elastic_beanstalk (12) |
| cp/03 | 呼ばれてから動く | aws_lambda, lambda_event_source_mapping, lambda_dead_letter_queue, lambda_provisioned_concurrency, lambda_reserved_concurrency, lambda_vpc_access, aws_serverless_application_repository, aws_outposts, aws_wavelength, vmware_cloud_on_aws, snowball_edge_compute_optimized (11) |

### S6幕間

| 幕間 | 主題 | 配置 | エンタメの核 |
|---|---|---|---|
| ex01 金の型 | ゴールデンAMI / EC2 Image Builder | cp/01の直後 | 矢吹の鋳物の比喩「型が悪けりゃ、何百個鋳ても全部悪い」 |
| ex02 見送りの三百秒 | ELB登録解除の遅延+スケールインの作法 | cp/01の直後(ex01の後) | 減らす方の作法。豆の帳面の石段の見送りと響き合わせ |

## S7 ほどよい距離編の話単位割当(31語/2話+幕間2本)

**シーズンアーク「返事を待たない」**: 4年目2月〜3月。同期呼び出しの数珠つなぎをキューとイベントで切る。技術と並走する写し絵——「瀬名さんに聞かないと進まない」という**組織の同期呼び出し**を美咲が自覚する(結論はS8。ここでは自覚と「受け手を増やすしかない」の言語化まで)。疎結合=「相手の都合で受け取れるようにする気遣い」。幕間ex02「置き傘」はS8③への静かな前震(人物回)。

| 話 | タイトル(案) | 担当用語(数) |
|---|---|---|
| dc/01 | 返事を待たない手紙 | loose_coupling, amazon_sqs, sqs_standard_queue, sqs_fifo_queue, sqs_fifo_message_group_id, sqs_fifo_deduplication_id, sqs_visibility_timeout, sqs_dead_letter_queue, sqs_delay_queue, sqs_long_polling, sqs_message_retention, amazon_sns, sns_fanout_pattern, sns_fifo_topic, sns_subscription_filter_policy (15) |
| dc/02 | 起きたことから始める | event_driven_architecture, amazon_eventbridge, eventbridge_event_bus, eventbridge_rule, eventbridge_scheduler, eventbridge_archive_replay, s3_event_notification, dynamodb_streams, aws_step_functions, step_functions_state_machine, step_functions_standard_workflow, step_functions_express_workflow, step_functions_retry_catch, amazon_mq, amazon_appflow, aws_appsync (16) |

### S7幕間

| 幕間 | 主題 | 配置 | エンタメの核 |
|---|---|---|---|
| ex01 二度届く手紙 | 冪等性(at-least-onceと重複処理) | dc/01の直後 | 矢吹の宅配の判子。「配達が悪いんやない。台帳のない家が悪いんや」 |
| ex02 置き傘 | (人物回・技術新出なし)瀬名の置き傘 | dc/02の直後 | 事情は一切説明しない。守屋の「濡れて帰った日が一度あった、いうだけ」 |

## S8 誰がいなくても編の話単位割当(39語/3話+幕間2本)

**シーズンアーク「誰がいなくても」**: 4年目4月〜6月。①観測(青柳の「検知」の完成前半・狼少年アラームの失敗フック)②IaC(「図面から建て直せるか」・ドリフトの失敗フック・私学連合会の移行道具箱)③**「瀬名がいない日」本番回**——瀬名の急な長期不在(事情は説明しない)+社内IdP障害+本番劣化の三重奏。守屋の全伏線回収(紙のBCP・金庫の封筒=break-glass開封)。美咲がインシデントコマンダーとして立ち、瀬名の判断要請0件で収束。青柳の「検知して止めて戻せる」完成宣言(Config)。**瀬名の去就(提案・プロットレビューで確定)**: 退職せず東京拠点へ異動し非常勤の相談役へ。SAの席は美咲が継ぐ。「最後の赤丸が、今日消えた」(net/01からの最終回収)。

| 話 | タイトル(案) | 担当用語(数) |
|---|---|---|
| gv/01 | 先に鳴る鈴 | amazon_cloudwatch, cloudwatch_metric, cloudwatch_alarm, cloudwatch_logs, cloudwatch_logs_insights, aws_x_ray, amazon_managed_grafana, amazon_managed_service_for_prometheus, aws_health_dashboard, aws_compute_optimizer, aws_auto_scaling, aws_cli, aws_management_console (13) |
| gv/02 | もう一度、同じ家を建てる | aws_cloudformation, cloudformation_stack, cloudformation_change_set, cloudformation_stackset, aws_organizations, aws_control_tower, aws_service_catalog, aws_license_manager, aws_application_migration_service, aws_dms, aws_datasync, aws_transfer_family, aws_snow_family (13) |
| gv/03 | 瀬名がいない日 | aws_systems_manager, systems_manager_session_manager, systems_manager_patch_manager, aws_config, config_rule, aws_cloudtrail, cloudtrail_management_data_events, cloudtrail_organization_trail, aws_trusted_advisor, trusted_advisor_checks, aws_well_architected_tool, well_architected_framework, well_architected_pillars (13) |

### S8幕間

| 幕間 | 主題 | 配置 | エンタメの核 |
|---|---|---|---|
| ex01 合成の客 | CloudWatch Synthetics(カナリア外形監視) | gv/01の直後 | 「本物の客を最初の検知器にしない」。カナリアの命名を風間が却下 |
| ex02 呼び出しの順番 | SSM Incident Manager(エスカレーション・オンコール) | gv/02の直後(③の前振り) | 守屋の紙に既にエスカレーションが実装されていた。紙と機械の二重化 |

## S9 説明できる請求書編の話単位割当(30語/2話+幕間2本)

**シーズンアーク「説明できる請求書」**: 4年目7月〜8月。城戸メイン。①購入オプション——「サイズを直してから約束する」「約束は、読める未来にだけする」。城戸の前職の失敗談(初の過去語り)。②転送コストの地図と説明の道具箱——締めに**安全予算の言語化**(S2「安全は売上を生まない工事」の回収。「復旧能力という商品の原価」として経営会議へ)。cost_optimization家族33語のうち3語(s3_lifecycle_transition_cost, s3_minimum_storage_duration, s3_retrieval_fee)はS1-01担当済みのため、本シーズンは残り30語。

| 話 | タイトル(案) | 担当用語(数) |
|---|---|---|
| ct/01 | 約束で買う | ec2_on_demand_instances, reserved_instances, standard_reserved_instances, convertible_reserved_instances, reserved_instance_utilization_coverage, savings_plans, compute_savings_plans, ec2_instance_savings_plans, savings_plans_utilization_coverage, spot_instances, ec2_spot_interruption, fargate_spot, ec2_capacity_reservation, ec2_dedicated_host, compute_optimizer_recommendation (15) |
| ct/02 | 運賃の地図 | aws_cost_explorer, aws_cost_and_usage_report, aws_budgets, budgets_actions, cost_allocation_tags, organizations_consolidated_billing, data_transfer_cost, data_transfer_cross_az, data_transfer_inter_region, cloudfront_price_class, cloudfront_data_transfer_savings, s3_requester_pays, nat_gateway_data_processing_cost, vpc_endpoint_cost_optimization, intelligent_tiering_monitoring_fee (15) |

### S9幕間

| 幕間 | 主題 | 配置 | エンタメの核 |
|---|---|---|---|
| ex01 レンズの向き | S3 Storage Lens(倉庫の航空写真) | ct/01の直後 | 矢吹×城戸。「紺屋の白袴」。係やのうて癖にする(巡回の思想) |
| ex02 跳ねる前の震え | Cost Anomaly Detection(コスト異常検知) | ct/02の直後(S9エピローグ) | 17か月の悔いへの4年越しの返歌。「私より14か月早い。ええ弟子です」 |

## S10 完結編・劇場版(6語+総集/前後編2話+幕間1本)

**「波の高さを知る日」(前編)/「電気が戻った日」(後編)**: 4年目9月〜10月。**富士山噴火の降灰**が首都圏の電力・通信を段階的に麻痺させ、東京リージョンが使えなくなる——**4年間「東京が使えない日」のために組んできた矢印の、本番**。シリーズ最終テーゼ: 南海トラフに備えてきた会社に、別の山が来る——「訓練は全部、地震の顔をしとった」「備えは災害の名前やのうて、能力に付く」。各編7,000〜9,000字の劇場版。

- **前編(stateless_workload, stateful_workload, api_gateway_throttling_usage_plan)**: 噴火警戒レベル引き上げ〜噴火〜降灰拡大の猶予に、状態の台帳の読み合わせ・優先枠の数字化(「どれを最後まで止めないか」=狩野の完成)・人と燃料の備え(守屋・城戸)を配る。首都圏の海が静かになっていき、瀬名が不通になり、幕は**繋がらない番号を3秒聞いてから、美咲が東京リージョンを切る**決断で落ちる(ミッドポイント)。
- **後編(auto_scaling, horizontal_scaling, vertical_scaling)**: 三つの波——①大阪単独運転(水平/垂直/Auto Scaling総集の実戦)②**電気が戻った日の波**(滝本の予言の本番: 停電圏の一斉アップロードを優先枠とスケーリングで受け切る——社是の本番)③戻しの波(フェイルバック——矢吹「切るより戻す方が難しい」「どの単位で戻すんや」の最終回収。歓声なし、「戻せたな」の一言)。瀬名は安否不明のまま数日——**判断は頼らず、案じることはやめない**(人間SPOFの最終回答)。消息は短い一行で(事情は最後まで説明しない)。
- **災害の作法(厳守)**: 地震・津波は起こさない。火砕流等の人的被害圏は「避難完了の事実」一言で処理し**死者を出さない**。降灰被害は内閣府2020年想定の温度(停電=降雨時拡大、通信=非常電源枯渇と燃料補給困難、交通麻痺)。AWSの内部事情・AZ物理位置は発明せず、**公式ステータス風の観測事実のみ**。瀬名の不通は輻輳・停電の一般事実まで。
- **構図「助けに来る人々」**: 歴代ゲストが自分の持ち場から一手だけ(滝本=受援経験者の予言と確認電話、戸倉=紙の台帳の読み合わせ+**"何か"のストレート**(後編・美咲にだけ・一度だけ)、狩野=優先度、守屋=安否の分担「案じるのは、二人でやりましょ」、城戸=燃料と電池の即決裁、風間=非常時権限、矢吹=戻しの紙)。誰も万能にしない・入退場丁寧を厳守。
- 美咲のアルバム最終回収(裏書き=祖母の字。「裏があるから、記録なんよ」)。新人一人が初登場(名前と問いの受け渡しのみ)——「それは、本当に戻せるんですか」を次の世代へ(円環の完成)。
- 幕間ex01「最後の頁」= シリーズエピローグ(人物回・何も起こさない。書かれたものたちの一周と、戸倉の葉書「台帳、全部読めた。もう来んでええ。……豆は送る」)。

## 続編構想(正典の種。本シリーズ完結後)

- **SAP編(続編)**: 美咲がSAP(ソリューションアーキテクト – プロフェッショナル)を目指す物語。起点はS10の学び——「切る判断はSAAで打てる。戻る日の段取りまで先に打つのが、あの人の級や」。瀬名(SAP保持・東京・非常勤)が遠くから問いを返す構図を復活させ、マルチアカウント戦略・移行・大規模設計などSAP試験範囲を担当する。
- **DEA編(スピンオフ)**: 真鍋一花がDEA(データエンジニア – アソシエイト)範囲を担当するスピンオフ。戸倉の帳面の系譜(帳面の会は継続中)と、S5で建てた川・湖・台帳の運用が舞台。青柳との掛け合いを軸に。
- いずれも本編の正典(人物・年表・資格設定)を引き継ぐ。着手判断は監修者。

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
| 赤丸にオーナーと期限がなかった(気づきを仕組みに載せる) | net/01(日付と持ち主の運用開始) | **gv/03**(Config常時記録+config ruleで「図面に還っていない変更」の自動検知——青柳の完成宣言) |
| 瀬名の置き傘(常備の鞄) | **dc/ex02**(人物回) | **gv/03**(月曜朝、鞄が席から消えている) |
| 「削った金は、消すな。移せ」 | an/ex02(Redshift Serverlessの浮き) | **ct/02**(安全予算の言語化——復旧能力という商品の原価) |
| タグ付け推論のピーク(行事日に平常の20倍) | an/03(S6への橋) | **cp/01〜03**(波の設計——ASG/コンテナ/Lambda三段) |
| Snowball Edgeの防災演習(現地処理の備え) | **cp/03** | **S10**(臨時情報下の備えの一部として再確認) |
| 組織の同期呼び出し(瀬名待ち4件・「受け手を増やすしかない」) | **dc/01〜02**(美咲の自覚) | **gv/03**(受け手が増えたチームが、判断要請0件で収束) |
| 瀬名の去就: 東京拠点へ異動・非常勤の相談役(提案) | gv/03プロット | **プロットレビューで確定**。以後の再登場はS10のリモート一言まで |
| 新人(名前のみ・継承の受け皿) | **S10で初登場** | S10後編の最終場面で美咲が第一の問いを渡す(円環)。掘り下げない |
| 滝本「電気が戻った日に、一斉に上げるがです」 | storage/06(初出)→S10前編(受援経験者の予言として再掲) | **S10後編**(予言の本番——タイトル回収) |
| 瀬名の不通(繋がらない番号) | **S10前編**(切替決断の直前) | **S10後編**(短い一行の消息。事情は最後まで説明しない。「案じるのは二人で」=守屋との分担) |
| 矢吹「切るより、戻す方が難しいんや」(戻しの紙) | **S10前編** | **S10後編**(フェイルバックの単位と順序。「戻せたな」の一言) |
| 青柳「検知して止めて戻せる仕組み」 | storage/05 | net/01で芽(監視自動化)→S8①② |
| 城戸「請求書で説明できますか」 | storage/01 | net/02(NAT処理料金)→S9 |
| 真鍋一花(東雲の若手、矢吹の元部下) | **net/02で初登場(カメオ)** | S4〜S5でメイン |
| 滝本早苗(高知の自治体防災担当) | **storage/06で初登場** | net/03、S10 |
| CloudFrontオリジンフェイルオーバー実発動 | S1 DR編(訓練) | **storage/06**(本番) |
| 東雲の素材管理DBは急ぎのリフト&シフト(設計は未見直し) | S1-03〜04の裏側(db/03で明示) | **db/03**(設計負債の顕在化)→db/04(間取りから建て直す) |
| 戸倉の帳面「器を替える日は、間取りを疑う日」・設計レビューの型 | **db/03** | db/04(GA前の最終関門)→**S5**(分析のスキーマ設計で真鍋が型を運用) |
| 戸倉「器の話でほんまに詰まったときだけは、来い」(ここぞ登場の下地) | **db/ex03** | S5で一度(帳面レビューか葉書)、**S10**で一言(全キャラ集結)。万能化しない——出るたびに入退場を丁寧に |
| 閉店後の「帳面の会」(真鍋×戸倉の隠れた師弟。戸倉の隠れAWS勉強) | **db/ex03**(芽)以後は匂わせのみ | S5以降の要所で一言・葉書で継続。帳面の隅の横文字メモは気づいても指摘しない |
| 戸倉が「教える人」になった"何か"(若い頃は教える人ではなかった) | **db/ex03**で匂わせ一箇所のみ | **S5でジャブ→S10でストレート**。S5-02の帳面の会で輪郭だけ(戸倉が自分から半歩漏らすが言い切らない。真鍋も聞き返さない)。S10=本回収。**中身は確定済み(監修者承認)**: 「引けない帳面の悔い」——DC閉鎖を前に、29冊の帳面が自分にしか引けない記録だと悟った。「引けん記録は、無いのと同じ」が自分自身に跳ね返った日から、読める人を残すことが彼の仕事になった。S10で助けに来る理由=記録の会社の危機に「読める人を残しに来る」 |

## ストレージ編(既刊)Updateプラン

※出版前のためUpdate可。ただし**本文修正は今は実施しない**。実施時期は次の改稿バッチ(S2執筆前を推奨)。

1. **用語コラム形式のロールアウト**: storage/02〜05とresilience_and_dr/01の用語表を、storage/01と同じコラム形式(太字一行決め手+2〜4文)へ統一する。
2. **読書順ナビ**: READMEの目次をシーズン制に再編し、各編末尾に「次の話: 〜」リンクを追加。resilience_and_dr/01の「(完結)」表記を「シーズン1 第7話の前日譚」的位置付けに改める(storage/06がS1の最終話になるため)。
3. **接続線の微修正(数行)**: storage/05の風間初出にnet/06(WAF回)への含みを一行。storage/02のAWS Backup節にstorage/06で効く「復元訓練」への含みを一行。
4. **表記統一**: 既刊の「編」番号をシーズン表記(S1-01〜S1-07)に揃える(ファイル名は変更せずfront matterと冒頭表記のみ)。
5. 技術内容・用語割当・クイズは変更しない(コラム化は形式変換のみ)。

## 制作ワークフロー(確認)

プロット(本ファイル+個別プロット)→ Opus執筆 → 監督レビュー(物語+技術の二段階、writing-guide準拠)→ 修正ループ → コラム・カバレッジ機械検証 → PR。
