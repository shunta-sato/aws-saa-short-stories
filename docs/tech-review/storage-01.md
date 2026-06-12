# 技術レビュー: stories/storage/01_請求書は嘘をつかない

Issue #7 対応。本文・用語コラム・クイズ中の技術的主張をAWS公式ドキュメントと照合した結果。判定は ✅(正確)/⚠️(注意付きで正確)/❌(要修正)。

レビュー実施日: 2026-06-12。照合先は各行の出典(AWS公式ドキュメント)。

| # | 本文中の主張 | 出典 | 判定 |
|---|---|---|---|
| 1 | Standard-IAは「低頻度アクセス・即時取得・複数AZ」の3条件で選ぶ | S3 User Guide: storage-class-intro | ✅ |
| 2 | Standard-IA/One Zone-IAの最小ストレージ期間は30日。期間前削除で残り日数分課金 | storage-class-intro(Comparing the Amazon S3 storage classes) | ✅ |
| 3 | One Zone-IAはStandard-IA比で約2割安 | S3料金ページ(約20%安) | ✅ |
| 4 | IA系はGB単位の取り出し料金がある。Intelligent-Tieringのアクセス階層間には取り出し料金がない | storage-class-intro / intelligent-tiering | ✅ |
| 5 | Intelligent-Tieringはオブジェクト単位の監視料金があり、128KB未満は監視・自動階層化の対象外 | intelligent-tiering | ✅ |
| 6 | Deep Archiveは標準取り出し12時間・バルク48時間で、Expedited(迅速)は存在しない | restoring-objects-retrieval-options(対応表でDeep ArchiveのExpeditedは「Not available」) | ✅ |
| 7 | Glacier Flexible Retrievalの迅速取り出しは1〜5分 | restoring-objects-retrieval-options | ⚠️ 250MB未満のオブジェクトで典型1〜5分。大きなオブジェクトはスループット依存。学習用の簡略化として許容 |
| 8 | Deep Archiveの最小ストレージ期間は180日 | storage-class-intro | ✅ |
| 9 | PutObjectは5GBまで。それ以上はマルチパートアップロード必須。100MB超で推奨 | mpuoverview | ✅ |
| 10 | 未完了マルチパートのパートは課金され続け、ライフサイクルで自動中断・削除できる | mpu-abort-incomplete-mpu-lifecycle-config | ✅ |
| 11 | Glacier系へ移行すると1オブジェクトあたり約40KBの追加メタデータ(8KBはS3 Standard料金、32KBはGlacier料金) | lifecycle-transition-general-considerations | ✅ |
| 12 | 小オブジェクトはライフサイクルのサイズフィルタで移行対象から除外できる(128KB未満は既定で移行されない) | lifecycle-transition-general-considerations(2024年9月の既定動作変更を含む) | ✅ |
| 13 | 移行はオブジェクトごとのリクエスト課金があり、小オブジェクト大量移行はコスト逆転しうる | 同上+S3料金ページ | ✅ |
| 14 | Transfer Accelerationはエッジロケーション経由でアップロード経路を最適化する | transfer-acceleration | ✅ |
| 15 | gp3はgp2より約2割安く、ベースライン3,000 IOPS、IOPS/スループットを容量と独立に設定可 | EBS User Guide: general-purpose | ✅ |
| 16 | EBS Multi-Attachはio1/io2限定・同一AZ限定・クラスタ対応FS前提 | ebs-volumes-multi | ✅ |
| 17 | EFSは複数AZ・複数インスタンスからNFSマウントできる共有ストレージ(SMB非対応) | EFS User Guide: how-it-works | ✅ |
| 18 | EFSライフサイクルは「最終アクセス」基準でIAへ移行し、削除はしない(S3は「作成日数」基準で削除も可能) | lifecycle-management-efs | ✅ |
| 19 | 7日で削除されるデータをIAに置くと、削除後も30日分課金され損 | 最小ストレージ期間(#2)からの帰結 | ✅ |

## 結論

❌(要修正)は0件。⚠️は#7の1件のみで、学習コンテンツとしての簡略化の範囲内と判断し本文は修正しない(コラムは「1〜5分」の典型値表記を維持)。

## 残課題(Issue #8 へ)

同形式のレビュー表を storage/02〜05、resilience_and_dr/01 についても作成する。
