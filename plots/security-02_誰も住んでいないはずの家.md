# プロット: security/02 誰も住んでいないはずの家

| 項目 | 値 |
|---|---|
| 状態 | ready |
| family / episode | security_identity_and_access / 2 |
| terms | organizations_organizational_unit, service_control_policy, aws_iam_identity_center, iam_identity_center_permission_set, iam_cross_account_access, iam_permissions_boundary, iam_session_policy, iam_abac, resource_based_policy, aws_resource_access_manager_aws_ram, aws_directory_service(11語) |
| 時系列 | S3-01の数週間後 |
| 分量 | 5,000〜6,000字 |

## ねらい

東雲買収の遺産——管理外の旧AWSアカウント発見を機に、マルチアカウント統治(Organizations/SCP/Identity Center)を体系化。アークの第二段: その家に「誰かが住んでいた形跡」。

## ビート

1. **冒頭ログ断片**: 旧アカウントでの、久しく無かったAPI呼び出しの記録1行(3か月前の日付)。
2. **起**: 城戸の経費精査で、誰も知らないAWSの請求(月数千円)が見つかる——東雲時代の検証用アカウント。買収時の棚卸し漏れ。矢吹「……DCは畳んだが、家はもう一軒あったんか」。中を見ると、見知らぬロールと古いアクセスキー、そして3か月前のAPI呼び出しの形跡。誰かが、いた。
3. **承(家をまとめる)**: 野良アカウントの再発防止としてAWS Organizations導入。organizations_organizational_unit(本番/検証/サンドボックスのOU)、service_control_policy=「OUごとの、越えられない塀」(管理者でも塀の外へは出られない)。旧東雲アカウントは隔離OUへ収容し調査保全。
4. **転1(入り方を揃える)**: アカウントが増えると名札も増える→aws_iam_identity_center(旧SSO)で一つの名札から複数アカウントへ。iam_identity_center_permission_set=アカウント横断の鍵束の型。裏側の社内ディレクトリ連携でaws_directory_service(守屋の社内AD——ex04の名前の台帳の人がまた効く)。
5. **転2(貸し方の文法)**: クロスアカウントの整理。iam_cross_account_access(ロール貸与)、resource_based_policy(リソース側に書く許可——バケットポリシーは既知、の接続)、aws_resource_access_manager_aws_ram(サブネット等の共有)。委譲の暴走を防ぐ道具として iam_permissions_boundary(「渡す鍵束の上限枠」)とiam_session_policy(「今回だけの絞り込み」)。iam_abac=タグで鍵束を書く(プロジェクトが増えても鍵束が増えない)。
6. **結**: 旧アカウントの調査結果——住んでいた形跡はあるが、正体は掴めない。持ち出された形跡も「無いとは言い切れない」。風間「『無い』の証明は、記録が無ければできません。だから記録の話を、この季節の最後にやります」。狩野が脅迫や漏えいの初動手順(法務側)を用意し始める(③への橋)。

## 対比

- SCP(塀=上限)vs IAMポリシー(鍵束=許可)——SCPは許可を与えない
- Permissions Boundary(委譲の上限)vs SCP(アカウントの上限)
- アイデンティティベース vs リソースベースのポリシー

## 書いてはいけないこと

- KMS(③)、GuardDuty/Detective(⑤)の先取り。侵入者の正体の確定。
