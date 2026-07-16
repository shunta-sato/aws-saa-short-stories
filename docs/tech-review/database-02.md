# 技術レビュー: stories/database_architecture/02_六つの写し一つの器

本文・用語コラム・クイズ中の技術的主張をAWS公式ドキュメントと照合した結果。判定は ✅(正確)/⚠️(注意付きで正確)/❌(要修正)。

レビュー実施日: 2026-07-16。照合先は各行の出典(AWS公式ドキュメント)。

| # | 本文中の主張 | 出典 | 判定 |
|---|---|---|---|
| 1 | AuroraはMySQL/PostgreSQL互換で、アプリ側はドライバ・SQLを原則そのまま使える | Aurora User Guide: What is Amazon Aurora(drop-in compatibility) | ✅ |
| 2 | クラスターボリュームは3AZ×2=6コピーの共有分散ストレージ | Aurora User Guide: Aurora storage and reliability(six copies across three AZs) | ✅ |
| 3 | 2コピー喪失で書き込み継続、3コピー喪失でも読み取り可 | Aurora User Guide / Aurora FAQs(write availability with 2 copies lost, read with 3) | ✅ |
| 4 | ストレージは10GB刻みで最大128TiBまで自動拡張 | Aurora User Guide: cluster volume(10GiB増分、最大128TiB。エンジン版により上限差あり) | ✅ |
| 5 | Auroraレプリカは同一クラスターボリュームを読み、最大15台 | Aurora User Guide: Replication with Amazon Aurora(up to 15 Aurora Replicas) | ✅ |
| 6 | Auroraレプリカの遅延は通常10〜20ミリ秒級 | Aurora FAQs「typically less than 100 ms」/ User Guide(usually much less than 100 ms; 10ms台の記述はre:Invent資料等)。本文は「実測で10〜20ミリ秒級」と実測値として描写 | ⚠️ 公式の保証値は「通常100ms未満」。物語中は自社実測として提示しており矛盾はないが、コラムも「級」表記で断定を避けた |
| 7 | フェイルオーバーはレプリカ昇格で通常30秒前後 | Aurora User Guide: Failover(typically less than 30 seconds / within 30 seconds) | ✅ |
| 8 | 書き込みインスタンスはクラスターに1台(単一ライター)で、レプリケーション負荷をストレージ層が担う | Aurora User Guide(single-master構成。ログベースのストレージ複製) | ✅ |
| 9 | ライター=クラスターエンドポイント、リーダーエンドポイントは読み取りを負荷分散し、フェイルオーバー後も自動で付け替わる | Aurora User Guide: Amazon Aurora connection management(cluster/reader/custom endpoints) | ✅ |
| 10 | リーダーの分散はDNSベースで、接続を長く使い回すと偏る。カスタムエンドポイントの存在 | Aurora User Guide: connection management(DNSラウンドロビン、custom endpoints) | ✅ |
| 11 | 標準RDSリードレプリカは非同期・各自ストレージ全量保持で、レプリカ3台なら保存費は本体込みで4倍 | RDS User Guide: read replicas(独立したDBインスタンスとしてストレージを持つ) | ✅ |
| 12 | Aurora Serverless v2はACU単位・0.5刻みで秒単位にスケール、最小/最大ACUを設定、使用分課金 | Aurora User Guide: Aurora Serverless v2(0.5 ACU増分、秒単位スケーリング) | ✅ |
| 13 | 最小ACU分は無負荷でも課金される | Aurora User Guide / Pricing(最小容量分の課金。※2024年以降の自動一時停止(0 ACU)は特定バージョン限定のため、SAA水準では「最小分は課金」で扱う) | ⚠️ 注記の通り簡略化(用語集準拠) |
| 14 | 定常高負荷はプロビジョンドが単価で有利 | Aurora User Guide: Serverless v2 use cases / Pricing比較 | ✅ |
| 15 | Aurora Global Databaseはストレージ層のレプリケーションで遅延は通常1秒未満、本体性能への影響が小さい | Aurora User Guide: Global databases(dedicated infrastructure、typical latency < 1 second、low performance impact) | ✅ |
| 16 | 災害時は二次リージョンを昇格。昇格そのものは1分未満(目標)、切替全体は数分の訓練目標 | Aurora User Guide: Global databases(promote a secondary region in less than 1 minute / RTO目標は運用値として描写) | ✅ |
| 17 | Redshiftは列指向のDWHで、OLTP(行単位の読み書き)はRDS/Aurora、集計・BI・定期レポートはRedshift | Redshift documentation(columnar storage、DWHユースケース) | ✅ |
| 18 | DocumentDBはMongoDB互換のドキュメントDB | DocumentDB documentation(MongoDB compatibility) | ✅ |
| 19 | Neptuneは頂点と辺の関係探索に特化したグラフDB | Neptune documentation(graph database、SPARQL/Gremlin/openCypher) | ✅ |
| 20 | KeyspacesはApache Cassandra互換のマネージドワイドカラムDBで、クライアント互換のままクラスター運用を畳める | Keyspaces documentation(Cassandra-compatible、serverless) | ✅ |
| 21 | 切替時の停止を伴う移行(告知の上、窓を取って実施)という運用描写 | 一般的な移行プラクティス(物語上の運用判断) | ✅(仕様主張ではない) |
| 22 | フェイルオーバー後、旧ライターへの直書き接続は読み取り専用エラーになる | Aurora User Guide: Failover(旧writerはreaderとして再起動される) | ✅ |

## 物語レビュー(universe整合)

- 時系列: 3年目5月下旬〜6月、db/01の1か月半後。梅雨入り前の神戸。瀬名は書面参加(東京)——理由は描かず、S4アーク「数日単位の不在」に従う。
- メタデータDB=PostgreSQL(storage/02正典)に合わせ、プロットの「同じMySQLの顔」を「同じPostgreSQLの顔」に調整(Aurora PostgreSQL互換)。
- 失敗フック: 旧ホスト名直書きの月次バッチが昇格後に迷子(読み取り専用エラー)。書いたのが3年前の真鍋自身と判明する構図で誰も悪人にしない(「人のしくじりやと思って調べてたら、3年前の自分でした」)。S2「名前の見つけ方」の記憶と接続。
- 器の品評会: 採用1(Keyspaces)・棄却2(DocumentDB、Redshiftは先送り+線引き)・PoC 1(Neptune)。各棄却に理由あり。矢吹の「全部Standardに置いたあの春と同じや」でS1-01と接続。
- 狩野の成長描写(「止めないでください」の頃からの変化)は universe.md の成長アークに一致。
- 問いの継承: 美咲が「瀬名さんなら何を訊くか」を先回りして資料に書き、瀬名の書面コメントと一致する構図(試問口調なし、書面3行)。
- 真鍋の口癖「数えました」、青柳の素朴な質問(単一ライターの正直な扱い)、城戸の単価の言葉——全員 universe.md の話法に一致。方言濃度は規約内。
- 禁止事項遵守: DynamoDB設計論なし、Redshift本格解説なし(S5予告のみ)、Backtrackの名前も出さない(幕間ex02担当)、「Auroraは常にRDSより上」と言わない(エンジン・コスト棄却の余地を城戸の線引きで担保)。
- 結末の「検証1万件の泣きどころ」はdb/03への橋(先取りせず予感のみ)。
- 具体値: 保存費4倍、フェイルオーバー実測2分50秒→30秒前後、書き込み2.6倍、6コピー(3AZ×2)、10GB刻み・最大128TiB、レプリカ最大15台、遅延10〜20ms級、ACU 0.5刻み、検証稼働は日中の3割・夜間ゼロ、Global Database遅延1秒未満、直書き3本(1+2)、訓練7月18日 — 規約の最低5つを満たす。
- 本文5,570字(空白除く)、担当11語全登場、term_id漏れなし。
