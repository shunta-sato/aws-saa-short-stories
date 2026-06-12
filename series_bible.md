# SAA-C03 短編小説集 シリーズバイブル

## コンセプト

SAA-C03の用語集(441語)を、連作お仕事小説として「文脈と意思決定」で覚える。各編は約5,000字、1つのtaxonomy_familyの用語群をカバーし、物語の山場は必ず「技術選定の分岐」に置く。全編読了で全用語に文脈が付くことを目指す。

## 世界観・登場人物(連作で固定)

- **フォトリム社**: 写真・動画共有サービスの中堅企業。ユーザー数は成長中で、機能追加・買収・コンプライアンス対応が次々に発生する。
- **瀬名美咲(せな・みさき)**: 主人公。インフラエンジニア。優秀だが経験が浅く、失敗から学ぶ。一人称視点ではなく三人称。
- **堂島(どうじま)**: 先輩エンジニア。要点を突く助言役。「数字を見ろ」「要件語を読め」が口癖。説教臭くしすぎない。
- 各編で必要に応じてゲスト(経理部、法務部、買収先のエンジニア等)を出してよい。

## 文体・構成ルール

1. 三人称・お仕事小説風。現実的なトラブル(請求書、苦情、監査、障害)から始める。
2. 山場は技術選定の分岐。「なぜそれを選び、なぜ他を捨てたか」を会話と思考で描く。競合サービスとの差分(棄却理由)を必ず台詞か地の文に入れる。
3. 試験で問われる具体値(日数、上限、時間)は物語に自然に埋め込む。
4. 1編につき最低1つ「失敗または手痛い学び」を入れる(記憶のフック)。
5. 末尾に必ず以下を付ける:
   - 「## この章の登場用語と決め手」: term_id と物語での決め手の表
   - 「## 確認クイズ」: 3問(答え付き)
6. 本文は4,500〜6,000字。用語の羅列にしない。割当用語はすべて本文に登場させ、用語表に載せる。
7. ファイル名: `NN_<family>_<タイトル>.md`。冒頭に題名とfamily表記。

## 既刊と用語割当

| 編 | family | タイトル | 割当用語 |
|---|---|---|---|
| 01 | storage_architecture (1/5) | 請求書は嘘をつかない | s3_standard, s3_standard_ia, s3_one_zone_ia, s3_lifecycle_policy, s3_minimum_storage_duration, s3_retrieval_fee, s3_intelligent_tiering, s3_glacier_deep_archive, s3_glacier_retrieval_options, s3_lifecycle_transition_cost, s3_multipart_upload, transfer_acceleration, ebs_gp3, ebs_multi_attach, amazon_efs, efs_lifecycle_management |
| 02 | storage_architecture (2/5) | ブロックの行方(EBS編) | amazon_ebs, ebs_gp2, ebs_io1, ebs_io2, ebs_provisioned_iops, ebs_st1, ebs_sc1, ebs_snapshot, ebs_snapshot_incremental, ebs_fast_snapshot_restore, instance_store, aws_backup |
| 03 | storage_architecture (3/5) | 引っ越しと四つのFSx(ファイルストレージ編) | efs_standard, efs_infrequent_access, efs_one_zone, efs_performance_mode, efs_throughput_modes, amazon_fsx_for_all_types, fsx_windows_file_server, fsx_lustre, fsx_netapp_ontap, fsx_openzfs |
| 04 | storage_architecture (4/5) | データセンターを畳む日(ハイブリッド編) | aws_storage_gateway, storage_gateway_file_gateway, storage_gateway_volume_gateway_cached, storage_gateway_volume_gateway_stored, storage_gateway_tape_gateway, snowball_edge_storage_optimized, snowcone |
| 05 | storage_architecture (5/5) | 消せないデータ、消えないデータ(S3保護編) | amazon_s3, storage_class, amazon_s3_glacier, s3_versioning, s3_object_lock, s3_object_lock_compliance_mode, s3_object_lock_governance_mode, s3_legal_hold, s3_mfa_delete, s3_same_region_replication, s3_cross_region_replication, s3_replication_time_control, s3_select, s3_byte_range_fetch, s3_glacier_instant_retrieval, s3_glacier_flexible_retrieval |
| 06 | resilience_and_dr (完結) | 金曜日のゲームデー(DR編) | rpo, rto, high_availability, fault_tolerance, single_point_of_failure, multi_az, backup_restore, pilot_light, warm_standby, active_passive_failover, active_active_failover, multi_region_architecture, cloudfront_origin_failover |

## 連作の継続設定(これまでの出来事)

- 01: ストレージコスト爆発→ライフサイクル設計で解決。Deep Archive誤投入事件(12時間待ち)。動画機能開始、編集チームはEFS+gp3。
- 02以降で使える伏線: 動画機能のDB負荷、買収話(オンプレ企業「東雲アーカイブズ社」)、コンプライアンス強化、リージョン障害訓練(ゲームデー)。

## 今後の計画(未着手family)

networking_and_application_security(75語、推定5編)、security_identity_and_access(67語、推定4編)、database_architecture(41語、3編)、compute_and_containers(39語、3編)、data_ingestion_and_analytics(39語、3編)、management_governance_and_observability(39語、3編)、cost_optimization(33語、2編)、decoupling_and_integration(31語、2編)、performance_and_scaling(7語、1編)。
