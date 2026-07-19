# 技術レビュー: stories/data_ingestion_and_analytics/01_数えながら流す

本文・用語コラム・クイズ中の技術的主張をAWS公式ドキュメントと照合した結果。判定は ✅(正確)/⚠️(注意付きで正確)/❌(要修正)。

レビュー実施日: 2026-07-19。照合先は各行の出典(AWS公式ドキュメント)。

| # | 本文中の主張 | 出典 | 判定 |
|---|---|---|---|
| 1 | Kinesisはリアルタイムデータの取り込み・処理・配信を担うサービス群で、保持/複数消費=Data Streams、配送=Firehose、映像=Video Streamsと役割で分かれる | Amazon Kinesis product documentation(ファミリー構成) | ✅ |
| 2 | Kinesis Data Streamsは複数コンシューマが独立して読め、保持期間内はリプレイ(再読み込み)できる | Kinesis Data Streams Developer Guide: What is Kinesis Data Streams | ✅ |
| 3 | 1シャードあたり書き込み1MB/sまたは1,000レコード/s、読み取り2MB/s | Kinesis Data Streams Developer Guide: Quotas and limits(shard throughput) | ✅ |
| 4 | パーティションキーのハッシュでレコードの行き先シャードが決まり、同一キー=同一シャードで順序が保たれる | Kinesis Data Streams Developer Guide: Terminology(partition key、sequence number per shard) | ✅ |
| 5 | 低カーディナリティのキー(学校ID等)はシャードを増やしても特定シャードに集中する(ホットシャード) | Kinesis Data Streams Developer Guide / Best practices(partition key設計) | ✅ |
| 6 | 保持期間は既定24時間、最大365日まで延長可。延長分は追加料金 | Kinesis Data Streams Developer Guide: Changing the Data Retention Period / Pricing(extended retention) | ✅ |
| 7 | 消費が止まった場合、再開時点で保持期間より古いレコードは失われリプレイ不可(停止約36時間・既定24時間→約12時間分喪失) | 同上(retention期間経過後のレコードは読み取り不可。土曜20:13停止→月曜8:00再開で、日曜8:00以前に取り込まれた分=停止開始からの約12時間分が期限切れ、という本文の算術は保持24時間と整合) | ✅ |
| 8 | 共有スループットの読みは2MB/s/シャードを全コンシューマで分け合い、読み手が増えると遅延が伸びる(取得呼び出しの枠も共有) | Kinesis Data Streams Developer Guide: Developing consumers(shared 2MB/s per shard、GetRecords 5 calls/sec per shard、複数コンシューマでの遅延増加) | ✅ |
| 9 | 拡張ファンアウトは登録コンシューマごとに専用2MB/s/シャードを割り当て、HTTP/2でプッシュ配信。コンシューマ登録ごとに追加料金 | Kinesis Data Streams Developer Guide: Enhanced fan-out(SubscribeToShard、dedicated throughput)/ Pricing | ✅ |
| 10 | Amazon Data FirehoseはS3・Redshift・OpenSearch等へのフルマネージド配信で、コンシューマのコードを書かずに済む。旧称Kinesis Data Firehose | Amazon Data Firehose Developer Guide: What is Amazon Data Firehose | ✅ |
| 11 | FirehoseはKinesis Data Streamsをソースにできる(同じ川の別の読み手として構成) | Amazon Data Firehose Developer Guide: Source(Kinesis Data Streams as source) | ✅ |
| 12 | バッファリングヒントはサイズ(MB)と間隔(秒)の早い者勝ちで書き出す。本文の設定は5MBまたは300秒 | Amazon Data Firehose Developer Guide: Buffering hints(S3宛の既定は5MiB/300秒、サイズ・間隔の先に達した方) | ✅ |
| 13 | Firehoseはバッファ分の遅延が必ずあるニアリアルタイム配信で、分単位の鮮度要件の集計はストリームを直接読む側に置く | 同上(near real-time delivery)。ゼロバッファリング設定でも数秒の遅延はあり、いずれにせよ集計処理自体はFirehoseの機能ではない | ✅ |
| 14 | 小さいファイルの乱立をバッファでまとめて防ぐのがバッファリングの狙いの一つ | Amazon Data Firehose Developer Guide / S3 best practices(small file problem) | ✅ |
| 15 | レコード変換: 配信前にLambdaで変換・整形・フィルタできる。Parquet/ORCへの形式変換は組み込み(Glueのスキーマ定義を参照、Lambda不要)。変換失敗レコードはエラー用プレフィックスでS3へ退避 | Amazon Data Firehose Developer Guide: Transform source data(Lambda transformation)/ Converting input record format(Glue Data Catalogのスキーマ参照)/ Data delivery failure handling(processing-failed prefix) | ✅(後2点はコラムのみの記載) |
| 16 | MSKはApache Kafka互換のマネージドストリーミング。Kafkaクライアント・トピック・エコシステム資産が要件のときに選び、互換要件がなければKinesis側で運用を軽くする | Amazon MSK Developer Guide: What is Amazon MSK | ✅ |
| 17 | Kinesis Video Streamsはカメラ・デバイスからの映像ストリームの取り込み・保存・処理に特化(行データのData Streamsとはデータ種別が別) | Kinesis Video Streams Developer Guide: What is Kinesis Video Streams | ✅ |
| 18 | SQSとの対比: キューは取得・削除でメッセージが消え、複数コンシューマが同じデータを独立にリプレイする用途には不適 | SQS Developer Guide / Kinesis FAQs(SQS vs Kinesis使い分け) | ✅ |
| 19 | 秒間4,000件×平均0.5KB=2MB/s。容量では2シャード、件数制約(1,000件/s)で4シャードが下限、余裕を見て6シャード | #3の仕様からの計算(物語上の自社数値) | ✅ |
| 20 | 5分ごとにDBを直接ポーリングする案の棄却(行事ピーク時にDB負荷が跳ねる) | 設計判断(仕様主張ではない) | ✅(仕様主張ではない) |
| 21 | 喪失分をFirehose→S3経由の写しから埋め戻す復旧 | 設計プラクティス(2経路化。仕様主張ではない) | ✅(仕様主張ではない) |
| 22 | β初日3分台・運動会当日「5分より内側」の遅延、1,900万件/三連休、約230万件/12時間分等 | 物語上の自社計測値(仕様主張ではない) | ✅(仕様主張ではない) |
| 23 | クイズ2「書き込みは1MB/sまたは1,000レコード/sの先に達する方で制約」 | #3と同一 | ✅ |
| 24 | クイズ3「保持期間の延長・遅延監視・二経路化」の再発防止3点 | #6-8、#21(遅延監視はGetRecords.IteratorAgeMilliseconds等の標準プラクティス) | ✅ |

## 物語レビュー(universe整合)

- 時系列: 3年目8月下旬〜10月(S4-04の最終負荷試験=7月末の直後)。「思い出検索」秋β公開=9月第二週、三連休の障害=9月の連休、結=10月第二土曜の運動会集中日。series-plan S5の時間軸(3年目夏〜秋、秋βを跨ぐ)に整合。
- 真鍋メイン(S5アーク): 口癖の進化「数えてから、流す」→「流しながら数える」を結の台詞で明示。S4-04のホットパーティションの学びを、川では最初から複合キー(学校ID#ユーザーID)で回避——失敗の再演ではなく成長の証明として使用(プロット指定どおり)。
- 設計レビューの型の制度化(S5人間主題①): 問い合わせ一覧の書式に「何分まで古くてよいか(鮮度)」の列が増える。狩野の「通算3件目ね」はS4-04の「2件目の適用」と整合。空堀の帳面の書式への言及と、結の「引けん記録は、無いのと同じ」(戸倉の言葉を名を出さず引用)——S5以降は匂わせのみ、の正典に従い戸倉本人は登場させない(本格登場はS5-02の帳面の会)。
- 瀬名の扱い: 東京から書面一行のみ(「幅の根拠は分かった。深さの根拠は、あるか」)。不在の理由は書かない(S8前震の継続)。この一行が保持期間の失敗フックの伏線として機能し、失敗回で回収される。
- 失敗フック: 保持期間既定24時間×消費停止36時間=12時間分喪失。誰も悪人にしない——係が例外で止まったのは検証に出ない形のレコードのせい、真因は「止まったことを知らせる仕組みがなかった」ことに置く。青柳が「直してから報告」の誘惑を退けて先に電話する場面で、彼の「報告が遅れがち」アークの成長を示す。監視(読み手の遅延)の整備はS8への種(プロット指定)。
- 学ぶ側の自力到達: 青柳が保持期間の算術(「止まってたのは36時間です」)と共有帯域の限界を自分で言い当てる。試問口調なし。
- 棄却理由: 5分間隔バッチ(DB負荷)、SQS(読んだら消える)、自前Lambda配送(運用の自作)、Firehose経由の急上昇(バッファ遅延+集計は配送の仕事ではない)、全読み手への拡張ファンアウト(追加課金→遅れて困る読み手だけ)、MSK(Kafka資産は先方のみ→「エコシステムが要件になった日に再考」の台帳予約)、KVS(線引きのみ・商品判断は狩野預かり)。「ストリームは常にバッチより優れる」の単純化を回避——月次レポートは日次のまま残す。
- 話法: 真鍋=標準語寄り+柔らかい関西、青柳・狩野・瀬名=標準語、城戸=丁寧な関西混じりの数字の言葉、矢吹=関西弁(テープと川の対比)、美咲の関西語彙は「あかん」1箇所(規約1〜3箇所内)。
- 禁止事項遵守: Lambdaイベントソースマッピングの詳説なし(S6)、SQS/SNS/EventBridgeは軽い対比のみ(S7)、Flinkのウィンドウ集計なし(幕間ex01担当——集計係の実装詳細は意図的に書いていない)、Parquet/列指向の深掘りなし(S5-02担当。コラムで組み込み変換の事実のみ)。AZ・災害の扱いなし。
- S5-02への橋: 湖のファイル数の膨張と「湖、そろそろ棚が要ります」(プロット指定の台詞)。
- 用語コラム12語=front matterと一致、term_idは本文に不使用。本文5,560字前後(空白除く)で規定(5,500〜6,500)内。具体値は5分/96ms/14〜38時間/1MB/s・1,000件/s・2MB/s/6シャード/24時間・365日・7日/5MB・300秒/2MB/s per consumer/秒間4,000件/1,900万件・230万件ほか、規約の最低5つを大きく超える。
