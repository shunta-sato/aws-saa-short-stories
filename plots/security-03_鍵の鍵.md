# プロット: security/03 鍵の鍵

| 項目 | 値 |
|---|---|
| 状態 | ready |
| family / episode | security_identity_and_access / 3 |
| terms | aws_kms, kms_key_policy, kms_aws_managed_key, kms_customer_managed_key, kms_data_key, kms_envelope_encryption, kms_grant, kms_key_rotation, kms_multi_region_key, aws_cloudhsm, aws_certificate_manager_acm, acm_dns_validation, ebs_volume_encryption, s3_sse_s3, s3_sse_kms, s3_sse_c(16語) |
| 時系列 | S3-02の直後。初冬 |
| 分量 | 5,500〜6,500字(担当語多のため上限緩和) |

## ねらい

「貴社のデータを保有している」という脅迫メール(実物かブラフか不明)を受け、「仮に持ち出されていたとして、読めるのか」を検証する緊迫の中で暗号化を体系化する。恐怖を煽る回ではなく、設計が恐怖を数えられる不安に変える回。

## ビート

1. **冒頭ログ断片**: 外部からの1通のメールの受信記録(件名のみ。「Re: your data」)。
2. **起**: 狩野宛に英語の脅迫メール。「顧客データを保有している。連絡されたくなければ——」。添付の「証拠」は数行のファイルリスト(本物とも作り物とも判別できない粒度)。狩野が初動手順どおり法務・警察相談と並行し、技術側への問いは一つ——「**仮に持ち出されていたとして、中身は読めるの?**」
3. **承(封筒の文法)**: aws_kmsを風間と美咲で体系化。kms_envelope_encryption=「データはデータキーで包み、データキーはKMSの鍵で包む」二重封筒。kms_data_key、kms_key_policy(鍵に付く、鍵専用の許可)、kms_aws_managed_key vs kms_customer_managed_key(統制・ローテーション・ポリシー自由度の差でCMKへ)。kms_key_rotation(自動年次)。kms_grant=「鍵の又貸しの一筆」(サービス統合用)。kms_multi_region_key=大阪DRの複製が同じ鍵で読める設計。aws_cloudhsm=専有HSMが要る規制要件のときの別解(棄却理由込み)。
4. **転1(全在庫の検分)**: S3の暗号化方式の棚卸し——s3_sse_s3(既定・お任せ)、s3_sse_kms(鍵の統制と監査が付く。学校・法人はこれへ)、s3_sse_c(自前鍵持込——運用重で棄却)。EBSはebs_volume_encryption(スナップショット連鎖の暗号化はS1-02の記憶と接続)。結論: 主要データは暗号化済み、一部の古い検証データが平文→即時暗号化。「読める可能性のある在庫」がゼロに近づいていく緊張の工程表。
5. **転2(通信の証明書)**: 併走してaws_certificate_manager_acm(発行・自動更新)、acm_dns_validation(DNS検証=Route 53と接続、メール検証との対比)。「運ぶ途中」と「置いてある間」の暗号化を一枚に。
6. **結**: 検分の結論——「持ち出しの証拠なし。仮に持ち出されていても、読める平文は存在しない」。狩野は要求を無視して当局対応へ(脅迫メールへの返信はしない)。以後、続報なし——ブラフだった公算が高いが、確定はしない(捕まらない現実路線)。城戸「読めん紙切れに、身代金は払えませんわな」。風間「恐怖は、在庫が数えられないから大きくなる。数えたら、ただの管理です」。

## 対比

- SSE-S3 / SSE-KMS / SSE-C(統制・監査・運用負担)
- AWSマネージド鍵 vs カスタマーマネージド鍵
- KMS vs CloudHSM(マネージド vs 専有、規制要件)
- DNS検証 vs メール検証(自動更新の可否)

## 書いてはいけないこと

- 脅迫者との交渉劇(返信しない。ドラマはうち側の検分に置く)。Macie等の検知(⑤)。
