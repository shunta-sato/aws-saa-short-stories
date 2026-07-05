# プロット: security/04 一晩の鍵交換

| 項目 | 値 |
|---|---|
| 状態 | ready |
| family / episode | security_identity_and_access / 4 |
| terms | s3_bucket_policy, s3_acl, s3_block_public_access, s3_object_ownership_bucket_owner_enforced, s3_presigned_url, s3_access_points, efs_access_points, vpc_endpoint_policy, amazon_cognito, alb_authentication_oidc_cognito, api_gateway_authorizers, aws_secrets_manager, secrets_manager_rotation, systems_manager_parameter_store, parameter_store_secure_string(15語) |
| 時系列 | S3-03の直後。冬 |
| 分量 | 5,500〜6,500字 |

## ねらい

シーズンの山場・カウントダウン回(エヴァ13話相当)。侵入の入口が判明——旧東雲コードにハードコードされたシークレット。攻撃者に使われる前に、一晩で全シークレットを交換する作戦。アクセス制御と秘密管理を実戦の道具として体系化。

## ビート

1. **冒頭ログ断片**: 公開コード共有サイト上の、あるリポジトリのフォーク記録1行。
2. **起**: 真鍋一花(移行コードの整理中)が発見——旧東雲のバッチコードに、DB接続文字列とアクセスキーがハードコード。しかもそのコードは、買収前に外部委託先へ渡った版が存在し、どこまで拡散したか追えない。S3-02の「住んでいた形跡」と辻褄が合う。**この鍵は、生きていて、外にある**。
3. **承(作戦立案)**: 全シークレットの棚卸しと一斉交換を、利用者影響なしの一晩でやる。美咲が指揮、瀬名は検算のみ。役割分担のホワイトボード(S1の週次総力戦の夜間版)。交換先の受け皿: aws_secrets_manager(DB系=secrets_manager_rotationで以後自動交換)、systems_manager_parameter_store+parameter_store_secure_string(設定値系=安価。使い分けは「自動ローテーションが要るか」)。
4. **転1(カウントダウン実行)**: 23時開始。真鍋がコード側の参照を書き換え、美咲が新旧キー並行期間を管理、青柳が旧キーの使用をログで監視——「旧キー、まだ呼ばれてます……東雲の残バッチでした」(正規の消し忘れと判明する冷や汗ビート)。午前3時、旧キー全滅を確認して無効化。**攻撃者が使う前に、鍵側を殺した**。
5. **転2(入り口の総点検)**: 再発防止の網。S3系——s3_block_public_access(アカウント全体で強制)、s3_bucket_policy vs s3_acl(ACLはレガシー)、s3_object_ownership_bucket_owner_enforced(ACL無効化=所有者強制)、s3_presigned_url(共有の正道。CloudFront署名との層の違い再掲)、s3_access_points(用途別の入り口分割)、efs_access_points(POSIX強制)、vpc_endpoint_policy(門にも鍵束——net/02の門と接続)。アプリの認証はamazon_cognito(ユーザープール=認証)+alb_authentication_oidc_cognito(ALBで認証を肩代わり)+api_gateway_authorizers(APIの門番)。
6. **結**: 夜明け。被害の証拠なし、ただし「使われる前だった」のか「使われた形跡を消された」のかは確定できない(現実路線の不気味さを一滴残す)。真鍋「数えてから流す、はデータだけの話じゃなかったですね。鍵も、数えてからでした」。矢吹が真鍋の合流を正式に打診される(S4への橋)。風間「残るは、検知です。次で、この季節を閉じます」。

## 対比

- Secrets Manager(自動ローテーション)vs Parameter Store(安価・設定値)
- バケットポリシー vs ACL(レガシー)+Object Ownership
- presigned URL vs CloudFront署名(層)
- Cognito/ALB認証/API GWオーソライザーの層の違い

## 書いてはいけないこと

- ハードコードされた鍵の悪用手順。GuardDuty/Detective(⑤)の先取り。真鍋の本格合流はS4(打診まで)。
