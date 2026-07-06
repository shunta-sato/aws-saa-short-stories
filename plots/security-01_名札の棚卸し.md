# プロット: security/01 名札の棚卸し

| 項目 | 値 |
|---|---|
| 状態 | ready |
| family / episode | security_identity_and_access / 1(S3第1話) |
| terms | iam, iam_user, iam_group, iam_role, iam_policy, iam_identity_policy, iam_root_user, iam_access_key, multi_factor_authentication_mfa, sts_assume_role, iam_trust_policy, iam_policy_evaluation_logic, iam_explicit_deny, shared_responsibility_model(14語) |
| 時系列 | 2年目秋。S2-06の直後、風間の「私の番」開始 |
| 分量 | 5,000〜6,000字 |

## シーズンアーク「静かな侵入者」

S3は5話貫通の潜入戦。**各話の冒頭に、タイムスタンプ付きの無機質なログ断片を1行だけ置く**(誰の視点でもない、結果だけの記録。手口は描かない)。侵入者は最後まで捕まらない(現実路線)。読者の緊張は「もう中にいるのでは」で維持する。

## ねらい

風間主導の全権限棚卸しでIAMの文法を体系化する開幕回。「名札(誰か)と鍵束(何ができるか)」の比喩を確立。アークの種(不審なサインイン試行)を末尾に置く。

## ビート

1. **冒頭ログ断片**: 深夜、存在しないユーザー名での連続サインイン失敗の記録(結果のみ1行)。
2. **起**: 風間の着任第一声「名札の台帳を見せてください」→台帳がない。iam_userの乱立、共有されたaws_access_key、退職者のキーが生きている疑い。コミットに長期キーが混入しかけるヒヤリ(検知はpre-commitフック。実害なし)。
3. **承(名札の文法)**: iamの原則を風間が板書——「認証(名札)と認可(鍵束)」。iam_user=人の名札(最小限に)、iam_group=名札の束、iam_policy/iam_identity_policy=鍵束の中身(JSON)。iam_root_userは金庫の奥へ(MFA+日常使用禁止)。multi_factor_authentication_mfa全員必須化。shared_responsibility_model——「AWSは金庫を守る。金庫の鍵の配り方はうち」を城戸の保険の比喩で。
4. **転1(人に鍵を持たせない)**: 長期キーの根絶方針。EC2やアプリはiam_role+sts_assume_role(一時的な名札の借用)。iam_trust_policy=「誰がこのロールを被れるか」の貸出条件。「鍵を配る設計から、名札を貸す設計へ」。
5. **転2(評価の文法)**: 権限が「あるはずなのに使えない」小事件→iam_policy_evaluation_logic(明示的Deny>Allow>暗黙のDeny)とiam_explicit_denyを現物で学ぶ。美咲が自力で評価順を辿る。
6. **結**: 棚卸し完了、退職者キー3件無効化。風間がCloudTrailの記録を眺めて一言「——このサインイン試行、ずっと続いてますね。名前を、試している」。狩野に月次報告の新形式(名札の台帳)を約束。静かに閉じる。

## 対比(棄却理由込み)

- IAMユーザー+長期キー(棄却方向)vs ロール+STS(推奨)
- ルートユーザーの日常使用の禁止
- 明示的Deny/Allow/暗黙のDenyの評価順

## 書いてはいけないこと

- 攻撃手口の再現手順。Organizations/SCP(②)、GuardDuty等(⑤)の先取り。
