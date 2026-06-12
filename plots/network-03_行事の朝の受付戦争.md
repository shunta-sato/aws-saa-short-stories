# プロット: network/03 行事の朝の受付戦争

| 項目 | 値 |
|---|---|
| 状態 | ready |
| family / episode | networking_and_application_security / 3 |
| terms | elastic_load_balancing_elb, application_load_balancer, alb_listener_rule, alb_path_based_routing, alb_host_based_routing, alb_target_group, alb_sticky_sessions, network_load_balancer, nlb_static_ip_elastic_ip, nlb_tls_listener, nlb_udp_support, elb_cross_zone_load_balancing, gateway_load_balancer, gateway_load_balancer_endpoint(14語) |
| 時系列 | 春の行事シーズン(入学式・運動会前) |
| 分量 | 5,500〜6,500字(担当語が多いため上限緩和) |

## ねらい

ELBファミリー全体を「受付」の比喩で体系化する、S2の技術的な山場。学校向けプランの行事スパイクという顧客文脈で、ALBの振り分け機能群を実戦投入する。滝本(自治体)を行事文脈で1シーン再登場させる。

## あらすじ

入学式シーズン、学校向けプランの閲覧が月曜朝に集中しアプリが悲鳴を上げる。モノリスだったWebをALBの振り分けで段階分割し、配信スパイクを乗り切る。並行して、式場向け映像中継の固定IP要件(NLB)、セキュリティ機器の検査要件(GWLB)という別系統の「受付」も整理し、ELB4種の対応表を完成させる。

## ビート

1. **起**: 月曜8時、入学式の写真公開と同時に閲覧集中。各学校の保護者が一斉アクセス。CPUは余っているのに特定機能(サムネイル一覧)だけ遅い——モノリスの内部で奪い合い。
2. **承(ALBの解剖)**: **application_load_balancer**を中心に再設計。**alb_target_group**(ヘルスチェック単位・ASG連携)、**alb_listener_rule**(優先度評価)、**alb_path_based_routing**(/album と /api を分離)、**alb_host_based_routing**(school.photorim.example と wedding.photorim.example を1台に集約=コスト)。「1つのALBに複数の顔と複数の出口を持たせる」設計で機能別ターゲットグループへ分割。
3. **転1(スティッキーの罠)**: 分割後、ログイン状態が不安定に。原因は旧アプリのローカルセッション+**alb_sticky_sessions**頼みの構成がスケールインで切れること。「スティッキーは改修猶予の暫定策。本命はセッション外部化」——ElastiCache移行はS4の宿題として明示的に積む(伏線)。
4. **転2(別系統の受付)**: ①式場向けライブ中継の要件「会場側ファイアウォールのIP許可リストに載せたい」→**network_load_balancer**+**nlb_static_ip_elastic_ip**(ALBは固定IP不可で棄却)。TLS終端は**nlb_tls_listener**(ACM連携・エンドツーエンド暗号化ならTCPパススルー)。会場からの映像はUDP系プロトコル→**nlb_udp_support**(UDPはNLB一択)。②セキュリティ検査アプライアンスの導入検討(風間の要請)→**gateway_load_balancer**+**gateway_load_balancer_endpoint**(GENEVE・検査VPC集約)。「S3用ゲートウェイエンドポイントと名前が似て非なるもの」の注意をnet/02と接続して一言。
5. **転3(クロスゾーンの偏り)**: 行事ピーク中、AZ間でターゲット数が偏り片側だけ高負荷。**elb_cross_zone_load_balancing**(ALB常時有効/NLB既定無効)の対比で解消。**elastic_load_balancing_elb**ファミリー表(ALB=L7/NLB=L4/GWLB=検査)を矢吹が「受付の三業態」としてまとめる。
6. **結**: 行事の朝を無事に乗り切る。滝本から「秋の防災訓練の写真共有、学校のときみたいに重うならんですろうか」と問い合わせ(net/05のCDN・S10への接続)。締めは美咲の「受付を増やすことと、受付の種類を選ぶことは別の仕事」。

## 必須の対比(棄却理由込み)

- ALB(L7・ルール・固定IP不可)vs NLB(L4・固定IP・UDP/TLS)vs GWLB(透過検査)
- スティッキーセッション(暫定)vs セッション外部化(本命、S4へ)
- クロスゾーン: ALB常時有効 / NLB・GWLB既定無効(AZ間転送の扱い)

## 具体値の例

リスナールールの優先度評価、ターゲットグループ単位のヘルスチェック、NLBのAZごとEIP、TLSリスナーとACM、GENEVE、クロスゾーン既定値の差。

## 書いてはいけないこと

- Auto Scaling本体の深掘り(S6担当。「台数はASGが増やす、振り分けは受付」程度の言及まで)。
- CloudFrontでの解決を先取りしない(net/05の主題。「キャッシュで根本から減らす手は次回」と引きに使うのは可)。
