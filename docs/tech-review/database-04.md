# 技術レビュー: stories/database_architecture/04_数えてから建てる

本文・用語コラム・クイズ中の技術的主張をAWS公式ドキュメントと照合した結果。判定は ✅(正確)/⚠️(注意付きで正確)/❌(要修正)。

レビュー実施日: 2026-07-17。照合先は各行の出典(AWS公式ドキュメント)。

| # | 本文中の主張 | 出典 | 判定 |
|---|---|---|---|
| 1 | DynamoDBはキー中心の大規模・低レイテンシアクセスに向くマネージドNoSQLで、JOIN・アドホックSQLの主戦場ではない(Auroraと棲み分け) | DynamoDB Developer Guide: What is Amazon DynamoDB | ✅ |
| 2 | RDBは読みをレプリカで分散できるが、書き込みは単一ライターに集中する(Auroraは単一ライター構成) | Aurora User Guide(single-master構成。db-02レビュー#8と同一の正典) | ✅ |
| 3 | DynamoDBの設計はアクセスパターン(問い合わせ)を先に洗い出してからキーを決める | DynamoDB Developer Guide: Best practices for designing partition keys / NoSQL design("you shouldn't start designing your schema until you know the questions it needs to answer") | ✅ |
| 4 | パーティションキーは項目の物理配置先をハッシュで決める。高カーディナリティ・均等分散が前提 | DynamoDB Developer Guide: Partitions and data distribution / Best practices | ✅ |
| 5 | ソートキーで同一パーティションキー内の範囲取得(「この人のこの期間」を1回のQueryで) | DynamoDB Developer Guide: Working with queries(sort key range conditions) | ✅ |
| 6 | GSIは別のパーティションキー/ソートキーで引ける後付け可能なインデックスで、独自のキャパシティを持ち、強整合読み取り不可 | DynamoDB Developer Guide: Global secondary indexes(create anytime、own provisioned throughput、eventual consistency only) | ✅ |
| 7 | LSIはテーブル作成時のみ定義可・同一パーティションキー・項目コレクション10GB上限(強整合は可) | DynamoDB Developer Guide: Local secondary indexes(item collection size limit 10 GB、created at table creation) | ✅ |
| 8 | RCU=強整合読み取り1回/秒(4KBまで)、結果整合はその半分(1RCUで2回)、WCU=書き込み1回/秒(1KBまで)、サイズは切り上げ | DynamoDB Developer Guide: Read/write capacity mode(capacity unit sizes) | ✅ |
| 9 | 0.4KBの書き込み=1WCU、1.2KBの書き込み=2WCU | 同上(1KB単位の切り上げ) | ✅ |
| 10 | 強整合読み取りはRCU消費2倍(結果整合の2倍) | DynamoDB Developer Guide: Read consistency / capacity mode | ✅ |
| 11 | 既定は結果整合読み取り。強整合はリクエスト時に指定 | DynamoDB Developer Guide: Read consistency | ✅ |
| 12 | 読めない負荷はオンデマンドで受け、安定後にプロビジョンド+Auto Scalingへ切り替える(容量モードは変更可能) | DynamoDB Developer Guide: On-demand mode / Provisioned mode(モード切替は24時間に1回等の制限あり。本文は3週間後の切替なので抵触しない) | ✅ |
| 13 | オンデマンドは従量課金で、安定大容量ではプロビジョンドの方が安い場合がある(単価は従量が高い) | DynamoDB Pricing(on-demand vs provisioned) | ✅ |
| 14 | DynamoDB Auto ScalingはApplication Auto Scalingで目標使用率に追従(本文では70%) | DynamoDB Developer Guide: Managing throughput capacity with auto scaling(target utilization 20–90%) | ✅ |
| 15 | 1パーティションあたりのスループット上限は書き1,000WCU/秒(読み3,000RCU/秒)。テーブル全体に余裕があってもホットキーで詰まる | DynamoDB Developer Guide: Partitions and data distribution(per-partition maximums)/ Best practices(hot partition) | ✅ |
| 16 | 「寄りを均す仕組みは器にもあるが、集中が続けば追いつかない」 | DynamoDB Developer Guide: adaptive capacityの存在と限界(sustained hot keyは設計で解決) | ✅(断定を避けた描写) |
| 17 | ホットパーティション対策はキー設計(複合キー化・書き込みシャーディング=サフィックス分割、読みはスキャッタギャザー) | DynamoDB Developer Guide: Using write sharding to distribute workloads evenly | ✅ |
| 18 | TTLは項目属性のエポック秒で期限切れ項目を追加コストなしにバックグラウンド削除。削除は期限ちょうどでなく数日以内 | DynamoDB Developer Guide: Time to Live(no extra cost、"typically deletes expired items within a few days")読み側で期限切れをフィルタする推奨も同ガイド | ✅ |
| 19 | PITRは有効化から35日間、任意の秒(per-second granularity)へ新しいテーブルとして復元 | DynamoDB Developer Guide: Point-in-time recovery(35日、restore to a new table) | ✅ |
| 20 | グローバルテーブルはマルチリージョン・マルチアクティブ、双方向レプリケーション、結果整合、「昇格」概念なし | DynamoDB Developer Guide: Global tables(multi-active、all replicas writable) | ✅ |
| 21 | レプリケーション遅延「普段は1秒とかからんくらい」 | DynamoDB Global tables(replication typically within a second。物語中は自社観測の口語として提示) | ⚠️ 公式は「通常1秒以内」程度の目安表現。断定を避けた口語表現で整合 |
| 22 | 同時書き込みの競合は「あとから書いた方が勝ち」(last writer wins) | DynamoDB Developer Guide: Global tables conflict resolution(last writer wins) | ✅ |
| 23 | 平時の書き込みを東京へ寄せる運用規律(両方書ける≠両方に書く) | 設計プラクティス(仕様主張ではなく運用判断。write partitioningはAWSブログ等でも推奨パターン) | ✅(仕様主張ではない) |
| 24 | DAXはDynamoDB専用のマネージドインメモリキャッシュ。API互換でアプリ改修最小、読みはマイクロ秒級 | DynamoDB Developer Guide: In-memory acceleration with DAX(microseconds、API-compatible) | ✅ |
| 25 | DAXが効くのは結果整合の読みで、強整合読み取り・書き込みの高速化には効かない(強整合はパススルー) | DAX Developer Guide: consistency(strongly consistent reads pass through to DynamoDB) | ✅ |
| 26 | DAX vs ElastiCache: DynamoDB特化(改修最小)vs 汎用(キャッシュ層を自前実装) | DAX documentation / ElastiCache documentation(使い分けの標準論点) | ✅ |
| 27 | Aurora Global Database(単方向・昇格あり)とグローバルテーブル(双方向・マルチアクティブ)の対比 | Aurora User Guide: Global databases / DynamoDB Global tables | ✅ |
| 28 | GA初日1日3,400万件、ピーク秒間4,000件、特定校秒間2,600件、CPU 87%等の負荷数値 | 物語上の自社計測値(仕様主張ではない) | ✅(仕様主張ではない) |
| 29 | 法人最大アカウント700万点×約1.6KB≒11GBでLSIの10GB上限を超過するため棄却 | 物語上の試算。10GB上限自体は#7の出典 | ✅ |
| 30 | クイズ3の「1パーティション秒間1,000WCU程度が上限」 | DynamoDB Developer Guide: per-partition maximums(1,000 WCU/sec) | ✅ |

## 物語レビュー(universe整合)

- 時系列: 3年目・7月(db/03の設計レビュー制度化=6月最終金曜、幕間ex03=7月最初の土曜の直後)。最終負荷試験は7月最後の金曜。秋β(db/02の狩野「秋にβを当てたい」)の前で正典に整合。
- 幕間ex03との接続: 戸倉が赤鉛筆で足した「何件返す」の列が問い合わせ一覧の書式に入っている(帳面の貸し借りの継続)。葉書の文面で「時間あたりの最大」の列の追加を報告——帳面の続きを真鍋が書く、の関係アークに一致。
- 矢吹の「どの単位で戻すんや」がパーティションキー=ユーザーID(復元単位を間取りに彫る)とPITRのユーザー単位書き戻しで回収。シーズンアーク「数える人」の締めとして、真鍋の「で、1日何件です?」が冒頭の棄却根拠(1日3,400万件)で機能。
- 失敗フック: ホットパーティション(学校ID)。「1日単位で数えて安心した=数える解像度が粗かった」として、真鍋の天才性でなく数える習慣と書式の改善(「時間あたりの最大」列)で解決——真鍋万能化の禁止に従う。誰も悪人にしない(設計レビューを通っていた=書式の欄が足りなかっただけ、という着地)。net/03「行事の朝の受付戦争」の記憶で矢吹が気づきの糸口を出す(既刊接続)。
- 棄却理由: ライタースケールアップ(効くが終わらない・器の階段)、全面移行(柔軟な検索はAurora)、LSI(10GB超過の実測)、初手プロビジョンド(読めない負荷)、全画面強整合(RCU2倍)、ElastiCache(汎用ゆえの実装負担)、平時の双方向書き込み(後勝ち競合)——各選定に棄却が付く。
- 人物の話法: 青柳=標準語、狩野=標準語、瀬名=標準語(書面1行のみ・前に出ない)、城戸=丁寧な関西混じりの数字の言葉、矢吹=大阪寄り関西、真鍋=標準語寄り+柔らかい関西。美咲の関西語彙は本編で抑制(規約内)。試問口調なし——青柳がGSI×強整合の矛盾を自力で見つける場面を配置。
- 瀬名の扱い: 今週も東京(理由は書かない=S8前震)、書面コメント1行、赤丸への言及1行のみ。プロットの指定どおり。
- 禁止事項遵守: DynamoDB Streamsは本文に登場させず(S7担当)、Kinesis等の取り込み系はS5への橋の台詞(「今度は、流す」)に留め、サービス名を出さない。「NoSQLが上位互換」的な単純化なし。β公開日そのものは描かない。
- 用語コラム14語=front matterと一致、term_idは本文に不使用。本文6,096字(空白除く)——14語回の許容(7,000字)内。具体値は#28-30ほか20点超で規約の最低5つを満たす。
