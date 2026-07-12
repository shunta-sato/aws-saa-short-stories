# 技術レビュー: stories/security_identity_and_access/04_一晩の鍵交換

本文・用語コラム・クイズ中の技術的主張をAWS公式ドキュメントと照合した結果。判定は ✅(正確)/⚠️(注意付きで正確)/❌(要修正)。

レビュー実施日: 2026-07-12。照合先は各行の出典(AWS公式ドキュメント)。

| # | 本文中の主張 | 出典 | 判定 |
|---|---|---|---|
| 1 | Secrets ManagerはDB認証情報等を保管し、Lambda関数で自動ローテーションできる。RDS等にはマネージドなローテーション関数が提供される | Secrets Manager User Guide: rotating-secrets / rotate-secrets_managed | ✅ |
| 2 | Secrets Managerはシークレット1件ごとに月額課金($0.40/件/月+APIコール課金) | Secrets Manager Pricing | ✅ |
| 3 | ローテーション間隔は30日ごと等に設定できる | Secrets Manager User Guide: rotating-secrets(スケジュール設定) | ✅ |
| 4 | Parameter Storeは階層パスで設定値を保存し、標準パラメータは追加料金なし | Systems Manager Pricing / Parameter Store User Guide | ✅ |
| 5 | SecureStringはKMSで暗号化されるパラメータタイプ。自動ローテーション機能はない | Parameter Store User Guide: securestring-parameters | ✅ |
| 6 | 使い分けは「自動ローテーションが要るならSecrets Manager、置くだけならParameter Store」 | 両サービスのUser Guide比較(SAA定番の判断基準) | ✅ |
| 7 | Block Public Accessはバケットポリシー/ACLの公開設定を上書きする安全装置で、アカウント単位・バケット単位で適用できる | S3 User Guide: access-control-block-public-access | ✅ |
| 8 | S3 ACLはレガシーであり、現在は無効化(bucket owner enforced)が推奨 | S3 User Guide: about-object-ownership(「大部分のユースケースでACLは不要」) | ✅ |
| 9 | Object Ownership: bucket owner enforcedはACLを無効化し、アップロード者に関わらず所有者をバケット所有者に統一。新規バケットの既定 | S3 User Guide: about-object-ownership(2023年4月以降の新規バケット既定) | ✅ |
| 10 | 署名付きURLは署名者の認証情報で有効な期限付きURL。SigV4での有効期限は最大7日。署名に使った認証情報が失効すればURLも失効 | S3 User Guide: using-presigned-url(ShouldIUsePresignedURLs) | ✅ |
| 11 | S3署名付きURL(倉庫の窓口の一時許可)とCloudFront署名付きURL(配信網の層)の使い分け | S3 User Guide / CloudFront Developer Guide: private-content | ✅ |
| 12 | S3アクセスポイントは1バケットに用途別の名前付き入り口を複数作り、専用ポリシーとVPC限定を持たせられる | S3 User Guide: access-points | ✅ |
| 13 | EFSアクセスポイントは入り口ごとにルートディレクトリとPOSIXユーザー/グループを強制する | EFS User Guide: efs-access-points | ✅ |
| 14 | VPCエンドポイントポリシーはエンドポイント経由で可能な操作・宛先(特定バケットのみ等)を制限する。SG/NACLでは宛先バケット単位の制御は書けない | VPC User Guide: vpc-endpoints-access | ✅ |
| 15 | バケットポリシーでTLSでない通信を拒否できる(aws:SecureTransport条件) | S3 User Guide: security best practices(HTTPS強制) | ✅ |
| 16 | Cognitoユーザープール=サインアップ/サインイン/トークン発行、アイデンティティプール=AWS一時資格情報への引き換え | Cognito Developer Guide: what-is-amazon-cognito | ✅ |
| 17 | ALBのリスナールールのauthenticateアクションでCognito/OIDC IdPと連携し、バックエンド到達前に認証を完了できる(アプリ改修不要) | ELB User Guide: listener-authenticate-users | ✅ |
| 18 | API GatewayのオーソライザーはCognitoユーザープール、Lambdaオーソライザー、IAM認可(SigV4)の3方式 | API Gateway Developer Guide: apigateway-control-access | ✅ |
| 19 | 従業員のSSOはIAM Identity Center、アプリ利用者の認証はCognito、という分岐 | 両サービスのUser Guide(SAA定番の判断基準) | ✅ |
| 20 | クイズ2: クロスアカウントアップロードの所有者問題はbucket owner enforcedで恒久解決 | S3 User Guide: about-object-ownership | ✅ |

## 結論

❌(要修正)は0件、⚠️も0件。

## 物語レビュー(universe整合)の記録

- 冒頭ログ断片あり(fork記録のみ。悪用手口は描かない)。侵入者は特定されないまま(シーズンアーク準拠)。GuardDuty等の検知系はsec/05へ持ち越し(先取りなし)
- 時系列: 立春(2月上旬)。S3-03(1月中旬〜下旬)の直後。fork記録02-02→発見02-04頃→当夜作戦→翌週総点検→金曜報告
- 伏線整合: 9月の足跡(S3-02)と脅迫メール(S3-03)の説明が「コード内のハードコード鍵」で繋がる(確定はさせない)。真鍋の神戸合流打診=S4への橋(本格合流はS4、プロット指定どおり打診まで)。「従業員はIdentity Center、利用者は別」(S3-02)の宿題をCognitoで回収。net/02のゲートウェイエンドポイント、S1-03のEFS、面接日の公開バケット指摘(S1-01)を記憶として接続
- 方言: 美咲の関西語彙は緊急時の1箇所(「切るんは待って。出所見てからや」)。矢吹は関西弁、真鍋は柔らかい関西、瀬名は標準語1発言(「戻す手順は?」)で前に出ない
- 山場=技術選定の分岐: Secrets Manager vs Parameter Store、バケットポリシー vs ACL、presigned URL vs CloudFront署名、Cognito/ALB認証/オーソライザーの層。失敗・冷や汗: 午前2時14分の旧キー呼び出し(正規の消し忘れ=東雲の残バッチ)
- 成長ビート: 美咲(取り上げず数字で確かめる指揮)、青柳(検知から報告まで11秒)、狩野(止める人→起きて待つ人)、矢吹×真鍋(継承)
