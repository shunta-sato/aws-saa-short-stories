# 技術レビュー: stories/security_identity_and_access/05_検知して止まって戻せる

本文・用語コラム・クイズ中の技術的主張をAWS公式ドキュメントと照合した結果。判定は ✅(正確)/⚠️(注意付きで正確)/❌(要修正)。

レビュー実施日: 2026-07-13。照合先は各行の出典(AWS公式ドキュメント)。

| # | 本文中の主張 | 出典 | 判定 |
|---|---|---|---|
| 1 | GuardDutyはCloudTrail(操作記録)・VPCフローログ(通信記録)・DNSログを分析するマネージド脅威検知 | GuardDuty User Guide: what-is-guardduty(基盤データソース3種) | ✅ |
| 2 | GuardDutyはエージェント不要(「サーバーには何も入れない」)で、記録の側を機械学習で読む | GuardDuty User Guide / FAQs(ログ・検出結果を直接取得、ワークロード性能への影響なし) | ✅ |
| 3 | GuardDutyは検知サービスであり、通信の遮断は主機能ではない(遮断は別の道具) | GuardDuty User Guide(検出結果の生成。自動対応はEventBridge等との組み合わせ) | ✅ |
| 4 | DetectiveはGuardDutyの検出・CloudTrail・VPCフローログを自動で束ね、エンティティ単位の時系列グラフで調査を支援する | Detective FAQs「extracts time-based events … from AWS CloudTrail, Amazon VPC Flow Logs, Amazon GuardDuty findings …」 | ✅ |
| 5 | Detectiveは最大1年分の集約データを保持する | Detective FAQs「Amazon Detective maintains up to a year of aggregated data」 | ✅ |
| 6 | 「鳴ってから慌てて有効にしても、それ以前の記録は絵にならない」(有効化以降のデータで分析) | Detective FAQs「starts collecting log data as soon as it is enabled」(ベースライン確立は2週間の監視後) | ✅ |
| 7 | InspectorはEC2・ECRコンテナイメージ・Lambdaを既知の脆弱性(CVE)と意図しないネットワーク露出について継続スキャンする | Inspector User Guide: what-is-inspector(EC2/ECR/Lambdaの継続スキャン、CVEとネットワーク到達可能性) | ✅ |
| 8 | GuardDuty(振る舞い=脅威)とInspector(弱点=脆弱性)の役割分担 | 両User Guide(SAA定番の判断基準) | ✅ |
| 9 | MacieはS3内の機密データ(個人情報等)を機械学習とパターン照合で発見・分類する | Macie User Guide: what-is-macie | ✅ |
| 10 | Macieはスキャンしたデータ量で課金され、自動発見はサンプリングで対象を絞れる | Macie Pricing / User Guide: automated sensitive data discovery | ✅ |
| 11 | Macieは暗号化やアクセス制御そのものは行わない(データ分類の係) | Macie User Guide(発見・分類・可視化が主機能) | ✅ |
| 12 | Security HubはGuardDuty・Inspector・Macie等の検出結果を集約し、セキュリティ基準チェック(スコア)と対応管理を行う | Security Hub User Guide: what-is-securityhub(findings集約、AWS Foundational Security Best Practices等の基準、セキュリティスコア) | ✅ |
| 13 | Security Hubは各検出サービスの代替ではない(集約・姿勢管理の層) | Detective FAQs「With AWS Security Hub, you have a single place that aggregates, organizes, and prioritizes your security alerts」 | ✅ |
| 14 | ArtifactはAWS自身が受けた監査レポート(SOC、ISO、PCI等)や契約文書をセルフサービスで取得するポータル | Artifact User Guide: what-is-artifact | ✅ |
| 15 | Artifactに自社環境の証拠はない(AWS側=責任共有の相手側の証明) | Artifact User Guide(AWSのコンプライアンスレポートが対象) | ✅ |
| 16 | Audit Managerは監査フレームワークに沿って自社AWS環境の証拠を継続的・自動的に収集し、監査準備を支援する | Audit Manager User Guide: what-is(継続的な証拠収集、事前構築フレームワーク) | ✅ |
| 17 | Shield StandardはL3/L4のDDoS保護で全AWS利用者に自動・無償。AdvancedはSRT支援・コスト保護付きの有償版 | Shield Developer Guide(S2-06のtech-reviewでも照合済み。再掲) | ✅ |
| 18 | WAFはWeb ACLでHTTP/HTTPSリクエストを検査するL7ファイアウォール。CloudFront・ALB・API Gatewayに関連付ける | WAF Developer Guide(S2-06のtech-reviewでも照合済み。再掲) | ✅ |
| 19 | Network FirewallはVPCに置くマネージドのステートフルファイアウォールで、ドメイン名ベースの外向きフィルタリングとシグネチャ(IPS的)検査ができる | Network Firewall Developer Guide: what-is-aws-network-firewall(stateful inspection、domain list filtering、Suricata互換ルール) | ✅ |
| 20 | セキュリティグループは宛先をIP/ポートでしか指定できず、ドメイン名での外向き制御は書けない | VPC User Guide: security-group-rules(ルールはプロトコル/ポート/CIDR・プレフィックスリスト・SG参照) | ✅ |
| 21 | Firewall ManagerはOrganizations全体へWAF・Shield Advanced・セキュリティグループ・Network Firewall等のポリシーを一括配布し、新規アカウントへ自動適用する | Firewall Manager Developer Guide: what-is(対応ポリシー種別と自動適用) | ✅ |
| 22 | Firewall Managerの前提はAWS Organizations(全機能)とAWS Configの有効化 | Firewall Manager Developer Guide: prerequisites(Organizations全機能・管理アカウント指定・Config有効化) | ✅ |
| 23 | 冒頭ログとGuardDuty検出の「重要度 High」表記 | GuardDuty User Guide: findings-severity(Low/Medium/High等の重要度) | ✅ |
| 24 | クイズ1: 脅威検知=GuardDuty、脆弱性=Inspector、機密データ発見=Macieの三分割 | 各User Guide(SAA定番の判断基準) | ✅ |
| 25 | クイズ2: AWS側の証明=Artifact、自社側の証拠=Audit Managerの対 | 両User Guide | ✅ |
| 26 | クイズ3: ドメインベース外向き制御=Network Firewall+組織一括適用=Firewall Manager、SGはドメイン指定不可 | Network Firewall / Firewall Manager Developer Guide | ✅ |

## 結論

❌(要修正)は0件、⚠️も0件。

補足: Detectiveの「最大1年」はレビュー実施日にAWS公式FAQ(aws.amazon.com/detective/faqs)の原文「maintains up to a year of aggregated data」で確認済み。

## 物語レビュー(universe整合)の記録

- 冒頭ログ断片あり(GuardDuty検出1行。手口は描かない)。侵入者は最後まで特定されない(シーズンアーク「静かな侵入者」準拠)。勝利条件を「叩かれても倒れない・気づける・説明できる」と明文化してアークを決着
- 時系列: 2月末〜3月最初の金曜。S3-04(立春の鍵交換)の数週間後、ex03(2週間後のIMDSv2)の直後。GuardDuty導入2週間=S3-04末の風間の宿題「残るは、検知です」の回収
- 伏線整合: 青柳の採用面接の言葉(S1-01)を美咲が本人に初めて明かす(面接票の丸三つ)。20分(S1-05)→11秒(S3-04)→今回の4分・19分の系譜。ex03で名前だけ出たInspectorの「また今度」を回収。S2-06の三層(Shield/WAF/「三階は次の季節」)をNetwork Firewallで回収。S3-01の「社外レガシー連携2本」の1本が失敗フックの口になる(例外の期限管理)。9月の足跡・1月の手紙・2月のforkへの参照は記憶としてのみ
- 瀬名の父入院の前震: 着信と「……親父が、入院した」の一言まで(プロットの「詳細は説明しない」を遵守)。手帳の赤丸「瀬名さんの引き継ぎ台帳(いつか)」でS8への静かな不穏を置いて閉幕
- CloudTrail/Configの本格解説はなし(S8担当)。Detectiveの材料・Firewall Managerの前提として名前が出るのみ(プロットの許容範囲内)
- 方言: 美咲の関西語彙は感情が動く2箇所(「軽う見てました」「付けてん」)。矢吹は関西弁、城戸は乾いた関西寄り、風間・青柳・瀬名は標準語。瀬名の台詞は最小限(前に出ない)
- 山場=技術選定の分岐: GuardDuty/Inspector/Macie/Detectiveの役割分担、Security Hub vs 手作業台帳、Artifact vs Audit Manager、Network Firewall vs SG/WAF、Firewall Manager vs 手作業配布——いずれも棄却理由つき
- 失敗・手痛い学び: 例外扱いの鍵1本のローテーション先送り(低権限ゆえの軽視)+Macieが見つけた検証バケットの本物の連絡網CSV
- 具体値: 2時7分/2時11分/2時26分(検知4分・初動19分)、失敗413件、週数十件、6台41件(至急3件)、約9,000行、スコア62点、最大1年、5アカウント
