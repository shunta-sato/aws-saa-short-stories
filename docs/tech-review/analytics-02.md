# 技術レビュー: stories/data_ingestion_and_analytics/02_湖の底の台帳

本文・用語コラム・クイズ中の技術的主張をAWS公式ドキュメントと照合した結果。判定は ✅(正確)/⚠️(注意付きで正確)/❌(要修正)。

レビュー実施日: 2026-07-26。照合先は各行の出典(AWS公式ドキュメント)。

| # | 本文中の主張 | 出典 | 判定 |
|---|---|---|---|
| 1 | データレイクは構造化・非構造化データを生のまま一元保管し、スキーマは読む時に当てる(schema-on-read)。用途を後から決められる | AWS What is a data lake?(aws.amazon.com/what-is/data-lake)/ Storage Best Practices for Data and Analytics Applications whitepaper | ✅ |
| 2 | DWHは入れる前に整形する(schema-on-write)——レイクとの対比 | 同上(data lake vs data warehouse比較) | ✅ |
| 3 | Glue Data Catalogはテーブル定義・スキーマ・データの置き場を管理するメタデータストアで、中身は動かさない。Hiveメタストア互換 | AWS Glue Developer Guide: Data Catalog / Populating the catalog | ✅ |
| 4 | Glueクローラーはデータストアを走査し、スキーマ・パーティションを推定してカタログのテーブルを自動作成・更新できる。スケジュール実行(日次等)が可能 | AWS Glue Developer Guide: Defining crawlers / Crawler scheduling | ✅ |
| 5 | カタログを更新しないと新しいデータ(新パーティション)がAthenaのクエリに現れない | Athena User Guide: Partitioning data(MSCK REPAIR TABLE / crawler等でのパーティション追加) | ✅ |
| 6 | Glue ETLジョブはサーバーレスSpark。クラスタ管理不要、DPU時間課金 | AWS Glue Developer Guide: AWS Glue jobs / AWS Glue pricing(DPU-hour) | ✅ |
| 7 | Parquetは列指向で、必要な列だけ読める+圧縮が効き、スキャン量とコストが大幅に減る(本文: 7.8TB→700GB弱、約9割減) | Athena User Guide: Columnar storage formats / Performance tuning(Top 10 Performance Tuning Tips for Athena: 圧縮・列指向で30〜90%削減の事例) | ✅(数値は物語上の自社実測) |
| 8 | FirehoseにはParquet/ORCへの組み込み形式変換がある(Lambda不要) | Amazon Data Firehose Developer Guide: Converting input record format | ✅ |
| 9 | AthenaはS3のデータをサーバーレスで直接SQLクエリし、課金はスキャンしたデータ量(1TBあたり) | Athena User Guide: What is Amazon Athena / Athena pricing(per TB scanned) | ✅ |
| 10 | パーティショニング(date=等)+WHERE句の絞りで読む範囲を限定できる(本文: 800GB→20GB以下、1/40) | Athena User Guide: Partitioning data | ✅(比率は物語上の設定) |
| 11 | Athenaワークグループでクエリを用途別に分離し、結果の置き場(出力ロケーション)・クエリごとのスキャン上限・メトリクスを統制できる。上限超過クエリはキャンセルされる | Athena User Guide: Using workgroups to control query access and costs / Setting data usage control limits(per-query data usage control はクエリをキャンセルする) | ✅ |
| 12 | ワークグループごとのスキャン量メトリクスにCloudWatchアラームを張れる | Athena User Guide: Monitoring Athena queries with CloudWatch metrics(workgroup単位のDataScannedInBytes等) | ✅ |
| 13 | AthenaフェデレーテッドクエリはLambdaベースのデータソースコネクタ経由でRDS/Aurora・DynamoDB等へ横断SQLを実行できる | Athena User Guide: Using Amazon Athena Federated Query(prebuilt connectors: DynamoDB, JDBC/RDS等) | ✅ |
| 14 | Lake Formationはデータレイクの権限を中央管理し、データベース/テーブル/列レベル(行レベルも)の許可を一元化。Athena・Redshift Spectrum・Glue・EMR等の分析サービスがその許可の範囲でカタログを参照する | AWS Lake Formation Developer Guide: What is Lake Formation / Data filters(column-level, row-level, cell-level security)/ Working with other AWS services | ✅ |
| 15 | 列そのものを特定ロールから見せない(位置情報・顔検出列の除外) | Lake Formation Developer Guide: Data filters(column exclusion) | ✅ |
| 16 | OpenSearch Serviceは全文検索・あいまい検索・ログ分析のマネージド検索エンジン(旧Elasticsearch Service)。低レイテンシの検索窓用途 | Amazon OpenSearch Service Developer Guide: What is Amazon OpenSearch Service | ✅ |
| 17 | FirehoseはOpenSearch Serviceを配送先にできる | Amazon Data Firehose Developer Guide: Choose destination(OpenSearch Service) | ✅ |
| 18 | RDBのbtree索引は前方一致までで、中間一致・あいまい検索は構造的に不得手(db/03の書き換えは前方一致まで、の整合) | PostgreSQL docs: Index types(btreeとLIKE前方一致)/ 一般的DB設計知識 | ✅ |
| 19 | EMRはSpark/Hadoopのマネージドクラスタでフレームワークの細部制御が可能。スポットインスタンス(特に中断耐性のあるノード)でコスト削減、使い終わったら終了する運用 | Amazon EMR Management Guide: What is Amazon EMR / Cluster configuration guidelines and best practices(Spot Instances、transient cluster) | ✅ |
| 20 | 「サーバーレスで軽いETLはGlue、クラスタ制御・大規模はEMR」の使い分け | AWS Glue FAQs(When should I use AWS Glue vs Amazon EMR?) | ✅ |
| 21 | Redshift SpectrumはRedshiftクラスタからS3の外部テーブルをロードせず直接クエリし、テーブル定義に外部スキーマ(Glue Data Catalog)を使う。スキャン量ベースの課金がある | Amazon Redshift Database Developer Guide: Amazon Redshift Spectrum / Redshift pricing(Spectrum: per TB scanned) | ✅ |
| 22 | COPYはS3からRedshiftへの並列一括ロード(INSERT繰り返しより推奨)。UNLOADはクエリ結果をS3へ書き出し、Parquet形式にも対応 | Redshift Database Developer Guide: COPY / UNLOAD(FORMAT AS PARQUET)/ Best practices for loading data | ✅ |
| 23 | 事故の算術: 1回800GB弱×1日96回(15分間隔)×3日=約230TB。700GBの湖を約330回全量スキャン | 物語上の自社数値(#9のスキャン課金モデルと整合。230TB×スキャン単価≒18万円は妥当な水準) | ✅(仕様主張ではない) |
| 24 | 月2TBペースの湖の成長、オブジェクト4,100万、EMR月次4時間・8時間→70分、スポットで6割安、Redshift 2ノード、行事1回4,000枚・タグ付与3割 等 | 物語上の自社数値(仕様主張ではない) | ✅(仕様主張ではない) |
| 25 | クイズ1〜3の解答(スキャン削減3点セット、Athena/OpenSearch/Redshift+Spectrumの用途マッピング、Glue vs EMR+カタログ共有) | #7〜#12、#16、#19〜#21と同一の根拠 | ✅ |

## 物語レビュー(universe整合)

- 時系列: 3年目10月下旬〜11月中旬。S5-01の結(10月第二土曜の運動会集中日)の直後から始まり、幕間ex01(10月の月次確認)とも整合。七五三の週末で締め、S6(11月下旬開始)へ渡す。
- 真鍋メイン(S5アーク②継続): 「数えてから、流す」の型が湖に拡張。設計レビュー書式の進化系譜——S4「1日何件・何件返す」→S5-01「鮮度」列→本話「スキャン量」列——を失敗フックの学びとして接続(「聞いてへんことは、書かれへん」)。
- 戸倉の"何か"のジャブ(シーズン正典・監修者承認済み): 帳面の会の場面で「わしにしか引けん帳面やった」「思い知った日の話は、まあ、ええ」——言い切らない・聞き返さない一往復をプロット指定どおり配置。中身(引けない帳面の悔い)は説明せず、S10まで温存。入退場丁寧(ストーブの火入れ・石段・暖簾)。
- 失敗フック: Athenaスキャン課金事故(金土日3日で18万円)。誰も悪人にしない——試作申請は簡易書式で承認済み、書式に欄がなかっただけ(S4-04と同型の着地)。対策は書式(運用)+ワークグループ上限(構造)+メトリクス監視の三層で、「人の注意」に依存しない。
- S1-01接続: 城戸「請求書は嘘をつかん、て言いますけどな。湖の請求書は、正直な上に、足が速い」+美咲の「説明に6週間かけた春から3年目の秋」の回想——タイトル回収を台詞と地の文で二重化しつつ、メタ参照なし(出来事の呼び名として参照)。
- db/03宿題の回収: 「索引に乗らない前方一致」→本文で「あれは前方一致までの話」と当時の凌ぎ方を正確に踏まえ、中間一致・表記ゆれをOpenSearchへ。器の書き換えを無効化しない(役割分担として描写)。
- db/02接続: 「行の器と列の倉庫」の線引きをParquet(列指向)の説明の下敷きに使用(明示の再解説はしない)。
- 瀬名の扱い: 東京からリモートで一度も発言しない一場面のみ(db/03「今日の会議、私は一度も要らなかった」の静かな回収)。不在の理由は書かない(S8前震の継続)。
- 青柳の成長線: S5-01の「止まったら分かる」見張りに「読み過ぎたら分かる」が加わる(S8観測編への種)。誤削除・障害の当事者経験が監視の言葉で蓄積されていく描き方を維持。
- 風間: 「止める人」から「列で許せるなら残りは堂々と速くしていい」へ——S3の網(名札の季節)の再演をLake Formationの一場面で。実装詳細の羅列はしない(プロットの禁止事項遵守)。
- 棄却理由: 使い捨て抽出スクリプト(台帳なし)、JSONのままの全列読み(Parquetへ)、Firehose直Parquet変換(採らず——原本の生区画を残す二層の選択として)、Athenaで検索窓(百ミリ秒要件)、RDB索引であいまい検索(前方一致まで)、Glueで月次大物(8時間→EMR)、EMR常設(月4時間のみ)、全量Redshift投入(床が高い→Spectrum)、毎朝の定型をAthenaで(タクシーの比喩)、バケットポリシー継ぎ接ぎ(監査で破れる→Lake Formation)。
- 禁止事項遵守: QuickSuite/AI系の先取りなし(狩野の橋は「読ませたいの」の要望止まり)、Kinesis再解説なし(参照のみ)、Lake Formationは思想+列マスク一例まで、帳面の会は短く・技術判断は神戸側で完結。AZ・災害の扱いなし。
- 話法: 真鍋=標準語寄り+柔らかい関西、青柳・狩野・風間・瀬名=標準語、城戸=丁寧で乾いた関西、矢吹=関西弁(倉庫・工房の比喩)、戸倉=ゆっくりした大阪弁、美咲の関西語彙は「あかんて」1箇所(規約1〜3箇所内)。
- 間の点検: 各場面に用のない一文(洗い忘れの湯呑み、蜜柑、薬缶、加湿器、港の灯)、台詞の前後の手の動き(湯呑みの底、電卓のキャップ、菓子折、指の節)、無駄口1箇所(Parquet=寄木張りの床)。
- 用語コラム15語=front matterと一致、term_idは本文に不使用。本文約7,200字(空白除く)——プロットの許容上限(7,000)を僅かに超えるが、writing-guide本文ルール5(字数上限なし・分量欄は下限の目安)に基づき、間の増補分として監修判断で許容。具体値は月+2.1TB/4,100万オブジェクト/7.8TB→700GB/2日半→4分/15分おき96回/3日230TB・18万円/330回/10GB上限/1/40・20GB/2,400万件・8時間→70分・スポット6割/2ノード/4,000枚・3割ほか、規約の最低5つを大きく超える。
