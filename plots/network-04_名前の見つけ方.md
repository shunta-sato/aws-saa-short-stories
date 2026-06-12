# プロット: network/04 名前の見つけ方

| 項目 | 値 |
|---|---|
| 状態 | ready |
| family / episode | networking_and_application_security / 4 |
| terms | amazon_route_53, route53_alias_record, route53_health_check, route53_failover_routing, route53_weighted_routing, route53_latency_based_routing, route53_geolocation_routing, route53_geoproximity_routing, route53_multivalue_answer_routing, private_hosted_zone, aws_global_accelerator, global_accelerator_static_anycast_ip(12語) |
| 時系列 | 夏。海外展開プロジェクト始動 |
| 分量 | 5,000〜6,000字 |

## ねらい

Route 53のルーティングポリシー7種を「要件語→ポリシー」の対応で体系化する回。式場プランの海外展開(ハワイ・グアム挙式の現地撮影チーム)を舞台に、DNSの設計判断とGlobal Acceleratorの位置付けを描く。

## あらすじ

式場大手との提携で海外挙式の撮影・即日共有サービスが始まる。海外からのアップロード/閲覧が遅い問題、新旧システムの段階移行、内部名の整理という3つの課題を、すべて「名前(DNS)の設計」として解いていく。

## ビート

1. **起**: 提携先からのクレーム——「ハワイの式場から動画が上がらない、現地の親族が見られない」。美咲が地球儀を前にレイテンシの正体を考える(物理距離はどうにもならない)。
2. **承(Route 53の文法)**: **amazon_route_53**の基礎を青柳に説明させる。zone apexの**route53_alias_record**(CNAME不可・AWSリソース連動・クエリ無料)から。ルーティングポリシーの対応表を1つずつ要件語で埋める:
   - 新バージョンへの段階移行(10%→50%)=**route53_weighted_routing**
   - 海外ユーザーを近いリージョンへ=**route53_latency_based_routing**(「測定値で選ぶ」)
   - 国・地域で必ず分けたい(コンテンツ権利・法令)=**route53_geolocation_routing**(「地図で固定」)
   - リージョン間の流量をバイアスで調整=**route53_geoproximity_routing**(「つまみで配分」)
   - 簡易な複数IP返却+死活=**route53_multivalue_answer_routing**(「ロードバランサの代わりにはならない」)
   - 障害時の主従切替=**route53_failover_routing**+**route53_health_check**(DR編の復習として接続。TTLの教訓を一言再掲)
3. **転1(内部名の整理)**: 移行で増えた内部サービスのエンドポイントがIP直書きで散乱→**private_hosted_zone**で内部DNS(db.internal等)。「同じ名前で社内は内部ALB、社外は公開サイト」(スプリットビュー)も式場提携の検証環境で使う。VPCのDNS属性が前提という細部はnet/02と接続。
4. **転2(DNSでは縮まらない距離)**: レイテンシベースで改善したが、アップロード自体がまだ遅い+提携先から「機材のファイアウォールに固定IPで登録したい」。DNS切替はTTLの遅延もある→**aws_global_accelerator**+**global_accelerator_static_anycast_ip**(エッジで受けてAWSバックボーン・anycast固定IP2つ・TCP/UDP・即時フェイルオーバー)。「キャッシュするCloudFrontとは別物。配信は次回」の線引きを明確に(net/05への引き)。
5. **転3(小さな失敗)**: 加重ルーティングの検証で、TTLを長いまま重みを変えて「切り替わらない」と騒ぐ小事件(犯人は自分たちのキャッシュ)。DNSの変更は「伝播を待つ」ものという身体感覚を獲得。
6. **結**: 海外の式場から「親族がその場で見られた」という便り。矢吹「名前ちゅうのは、結局『どこへ案内するか』の約束やな」。次回への引き: 「世界中に配るなら、毎回東京まで取りに来させるんか?」(CDNへ)。

## 必須の対比(棄却理由込み)

- ルーティングポリシー7種の要件語対応(加重/レイテンシ/地理/近接+バイアス/複数値/フェイルオーバー/シンプル)
- alias vs CNAME(apex可否・課金・AWS連動)
- Global Accelerator vs Route 53(ネットワーク層の経路最適化+固定IP vs DNS応答の制御)
- Global Accelerator vs CloudFront(非キャッシュ/キャッシュ——詳細は次回)

## 具体値の例

anycast固定IP2個、TTLと切替遅延、zone apex、レイテンシ/地理の判定基準の違い、ヘルスチェックとフェイルオーバーの組み合わせ。

## 書いてはいけないこと

- CloudFrontの本格解説(net/05)。
- 「Global Acceleratorは常にRoute 53より優れる」という単純化(コスト・要件次第)。
