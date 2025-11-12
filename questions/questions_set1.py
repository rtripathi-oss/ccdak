questions_set1 = [
    {
        "question": "Assuming a Kafka topic is configured with the following settings:\n- log.segment.bytes = 1073741824 (1GB)\n- log.retention.ms = 86400000 (1 day)\n- log.retention.bytes = -1\n\nWhich of the following statements accurately describes the log retention policy for this Kafka topic?",
        "options": [
            "Logs are retained based on size; once the log size exceeds 1GB, older segments are deleted.",
            "Logs are retained for exactly one day, regardless of the size of the log.",
            "Logs are retained until the size of the log exceeds 1GB or for one day, whichever comes first.",
            "Logs are retained indefinitely, as log.retention.bytes is set to -1, overriding other retention configurations."
        ],
        "answer": "Logs are retained for exactly one day, regardless of the size of the log.",
        "explanation": "log.retention.ms=86400000 (1 day) enforces time-based retention. log.retention.bytes=-1 disables size-based retention, so logs are deleted after one day."
    },
    {
        "question": "A Kafka topic is configured with cleanup.policy='compact,delete', min.cleanable.dirty.ratio=0.5, delete.retention.ms=86400000 (1 day), and segment.ms=43200000 (12 hours). Which statement correctly describes the behavior?",
        "options": [
            "Log compaction and deletion are mutually exclusive; only one policy can be active at any time.",
            "Log compaction will occur once 50% of the segment data is marked as dirty, and logs older than 1 day will be deleted.",
            "Deleted records are removed immediately from the log; delete.retention.ms specifies the retention time for all records.",
            "segment.ms dictates the maximum lifespan of any record in the log, after which it is eligible for compaction or deletion."
        ],
        "answer": "Log compaction will occur once 50% of the segment data is marked as dirty, and logs older than 1 day will be deleted.",
        "explanation": "Both compaction and deletion policies apply. Compaction occurs when 50% of records are dirty, and delete.retention.ms=1 day controls how long deleted records stay before removal."
    },
    {
        "question": "In a Kafka cluster, the Controller is a critical component. Which of the following statements accurately describe the Controller? (Select two)",
        "options": [
            "Elected by broker majority.",
            "Elected by Zookeeper ensemble.",
            "Responsible for partition leader election.",
            "Manages consumer group offsets.",
            "Automatically assigns replicas to brokers based on load."
        ],
        "answer": ["Elected by Zookeeper ensemble.", "Responsible for partition leader election."],
        "explanation": "The Controller is elected by Zookeeper and handles partition leader elections. It doesn’t manage offsets or balance replicas automatically."
    },
    {
        "question": "If the Controller broker goes down in a Kafka cluster, how is a new Controller elected?",
        "options": [
            "By broker majority voting.",
            "By the Zookeeper ensemble based on ephemeral node sequence.",
            "By Kafka clients that detect failure first.",
            "By random broker selection."
        ],
        "answer": "By the Zookeeper ensemble based on ephemeral node sequence.",
        "explanation": "Each broker registers an ephemeral node in Zookeeper. When the current Controller’s node disappears, Zookeeper triggers re-election; the next broker in sequence becomes the new Controller."
    },
    {
        "question": "A Kafka producer uses acks=all with replication factor=3 and min.insync.replicas=2. If both replicas go offline, what happens?",
        "options": [
            "The producer will still publish messages but with possible data loss.",
            "The producer will temporarily be unable to publish messages until a replica comes online.",
            "The producer continues publishing without impact.",
            "The producer switches to another topic’s partition automatically."
        ],
        "answer": "The producer will temporarily be unable to publish messages until a replica comes online.",
        "explanation": "acks=all requires acknowledgments from all in-sync replicas. With both replicas offline, the producer can’t receive the required ACKs and fails to publish until one replica returns."
    },
    {
        "question": "When a Kafka broker starts, which of the following does NOT occur?",
        "options": [
            "Registering itself with Zookeeper.",
            "Loading replica assignments for partitions it hosts.",
            "Creating a new Zookeeper znode for each topic it hosts.",
            "Initializing log directories for partitions it hosts."
        ],
        "answer": "Creating a new Zookeeper znode for each topic it hosts.",
        "explanation": "Topic znodes are created when topics are created, not during broker startup. Brokers only register themselves and initialize their partitions."
    },
    {
        "question": "How does the Kafka Controller ensure partition leadership is evenly distributed among brokers?",
        "options": [
            "By periodically triggering rebalances.",
            "By assigning leaders to the least-loaded brokers.",
            "By using a round-robin algorithm.",
            "It does not actively manage leadership distribution."
        ],
        "answer": "It does not actively manage leadership distribution.",
        "explanation": "The Controller elects leaders based on ISR order but does not balance leadership load automatically. Distribution depends on replica assignment."
    },
    {
        "question": "In a 5-broker Kafka cluster with a topic of 10 partitions (replication factor=3), a network partition splits brokers into Group A (2) and Group B (3). Both groups can reach Zookeeper. What happens?",
        "options": [
            "Partitions with leaders in Group A continue normally, others go offline.",
            "Partitions with leaders in Group B continue, Group A’s leaders are re-elected in Group B.",
            "All partitions go offline until network is restored.",
            "Behavior is non-deterministic and depends on Controller location."
        ],
        "answer": "Partitions with leaders in Group B continue, Group A’s leaders are re-elected in Group B.",
        "explanation": "Group B has the majority (3/5) and can maintain quorum with Zookeeper, so its leaders continue. Group A brokers lose leadership until reconnected."
    },
    {
        "question": "A Kafka broker is configured with num.io.threads=8, num.network.threads=4, num.replica.fetchers=2. What do these control?",
        "options": [
            "Disk I/O, network I/O, and replica fetching from leader respectively.",
            "Network I/O, disk I/O, and replica fetching from leader respectively.",
            "Disk I/O, network I/O, and replication to followers respectively.",
            "Replication to followers, disk I/O, and network I/O respectively."
        ],
        "answer": "Disk I/O, network I/O, and replica fetching from leader respectively.",
        "explanation": "num.io.threads handles disk I/O, num.network.threads handles network connections, and num.replica.fetchers controls follower fetch threads."
    },
    {
        "question": "A Kafka broker is configured with:\n- log.segment.bytes=1073741824\n- log.segment.ms=86400000\n- log.retention.bytes=-1\n- log.retention.ms=604800000\n\nWhen will a new segment start, and how long are old segments retained?",
        "options": [
            "New segment after 1GB or 24 hours, whichever first; old segments kept for 7 days.",
            "New segment after 1GB or 24 hours; old segments retained indefinitely.",
            "New segment after 1GB; old segments kept 7 days or until total >1GB.",
            "New segment every 24 hours; old segments kept 7 days or until total >1GB."
        ],
        "answer": "New segment after 1GB or 24 hours, whichever first; old segments kept for 7 days.",
        "explanation": "log.segment.bytes=1GB and log.segment.ms=1 day trigger new segments; log.retention.ms=7 days deletes older segments, while log.retention.bytes=-1 disables size-based deletion."
    },
    {
        "question": "A Kafka cluster is configured with the following settings:\n- default.replication.factor=2\n- min.insync.replicas=2\n\nWhat is the minimum number of brokers required in the cluster to ensure that the cluster can tolerate at least one broker failure without losing the ability to serve write requests?",
        "options": ["1", "2", "3", "4"],
        "answer": "3",
        "explanation": "With min.insync.replicas=2, Kafka requires two in-sync replicas to acknowledge writes. To tolerate one broker failure and still meet this requirement, at least 3 brokers are needed — so two remain available if one fails."
    },
    {
        "question": "A Kafka cluster has the following configuration:\n- num.partitions=6\n- default.replication.factor=3\n\nHow many replicas will be created in total across all brokers for a newly created topic that uses the default settings?",
        "options": ["6", "9", "12", "18"],
        "answer": "18",
        "explanation": "Each of the 6 partitions has 3 replicas (1 leader + 2 followers). Total replicas = 6 × 3 = 18."
    },
    {
        "question": "A Kafka cluster has the following configuration:\n- unclean.leader.election.enable=false\n\nWhat is the implication of this setting when a partition leader fails and there are no in-sync replicas (ISRs) available?",
        "options": [
            "The partition will remain unavailable until the failed leader recovers.",
            "The partition will elect a new leader from the out-of-sync replicas to maintain availability.",
            "The partition will automatically create a new replica to replace the failed leader.",
            "The partition will be reassigned to another broker in the cluster."
        ],
        "answer": "The partition will remain unavailable until the failed leader recovers.",
        "explanation": "When unclean.leader.election.enable=false, Kafka prioritizes consistency over availability. If no ISR is available, the partition becomes unavailable until the original leader or an ISR recovers."
    },
    {
        "question": "A Kafka broker is configured with the following settings:\n- num.replication.fetchers=4\n- replica.fetch.max.bytes=1048576\n\nWhat is the maximum amount of data that can be fetched by the broker for replication purposes in a single request?",
        "options": ["1 MB", "4 MB", "1048576 bytes", "4194304 bytes"],
        "answer": "1 MB",
        "explanation": "replica.fetch.max.bytes=1048576 means each fetcher thread can fetch up to 1 MB in a single request. num.replication.fetchers=4 defines the number of threads, not the total fetch size per request."
    },
    {
        "question": "A Kafka cluster is configured with the following settings:\n- log.retention.hours=48\n- log.retention.bytes=1073741824\n- log.segment.bytes=536870912\n\nAssuming a topic has a constant message production rate, which of the following factors will trigger a log segment to be eligible for deletion?",
        "options": [
            "The log segment is older than 48 hours.",
            "The log segment size exceeds 536870912 bytes (512 MB).",
            "The total size of all log segments for the topic exceeds 1073741824 bytes (1 GB).",
            "All of the above."
        ],
        "answer": "All of the above.",
        "explanation": "Kafka deletes segments based on time or size thresholds. If a segment exceeds retention time (48 hours), the per-segment size (512MB), or total log size (1GB), it becomes eligible for deletion."
    },
    {
        "question": "A client connects to a broker in a Kafka cluster and sends a produce request for a topic partition. The broker responds with a 'Not Enough Replicas' error. What does the client do next?",
        "options": [
            "Retries sending the produce request to the same broker",
            "Sends metadata request to the same broker to refresh its metadata",
            "Sends produce request to the controller broker",
            "Sends metadata request to the Zookeeper to find the controller broker"
        ],
        "answer": "Sends metadata request to the same broker to refresh its metadata",
        "explanation": "A 'Not Enough Replicas' error indicates that the broker doesn’t have sufficient in-sync replicas. The client responds by refreshing metadata from the broker to update cluster and partition information."
    },
    {
        "question": "A Kafka consumer is consuming from a topic partition. It sends a fetch request to the broker and receives a 'Replica Not Available' error. What is the consumer's next action?",
        "options": [
            "Backs off and retries the fetch request after a short delay",
            "Sends an offset commit request to trigger partition rebalancing",
            "Sends a metadata request to refresh its view of the cluster",
            "Closes the connection and tries connecting to a different broker"
        ],
        "answer": "Sends a metadata request to refresh its view of the cluster",
        "explanation": "The consumer updates its metadata when it receives 'Replica Not Available', as this error means its cluster view is stale. It re-fetches metadata to locate the correct leader broker."
    },
    {
        "question": "What happens if you produce to a topic that does not exist, and the broker setting auto.create.topics.enable is set to false?",
        "options": [
            "The broker will create the topic with default configurations",
            "The broker will reject the produce request and the producer will throw an exception",
            "The producer will automatically create the topic",
            "The producer will wait until the topic is created"
        ],
        "answer": "The broker will reject the produce request and the producer will throw an exception",
        "explanation": "With auto.create.topics.enable=false, Kafka does not auto-create topics. The broker rejects the produce request, and the producer throws a TopicExistsException."
    },
    {
        "question": "What is the default value of auto.create.topics.enable in Kafka?",
        "options": ["true", "false", "It is not set by default", "It depends on the Kafka version"],
        "answer": "true",
        "explanation": "By default, Kafka sets auto.create.topics.enable=true, meaning that a topic is automatically created when a producer or consumer interacts with a non-existent topic."
    },
    {
        "question": "When a topic is automatically created due to auto.create.topics.enable being true, what configurations are used for the new topic?",
        "options": [
            "The configurations specified by the producer or consumer",
            "The default configurations set on the broker",
            "A combination of producer/consumer configurations and broker defaults",
            "No configurations are set, the topic is created with empty configuration"
        ],
        "answer": "The default configurations set on the broker",
        "explanation": "Kafka auto-creates topics using the broker’s default topic configurations: num.partitions and default.replication.factor. Producer or consumer configs are not used for topic creation."
    },
    {
        "question": "Can Kafka's zero-copy optimization be used in combination with compression?",
        "options": [
            "Yes, zero-copy and compression can be used together seamlessly.",
            "No, zero-copy is incompatible with compression and cannot be used together.",
            "Zero-copy can be used with compression, but it requires additional configuration.",
            "Zero-copy is automatically disabled when compression is enabled."
        ],
        "answer": "Yes, zero-copy and compression can be used together seamlessly.",
        "explanation": (
            "Kafka's zero-copy optimization can be used in combination with compression seamlessly. "
            "Zero-copy operates on the compressed data directly without decompression, while compression "
            "reduces data size before transfer — both can work together efficiently."
        )
    },
    {
        "question": "What is the relationship between `replication.factor` and `min.insync.replicas`?",
        "options": [
            "`min.insync.replicas` must be less than or equal to the `replication.factor`",
            "`min.insync.replicas` must be greater than the `replication.factor`",
            "`min.insync.replicas` and `replication.factor` are independent settings",
            "`min.insync.replicas` must be equal to the `replication.factor`"
        ],
        "answer": "`min.insync.replicas` must be less than or equal to the `replication.factor`",
        "explanation": (
            "`min.insync.replicas` defines the minimum number of replicas that must acknowledge a write. "
            "It cannot be greater than the replication factor; otherwise, no write can succeed."
        )
    },
    {
        "question": "What happens when a producer sends a message with `acks=all` but not enough replicas are in sync?",
        "options": [
            "The producer will receive an acknowledgment and the write will succeed",
            "The producer will receive an error indicating insufficient in-sync replicas",
            "The producer will wait indefinitely for replicas to sync",
            "The producer ignores `min.insync.replicas` and writes successfully"
        ],
        "answer": "The producer will receive an error indicating insufficient in-sync replicas",
        "explanation": (
            "With `acks=all`, Kafka requires acknowledgments from all in-sync replicas. "
            "If the number of in-sync replicas is less than `min.insync.replicas`, the write fails."
        )
    },
    {
        "question": "What happens if you set both `log.retention.ms` and `log.retention.minutes`?",
        "options": [
            "The larger unit (minutes) takes precedence",
            "The smaller unit (milliseconds) takes precedence",
            "Kafka uses an average of both",
            "It causes a configuration error"
        ],
        "answer": "The smaller unit (milliseconds) takes precedence",
        "explanation": (
            "Kafka follows unit-based precedence: ms > minutes > hours. "
            "So `log.retention.ms` overrides `log.retention.minutes` or `log.retention.hours`."
        )
    },
    {
        "question": "How can you set a retention period of 2 weeks for a specific topic?",
        "options": [
            "Set `retention.ms=1209600000` in the topic configuration",
            "Set `log.retention.hours=336` in the broker configuration",
            "Set `log.retention.ms=1209600000` in the broker configuration",
            "Set `retention.ms=1209600000` in the broker configuration"
        ],
        "answer": "Set `retention.ms=1209600000` in the topic configuration",
        "explanation": (
            "For a specific topic, `retention.ms` must be configured in the topic settings. "
            "1209600000 ms equals 2 weeks."
        )
    },
    {
        "question": "Which of the following is stored in the Kafka `__consumer_offsets` topic? (Select two)",
        "options": [
            "The latest committed offset for each consumer group",
            "The list of consumers in each consumer group",
            "The mapping of partitions to consumer groups",
            "The last produced message for each topic partition",
            "The earliest committed offset for each consumer group"
        ],
        "answer": ["The latest committed offset for each consumer group", "The mapping of partitions to consumer groups"],
        "explanation": (
            "The `__consumer_offsets` topic stores:\n\n"
            "- The latest committed offset for each consumer group (A)\n"
            "- The mapping of partitions to consumer groups (C)\n\n"
            "Other data like consumer lists or messages are not stored here."
        ),
        "multiple": True
    },
    {
        "question": "There are two consumers C1 and C2 belonging to the same group G subscribed to topics T1, T2, and T3. Each topic has 4 partitions. Assuming all partitions have data, how many partitions will each consumer be assigned with the Range Assignor?",
        "options": [
            "C1: 6 partitions, C2: 6 partitions",
            "C1: 4 partitions, C2: 8 partitions",
            "C1: 2 partitions from each topic, C2: 2 partitions from each topic",
            "C1: 1 partition from each topic, C2: 3 partitions from each topic"
        ],
        "answer": ["C1: 6 partitions, C2: 6 partitions"],
        "explanation": "With the Range Assignor, each consumer will be assigned a contiguous range of partitions from each topic. Each gets 2 partitions from each topic, totaling 6 each.",
    },
    {
        "question": "With the Round Robin Assignor, which consumer(s) will be assigned partition 2 from topic T1 (C1, C2, C3, C4 consuming T1 with 3 partitions and T2 with 2 partitions)?",
        "options": ["C1", "C2", "C3", "C4"],
        "answer": "C",
        "explanation": (
            "The Round Robin Assignor assigns partitions sequentially. "
            "C3 gets T1-2, so partition 2 of T1 is assigned to C3."
        ),
    },
    {
        "question": "There are three consumers C1, C2, C3 in group G consuming topic T with 10 partitions. Using the Sticky Assignor, if C1 leaves, how will partitions be rebalanced?",
        "options": [
            "All partitions will be reassigned evenly among C2 and C3",
            "C2 and C3 will retain existing partitions, and C1's will be reassigned",
            "All partitions will be reassigned randomly",
            "Partitions from C1 will not be reassigned"
        ],
        "answer": "C2 and C3 will retain existing partitions, and C1's will be reassigned",
        "explanation": (
            "The Sticky Assignor minimizes partition movement, so C2 and C3 keep their partitions, "
            "and only C1’s partitions are reassigned."
        ),
    },
    {
        "question": "A Kafka Streams app receives 'Offset Out Of Range' error. How should it handle this?",
        "options": [
            "Reset to the earliest offset and retry",
            "Reset to the latest offset and retry",
            "Shut down the application",
            "Ignore and continue"
        ],
        "answer": "Reset to the earliest offset and retry",
        "explanation": (
            "The correct way is to reset the offset to the earliest available and retry. "
            "The error means the app tried to read from a deleted offset."
        ),
    },
    {
        "question": "You are consuming JSON messages from a Kafka topic. Which consumer property should you set?",
        "options": [
            "key.deserializer=JsonDeserializer",
            "value.deserializer=JsonDeserializer",
            "key.deserializer=StringDeserializer",
            "value.deserializer=StringDeserializer"
        ],
        "answer": "value.deserializer=JsonDeserializer",
        "explanation": (
            "Since the values are JSON, you must set `value.deserializer=JsonDeserializer`."
        ),
    },
    {
        "question": "A consumer wants to read messages from a specific partition. Which method should be used?",
        "options": [
            "KafkaConsumer.subscribe(String topic, int partition)",
            "KafkaConsumer.assign(Collection<TopicPartition> partitions)",
            "KafkaConsumer.subscribe(Collection<TopicPartition> partitions)",
            "KafkaConsumer.assign(String topic, int partition)"
        ],
        "answer": "KafkaConsumer.assign(Collection<TopicPartition> partitions)",
        "explanation": (
            "Use `assign()` to directly specify the partitions a consumer should read from."
        ),
    },
    {
        "question": "What happens when a consumer is assigned a non-existent partition?",
        "options": [
            "It ignores it and continues",
            "It throws an exception and stops",
            "It creates the partition automatically",
            "It waits for the partition to be created"
        ],
        "answer": "It throws an exception and stops",
        "explanation": (
            "Kafka will throw `UnknownTopicOrPartitionException` when a partition doesn’t exist."
        ),
    },
    {
        "question": "Can a consumer dynamically change its partitions without restarting?",
        "options": [
            "Yes, with subscribe()",
            "Yes, with assign()",
            "No, only at startup",
            "No, assignment is fixed"
        ],
        "answer": "Yes, with assign()",
        "explanation": (
            "Calling `assign()` again with a new list of partitions changes assignment dynamically."
        ),
    },
    {
        "question": "A consumer crashes and restarts. What happens next?",
        "options": [
            "It resumes from the last committed offset",
            "It starts from the earliest offset",
            "It starts from the latest offset",
            "It gets a new set of partitions"
        ],
        "answer": "It resumes from the last committed offset",
        "explanation": (
            "When a consumer restarts, it resumes from the last committed offset for each partition."
        ),
    },
    {
        "question": "Which of the following is stored in Zookeeper for a Kafka cluster? (Select two)",
        "options": ["Consumer offsets", "Kafka broker information", "Topic partition assignments", "Topic-level configurations", "Producer client IDs"],
        "answer": ["Kafka broker information", "Topic-level configurations"],
        "explanation": "Zookeeper stores broker info and topic-level configs; consumer offsets are stored in Kafka itself."
    },
    {
        "question": "In a Kafka cluster, you have a topic with 6 partitions and a replication factor of 3. How many replicas of each partition will be spread across the brokers?",
        "options": ["1", "2", "3", "6"],
        "answer": "3",
        "explanation": "Replication factor determines copies per partition; here, 3 replicas per partition."
    },
    {
        "question": "What happens when a new consumer joins an existing consumer group?",
        "options": ["Starts from earliest offset", "Starts from latest offset", "Assigned subset of partitions, consuming from last committed offset", "Waits for next rebalance"],
        "answer": ["Assigned subset of partitions, consuming from last committed offset"],
        "explanation": "Joining triggers a rebalance; consumer starts from last committed offsets."
    },
    {
        "question": "What is the purpose of the `group.id` property in a Kafka consumer configuration?",
        "options": ["ID of consumer", "ID of consumer group", "ID of cluster", "ID of partitions"],
        "answer": "ID of consumer group",
        "explanation": "`group.id` identifies which group the consumer belongs to."
    },
    {
        "question": "What is the default behavior of the auto.offset.reset configuration in Kafka consumers?",
        "options": ["Starts from earliest", "Starts from latest", "Throws exception", "Waits for committed offset"],
        "answer": "Throws exception",
        "explanation": "If no committed offset found, by default Kafka throws an exception."
    },
    {
        "question": "When enable.auto.commit is false, what happens when commitSync() is called?",
        "options": ["Commits processed messages", "Commits fetched but unprocessed", "Throws exception", "Waits for next batch"],
        "answer": "Commits processed messages",
        "explanation": "`commitSync()` manually commits offsets of processed messages."
    },
    {
        "question": "What is the purpose of the isolation.level configuration in Kafka consumers?",
        "options": ["Control visibility of transactional messages", "Max records per batch", "Behavior on partition reassignment", "Consistency level"],
        "answer": "Control visibility of transactional messages",
        "explanation": "`isolation.level` controls visibility of transactional messages (read_committed vs read_uncommitted)."
    },
    {
        "question": "What happens if poll() is called on a KafkaConsumer from multiple threads?",
        "options": ["Parallel processing", "Throws ConcurrentModificationException", "Undefined behavior", "Sequential by turn"],
        "answer": "Undefined behavior",
        "explanation": "KafkaConsumer is not thread-safe; calling poll() from multiple threads can corrupt state."
    },
    {
        "question": "What is the recommended approach to process messages concurrently using KafkaConsumer?",
        "options": ["Share single consumer", "Multiple consumers in separate threads", "Thread pool on one consumer", "Synchronize shared consumer"],
        "answer": "Multiple consumers in separate threads",
        "explanation": "Use one KafkaConsumer per thread to ensure thread safety and parallelism."
    },
    {
        "question": "How does Kafka ensure messages are processed in a balanced way with multiple consumers?",
        "options": ["Equal messages", "Round-robin partition assignment", "Adjusts dynamically by load", "Uses ZooKeeper to balance"],
        "answer": "Round-robin partition assignment",
        "explanation": "Kafka balances partitions among consumers using round-robin assignor by default."
    },
    {
        "question": "What is the primary benefit of Kafka's zero-copy optimization?",
        "options": ["Reduces memory overhead", "Removes serialization", "Improves security", "Increases parallelism"],
        "answer": "Reduces memory overhead",
        "explanation": "Zero-copy minimizes memory duplication by transferring data directly from disk to network buffer."
    },
    {
        "question": "What is the purpose of the `isolation.level` setting in the Kafka consumer configuration?",
        "options": ["Max records", "Visibility of transactional messages", "Offset behavior", "Wait timeout"],
        "answer": "Visibility of transactional messages",
        "explanation": "Controls whether the consumer reads committed messages only or all messages."
    },
    {
        "question": "What is the default value of the `isolation.level` setting in the Kafka consumer configuration?",
        "options": ["read_uncommitted", "read_committed", "transactional", "none"],
        "answer": "read_uncommitted",
        "explanation": "The default value of the `isolation.level` setting in the Kafka consumer configuration is `read_uncommitted`. This means that by default, the consumer will read all messages, including transactional messages that are not yet committed. It may consume messages from transactions that are later aborted. To only read committed messages, you must explicitly set the `isolation.level` to `read_committed`."
    },
    {
        "question": "What happens when a consumer with `isolation.level=read_committed` encounters a message that is part of an ongoing transaction?",
        "options": [
            "The consumer will read the message immediately",
            "The consumer will wait until the transaction is committed before reading the message",
            "The consumer will skip the message and move on to the next one",
            "The consumer will throw an exception and stop consuming"
        ],
        "answer": "The consumer will wait until the transaction is committed before reading the message",
        "explanation": "When a consumer with `isolation.level=read_committed` encounters a message that is part of an ongoing transaction, it will wait until the transaction is committed before reading the message. This ensures that the consumer only sees messages that are part of successful transactions and prevents consuming uncommitted or aborted messages."
    },
    {
        "question": "What is the purpose of the `max.poll.records` setting in the Kafka consumer configuration?",
        "options": [
            "To specify the maximum number of records to return in a single poll",
            "To control the maximum amount of data the consumer can receive per second",
            "To set the maximum number of partitions the consumer can subscribe to",
            "To determine the maximum number of consumers allowed in a consumer group"
        ],
        "answer": "To specify the maximum number of records to return in a single poll",
        "explanation": "The `max.poll.records` setting specifies the maximum number of records to return in a single poll. When the consumer calls `poll()`, it will retrieve up to this number of records. The default is 500. Adjusting this value helps balance throughput and latency — higher values increase throughput but can raise latency."
    },
    {
        "question": "How does the `max.poll.interval.ms` setting affect the behavior of a Kafka consumer?",
        "options": [
            "It specifies the maximum amount of time the consumer can wait before polling for new records",
            "It sets the maximum interval between two consecutive polls before the consumer is considered dead",
            "It determines the maximum time allowed for message processing before committing offsets",
            "It controls the maximum number of records the consumer can poll in a single request"
        ],
        "answer": "It sets the maximum interval between two consecutive polls before the consumer is considered dead",
        "explanation": "The `max.poll.interval.ms` setting specifies the maximum interval between two consecutive polls before the consumer is considered dead. If the consumer doesn’t poll within this time (default: 5 minutes), Kafka considers it failed and triggers a rebalance to redistribute its partitions."
    },
    {
        "question": "What happens when a Kafka consumer is marked as dead due to exceeding the `max.poll.interval.ms` interval?",
        "options": [
            "The consumer is automatically rebalanced, and its partitions are reassigned to other consumers in the group",
            "The consumer receives an exception and must manually rejoin the consumer group",
            "The consumer's offset commits are rolled back, and it starts consuming from the beginning of the assigned partitions",
            "The consumer is permanently removed from the consumer group and cannot rejoin"
        ],
        "answer": "The consumer is automatically rebalanced, and its partitions are reassigned to other consumers in the group",
        "explanation": "When a Kafka consumer exceeds the `max.poll.interval.ms` limit, Kafka marks it as dead and triggers a rebalance. Its assigned partitions are reassigned to other consumers in the group to maintain continuous message processing."
    },
    {
        "question": "What triggers a partition rebalance in a Kafka consumer group?",
        "options": [
            "Adding a new topic to the Kafka cluster",
            "Changing the replication factor of a topic",
            "Adding a new consumer to the consumer group",
            "Modifying the consumer group ID"
        ],
        "answer": "Adding a new consumer to the consumer group",
        "explanation": "A partition rebalance is triggered when there’s a change in group membership — for example, when a new consumer joins the group. Kafka reassigns partitions to ensure even distribution of work. Removing or failing consumers also triggers rebalances."
    },
    {
        "question": "What happens to the partition assignments during a consumer group rebalance?",
        "options": [
            "Partitions are evenly distributed among the remaining consumers",
            "Partitions are assigned to the consumers based on the consumer group ID",
            "Partitions are randomly assigned to the consumers",
            "Partitions are assigned to the consumers based on the topic name"
        ],
        "answer": "Partitions are evenly distributed among the remaining consumers",
        "explanation": "During a rebalance, Kafka evenly distributes the topic partitions among active consumers using strategies like range or round-robin. This ensures balanced workload distribution across consumers."
    },
    {
        "question": "How can you minimize the impact of consumer group rebalances in a Kafka application?",
        "options": [
            "Increase the session timeout value for consumers",
            "Reduce the number of partitions for the consumed topics",
            "Implement a custom partition assignment strategy",
            "Use static group membership for consumers"
        ],
        "answer": "Use static group membership for consumers",
        "explanation": "Static group membership allows consumers to retain their partition assignments across restarts, minimizing rebalances."
    },
    {
        "question": "When a Kafka consumer wants to read data from a specific partition, what information does it need to provide?",
        "options": [
            "Topic name and consumer group ID",
            "Topic name and offset",
            "Topic name, partition number, and offset",
            "Topic name, partition number, and consumer group ID"
        ],
        "answer": "Topic name, partition number, and offset",
        "explanation": "The consumer must specify the topic name, partition number, and the offset to start reading from."
    },
    {
        "question": "How does a Kafka consumer determine which broker to connect to for a specific partition?",
        "options": [
            "Connects to any broker and requests metadata for the leader",
            "Connects directly to ZooKeeper",
            "Uses round-robin algorithm",
            "Connects to all brokers simultaneously"
        ],
        "answer": "Connects to any broker and requests metadata for the leader",
        "explanation": "Consumers request metadata from any broker, which tells them which broker is the leader for the partition."
    },
    {
        "question": "What happens if a consumer requests data from a non-existent partition?",
        "options": [
            "Broker creates the partition automatically",
            "Consumer receives empty response",
            "Consumer receives an error indicating partition does not exist",
            "Consumer is assigned another partition"
        ],
        "answer": "Consumer receives an error indicating partition does not exist",
        "explanation": "The broker returns an `UNKNOWN_TOPIC_OR_PARTITION` error if the requested partition does not exist."
    },
    {
        "question": "What does the `enable.auto.commit` property control in Kafka consumers?",
        "options": [
            "Automatically commits offsets at a fixed interval",
            "Automatically commits offsets after each message",
            "Enables or disables automatic offset commits",
            "Specifies how many offsets to commit per request"
        ],
        "answer": "Enables or disables automatic offset commits",
        "explanation": "`enable.auto.commit` determines whether the consumer commits offsets automatically or manually."
    },
    {
        "question": "An e-commerce company uses Kafka to process customer orders. During sales events, the order volume spikes significantly. Which approach ensures the system scales efficiently to handle these spikes in order volume?",
        "options": [
            "Automatically adjust the number of topics to spread the increased order messages across more Kafka topics during sales events.",
            "Use Kafka Connect with scalable Source Connectors to adjust the throughput based on order volume.",
            "Scale out the Kafka broker cluster by adding more brokers during high-volume periods and scale in when the volume decreases.",
            "Configure the Kafka producer to dynamically adjust batch size and linger time based on the current throughput of order messages."
        ],
        "answer": "Scale out the Kafka broker cluster by adding more brokers during high-volume periods and scale in when the volume decreases.",
        "explanation": "Scaling the Kafka broker cluster increases the system's capacity to handle higher message throughput during spikes. Adding brokers distributes partitions and improves overall throughput and performance."
    },
    {
        "question": "A streaming media company uses Kafka to ingest viewer watch history for real-time recommendation updates. Viewer engagement varies greatly, with peak times during new content releases. To handle variable ingestion rates, which configuration should be optimized?",
        "options": [
            "Adjust the replication factor of the watch history topic in real-time to handle the increased data volume.",
            "Increase and decrease the number of Kafka Connect Sink Connector tasks to efficiently write watch history data into Kafka.",
            "Scale the number of Kafka Streams applications processing the watch history data according to the ingestion rate.",
            "Dynamically modify the number of partitions in the watch history topic to manage the load during peak engagement times."
        ],
        "answer": "Scale the number of Kafka Streams applications processing the watch history data according to the ingestion rate.",
        "explanation": "Kafka Streams applications handle the real-time processing load. Scaling instances dynamically matches processing capacity with ingestion rates, ensuring low latency and efficient resource use."
    },
    {
        "question": "A logistics company tracks shipping containers across the globe in real-time. This tracking information is stored in various formats across different databases. The company aims to centralize this data into Kafka for real-time visibility and to enable reactive logistics management. The IT team is proficient in SQL but new to Kafka. Which approach should they take to integrate this diverse data into Kafka efficiently?",
        "options": [
            "Use JDBC Source Connectors to ingest container tracking data into Kafka. Transform this data into a unified format using Kafka Streams for real-time logistics management.",
            "Streamline data into Kafka using custom scripts that extract data from databases and publish to Kafka, relying on Kafka Streams for necessary transformations.",
            "Consolidate data in the RDBMS using SQL procedures to match the target schema required by Kafka, then use JDBC Source Connectors to stream this unified data into Kafka.",
            "Ingest raw data into Kafka using JDBC Source Connectors, then employ ksqlDB to perform SQL-like transformations and route the data to various microservices."
        ],
        "answer": "Ingest raw data into Kafka using JDBC Source Connectors, then employ ksqlDB to perform SQL-like transformations and route the data to various microservices.",
        "explanation": "This approach leverages the team's SQL skills with ksqlDB for stream processing while using JDBC Source Connectors for easy ingestion from diverse databases."
    },
    {
        "question": "A retail company wishes to analyze customer transactions in real-time to personalize marketing efforts. Transaction data, including purchases and returns, is captured in a legacy system. The marketing team requires this data in a format that can be easily queried and joined with other customer data. Given the team's familiarity with SQL, what is the most effective way to achieve this?",
        "options": [
            "Use JDBC Source Connectors to ingest transaction data into Kafka, followed by Kafka Streams for data transformation and enrichment.",
            "Directly export transaction data to CSV files, use custom producers to send these files to Kafka, and then apply Kafka Streams for transformation.",
            "Ingest transaction data into Kafka using JDBC Source Connectors and leverage ksqlDB for transforming and querying the data in a SQL-like manner.",
            "Transform data within the legacy system using SQL stored procedures, then use JDBC Source Connectors to ingest the pre-transformed data into Kafka."
        ],
        "answer": "Ingest transaction data into Kafka using JDBC Source Connectors and leverage ksqlDB for transforming and querying the data in a SQL-like manner.",
        "explanation": "Using JDBC Source Connectors simplifies ingestion, while ksqlDB enables the team to use familiar SQL syntax for real-time queries and transformations."
    },
    {
        "question": "An automotive manufacturer aims to optimize its supply chain by analyzing sensor data from its manufacturing equipment in real-time. The sensor data is currently logged in a proprietary format in a traditional database. The operations team, skilled in SQL, seeks to convert this data into actionable insights. Considering their expertise and requirements, which solution would best suit their needs?",
        "options": [
            "Utilize JDBC Source Connectors to stream sensor data into Kafka, transforming the data into a more accessible format using Kafka Streams.",
            "Export sensor data to a common format like JSON, use Kafka Connect to ingest this data, and then apply ksqlDB to analyze and visualize the data in real-time.",
            "Stream sensor data directly into Kafka using custom producers, followed by data transformation through SQL procedures embedded within the Kafka ecosystem.",
            "Ingest sensor data into Kafka using JDBC Source Connectors, then use ksqlDB to perform real-time analytics and transform the data for downstream processing."
        ],
        "answer": "Ingest sensor data into Kafka using JDBC Source Connectors, then use ksqlDB to perform real-time analytics and transform the data for downstream processing.",
        "explanation": "JDBC Source Connectors simplify ingestion from SQL-based systems, and ksqlDB enables SQL-based stream processing for analytics and transformations."
    },
    {
        "question": "A company plans to synchronize data between a PostgreSQL database and a Kafka cluster to enable real-time analytics. Which connector should be used to efficiently import data from PostgreSQL into Kafka?",
        "options": [
            "JDBC Source Connector",
            "S3 Sink Connector",
            "Elasticsearch Sink Connector",
            "HDFS Sink Connector"
        ],
        "answer": "JDBC Source Connector",
        "explanation": "The JDBC Source Connector is specifically designed to import data from relational databases like PostgreSQL into Kafka topics for real-time analytics."
    },
    {
        "question": "Your organization requires real-time text search capabilities on data streamed through Kafka. Which connector best facilitates exporting data from Kafka topics into Elasticsearch to meet this requirement?",
        "options": [
            "JDBC Sink Connector",
            "Elasticsearch Sink Connector",
            "MongoDB Sink Connector",
            "Kafka Connect File Sink Connector"
        ],
        "answer": "Elasticsearch Sink Connector",
        "explanation": "The Elasticsearch Sink Connector exports data from Kafka topics directly into Elasticsearch, enabling fast, full-text search and analytics capabilities."
    },
    {
        "question": "A streaming application is designed to process events in real-time and then store processed events in an Amazon S3 bucket for long-term analysis. Which connector configuration is most appropriate for this use case?",
        "options": [
            "JDBC Source Connector",
            "S3 Sink Connector",
            "MQTT Source Connector",
            "File Source Connector"
        ],
        "answer": "S3 Sink Connector",
        "explanation": "The S3 Sink Connector is used to export processed Kafka topic data to Amazon S3 for archival and analytical purposes."
    },
    {
        "question": "An IoT company collects temperature and humidity data from sensors deployed in various locations. The goal is to correlate this environmental data with location-specific weather forecasts retrieved from an external API. Which approach best facilitates this integration and processing within the Kafka ecosystem?",
        "options": [
            "Ingest sensor data into a Kafka topic using MQTT connectors. Separately, use an HTTP Source Connector to fetch weather forecasts, and utilize Kafka Streams to join data based on location and timestamp.",
            "Directly stream sensor data and weather forecasts into Kafka using custom Kafka Producers implemented in Python that merge both data sets before publishing.",
            "Use the MQTT Source Connector to ingest sensor data into Kafka and make REST API calls within Kafka Streams to fetch weather data for enrichment.",
            "Implement an MQTT proxy to capture sensor data into Kafka and use JDBC Sink Connectors to push it to a database before enrichment and re-ingestion."
        ],
        "answer": "Ingest sensor data into a Kafka topic using MQTT connectors. Separately, use an HTTP Source Connector to fetch weather forecasts, and utilize Kafka Streams to join data based on location and timestamp.",
        "explanation": "This approach efficiently combines data ingestion via connectors and real-time stream enrichment using Kafka Streams without introducing unnecessary latency or external dependencies."
    },
    {
        "question": "A retail chain wants to integrate sales data from their Point of Sale (POS) systems across multiple stores into Kafka for real-time analysis and inventory management. Each store's POS system dumps sales records into a local SQL database. The integration needs to account for network bandwidth limitations. Which strategy optimally addresses these requirements?",
        "options": [
            "Deploy Kafka Connect with the JDBC Source Connector at each store to ingest sales data into Kafka, using SMTs to filter and reduce the size of the data on the fly.",
            "Utilize log-based Change Data Capture (CDC) connectors to monitor changes in each store's SQL database, streaming only new or changed sales records into Kafka.",
            "Implement custom Kafka Producers within the POS systems to directly publish sales data to Kafka, compressing messages to mitigate network bandwidth issues.",
            "Set up a central database to aggregate sales data from all stores nightly and use JDBC Sink Connector to push the data into Kafka for next-day processing."
        ],
        "answer": "Utilize log-based Change Data Capture (CDC) connectors to monitor changes in each store's SQL database, streaming only new or changed sales records into Kafka.",
        "explanation": "CDC connectors efficiently capture only data changes, reducing bandwidth usage and enabling real-time synchronization for central analytics."
    },
    {
        "question": "In a Kafka cluster, two topics, `TopicA` and `TopicB`, are configured to be co-partitioned. This means they have an identical number of partitions, and messages in corresponding partitions are related to each other. Given that both are consumed together, what is a critical consideration for ensuring data consistency across these co-partitioned topics?",
        "options": [
            "Ensuring both topics have the same replication.factor to prevent data loss.",
            "Using a custom partitioner that assigns messages to the same partition number in both topics based on key.",
            "Configuring TopicB with a higher number of partitions than TopicA to ensure scalability.",
            "Increasing max.poll.records to a higher value to ensure more messages are processed in each poll."
        ],
        "answer": "Using a custom partitioner that assigns messages to the same partition number in both topics based on key.",
        "explanation": "To maintain the relationship between co-partitioned topics, messages with the same key must go to the same partition number in both topics. This ensures alignment for join and correlation operations in stream processing."
    },
    {
        "question": "For a streaming application processing data from two co-partitioned topics, `TopicX` and `TopicY`, which configuration ensures that the stream processing application maintains message ordering and correlation between these topics?",
        "options": [
            "Configuring both topics with log.compaction=true to ensure message deduplication.",
            "Ensuring that both topics are consumed by the application in separate threads.",
            "Assigning a unique consumer group for each topic to maximize parallel processing.",
            "Ensuring both topics use the same key for related messages and are consumed by the same consumer group."
        ],
        "answer": "Ensuring both topics use the same key for related messages and are consumed by the same consumer group.",
        "explanation": "Kafka Streams ensures message ordering and correlation by partitioning data by key. Using the same key and consuming from the same consumer group guarantees that related records are processed together."
    },
    {
        "question": "In a Kafka Streams application that enriches user clickstream data by joining it with user profile information, what should be the characteristics of the topic storing user profiles for optimal join operations?",
        "options": [
            "compression.type = snappy",
            "cleanup.policy = delete",
            "cleanup.policy = compact"
        ],
        "answer": "cleanup.policy = compact",
        "explanation": "The user-profiles-topic should use cleanup.policy=compact since it represents the changelog of user profiles. Compaction ensures only the latest profile per user is retained, essential for accurate KTable joins."
    },
    {
        "question": "When developing a Kafka Streams application that aggregates transaction amounts by user ID, which key-serde configuration ensures optimal processing and state store management?",
        "options": [
            "Key Serde = Serdes.String(), Value Serde = Serdes.BigDecimal()",
            "Key Serde = Serdes.Long(), Value Serde = Serdes.Double()",
            "Key Serde = Serdes.String(), Value Serde = Serdes.String()"
        ],
        "answer": "Key Serde = Serdes.String(), Value Serde = Serdes.BigDecimal()",
        "explanation": "Since the key is a user ID (String) and the value is a transaction amount (BigDecimal), this serde combination ensures accurate serialization for aggregation and state store operations."
    },
    {
        "question": "In a Kafka Streams application monitoring log levels, logs are streamed and filtered for ERROR logs. What is the most appropriate configuration for the `application-logs` source topic to optimize performance?",
        "options": [
            "retention.bytes = -1",
            "cleanup.policy = compact",
            "min.insync.replicas = 2"
        ],
        "answer": "retention.bytes = -1",
        "explanation": "Setting retention.bytes = -1 prevents logs from being prematurely deleted based on topic size. This ensures all log events are available for processing, which is important for monitoring and alerting applications."
    },
    {
        "question": "For a Kafka Streams application that processes customer orders to calculate real-time metrics such as total orders per hour, which configuration ensures that the state store `orders-per-hour-metrics` is optimally managed for performance and recovery?",
        "options": [
            "state.store.replication.factor = 3",
            "state.store.log.compaction = true",
            "commit.interval.ms = 100"
        ],
        "answer": "state.store.replication.factor = 3",
        "explanation": "Setting state.store.replication.factor = 3 ensures high availability and fault tolerance for stateful operations. This replication helps recover state data quickly in case of node failures."
    },
    {
        "question": "Is Kafka Streams DSL ANSI SQL compliant?",
        "options": [
            "Yes",
            "No",
            "Partially",
            "It depends on the version"
        ],
        "answer": "No",
        "explanation": "Kafka Streams DSL is not ANSI SQL compliant. It is a Java-based API inspired by SQL concepts but designed for programmatic stream processing rather than strict SQL syntax."
    },
    {
        "question": "What is the primary language used for writing Kafka Streams applications?",
        "options": [
            "Python",
            "Java",
            "Scala",
            "SQL"
        ],
        "answer": "Java",
        "explanation": "Kafka Streams is a Java library built for JVM-based applications. Although it can also be used with Scala, the primary and native language for Kafka Streams development is Java."
    },
    {
        "question": "What is the role of RocksDB in Kafka Streams?",
        "options": [
            "It is used for storing output topics.",
            "It is used for storing intermediate processing state.",
            "It is used for storing the Kafka Streams application code.",
            "It is not used in Kafka Streams."
        ],
        "answer": "It is used for storing intermediate processing state.",
        "explanation": "RocksDB is the default embedded state store used in Kafka Streams to persist intermediate state locally for aggregations, joins, and windowed computations. It ensures durability and fast access to state data."
    },
    {
        "question": "In a Kafka Streams application, where are the processing topology configurations stored?",
        "options": [
            "In a special Kafka topic named 'streams-configs'",
            "In Zookeeper under the '/kafka-streams' znode",
            "In the Kafka Streams application code itself",
            "In a separate config file read by the Kafka Streams application"
        ],
        "answer": "In the Kafka Streams application code itself",
        "explanation": "In a Kafka Streams application, the processing topology (the DAG of processing nodes) is defined in the application code itself using the Kafka Streams DSL or the Processor API. Kafka Streams does not use Zookeeper or a special topic to store topology configurations."
    },
    {
        "question": "You are implementing a Kafka Streams application. The input is a KStream from a topic where the message values are in Avro format. What should you set for the `default.value.serde` property in the Streams configuration?",
        "options": [
            "Serdes.String()",
            "Serdes.ByteArray()",
            "SpecificAvroSerde",
            "GenericAvroSerde"
        ],
        "answer": "SpecificAvroSerde",
        "explanation": "If message values are in Avro format and specific Avro-generated classes exist, you should set `default.value.serde` to `SpecificAvroSerde`. It ensures proper serialization/deserialization of Avro data. `GenericAvroSerde` is used when specific classes are not generated."
    },
    {
        "question": "What is the recommended way to enhance the performance of a Kafka Streams application that does a simple map transformation on the input data?",
        "options": [
            "Increase the number of partitions of the output topic",
            "Enable state store caching",
            "Increase the commit interval",
            "Disable logging"
        ],
        "answer": "Increase the number of partitions of the output topic",
        "explanation": "For stateless operations like `map`, increasing the output topic's partitions allows more parallelism and throughput. Caching and commit intervals mainly impact stateful processing, not stateless transformations."
    },
    {
        "question": "You are running a Kafka Streams application in a Docker container. The application performs a complex join operation and maintains a large state store. Which of the following would provide the greatest performance improvement when restarting the container?",
        "options": [
            "Increase the heap size of the Docker container",
            "Mount a high-performance SSD for the RocksDB directory",
            "Increase the number of replicas for the input topics",
            "Use a more powerful CPU for the Docker host"
        ],
        "answer": "Mount a high-performance SSD for the RocksDB directory",
        "explanation": "Kafka Streams uses RocksDB for local state storage. Using a high-performance SSD for the RocksDB directory reduces restore time and improves read/write performance during restarts."
    },
    {
        "question": "You are deploying a Kafka Streams application that joins two high-volume streams. Which of the following is LEAST likely to improve the performance of the application?",
        "options": [
            "Ensuring that the two input streams have the same number of partitions",
            "Increasing the number of standby replicas for the state store",
            "Tuning the cache.max.bytes.buffering parameter",
            "Increasing the num.streams.threads parameter"
        ],
        "answer": "Increasing the number of standby replicas for the state store",
        "explanation": "Standby replicas improve fault tolerance but not runtime performance. The other configurations (partition alignment, caching, and thread count) directly improve processing throughput."
    },
    {
        "question": "Which of the following stream processing operations can be considered stateful? (Select all that apply)",
        "options": [
            "Filter: Discarding messages based on a condition",
            "Map: Transforming messages from one format to another",
            "Aggregate: Combining multiple messages into a single result",
            "Join: Combining messages from two different streams based on a common key",
            "Peek: Performing an action on each message without modifying it"
        ],
        "answer": "Aggregate, Join",
        "explanation": "Aggregate and Join operations are stateful because they maintain state over time (e.g., running totals or join buffers). Filter, Map, and Peek are stateless as they process each record independently."
    },
    {
        "question": "What is the purpose of state stores in Kafka Streams?",
        "options": [
            "To persist the intermediate results and enable fault tolerance",
            "To cache the input messages for faster processing",
            "To store the final output of the stream processing application",
            "To maintain the configuration of the Kafka Streams application"
        ],
        "answer": "To persist the intermediate results and enable fault tolerance",
        "explanation": "State stores persist intermediate results for stateful operations (like aggregations or joins). They enable fault tolerance by allowing recovery of the state after failures."
    },
    {
        "question": "How does Kafka Streams handle state recovery in case of a failure?",
        "options": [
            "By replaying all the input messages from the beginning",
            "By restoring the state from a snapshot stored in Kafka",
            "By rebuilding the state from the change log topic",
            "By retrieving the state from an external database"
        ],
        "answer": "By rebuilding the state from the change log topic",
        "explanation": "Kafka Streams maintains a changelog topic for each state store. Upon failure, the state is restored by replaying the changelog topic, not by reprocessing all input data."
    },
    {
        "question": "You have a Kafka Streams application that processes messages from an input topic with 6 partitions. The application performs a stateful aggregation using a KTable. How many local state stores will be created by default?",
        "options": ["1", "3", "6", "12"],
        "answer": "6",
        "explanation": "Kafka Streams creates one local state store per input partition. For an input topic with 6 partitions, there will be 6 state stores by default."
    },
    {
        "question": "What is the main advantage of using Kafka Streams DSL over the Processor API for stream processing?",
        "options": [
            "Kafka Streams DSL provides better performance compared to the Processor API",
            "Kafka Streams DSL offers a higher-level, declarative approach to defining stream processing logic",
            "Kafka Streams DSL supports stateful operations, while the Processor API is limited to stateless operations",
            "Kafka Streams DSL allows for easier integration with external systems compared to the Processor API"
        ],
        "answer": "Kafka Streams DSL offers a higher-level, declarative approach to defining stream processing logic",
        "explanation": "Kafka Streams DSL provides a simpler, more declarative way to define processing logic, while the Processor API is more flexible but lower-level. Both support stateful operations."
    },
    {
        "question": "Which Kafka metric would you monitor to identify potential leader election issues?",
        "options": [
            "LeaderElectionRateAndTimeMs",
            "RequestRate",
            "MessageInPerSec",
            "ISRTime"
        ],
        "answer": "LeaderElectionRateAndTimeMs",
        "explanation": "LeaderElectionRateAndTimeMs indicates the rate and time taken for leader elections. Monitoring this helps identify potential leader election issues within the Kafka cluster."
    },
    {
        "question": "What is the purpose of the ActiveControllerCount metric in Kafka?",
        "options": [
            "To count the number of active consumers",
            "To indicate the number of active brokers",
            "To show the number of active controller nodes",
            "To measure the rate of message production"
        ],
        "answer": "To show the number of active controller nodes",
        "explanation": "The ActiveControllerCount metric shows the number of active controller nodes in the Kafka cluster. There should be exactly one active controller in a healthy cluster."
    },
    {
        "question": "Which Kafka metric helps in monitoring the health of consumer groups?",
        "options": [
            "ConsumerLag",
            "ProducerRequestRate",
            "BrokerTopicBytesOutPerSec",
            "FetchLatency"
        ],
        "answer": "ConsumerLag",
        "explanation": "ConsumerLag monitors how far behind a consumer group is in processing messages. It’s a key indicator of consumer group health and processing timeliness."
    },
    {
        "question": "Which tool can be used to collect JMX metrics from Kafka brokers for monitoring?",
        "options": [
            "Logstash",
            "JConsole",
            "Metricbeat",
            "Telegraf"
        ],
        "answer": "Telegraf",
        "explanation": "Telegraf’s JMX plugin can collect JMX metrics from Kafka brokers and forward them to monitoring systems like InfluxDB or Prometheus."
    },
    {
        "question": "What does the BrokerTopicBytesOutPerSec metric measure in Kafka?",
        "options": [
            "The number of bytes produced to a topic per second",
            "The number of bytes consumed from a topic per second",
            "The number of bytes replicated per second",
            "The number of bytes stored in a topic"
        ],
        "answer": "The number of bytes consumed from a topic per second",
        "explanation": "BrokerTopicBytesOutPerSec measures the number of bytes consumed from a topic per second — a key indicator of consumer-side throughput."
    },
    {
        "question": "Which metric should be monitored to detect partition imbalance in a Kafka cluster?",
        "options": [
            "PartitionCount",
            "LeaderCount",
            "UnderReplicatedPartitions",
            "PartitionLoad"
        ],
        "answer": "PartitionLoad",
        "explanation": "PartitionLoad helps detect partition imbalance by indicating how partitions are distributed across brokers."
    },
    {
        "question": "Which Kafka metric indicates the rate of log flush operations?",
        "options": [
            "LogFlushRateAndTimeMs",
            "DiskFlushRate",
            "LogRetentionRate",
            "FlushTime"
        ],
        "answer": "LogFlushRateAndTimeMs",
        "explanation": "LogFlushRateAndTimeMs tracks how often and how long Kafka takes to flush logs to disk — important for data durability and performance monitoring."
    },
    {
        "question": "What is the significance of the RequestQueueSize metric in Kafka?",
        "options": [
            "It measures the number of requests waiting to be processed by Kafka brokers.",
            "It indicates the number of active consumer requests.",
            "It shows the total number of requests handled by Kafka brokers.",
            "It measures the size of the message queue in bytes."
        ],
        "answer": "It measures the number of requests waiting to be processed by Kafka brokers.",
        "explanation": "RequestQueueSize measures the number of requests waiting in the broker’s queue. A high value can signal that the broker is overloaded."
    },
    {
        "question": "Which Kafka metric would you monitor to understand the latency experienced by producers?",
        "options": [
            "ProducerRequestRate",
            "ProducerLatency",
            "RequestQueueSize",
            "ProducerRequestQueueTimeMs"
        ],
        "answer": "ProducerRequestQueueTimeMs",
        "explanation": "ProducerRequestQueueTimeMs measures how long producer requests wait in the broker queue before being processed, indicating producer latency."
    },
    {
        "question": "Which metric is critical for monitoring Kafka broker heap memory usage?",
        "options": [
            "BrokerHeapMemoryUsed",
            "JvmMemoryUsage",
            "HeapMemoryUsage",
            "BrokerJvmHeap"
        ],
        "answer": "JvmMemoryUsage",
        "explanation": "JvmMemoryUsage tracks how much heap memory is used by the Kafka broker’s JVM — critical for preventing memory-related performance issues."
    },
    {
        "question": "How can the client.id setting be useful in monitoring and troubleshooting Kafka clients?",
        "options": [
            "It allows setting different configuration parameters for each client",
            "It enables tracking and correlating client activity in logs and metrics",
            "It determines the partitioning strategy used by the client",
            "It specifies the maximum number of connections the client can establish"
        ],
        "answer": "It enables tracking and correlating client activity in logs and metrics",
        "explanation": "The client.id setting helps in monitoring and troubleshooting Kafka clients by allowing tracking and correlation of client activity in logs and metrics. When each client is assigned a unique client.id, it becomes easier to trace and analyze its behavior within the cluster for debugging and performance analysis."
    },
    {
        "question": "What happens when you set max.in.flight.requests.per.connection to a value greater than 1 in a Kafka producer?",
        "options": [
            "It increases the throughput of the producer",
            "It increases the latency of the producer",
            "It can lead to out-of-order delivery of messages",
            "It has no effect on the producer's behavior"
        ],
        "answer": "It can lead to out-of-order delivery of messages",
        "explanation": "Setting max.in.flight.requests.per.connection to a value greater than 1 allows multiple requests to be sent to the broker in parallel. While this can improve throughput, if a request fails and needs to be retried, subsequent requests may have already been processed, leading to out-of-order message delivery."
    },
    {
        "question": "What is the effect of setting acks=0 in a Kafka producer?",
        "options": [
            "The producer will wait for the broker to acknowledge the message before sending the next one",
            "The producer will wait for the leader and all replicas to acknowledge the message",
            "The producer will not wait for any acknowledgement from the broker",
            "The producer will throw an exception if the broker does not acknowledge the message"
        ],
        "answer": "The producer will not wait for any acknowledgement from the broker",
        "explanation": "When acks=0, the producer sends messages without waiting for any acknowledgement from the broker, meaning there is no delivery guarantee. The producer considers the send successful immediately after dispatching the message."
    },
    {
        "question": "What is the relationship between request.timeout.ms and delivery.timeout.ms in a Kafka producer?",
        "options": [
            "request.timeout.ms should always be greater than delivery.timeout.ms",
            "delivery.timeout.ms should always be greater than request.timeout.ms",
            "They should always be set to the same value",
            "They are independent and can be set to any value"
        ],
        "answer": "delivery.timeout.ms should always be greater than request.timeout.ms",
        "explanation": "delivery.timeout.ms defines the total time allowed for message delivery, including retries, while request.timeout.ms defines how long to wait for a single request’s response. delivery.timeout.ms must be greater to avoid premature timeouts."
    },
    {
        "question": "A Kafka producer needs to send unordered messages to a topic. Which properties are mandatory in the configuration? (Select two)",
        "options": [
            "compression.type",
            "partitioner.class",
            "bootstrap.servers",
            "key.serializer",
            "value.serializer",
            "client.id"
        ],
        "answer": "bootstrap.servers, value.serializer",
        "explanation": "The bootstrap.servers property specifies broker addresses, and value.serializer defines how message values are serialized. These are mandatory for a producer to work. Other properties like compression.type or client.id are optional."
    },
    {
        "question": "What is the purpose of setting compression.type in a Kafka producer configuration?",
        "options": [
            "To specify the compression algorithm used when sending data to Kafka",
            "To specify the compression algorithm used when storing data on Kafka brokers",
            "To enable or disable compression for the producer",
            "To set the compression level for the producer"
        ],
        "answer": "To specify the compression algorithm used when sending data to Kafka",
        "explanation": "compression.type defines which compression algorithm (gzip, snappy, lz4, zstd) the producer uses before sending data to Kafka. Brokers store compressed data as received, and consumers decompress it when reading."
    },
    {
        "question": "What is the effect of enabling compression on the producer side in Kafka?",
        "options": [
            "Reduced producer memory usage",
            "Increased consumer CPU usage",
            "Reduced network bandwidth usage",
            "Increased end-to-end latency"
        ],
        "answer": "Reduced network bandwidth usage",
        "explanation": "Producer-side compression reduces data size sent over the network, saving bandwidth. However, this increases CPU usage (for compression/decompression) and can slightly increase latency."
    },
    {
        "question": "What is the relationship between batch.size and linger.ms in a Kafka producer configuration?",
        "options": [
            "They are mutually exclusive settings",
            "linger.ms is only relevant if batch.size is set to 0",
            "batch.size is only relevant if linger.ms is set to 0",
            "They work together to control when a batch is considered ready to send"
        ],
        "answer": "They work together to control when a batch is considered ready to send",
        "explanation": "batch.size controls the maximum batch data size in bytes, and linger.ms defines how long to wait before sending an incomplete batch. The producer sends the batch when either threshold is met."
    },
    {
        "question": "What is the effect of increasing batch.size in a Kafka producer configuration?",
        "options": [
            "It increases the maximum size of each individual message",
            "It increases the maximum number of messages that can be sent in a single request",
            "It increases the maximum time a batch will wait before being sent",
            "It increases the maximum amount of memory the producer will use for buffering"
        ],
        "answer": "It increases the maximum number of messages that can be sent in a single request",
        "explanation": "A larger batch.size allows the producer to group more messages into one network request, improving throughput but using more memory and potentially adding slight delay before sending."
    },
    {
        "question": "What is the relationship between linger.ms and request.timeout.ms in the Kafka producer configuration?",
        "options": [
            "They are redundant settings that control the same thing",
            "linger.ms should always be set higher than request.timeout.ms",
            "request.timeout.ms should always be set higher than linger.ms",
            "They control independent aspects of the producer behavior"
        ],
        "answer": "request.timeout.ms should always be set higher than linger.ms",
        "explanation": "linger.ms defines how long the producer waits before sending batches, while request.timeout.ms defines how long it waits for broker responses. request.timeout.ms must be higher to prevent premature timeouts."
    },
    {
        "question": "What happens if linger.ms is set to 0 in the Kafka producer configuration?",
        "options": [
            "The producer will never send any messages",
            "The producer will wait indefinitely for each batch to fill up before sending",
            "The producer will send each message as soon as it is received, without batching",
            "The producer will use the default linger time"
        ],
        "answer": "The producer will send each message as soon as it is received, without batching",
        "explanation": "Setting linger.ms=0 disables waiting before sending. Each message is sent immediately, minimizing latency but reducing throughput since batching is effectively disabled."
    },
    {
        "question": "What does the `acks=all` setting in the Kafka producer configuration ensure?",
        "options": [
            "The producer will receive an acknowledgment only after the message is written to all replicas",
            "The producer will receive an acknowledgment only after the message is written to the leader replica",
            "The producer will receive an acknowledgment only after the message is written to all in-sync replicas",
            "The producer will not wait for any acknowledgment and will consider the write successful immediately"
        ],
        "answer": "The producer will receive an acknowledgment only after the message is written to all in-sync replicas",
        "explanation": "When the `acks` parameter is set to 'all' in the Kafka producer configuration, the producer will receive an acknowledgment only after the message is written to all in-sync replicas (ISRs). This ensures the highest level of durability, as the producer waits for the message to be persisted on multiple replicas before considering the write successful."
    },
    {
        "question": "What is the purpose of the `client.id` setting in the Kafka producer and consumer configurations?",
        "options": [
            "To specify a unique identifier for the client within a Kafka cluster",
            "To set the maximum number of requests the client can send or receive",
            "To determine the compression type used for message production or consumption",
            "To control the maximum amount of memory the client can use for buffering"
        ],
        "answer": "To specify a unique identifier for the client within a Kafka cluster",
        "explanation": "The `client.id` setting in Kafka producer and consumer configurations specifies a unique identifier for the client. It helps in identifying and tracking the client’s activity in logs and metrics, which is useful for debugging and monitoring. It does not affect client functionality or performance directly."
    },
    {
        "question": "What happens if multiple Kafka clients use the same `client.id` value?",
        "options": [
            "The clients will share the same configuration and connection pooling",
            "The clients will be treated as a single logical client by the Kafka brokers",
            "The behavior is undefined, and it may lead to unexpected results or errors",
            "The Kafka brokers will reject the connection attempts from clients with duplicate `client.id`"
        ],
        "answer": "The behavior is undefined, and it may lead to unexpected results or errors",
        "explanation": "If multiple clients use the same `client.id`, Kafka brokers do not enforce uniqueness, which can lead to confusing or incorrect correlations in logs and metrics. To avoid tracking and debugging issues, each client should use a unique `client.id`."
    },
    {
        "question": "If a producer sends a message with a key to a topic with 5 partitions, which partition will the message be written to?",
        "options": [
            "The partition is randomly selected",
            "The partition is determined based on the hash of the message key",
            "The partition is always the first partition (partition 0)",
            "The partition is determined by the broker"
        ],
        "answer": "The partition is determined based on the hash of the message key",
        "explanation": "Kafka’s default partitioner hashes the message key (using the murmur2 hash function) and maps it to a partition using the hash value modulo the number of partitions. This ensures messages with the same key always go to the same partition."
    },
    {
        "question": "What happens if a producer sends a message without a key to a topic with 3 partitions?",
        "options": [
            "The message is discarded",
            "The message is sent to a randomly selected partition",
            "The message is sent to all partitions",
            "The message is sent to the partition with the least amount of data"
        ],
        "answer": "The message is sent to a randomly selected partition",
        "explanation": "When no key is provided, Kafka’s default partitioner uses a round-robin approach to evenly distribute messages across partitions. Each new message goes to the next partition in sequence, ensuring balanced load distribution."
    },
    {
        "question": "Can a producer guarantee the order of messages within a partition when sending messages with different keys?",
        "options": [
            "Yes, messages within a partition are always guaranteed to be in the same order as they were sent by the producer",
            "No, messages with different keys can be written to the same partition in a different order than they were sent",
            "It depends on the configuration of the producer",
            "It depends on the configuration of the topic"
        ],
        "answer": "No, messages with different keys can be written to the same partition in a different order than they were sent",
        "explanation": "Kafka guarantees order only for messages with the same key in a given partition. Messages with different keys may be sent to different partitions or even to the same partition in a different order depending on the timing of write operations."
    },
    {
        "question": "What happens when a producer tries to send a message to a partition whose leader replica is not in-sync?",
        "options": [
            "The producer receives a `NotLeaderOrFollowerException` and retries sending the message",
            "The producer waits until the leader replica becomes in-sync before sending the message",
            "The message is automatically routed to another in-sync replica",
            "The producer receives a `LeaderNotAvailableException` and the message is discarded"
        ],
        "answer": "The producer receives a `NotLeaderOrFollowerException` and retries sending the message",
        "explanation": "If the leader for a partition is not in-sync, the producer receives a `NotLeaderOrFollowerException`, refreshes metadata, and retries sending the message to the new leader. Kafka producers never send directly to followers."
    },
    {
        "question": "In a topic with a replication factor of 3 and `min.insync.replicas` set to 2, what happens when a producer sends a message with `acks=all` and two replicas are not in-sync?",
        "options": [
            "The producer receives an acknowledgment and the message is successfully written",
            "The producer receives a `NotEnoughReplicasException` and the message is not written",
            "The producer waits indefinitely until at least two replicas become in-sync",
            "The message is written to the leader replica and the producer receives an acknowledgment"
        ],
        "answer": "The producer receives a `NotEnoughReplicasException` and the message is not written",
        "explanation": "With `acks=all` and `min.insync.replicas=2`, Kafka requires at least two in-sync replicas to acknowledge the write. If fewer are available, the producer gets a `NotEnoughReplicasException`, and the message is not committed."
    },
    {
        "question": "When using the Confluent REST Proxy to produce messages, what happens if the `value.schema.id` is provided in the request payload?",
        "options": [
            "The REST Proxy validates the payload against the schema specified by the ID",
            "The REST Proxy retrieves the schema from the Schema Registry and includes it in the produced message",
            "The REST Proxy ignores the `value.schema.id` field and produces the message without any schema information",
            "The REST Proxy returns an error indicating that the `value.schema.id` is not supported"
        ],
        "answer": "The REST Proxy validates the payload against the schema specified by the ID",
        "explanation": "When the `value.schema.id` is provided, the REST Proxy retrieves the schema from the Schema Registry and validates the message payload against it. If validation succeeds, it produces the message to Kafka; otherwise, it returns an error. This ensures that only schema-compliant messages are produced."
    },
    {
        "question": "What is the purpose of the `key.converter` and `value.converter` configurations in the Confluent REST Proxy?",
        "options": [
            "To specify the format of the message key and value in the produced messages",
            "To specify the serialization format for the message key and value in the REST API requests and responses",
            "To specify the compression type for the message key and value",
            "To specify the schema ID for the message key and value"
        ],
        "answer": "To specify the serialization format for the message key and value in the REST API requests and responses",
        "explanation": "The `key.converter` and `value.converter` configurations define how the message key and value are serialized/deserialized in REST API communication. They ensure proper encoding for formats like Avro, String, or ByteArray during REST Proxy interactions."
    },
    {
        "question": "How does the Confluent REST Proxy handle authentication and authorization for production and consumption of messages?",
        "options": [
            "The REST Proxy performs authentication and authorization based on the Kafka ACLs configured in the brokers",
            "The REST Proxy uses its own authentication and authorization mechanism independent of Kafka",
            "The REST Proxy relies on the Schema Registry for authentication and authorization",
            "The REST Proxy does not support authentication and authorization"
        ],
        "answer": "The REST Proxy uses its own authentication and authorization mechanism independent of Kafka",
        "explanation": "The REST Proxy enforces its own authentication and authorization at the REST API layer using Basic Auth or JWT, separate from Kafka broker ACLs. It validates credentials before allowing access to topics or consumer groups."
    },
    {
        "question": "What is the purpose of the Kafka REST Proxy?",
        "options": [
            "To provide a RESTful interface for producing and consuming messages in Kafka",
            "To manage Kafka clusters and monitor their health",
            "To store and retrieve Avro schemas for Kafka messages",
            "To stream data between Kafka and external systems"
        ],
        "answer": "To provide a RESTful interface for producing and consuming messages in Kafka",
        "explanation": "The Kafka REST Proxy exposes HTTP endpoints for producing and consuming Kafka messages, allowing non-Kafka applications to integrate with Kafka using simple REST APIs."
    },
    {
        "question": "Which HTTP method is used to produce messages to a Kafka topic via the REST Proxy?",
        "options": [
            "GET",
            "POST",
            "PUT",
            "DELETE"
        ],
        "answer": "POST",
        "explanation": "Producing messages via the REST Proxy requires sending a POST request to the topic endpoint. The POST method is used to submit data (messages) to Kafka through REST."
    },
    {
        "question": "How does the Kafka REST Proxy handle consumer offsets?",
        "options": [
            "It stores consumer offsets in a separate Kafka topic",
            "It manages consumer offsets using Zookeeper",
            "It relies on the Kafka brokers to store consumer offsets",
            "It does not manage consumer offsets"
        ],
        "answer": "It relies on the Kafka brokers to store consumer offsets",
        "explanation": "The REST Proxy leverages Kafka’s built-in offset management stored in the `__consumer_offsets` topic. It does not manage offsets itself but uses the broker’s native mechanism."
    },
    {
        "question": "What is the purpose of the `consumer.request.timeout.ms` configuration parameter in the Kafka REST Proxy?",
        "options": [
            "To set the maximum time to wait for a message to be consumed",
            "To set the maximum time to wait for a response from the Kafka broker",
            "To set the maximum time to keep a consumer instance alive without further requests",
            "To set the maximum time to wait for a consumer to join a consumer group"
        ],
        "answer": "To set the maximum time to keep a consumer instance alive without further requests",
        "explanation": "The `consumer.request.timeout.ms` parameter determines how long a consumer instance created through the REST Proxy can remain idle before being automatically closed."
    },
    {
        "question": "How does the Kafka REST Proxy handle authentication?",
        "options": [
            "It uses Kafka's native authentication mechanisms",
            "It supports basic authentication using username and password",
            "It relies on SSL/TLS for authentication",
            "It does not provide built-in authentication mechanisms"
        ],
        "answer": "It supports basic authentication using username and password",
        "explanation": "The REST Proxy supports HTTP Basic Authentication using username and password. Clients must include credentials in the request headers to access REST endpoints securely."
    },
    {
        "question": "What is the role of the `id` field in the request payload when producing messages via the Kafka REST Proxy?",
        "options": [
            "It specifies the Kafka topic to produce the message to",
            "It represents the key of the message",
            "It uniquely identifies the message within the Kafka cluster",
            "It is an optional field used for client-side message tracking"
        ],
        "answer": "It is an optional field used for client-side message tracking",
        "explanation": "The `id` field is a client-side identifier included for tracking or correlation. It’s not used by Kafka itself and is ignored after message production."
    },
    {
        "question": "How can you configure the Kafka REST Proxy to use SSL/TLS for secure communication?",
        "options": [
            "Set `ssl.enabled` to `true` in the REST Proxy configuration",
            "Enable SSL/TLS in the Kafka broker configuration",
            "Configure SSL/TLS in the client application code",
            "No additional configuration is required"
        ],
        "answer": "Set `ssl.enabled` to `true` in the REST Proxy configuration",
        "explanation": "To enable HTTPS communication, you must set `ssl.enabled=true` and configure SSL keystore and truststore parameters in the REST Proxy configuration file."
    },
    {
        "question": "Where does Confluent Schema Registry store the registered schema information?",
        "options": [
            "In Zookeeper under the `/schemas` znode",
            "In a special Kafka topic named `_schemas`",
            "In a relational database configured in Schema Registry",
            "In the Kafka broker's `schema` directory on disk"
        ],
        "answer": "In a special Kafka topic named `_schemas`",
        "explanation": "Confluent Schema Registry uses a special Kafka topic named `_schemas` to store registered schema information. Each schema is stored as a message in this topic, keyed by its schema ID. Zookeeper is not used for schema storage, and no external databases are required."
    },
    {
        "question": "What serialization formats are supported by the Confluent Schema Registry for storing schemas?",
        "options": [
            "Avro",
            "Protobuf",
            "JSON Schema",
            "XML Schema",
            "Thrift"
        ],
        "answer": ["Avro", "Protobuf", "JSON Schema"],
        "explanation": "Confluent Schema Registry supports Avro, Protobuf, and JSON Schema. These formats support schema evolution and compatibility checks. XML Schema and Thrift are not supported formats."
    },
    {
        "question": "Which of the following programming languages have official client libraries for interacting with the Confluent Schema Registry?",
        "options": [
            "Java",
            "Python",
            "Go",
            "C++",
            "JavaScript",
            "Ruby"
        ],
        "answer": ["Java", "Python", "Go"],
        "explanation": "Official Schema Registry clients are available for Java, Python, and Go. C++, JavaScript, and Ruby can interact with Schema Registry through REST API, but there are no official Confluent-provided libraries for them."
    },
    {
        "question": "What is the purpose of the compatibility setting in the Confluent Schema Registry?",
        "options": [
            "It defines which serialization format (Avro, Protobuf) is used",
            "It controls how schemas can evolve over time",
            "It sets the compatibility between different Schema Registry versions",
            "It configures compatibility between the Schema Registry and Kafka brokers"
        ],
        "answer": "It controls how schemas can evolve over time",
        "explanation": "The compatibility setting defines how schemas can evolve over time. It ensures backward, forward, or full compatibility between schema versions. It does not determine serialization format or compatibility with Kafka brokers."
    },
    {
        "question": "In Avro, what is the effect of adding a field to a record schema without a default value?",
        "options": [
            "It is a backward compatible change",
            "It is a forward compatible change",
            "It is both a backward and forward compatible change",
            "It is an incompatible change"
        ],
        "answer": "It is a forward compatible change",
        "explanation": "Adding a new field without a default value is forward compatible — new data can be read by old schemas, but old data cannot be read by new schemas. To make it backward compatible, a default value must be provided."
    },
    {
        "question": "What is the Avro schema evolution rule for removing a field?",
        "options": [
            "It is always a compatible change",
            "It is a backward compatible change",
            "It is a forward compatible change",
            "It is an incompatible change"
        ],
        "answer": "It is a backward compatible change",
        "explanation": "Removing a field in Avro is backward compatible because new schemas can read old data (ignoring removed fields), but it’s not forward compatible because old schemas cannot read new data missing that field."
    },
    {
        "question": "In Avro, what is the compatibility implication of changing the name of a record schema?",
        "options": [
            "It is a backward compatible change",
            "It is a forward compatible change",
            "It is both a backward and forward compatible change",
            "It is an incompatible change"
        ],
        "answer": "It is an incompatible change",
        "explanation": "Changing the name of a record schema is incompatible because Avro identifies schemas by name. Data written with the old name cannot be read by the new schema and vice versa."
    },
    {
        "question": "What happens when a Kafka consumer using KafkaAvroDeserializer encounters a message without a schema ID?",
        "options": [
            "The consumer throws a SerializationException",
            "The consumer skips the message and moves to the next one",
            "The consumer attempts to deserialize the message using the latest schema",
            "The consumer falls back to using the GenericRecord deserializer"
        ],
        "answer": "The consumer throws a SerializationException",
        "explanation": "KafkaAvroDeserializer requires a schema ID in the message payload. If missing, it cannot fetch the schema from Schema Registry and throws a SerializationException instead of skipping or guessing the schema."
    },
    {
        "question": "How can you handle a SerializationException thrown by the KafkaAvroDeserializer in a Kafka consumer?",
        "options": [
            "Catch the exception and retry deserializing the message with a different deserializer",
            "Catch the exception and skip the problematic message by committing its offset",
            "Catch the exception and manually retrieve the schema from the Schema Registry for deserialization",
            "Let the exception propagate and handle it at a higher level in the consumer application"
        ],
        "answer": "Catch the exception and skip the problematic message by committing its offset",
        "explanation": "When encountering a SerializationException, it’s best to catch the error, log it, and commit the offset of the problematic message to skip it. This prevents the consumer from being stuck on corrupted or invalid messages."
    },
    {
        "question": "What are the benefits of using Confluent Schema Registry and KafkaAvroDeserializer in a Kafka consumer?",
        "options": [
            "Automatic schema evolution and compatibility checks",
            "Improved deserialization performance compared to generic deserializers",
            "Ability to deserialize messages without knowing the schema upfront",
            "All of the above"
        ],
        "answer": "All of the above",
        "explanation": "Using Schema Registry and KafkaAvroDeserializer enables automatic schema evolution handling, faster deserialization with Avro’s binary format, and deserialization without knowing schemas ahead of time — all of the above."
    },
    {
        "question": "Where does the Confluent Schema Registry store its own configuration?",
        "options": [
            "In Zookeeper",
            "In a Kafka topic",
            "On the filesystem",
            "In a database"
        ],
        "answer": "In Zookeeper",
        "explanation": "The Confluent Schema Registry stores its configuration in Zookeeper, typically under the path `/schema-registry`. Configuration details such as `kafkastore.topic`, `master.eligibility`, `host.name`, and `port` are maintained there. While Kafka topics are used for schema data, Zookeeper is responsible for configuration storage."
    },
    {
        "question": "How does the Confluent Schema Registry ensure high availability?",
        "options": [
            "By running multiple instances and electing a master",
            "By relying on the availability of the underlying Kafka cluster",
            "By replicating data across multiple Zookeeper instances",
            "By using a distributed consensus protocol among instances"
        ],
        "answer": "By running multiple instances and electing a master",
        "explanation": "Schema Registry achieves high availability by running multiple instances in a cluster. One instance is elected as the master to handle write operations, while others can handle read requests. If the master fails, a new master is automatically elected, ensuring continuous operation without manual intervention."
    },
    {
        "question": "Where are the ACLs stored in a Kafka cluster by default at Zookeeper mode cluster?",
        "options": [
            "In the Kafka topic `_acls`",
            "Inside the broker's data directory",
            "In Zookeeper node `/kafka-acl/`",
            "In a separate ACL server"
        ],
        "answer": "In Zookeeper node `/kafka-acl/`",
        "explanation": "ACLs are stored in Zookeeper by default under the `/kafka-acl/` znode. This allows brokers to share ACL data consistently. For newer KRaft-based clusters (without Zookeeper), ACLs are stored in the internal Kafka topic `__cluster_metadata` instead."
    },
    {
        "question": "What Kafka CLI command can be used to add new ACL rules to a running Kafka cluster?",
        "options": [
            "kafka-acls.sh",
            "kafka-configs.sh",
            "kafka-topics.sh",
            "kafka-console-producer.sh"
        ],
        "answer": "kafka-acls.sh",
        "explanation": "The `kafka-acls.sh` CLI tool is used to manage ACLs in Kafka. It allows you to add, remove, or list ACL rules in a running cluster. Other tools like `kafka-configs.sh` or `kafka-topics.sh` handle configurations and topics respectively, not ACLs."
    },
    {
        "question": "Which of the following is NOT a valid resource type when defining ACLs in Kafka?",
        "options": [
            "Topic",
            "Consumer Group",
            "Cluster",
            "Partition"
        ],
        "answer": "Partition",
        "explanation": "Kafka ACLs apply to resource types such as Topic, Consumer Group, and Cluster. 'Partition' is not a valid ACL resource type, as ACLs operate at the topic level, covering all partitions within that topic."
    },
    {
        "question": "What is the purpose of ACLs (Access Control Lists) in Kafka?",
        "options": [
            "To encrypt messages for secure communication between clients and brokers",
            "To authenticate clients and authorize their access to Kafka resources",
            "To compress messages for efficient storage and transmission",
            "To validate the schema of messages produced to Kafka topics"
        ],
        "answer": "To authenticate clients and authorize their access to Kafka resources",
        "explanation": "ACLs (Access Control Lists) in Kafka control which users or clients can access specific Kafka resources. They define who can perform operations such as producing, consuming, or modifying topics, enforcing access security policies."
    },
    {
        "question": "How are ACLs stored and managed in Kafka for KRaft mode?",
        "options": [
            "ACLs are stored in a Controller node's local file system and managed using Kafka command-line tools",
            "ACLs are stored in the `__cluster_metadata` topic and managed using Kafka command-line tools",
            "ACLs are stored in a dedicated ACL server and managed through a REST API",
            "ACLs are stored in the Kafka broker's local file system and managed using configuration files"
        ],
        "answer": "ACLs are stored in the `__cluster_metadata` topic and managed using Kafka command-line tools",
        "explanation": "In KRaft mode, Kafka uses `StandardAuthorizer`, which stores ACLs in the internal topic `__cluster_metadata` instead of Zookeeper. ACLs are still managed using the `kafka-acls.sh` command-line tool."
    },
    {
        "question": "What happens when a client tries to perform an operation that is not allowed by the configured ACLs?",
        "options": [
            "The operation is performed, but a warning is logged in the Kafka broker logs",
            "The operation is rejected, and the client receives an authorization error",
            "The operation is performed, but the message is flagged as unauthorized",
            "The operation is delayed until the necessary ACLs are added"
        ],
        "answer": "The operation is rejected, and the client receives an authorization error",
        "explanation": "Kafka brokers enforce ACLs strictly. If a client attempts an unauthorized operation, the broker rejects it and returns an authorization error. The operation is never executed, ensuring security and consistency."
    },
    {
        "question": "What is the purpose of the `CreateTopics` ACL operation in Kafka?",
        "options": [
            "To allow a client to create new topics in a Kafka cluster",
            "To permit a client to produce messages to a specific topic",
            "To grant a client permission to delete topics from a Kafka cluster",
            "To enable a client to modify the configuration of existing topics"
        ],
        "answer": "To allow a client to create new topics in a Kafka cluster",
        "explanation": "The `CreateTopics` ACL operation authorizes clients to create new topics in Kafka. It’s usually granted to administrative users or automation systems responsible for managing topic lifecycles."
    },
    {
        "question": "What is the difference between `Read` and `Write` ACL operations in Kafka?",
        "options": [
            "`Read` allows consuming messages, while `Write` allows producing messages",
            "`Read` allows producing messages, while `Write` allows consuming messages",
            "`Read` allows modifying topic configurations, while `Write` allows deleting topics",
            "`Read` and `Write` are equivalent and can be used interchangeably"
        ],
        "answer": "`Read` allows consuming messages, while `Write` allows producing messages",
        "explanation": "`Read` permission enables a client to consume messages from a topic, while `Write` permission allows producing messages to that topic. Each permission type is distinct and must be explicitly granted."
    },
    {
        "question": "How can you grant a client permission to describe topics and consumer groups in a Kafka cluster?",
        "options": [
            "Assign the `DescribeConfigs` ACL operation to the client",
            "Grant the `Describe` ACL operation to the client",
            "Provide the `AlterConfigs` ACL operation to the client",
            "Give the `IdempotentWrite` ACL operation to the client"
        ],
        "answer": "Grant the `Describe` ACL operation to the client",
        "explanation": "The `Describe` ACL allows clients to view metadata for topics and consumer groups, such as configurations and partition details, without the ability to modify them. It's commonly used for monitoring and inspection."
    },
    {
        "question": "What is the purpose of the `ssl.keystore.location` and `ssl.keystore.password` configurations in Kafka?",
        "options": [
            "To specify the location and password of the truststore for verifying client certificates",
            "To specify the location and password of the keystore for broker authentication",
            "To specify the location and password of the keystore for client authentication",
            "To specify the location and password of the truststore for broker authentication"
        ],
        "answer": "To specify the location and password of the keystore for broker authentication",
        "explanation": "The `ssl.keystore.location` and `ssl.keystore.password` settings define where the broker’s keystore is stored and how to access it. This keystore contains the broker’s certificate and private key for SSL/TLS authentication."
    },
    {
        "question": "Which security protocol in Kafka provides both encryption and authentication for client-broker communication?",
        "options": [
            "PLAINTEXT",
            "SASL_PLAINTEXT",
            "SSL",
            "SASL_SSL"
        ],
        "answer": "SASL_SSL",
        "explanation": "The `SASL_SSL` security protocol in Kafka provides both encryption and authentication for client-broker communication. It combines SSL/TLS for encrypting data in transit with SASL mechanisms (such as PLAIN, SCRAM, or GSSAPI) for authenticating clients and brokers. This ensures both data confidentiality and identity verification, making `SASL_SSL` the most secure option for production environments."
    },
    {
        "question": "Which of the following statements about `acks` and `min.insync.replicas` are true? (Select all that apply)",
        "options": [
            "acks is a producer configuration, while min.insync.replicas is a topic configuration",
            "acks and min.insync.replicas are both producer configurations",
            "acks and min.insync.replicas are both topic configurations",
            "acks=all and min.insync.replicas=1 provides the strongest durability guarantee",
            "acks=1 and min.insync.replicas=2 provides the strongest durability guarantee",
            "For acks=all to provide any additional durability over acks=1, min.insync.replicas must be greater than 1"
        ],
        "answer": ["acks is a producer configuration, while min.insync.replicas is a topic configuration", 
                   "For acks=all to provide any additional durability over acks=1, min.insync.replicas must be greater than 1"],
        "explanation": "`acks` is a **producer configuration** specifying how many acknowledgments are required before a write is considered successful, while `min.insync.replicas` is a **topic configuration** defining how many replicas must acknowledge a write. For `acks=all` to provide stronger durability than `acks=1`, `min.insync.replicas` must be greater than 1. Otherwise, both configurations behave similarly in durability."
    },
    {
        "question": "What is the relationship between `unclean.leader.election.enable` and `min.insync.replicas`?",
        "options": [
            "They control the same thing and should always be set to the same value",
            "unclean.leader.election.enable overrides min.insync.replicas",
            "They are independent and one does not affect the other",
            "If unclean.leader.election.enable=true, min.insync.replicas can be violated during leader election"
        ],
        "answer": "If unclean.leader.election.enable=true, min.insync.replicas can be violated during leader election",
        "explanation": "`unclean.leader.election.enable` controls whether an out-of-sync replica can be elected as leader if all in-sync replicas fail. When set to `true`, it allows availability at the cost of durability — violating `min.insync.replicas`. This can lead to **data loss**, though it helps keep partitions available."
    },
    {
        "question": "A Kafka cluster has 3 brokers. You create a topic with 6 partitions and 2 consumers in a consumer group subscribed to this topic. What is the maximum number of partitions that can be assigned to a single consumer?",
        "options": ["1", "2", "3", "6"],
        "answer": "6",
        "explanation": "Kafka tries to balance partitions evenly among consumers. With 6 partitions and 2 consumers, one consumer could get up to **4 partitions** and the other 2. Therefore, the **maximum possible number** of partitions assigned to a single consumer is 6 if one consumer fails and the other takes all."
    },
    {
        "question": "A topic has 10 partitions and a replication factor of 3. There are 2 consumers in a consumer group subscribed to this topic. The cluster has 5 brokers. How would the partitions be assigned to the consumers to achieve maximum throughput?",
        "options": [
            "Consumer 1: Partitions 0-4, Consumer 2: Partitions 5-9",
            "Consumer 1: Partitions 0-9 and 0-1 replicas, Consumer 2: Partitions 0-9 and 3 replicas",
            "Consumer 1: Partitions 0, 1, 2, Consumer 2: Partitions 3, 4, 5, Unassigned: 6, 7, 8, 9",
            "Consumer 1: Partitions 0-9"
        ],
        "answer": "Consumer 1: Partitions 0-4, Consumer 2: Partitions 5-9",
        "explanation": "Kafka distributes partitions **evenly** among consumers in a group. With 10 partitions and 2 consumers, each will be assigned 5 partitions to maximize parallel processing. Replica placement or number of brokers does not affect partition-to-consumer assignment."
    },
    {
        "question": "Which of the following statements about Kafka topic configurations is true?",
        "options": [
            "Topic configurations can only be set when a topic is first created and cannot be changed later",
            "Topic configurations can be changed dynamically using the kafka-configs.sh tool",
            "Topic configurations are stored in Zookeeper and are not accessible through the Kafka broker",
            "Topic configurations are stored in the Kafka broker's configuration file and require a broker restart to take effect"
        ],
        "answer": "Topic configurations can be changed dynamically using the kafka-configs.sh tool",
        "explanation": "Kafka allows **dynamic updates** to topic configurations using the `kafka-configs.sh` tool — no broker restart needed. The updated configurations are stored in Zookeeper and automatically picked up by brokers. This flexibility enables real-time tuning without downtime."
    },
    {
        "question": "What is the default cleanup policy for Kafka topics?",
        "options": ["Delete", "Compact", "Delete and Compact", "None"],
        "answer": "Delete",
        "explanation": "By default, Kafka topics use the **Delete** cleanup policy. Old log segments are removed after reaching retention limits (time or size). The **Compact** policy must be explicitly enabled to retain only the latest record per key, suitable for changelog topics."
    },
    {
        "question": "What is the purpose of the `kafka-dump-log` tool in KRaft mode?",
        "options": [
            "To display the contents of the KRaft metadata log",
            "To modify the Kafka broker configuration",
            "To list the available Kafka topics",
            "To monitor the Kafka cluster performance"
        ],
        "answer": "To display the contents of the KRaft metadata log",
        "explanation": "In KRaft mode, the `kafka-dump-log` tool is used to display the contents of the KRaft metadata log. It helps inspect log segments and snapshots for the cluster metadata directory. For example: `bin/kafka-dump-log --cluster-metadata-decoder --files /path/to/kraft/metadata/log/00000000000000000000.log`. This tool decodes and prints metadata records for debugging and analysis. Configuration changes, topic listing, and performance monitoring are done via other tools."
    },
    {
        "question": "What is the purpose of the `kafka-metadata-shell` tool in KRaft mode?",
        "options": [
            "To modify the Kafka broker configuration",
            "To list the available Kafka topics",
            "To monitor the Kafka cluster performance",
            "To interactively inspect the KRaft metadata"
        ],
        "answer": "To interactively inspect the KRaft metadata",
        "explanation": "In KRaft mode, the `kafka-metadata-shell` tool provides an interactive shell to inspect the KRaft metadata. It allows you to navigate the metadata log and view the state of the cluster using commands like `ls` and `cat`. For example: `bin/kafka-metadata-shell --snapshot /path/to/kraft/metadata/log`. It is primarily used for debugging, not configuration, topic listing, or performance monitoring."
    },
    {
        "question": "What is the significance of the `kafka.controller:type=QuorumController,name=LastCommittedRecordOffset` metric in KRaft mode?",
        "options": [
            "It indicates the offset of the last record applied by the controller",
            "It represents the number of records that have been committed to the metadata partition",
            "It measures the lag between the active controller and the last committed record in the metadata partition",
            "It tracks the offset of the last record that was committed by the active controller"
        ],
        "answer": "It tracks the offset of the last record that was committed by the active controller",
        "explanation": "In KRaft mode, this metric tracks the offset of the last record committed by the active controller in the metadata partition. It provides visibility into how up-to-date the controller’s metadata is. Monitoring it helps ensure the controller is committing records as expected. The applied offset, record count, and lag are covered by other metrics."
    },
    {
        "question": "What is the purpose of the `metadata.max.idle.interval.ms` configuration in KRaft mode?",
        "options": [
            "To set the maximum time allowed for a metadata request to be idle before it is cancelled",
            "To specify the maximum time the active controller can be idle before a new controller is elected",
            "To configure the frequency at which the active controller writes no-op records to the metadata partition",
            "To define the maximum interval allowed between two consecutive metadata log segments"
        ],
        "answer": "To configure the frequency at which the active controller writes no-op records to the metadata partition",
        "explanation": "In KRaft mode, `metadata.max.idle.interval.ms` defines how often the active controller writes no-op (heartbeat) records to the metadata partition when there are no new updates. The default is 5000 ms (5 seconds). These no-op records keep followers synchronized and ensure metadata liveness. It doesn’t control idle request timeout, controller election, or log segment intervals."
    },
    {
        "question": "What is the role of the `kafka.controller:type=QuorumController,name=MaxFollowerLag` metric in KRaft mode?",
        "options": [
            "It measures the maximum lag between the active controller and the last committed record in the metadata partition",
            "It indicates the maximum lag between the active controller and the followers in terms of metadata records",
            "It represents the maximum number of records that a follower can lag behind the active controller",
            "It tracks the maximum lag between the followers and the last applied record in the metadata partition"
        ],
        "answer": "It indicates the maximum lag between the active controller and the followers in terms of metadata records",
        "explanation": "In KRaft mode, the `MaxFollowerLag` metric shows the maximum lag between the active controller and its followers, measured in metadata records. It helps identify if followers are falling behind in replicating metadata updates. A high value indicates synchronization issues. It doesn’t measure lag to committed records or applied offsets."
    },
    {
        "question": "What is the significance of the `kafka.server:type=SnapshotEmitter,name=LatestSnapshotGeneratedAgeMs` metric in KRaft mode?",
        "options": [
            "It indicates the age of the latest snapshot in milliseconds since the snapshot was generated",
            "It measures the time taken to generate the latest snapshot in milliseconds",
            "It represents the age of the latest snapshot in milliseconds since the process was started",
            "It tracks the time elapsed since the latest snapshot was loaded in milliseconds"
        ],
        "answer": "It indicates the age of the latest snapshot in milliseconds since the snapshot was generated",
        "explanation": "In KRaft mode, this metric measures how long ago the most recent metadata snapshot was created. Snapshots capture the controller’s state for faster recovery and log compaction. Monitoring this metric ensures snapshots are generated regularly. It does not indicate snapshot creation duration or process start time."
    },
    {
        "question": "What is the purpose of the `kafka.controller:type=KafkaController,name=ControlledShutdownCount` metric in KRaft mode?",
        "options": [
            "It measures the number of controlled shutdown requests received by the controller",
            "It indicates the number of brokers that have completed a controlled shutdown",
            "It represents the number of brokers that are currently in the process of controlled shutdown",
            "It tracks the number of controlled shutdown failures experienced by the controller"
        ],
        "answer": "It indicates the number of brokers that have completed a controlled shutdown",
        "explanation": "In KRaft mode, this metric counts brokers that have successfully completed a controlled shutdown. Controlled shutdown ensures a broker gracefully hands off partitions before stopping. The metric helps track rolling restarts or maintenance. It doesn’t measure requests, failures, or in-progress shutdowns."
    },
    {
        "question": "What is the significance of the `kafka.controller:type=KafkaController,name=GlobalTopicCount` metric in KRaft mode?",
        "options": [
            "It represents the total number of topics in the Kafka cluster",
            "It indicates the number of global topics that are not associated with any specific cluster",
            "It measures the number of topics that have global replication enabled",
            "It tracks the count of topics that are globally accessible across all Kafka clusters"
        ],
        "answer": "It represents the total number of topics in the Kafka cluster",
        "explanation": "In KRaft mode, the `GlobalTopicCount` metric shows the total number of topics (both internal and user-created) in the cluster. Monitoring it helps with capacity planning and tracking topic creation/deletion trends. It does not refer to cross-cluster or globally replicated topics."
    },
    {
        "question": "What is the purpose of the `kafka.controller:type=KafkaController,name=TopicDeletionCount` metric in KRaft mode?",
        "options": [
            "It measures the number of topics that have been marked for deletion",
            "It indicates the number of topics that have been successfully deleted",
            "It represents the count of failed topic deletion attempts",
            "It tracks the number of topics that are currently in the process of being deleted"
        ],
        "answer": "It indicates the number of topics that have been successfully deleted",
        "explanation": "In KRaft mode, this metric counts the topics successfully deleted from the cluster. Each time a topic is fully removed, the counter increases. It helps track deletion activity and cluster cleanup. It doesn’t count topics merely marked for deletion or failed attempts."
    },
    {
        "question": "What is the significance of the `kafka.controller:type=KafkaController,name=TopicChangeRate` metric in KRaft mode?",
        "options": [
            "It measures the rate at which new topics are being created in the Kafka cluster",
            "It indicates the rate at which existing topics are being modified or updated",
            "It represents the rate at which topics are being deleted from the Kafka cluster",
            "It tracks the overall rate of topic-related changes, including creation, modification, and deletion"
        ],
        "answer": "It tracks the overall rate of topic-related changes, including creation, modification, and deletion",
        "explanation": "In KRaft mode, the `TopicChangeRate` metric tracks how frequently topic-related changes occur in the cluster — including topic creation, configuration updates, and deletions. It reflects the dynamic activity of topic management. High rates may indicate frequent admin operations or automation processes."
    },
    {
        "question": "What is the purpose of the `kafka.controller:type=ControllerChannelManager,name=TotalQueueSize` metric in KRaft mode?",
        "options": [
            "It measures the total number of messages in the controller's request queue",
            "It indicates the total size of the metadata log in bytes",
            "It represents the total number of active controller connections",
            "It tracks the total number of pending controller requests"
        ],
        "answer": "It measures the total number of messages in the controller's request queue",
        "explanation": "The `TotalQueueSize` metric tracks how many requests are queued for processing by the controller. A high value means the controller is overloaded or slow to process requests, potentially causing latency and instability."
    },
    {
        "question": "What is the impact of having a large value for the `controller.quorum.request.timeout.ms` configuration in KRaft mode?",
        "options": [
            "It increases the time the controller waits for a quorum of voters to respond to a request",
            "It reduces the time the controller waits for a quorum of voters to respond to a request",
            "It sets the maximum time allowed for the controller to process a request",
            "It determines the frequency at which the controller sends heartbeats to the brokers"
        ],
        "answer": "It increases the time the controller waits for a quorum of voters to respond to a request",
        "explanation": "A higher `controller.quorum.request.timeout.ms` allows more time for voters to respond but delays failure detection and response. The default (2000 ms) usually balances responsiveness and stability."
    },
    {
        "question": "What is the purpose of the `kafka.controller:type=QuorumController,name=LastCommittedRecordOffset` metric in KRaft mode?",
        "options": [
            "It indicates the offset of the last record appended to the metadata log",
            "It represents the offset of the last record replicated to all the controllers",
            "It measures the offset of the last record applied by the active controller",
            "It tracks the offset of the last record committed by the active controller"
        ],
        "answer": "It tracks the offset of the last record committed by the active controller",
        "explanation": "This metric shows the offset of the most recent metadata record successfully committed by a quorum of controllers. It reflects progress in metadata replication and durability."
    }
];
