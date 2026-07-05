# AWS SAA-C03 短編小説集

AWS認定ソリューションアーキテクト – アソシエイト(SAA-C03)の頻出用語を、**連作お仕事小説**で覚えるための学習コンテンツです。

試験は「シナリオを読んで最適なサービスを選ぶ」形式です。用語を孤立した定義で暗記するより、**誰が・どんな要件で・なぜそれを選び・なぜ他を捨てたか**という文脈ごと記憶する方が、本番の判断力に直結します。各編は約5,000字、物語の山場はすべて技術選定の分岐に置かれています。

> **本コンテンツについて**: この短編小説集は、人間の企画・監修のもとAI(Anthropic Claude)が生成したものです。プロットの設計・事実確認・編集は人間とAIの協働で行っていますが、AWSのサービス仕様は更新されるため、必ず最新の公式ドキュメントで確認してください。詳細は [DISCLAIMER.md](DISCLAIMER.md) を参照してください。

## 読み方

1. 物語を普通に読む(1編10分程度)
2. 末尾の「用語コラム」で各用語の決め手とひっかけを整理する
3. 「確認クイズ」3問で定着を確かめる

## 目次

### 世界線: フォトリム([設定資料](universes/photorim/universe.md))

写真・動画共有サービスの架空企業フォトリム社。インフラエンジニアの堂島美咲を中心とした連作です。物語は**シーズン**単位で時系列に進みます。各編の末尾に「次の話」リンクがあるので、順番に読み進められます。

#### シーズン1: ストレージとレジリエンス(1年目)

| # | タイトル | 主な内容 |
|---|---|---|
| S1-01 | [請求書は嘘をつかない(中編)](stories/storage/01_請求書は嘘をつかない.md) | S3ストレージクラス、ライフサイクル、コスト設計。シリーズ導入の中編 |
| S1-02 | [ブロックの行方](stories/storage/02_ブロックの行方.md) | EBSボリュームタイプ、スナップショット、AWS Backup |
| S1-03 | [引っ越しと四つのFSx](stories/storage/03_引っ越しと四つのFSx.md) | EFS設計、4種のFSxの使い分け |
| S1-04 | [データセンターを畳む日](stories/storage/04_データセンターを畳む日.md) | Storage Gateway 4形態、Snowファミリー、移行判断則 |
| S1-05 | [消せないデータ、消えないデータ](stories/storage/05_消せないデータ消えないデータ.md) | バージョニング、Object Lock、レプリケーション、Glacier階層 |
| S1-06 | [金曜日のゲームデー](stories/resilience_and_dr/01_金曜日のゲームデー.md) | RPO/RTO、DR戦略4段階、フェイルオーバーの層 |
| S1-07 | [水曜日の本物](stories/storage/06_水曜日の本物.md) | シーズン1最終話。本番障害と「戻す単位」(復習・物語推進回) |

#### シーズン2: 城の通りと門(ネットワーク)(2年目)

全6話+幕間4本(幕間は用語集外の頻出トピックを補強するショートショート)。順次公開。

| # | タイトル | 主な内容 |
|---|---|---|
| S2-01 | [一本の通り道](stories/networking_and_application_security/01_一本の通り道.md) | VPC、サブネット、ルートテーブル、NAT、SG vs NACL |
| 幕間 | [通らなかった記録](stories/networking_and_application_security/ex01_通らなかった記録.md) | VPC Flow Logs(用語集外の頻出補強) |
| S2-02 | [門は増やして、道は閉じる](stories/networking_and_application_security/02_門は増やして道は閉じる.md) | VPCエンドポイント、PrivateLink、ピアリング、TGW、DX、VPN |
| 幕間 | [トンネルの両端](stories/networking_and_application_security/ex02_トンネルの両端.md) | Site-to-Site VPNの構成要素(VGW/CGW) |
| 幕間 | [一本足の専用線](stories/networking_and_application_security/ex03_一本足の専用線.md) | Direct Connect Gateway、DXの冗長化 |
| S2-03 | [行事の朝の受付戦争](stories/networking_and_application_security/03_行事の朝の受付戦争.md) | ELBファミリー(ALB/NLB/GWLB)、クロスゾーン、スティッキー |
| S2-04 | [名前の見つけ方](stories/networking_and_application_security/04_名前の見つけ方.md) | Route 53ルーティングポリシー7種、Alias、Global Accelerator |
| 幕間 | 名前が届かない日(執筆予定) | Route 53 Resolver(ハイブリッドDNS) |

シーズン2の残りとシーズン3以降(セキュリティ、データベース…)の構成は [plots/series-plan.md](plots/series-plan.md) を参照してください。

進捗と分野別の残り用語は [docs/coverage.md](docs/coverage.md) を参照(ストレージ57語・レジリエンス/DR 13語はカバー完了)。

## リポジトリ構成

```
stories/<分野>/        # 短編本体。冒頭のfront matterに担当用語を記載
universes/<世界線>/    # 舞台設定・登場人物・年表(物語は複数の世界線を持てます)
docs/writing-guide.md  # 執筆規約(共通ルール)
docs/coverage.md       # 用語カバレッジ(自動生成)
tools/check_coverage.py# カバレッジ検証スクリプト
```

新しい編・新しい世界線の追加方法は [docs/writing-guide.md](docs/writing-guide.md) を参照してください。

## 免責事項・ライセンス

- 非公式コンテンツです。AWSおよびAmazonとは関係ありません: [DISCLAIMER.md](DISCLAIMER.md)
- ライセンス: [CC BY-NC-SA 4.0](LICENSE)(表示 - 非営利 - 継承)
