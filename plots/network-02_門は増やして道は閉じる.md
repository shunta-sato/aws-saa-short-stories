# プロット: network/02 門は増やして、道は閉じる

| 項目 | 値 |
|---|---|
| 状態 | ready |
| family / episode | networking_and_application_security / 2 |
| terms | vpc_endpoint, s3_gateway_endpoint, s3_interface_endpoint, interface_endpoint_private_dns, aws_privatelink, privatelink_endpoint_service, vpc_peering, aws_transit_gateway, aws_direct_connect, aws_site_to_site_vpn, aws_client_vpn, efs_mount_target(12語) |
| 時系列 | net/01の直後(城戸のNATコスト指摘を受けて) |
| 分量 | 5,000〜6,000字 |

## ねらい

「外に出る道(NAT)」を増やした結果のコスト増を、「そもそも外に出ない道(エンドポイント)」で解決する回。閉域接続ファミリー(Peering/TGW/DX/VPN)を一枚の対応表に。真鍋一花の初カメオ。

## あらすじ

城戸が請求書を持ってくる: NATゲートウェイのデータ処理料金が跳ねている。内訳を見ると、S3への大量転送(サムネイル生成バッチ等)がNAT経由。**s3_gateway_endpoint**(無料)への切り替えで「AWS行きのトラフィックがインターネット向けの門を通る必要はない」を学ぶ。続いて拠点・パートナー接続の課題が連鎖し、閉域接続の選択肢を体系化する。

## ビート

1. **起**: 城戸の請求書レビュー。「NATの台数を増やしたのは正しい。でも、**通る必要のない荷物まで門を通ってませんか**」(数字の人の指摘)。調査するとプライベートサブネット→S3の大量転送がNAT経由(GB単価の処理料金)。
2. **承(エンドポイントの文法)**: **vpc_endpoint**の2形態。S3/DynamoDBは**ゲートウェイ型**(無料・ルートテーブルにプレフィックスリスト経路)、その他サービスは**インターフェイス型**(ENI・時間+データ課金)。S3には**s3_interface_endpoint**もある——「オンプレや別VPCからS3へ閉域で届きたい時はインターフェイス型」という使い分け。**interface_endpoint_private_dns**で「アプリのURLを変えずに」切り替え(VPCのDNS属性が前提、という細部)。Lambdaのジョブも修正不要で閉域化。
3. **転1(東京拠点との接続)**: 東京拠点(法人営業・風間のチーム)から社内システムへの接続要件。選択肢の階段: **aws_client_vpn**(個人端末・少人数)→**aws_site_to_site_vpn**(拠点・即日・IPsec・帯域は保証なし)→**aws_direct_connect**(専用線・安定帯域・リードタイム数週間〜)。「まずVPNで繋ぎ、DXが開通したらVPNはバックアップ回線に降格」という現実的な段取りを描く。
4. **転2(VPCが増えてきた)**: 分析用VPC・検証用VPCが増え、**vpc_peering**のメッシュが破綻し始める(CIDR重複の検証VPCが繋げない事故も一発)。**aws_transit_gateway**でハブ&スポーク化。「2〜3個ならPeering(安い・推移的ルーティング不可)、増えるならTGW(時間+データ課金)」の損益分岐。
5. **転3(パートナー接続と真鍋カメオ)**: 印刷・アルバム製本のパートナー企業に注文データAPIを公開する要件。Peeringだと「家ごと繋がる」(CIDR重複も問題)→**aws_privatelink**/**privatelink_endpoint_service**で「サービスという窓口だけを一方向に公開」。NLB前提という細部。——この検証の過程で、東雲出身のデータエンジニア・**真鍋一花**が大阪からリモートで一瞬登場(「その注文データ、1日何件です? 数えてから流しましょ」と一言だけ。矢吹が「俺の元部下や。数の鬼や」と紹介)。
6. **結**: **efs_mount_target**の整理(各AZにマウントターゲット、SGでポート2049——net/01のSG学習の応用としてさらっと)。城戸への報告: NAT処理料金がエンドポイント化でどれだけ下がったか。「門は増やして、道は閉じる。閉じた道は、請求書で説明できます」。

## 必須の対比(棄却理由込み)

- ゲートウェイ型(無料・S3/DynamoDB限定・ルート)vs インターフェイス型(有料・汎用・ENI+DNS)
- Peering(1対1・推移なし・CIDR重複不可)vs Transit Gateway(ハブ・スケール・課金)
- Client VPN / Site-to-Site VPN / Direct Connect(対象・速度・リードタイム・コスト)
- PrivateLink vs Peering(サービス単位の片方向 vs ネットワーク全体の双方向)

## 具体値の例

NATデータ処理はGB単価課金、ゲートウェイエンドポイント無料、DXのリードタイム数週間以上、NFS 2049、PrivateLinkのNLB前提。

## 書いてはいけないこと

- 真鍋を出しすぎない(台詞2つまで。本格登場はS4)。
- TGWを万能ハブとして無条件推奨しない(コスト言及必須)。
