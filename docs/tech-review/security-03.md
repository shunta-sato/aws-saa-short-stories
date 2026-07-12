# 技術レビュー: stories/security_identity_and_access/03_鍵の鍵

本文・用語コラム・クイズ中の技術的主張をAWS公式ドキュメントと照合した結果。判定は ✅(正確)/⚠️(注意付きで正確)/❌(要修正)。

レビュー実施日: 2026-07-12。照合先は各行の出典(AWS公式ドキュメント)。

| # | 本文中の主張 | 出典 | 判定 |
|---|---|---|---|
| 1 | エンベロープ暗号化: データはデータキーで暗号化し、データキーをKMSキーで暗号化して暗号文とともに保存する | KMS Developer Guide: concepts(Envelope encryption) | ✅ |
| 2 | KMSキー(対称)はKMSの外に平文で出ない。復号はKMSへの呼び出しで行う | KMS Developer Guide: overview / concepts | ✅ |
| 3 | データキーは平文と暗号化済みの対で払い出され(GenerateDataKey)、平文キーは使用後破棄する | KMS Developer Guide: concepts(Data keys) | ✅ |
| 4 | KMSが直接暗号化できるデータは4KBまで(コラム) | KMS API Reference: Encrypt(Plaintext最大4,096バイト) | ✅ |
| 5 | キーポリシーは鍵に付くリソースベースポリシー。クロスアカウントの利用にはキーポリシーとIAMポリシーの両方の許可が必要 | KMS Developer Guide: key-policies / key-policy-modifying-external-accounts | ✅ |
| 6 | AWSマネージドキー(aws/s3等)はキーポリシー変更不可・クロスアカウント利用不可・ローテーション年1回固定 | KMS Developer Guide: concepts(AWS managed keys)/ rotate-keys | ✅ |
| 7 | カスタマーマネージドキーの自動ローテーションは有効化すると年1回(既定365日)。キーIDは変わらず、旧素材は保持され、既存データの再暗号化は不要 | KMS Developer Guide: rotate-keys / rotating-keys-enable | ⚠️ 既定365日。ローテーション期間は90〜2560日で変更可能だが、本文は「年1回で設定する」という運用宣言なので正確 |
| 8 | グラントはキーポリシーを変更せずに鍵の使用権限を一時的・プログラム的に委任する仕組みで、AWSサービス統合が利用する | KMS Developer Guide: grants | ✅ |
| 9 | マルチリージョンキーは同じキーID・同じ鍵素材のレプリカを別リージョンに複製でき、リージョンを跨いで再暗号化なしに復号できる | KMS Developer Guide: multi-region-keys-overview | ✅ |
| 10 | 通常のKMSキーはリージョンの外では使えない | KMS Developer Guide: multi-region-keys-overview(Regional isolation) | ✅ |
| 11 | KMSキーの削除には7〜30日の待機期間がある(コラム) | KMS Developer Guide: deleting-keys | ✅ |
| 12 | CloudHSMはFIPS 140-2レベル3の専有HSM。規制要件で選び、可用性設計・運用は利用者側の責任 | CloudHSM User Guide: introduction | ⚠️ hsm1系はFIPS 140-2 L3。新世代hsm2m.mediumはFIPS 140-3 L3。SAA-C03の出題水準では140-2 L3の表記が標準的なため維持 |
| 13 | S3は現在、新規オブジェクトを既定で暗号化(SSE-S3)する。ただし既定暗号化の設定は過去のオブジェクトに遡及しない | S3 User Guide: default-encryption-faq(2023年1月以降の自動暗号化、既存オブジェクトは対象外) | ✅ |
| 14 | 平文の既存オブジェクトはS3インベントリで特定し、バッチオペレーションのコピーで暗号化して置き直せる | S3 User Guide: batch-ops-copy-object / storage-inventory | ✅ |
| 15 | SSE-S3は追加設定・追加料金なし。鍵の選択・キーポリシー統制・鍵単位の利用監査は不可 | S3 User Guide: UsingServerSideEncryption | ✅ |
| 16 | SSE-KMSはCloudTrailに鍵利用が記録され、キーポリシーでアクセス統制できる | S3 User Guide: UsingKMSEncryption | ✅ |
| 17 | S3バケットキーでKMSへのリクエストコストを最大99%削減できる。暗号化の強度は変わらない | S3 User Guide: bucket-key | ✅ |
| 18 | SSE-Cは顧客がリクエストごとに鍵を提供し、AWSは鍵を保存しない。鍵を失うとデータは復号不能 | S3 User Guide: ServerSideEncryptionCustomerKeys | ✅ |
| 19 | EBS: リージョン単位で「デフォルト暗号化」を有効化できる。既存の未暗号化ボリュームは直接暗号化できず、スナップショット→暗号化コピー→ボリューム再作成で対応 | EBS User Guide: EBSEncryption(encryption by default / encrypt unencrypted resources) | ✅ |
| 20 | 暗号化ボリュームのスナップショットおよびそこから作成するボリュームは暗号化される(連鎖) | EBS User Guide: EBSEncryption(How EBS encryption works) | ✅ |
| 21 | ACM公開証明書は発行・更新無料で有効期間13か月(395日) | ACM User Guide: acm-certificate / acm-bestpractices | ✅ |
| 22 | DNS検証はCNAMEレコードを1本置けば所有確認と自動更新が継続する(期限60日前に自動更新)。メール検証は更新のたびに人の承認が必要 | ACM User Guide: dns-validation / dns-renewal-validation / email-validation | ✅ |
| 23 | クイズ1: クロスアカウント復号にはキーポリシー+IAMの両方。AWSマネージドキーでは不可 | #5, #6と同じ | ✅ |

## 結論

❌(要修正)は0件。⚠️は#7(ローテーション期間のカスタム可)と#12(CloudHSMのFIPS世代)の2件で、いずれも学習コンテンツとしての簡略化の範囲内と判断し本文は修正しない。

## 物語レビュー(universe整合)の記録

- 冒頭ログ断片あり(手口は描かない)。侵入者/差出人は特定されないまま終わる(シーズンアーク準拠)
- 方言濃度: 美咲の関西語彙は感情が動く場面の1箇所(SSE-C棄却)。瀬名は標準語1発言のみで前に出ない
- 伏線整合: 9月の足跡(S3-02)は未回収のまま参照。「又貸し」(ex02)、gp3移行(S1-02)、年1,400円のドメイン(S3-02)を記憶として接続
- 時系列: 神戸の松の内(1/15)明けの1月中旬。冒頭ログ01-17、脅迫期限7日、報告書は十日目——期限は報告書の3日前に経過(整合)
- 技術選定の分岐: SSE 3方式、AWSマネージド/カスタマーマネージドキー、KMS/CloudHSM、DNS/メール検証。失敗イベント: 既定暗号化を全量暗号化と読み違えた美咲の学び
