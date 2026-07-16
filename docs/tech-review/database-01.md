# 技術レビュー: stories/database_architecture/01_行列は窓口で分ける

本文・用語コラム・クイズ中の技術的主張をAWS公式ドキュメントと照合した結果。判定は ✅(正確)/⚠️(注意付きで正確)/❌(要修正)。

レビュー実施日: 2026-07-16。照合先は各行の出典(AWS公式ドキュメント)。

| # | 本文中の主張 | 出典 | 判定 |
|---|---|---|---|
| 1 | RDSはリレーショナルDB(OLTP)のマネージドサービスで、パッチ・バックアップ・フェイルオーバーを任せられる | RDS User Guide: Welcome(マネージドリレーショナルDB、運用タスクの自動化) | ✅ |
| 2 | Multi-AZ配置は同期スタンバイへの自動フェイルオーバーで可用性を守り、スタンバイは読み取りに使えない | RDS User Guide: Multi-AZ deployments「the standby replica doesn't serve read traffic」 | ✅ |
| 3 | Multi-AZ DBクラスターはライター1台+読み取り可能なスタンバイ2台を3つのAZに配置し、従来型Multi-AZより高速なフェイルオーバー | RDS User Guide: Multi-AZ DB clusters(1 writer + 2 readable standby、3AZ、typically under 35 seconds failover) | ✅ |
| 4 | Multi-AZ DBクラスターの対応エンジンはMySQL/PostgreSQLに限られる(コラム) | RDS User Guide: Multi-AZ DB clusters — Supported engines(RDS for MySQL / RDS for PostgreSQL) | ✅ |
| 5 | リードレプリカは非同期レプリケーションで、読み取りスケールが目的。可用性の道具ではない | RDS User Guide: Working with read replicas(asynchronous replication、read-heavy workloads) | ✅ |
| 6 | レプリカ遅延は仕様であり、最新必須の読みはプライマリへ向ける(遅延は数百ms〜秒単位まで変動し得る) | RDS User Guide: read replicas(ReplicaLagメトリクス。遅延はワークロード依存) | ✅ |
| 7 | リードレプリカ作成にはソースの自動バックアップ有効化が前提(コラム) | RDS User Guide: read replicas prerequisites「enable automatic backups on the source DB instance」 | ✅ |
| 8 | レプリカの昇格は不可逆で、昇格後はレプリケーションが停止し独立インスタンスになる | RDS User Guide: Promoting a read replica(promotion後はスタンドアロン、レプリケーション停止、逆戻り不可) | ✅ |
| 9 | クロスリージョンリードレプリカは非同期で、リージョンDR(昇格)と遠隔読みに使う。非同期遅延分のデータ損失(RPO>0)があり得る | RDS User Guide: Cross-Region read replicas(async、DR用途、遅延の存在) | ✅ |
| 10 | RDS Proxyは接続プールでLambda等の接続急増を吸収し、フェイルオーバー時間を短縮する。クエリキャッシュではない | RDS Proxy documentation(connection pooling、failover時間を最大66%短縮、serverless/Lambdaユースケース) | ✅ |
| 11 | PostgreSQLの接続数上限(物語中1,000)はインスタンス構成に依存する値として描写 | RDS User Guide: max_connections(インスタンスメモリから算出されるパラメータ。固定値ではない) | ✅(物語上の具体値) |
| 12 | 自動バックアップは日次スナップショット+トランザクションログで、保持期間は最大35日 | RDS User Guide: Working with backups(retention period 0–35 days) | ✅ |
| 13 | 自動バックアップは既定ではインスタンス削除時に削除される(「一緒に消えるんが既定や」) | RDS User Guide: Deleting a DB instance(retain automated backupsを選ばなければ削除。既定挙動として正確) | ✅ |
| 14 | 手動スナップショットは無期限保持で、明示的に削除するまで残り、コピー・共有ができる | RDS User Guide: Creating a DB snapshot(kept until you delete them、copy/share対応) | ✅ |
| 15 | 暗号化スナップショットの共有にはカスタマーマネージドKMSキーの共有も必要(コラム) | RDS User Guide: Sharing a DB snapshot(default KMSキーの暗号化スナップショットは共有不可、CMKのキーポリシー共有が必要) | ✅ |
| 16 | PITRは保持期間内の任意の秒へ復元できるが、必ず新しいDBインスタンスとして作成される | RDS User Guide: Restoring to a point in time「creates a new DB instance」 | ✅ |
| 17 | PITRで復元できるのは直近およそ5分より前まで(latest restorable time) | RDS User Guide: latest restorable time「typically within 5 minutes of the current time」 | ✅ |
| 18 | ストレージオートスケーリングは空き容量がしきい値(割り当ての10%)を下回ると自動拡張し、縮小はできない | RDS User Guide: autoscaling(free space < 10% for ≥5 minutes で拡張。縮小非対応) | ✅ |
| 19 | 拡張後は次の拡張までクールダウン(6時間程度)がある(コラム) | RDS User Guide: autoscaling(6時間のクールダウン) | ✅ |
| 20 | ElastiCacheはRedis/Valkey互換またはMemcached互換のインメモリキャッシュで、DB手前の高頻度読みに使う | ElastiCache User Guide: What is ElastiCache(Valkey/Redis OSS/Memcached対応) | ✅ |
| 21 | Redisは永続化・レプリケーション・自動フェイルオーバー・データ構造(ソート済みセット)・Pub/Subを持ち、Memcachedはマルチスレッドで単純キャッシュ特化。Memcachedにはレプリケーション・バックアップがない | ElastiCache User Guide: Comparing Valkey, Memcached, and Redis OSS(機能比較表) | ✅ |
| 22 | ランキング用途にRedisのソート済みセットが適する | ElastiCache User Guide / Redis documentation(sorted setsのリーダーボードユースケース) | ✅ |
| 23 | クラスターモードはデータを複数シャードに分割して書き込み・容量を水平スケール。無効時は単一シャード(プライマリ+レプリカ)に全データが収まる必要がある | ElastiCache User Guide: Replication: Redis OSS (Cluster Mode Disabled) vs (Cluster Mode Enabled) | ✅ |
| 24 | 後からのクラスターモード切替は「作り直しの工事」(初期選択が重要) | 用語集YAML(モード切替は再構築を伴う)/ElastiCache User Guide | ⚠️ 新しめのRedis OSSエンジン(5.0.6以降)ではオンライン移行が提供されるが、SAA-C03の出題水準および用語集の記述(初期の規模見込みで選ぶ)に合わせた簡略化。本文は「大工事になるから見込みと一緒に台帳へ」という運用判断として描写しており誤りではない |
| 25 | 遅延読み込み(lazy loading)はキャッシュミス時にDBから読んで格納。必要なデータのみ保持・初回遅延・古いデータの可能性 | ElastiCache User Guide: Caching strategies — Lazy loading(advantages/disadvantages) | ✅ |
| 26 | 書き込み時更新(write-through)はDB書き込みと同時にキャッシュ更新。常に最新・書き込みコスト増・未読データの容量消費 | ElastiCache User Guide: Caching strategies — Write-through | ✅ |
| 27 | 両戦略でTTLを併用し、古いデータの滞留・未読データの住み着き・DB直接更新とのずれを期限切れで解消する | ElastiCache User Guide: Caching strategies — Adding TTL(両戦略の欠点緩和としてTTLを推奨) | ✅ |
| 28 | 「キャッシュはDBより安い読み窓口」(同一クエリの反復をDBで受けるよりキャッシュが単価で有利) | ElastiCache FAQs / Well-Architected: パフォーマンス効率(キャッシュによるDB負荷・コスト削減) | ✅(定性的主張として) |

## 物語レビュー(universe整合)

- 真鍋一花の神戸初出社(3年目春・4月)は universe.md「S4から神戸へ合流」と一致。口癖「で、1日何件です?」使用。net/02カメオ(注文データを数えた8分)との矛盾なし。
- メタデータDBがPostgreSQLである点は storage/02(EC2自前PostgreSQL)と接続。「2年前にEC2の自前運用から移して」はS1年表(1年目にRDS化、storage/06でMulti-AZフェイルオーバー実績)と整合。
- 青柳の「あの水曜日」は storage/06 の本番障害(Multi-AZ自動フェイルオーバー、断は数十秒〜数分)への正しい参照。
- 瀬名の「月・金だけ神戸」はS4アーク「東京との行き来が増える(理由は説明しない)」に従い、理由を一切描写していない。S3-05末尾(父の入院)との継続性あり。
- 方言濃度: 美咲の関西語彙は感情が動いた場面の2箇所(「一生もんです」「せやから〜」)。矢吹は関西弁のまま比喩(帳面・テープ)。瀬名は標準語のみ。規約の範囲内。
- 試問口調なし(矢吹は問わず語り、真鍋が聞く側。青柳はMemcachedの棄却理由とレプリカ遅延の原因に自力で辿り着く)。メタ参照なし。
- 失敗フック: 枚数カウンタのレプリカ読みによる「0枚」表示(苦情3件)。誰も悪人にせず、真鍋と美咲が責任を分け合う構図。
- Aurora本体の解説なし(名前出しのみ・db/02の領分を守る)。DynamoDBの設計論なし(db/04の領分)。
- 具体値: 読み書き比9:1、読み平常比9倍、接続数947/1,000、レプリカ2台、レプリカ遅延数百ms→最大8秒、苦情3件、DB時間の4割、1日約90万回、TTL 300秒、保持最大35日、直近5分より前、空き1割のしきい値 — 規約の最低5つを満たす。
