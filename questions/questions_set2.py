questions_set2 = [
    {
        "question": "How can you view the current configuration of a Kafka topic?",
        "options": [
            "Use the kafka-topics.sh --describe command",
            "Use the kafka-configs.sh --describe command",
            "Use the zookeeper-shell.sh command to navigate to the topic's configuration znode",
            "Look in the Kafka broker's log files for the topic configuration"
        ],
        "answer": "Use the kafka-configs.sh --describe command",
        "explanation": (
            "To view a Kafka topic's configuration, use:\n\n"
            "`kafka-configs.sh --bootstrap-server <broker> --entity-type topics --entity-name <topic> --describe`\n\n"
            "This command displays topic-level configurations such as retention, cleanup policy, and compression type. "
            "`kafka-topics.sh --describe` shows metadata (like partition count), not configuration properties."
        )
    },
    {
        "question": "What is the default behavior of kafka-console-consumer when no consumer group is specified?",
        "options": [
            "It joins a random consumer group",
            "It creates a new consumer group with a generated name",
            "It fails with an error indicating that a consumer group must be specified",
            "It consumes messages without joining any consumer group"
        ],
        "answer": "It creates a new consumer group with a generated name",
        "explanation": (
            "If you don't specify a consumer group using `--group`, the kafka-console-consumer creates a unique "
            "consumer group automatically, named something like `console-consumer-<random-string>`."
        )
    },
    {
        "question": "How does the kafka-console-consumer behave when you specify the --from-beginning option?",
        "options": [
            "It starts consuming messages from the earliest available offset in the assigned partitions",
            "It starts consuming messages from the latest available offset in the assigned partitions",
            "It starts consuming messages from a specific offset that you provide",
            "It starts consuming messages from a random offset in the assigned partitions"
        ],
        "answer": "It starts consuming messages from the earliest available offset in the assigned partitions",
        "explanation": (
            "`--from-beginning` makes the consumer start from the earliest offset. Without it, "
            "it starts from the latest offset and only reads new messages."
        )
    },
    {
        "question": "What happens when you run multiple instances of kafka-console-consumer with the same consumer group?",
        "options": [
            "The instances will consume messages independently, each receiving a copy of every message",
            "The instances will collaborate and distribute the partitions among themselves for parallel consumption",
            "The instances will compete for messages, and each message will be consumed by only one instance",
            "The instances will consume messages in a round-robin fashion, with each instance receiving a subset of messages"
        ],
        "answer": "The instances will collaborate and distribute the partitions among themselves for parallel consumption",
        "explanation": (
            "Consumers in the same group share partitions among themselves. Each partition is processed by only one "
            "consumer in the group — allowing parallel processing and fault tolerance."
        )
    },
    {
        "question": "How can you create a topic named 'test' with 3 partitions and a replication factor of 2 using the Kafka CLI?",
        "options": [
            "kafka-topics.sh --create --zookeeper localhost:2181 --topic test --partitions 3 --replication-factor 2",
            "kafka-topics.sh --create --bootstrap-server localhost:9092 --topic test --partitions 3 --replication-factor 2",
            "kafka-console-producer.sh --broker-list localhost:9092 --topic test --partitions 3 --replication-factor 2",
            "kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --partitions 3 --replication-factor 2"
        ],
        "answer": "kafka-topics.sh --create --bootstrap-server localhost:9092 --topic test --partitions 3 --replication-factor 2",
        "explanation": (
            "The correct command uses `kafka-topics.sh` with `--bootstrap-server`, not the deprecated `--zookeeper`."
        )
    },
    {
        "question": "Which command can you use to list all the topics in a Kafka cluster?",
        "options": [
            "kafka-topics.sh --list --zookeeper localhost:2181",
            "kafka-topics.sh --list --bootstrap-server localhost:9092",
            "kafka-console-producer.sh --list --broker-list localhost:9092",
            "kafka-console-consumer.sh --list --bootstrap-server localhost:9092"
        ],
        "answer": "kafka-topics.sh --list --bootstrap-server localhost:9092",
        "explanation": (
            "Use `kafka-topics.sh --list --bootstrap-server localhost:9092` to list all topics. "
            "The `--zookeeper` flag is deprecated."
        )
    },
    {
        "question": "How can you describe the configuration of a topic named 'test' using the Kafka CLI?",
        "options": [
            "kafka-topics.sh --describe --topic test --zookeeper localhost:2181",
            "kafka-topics.sh --describe --topic test --bootstrap-server localhost:9092",
            "kafka-configs.sh --describe --entity-type topics --entity-name test --zookeeper localhost:2181",
            "kafka-configs.sh --describe --entity-type topics --entity-name test --bootstrap-server localhost:9092"
        ],
        "answer": "kafka-configs.sh --describe --entity-type topics --entity-name test --bootstrap-server localhost:9092",
        "explanation": (
            "To view topic configuration, use `kafka-configs.sh` with `--bootstrap-server`. "
            "`kafka-topics.sh` shows metadata, not configuration properties."
        )
    },
    {
        "question": "Which Kafka CLI command is used to produce messages to a topic?",
        "options": [
            "kafka-console-producer.sh",
            "kafka-console-consumer.sh",
            "kafka-topics.sh",
            "kafka-configs.sh"
        ],
        "answer": "kafka-console-producer.sh",
        "explanation": (
            "Use `kafka-console-producer.sh` to send messages from the console to a Kafka topic."
        )
    },
    {
        "question": "How can you consume messages from the beginning of a topic named 'test' using the Kafka CLI?",
        "options": [
            "kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning",
            "kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test",
            "kafka-console-producer.sh --bootstrap-server localhost:9092 --topic test --from-beginning",
            "kafka-console-producer.sh --bootstrap-server localhost:9092 --topic test"
        ],
        "answer": "kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning",
        "explanation": (
            "`--from-beginning` makes the consumer start from the earliest offset, allowing it to read all available messages."
        )
    },
    {
        "question": "What is the purpose of the --group option in kafka-console-consumer.sh?",
        "options": [
            "To specify the consumer group ID for the console consumer",
            "To specify the number of consumer instances in the group",
            "To specify the list of topics to consume from",
            "To specify the bootstrap server for the consumer"
        ],
        "answer": "To specify the consumer group ID for the console consumer",
        "explanation": (
            "The `--group` flag sets the consumer group ID. Consumers with the same group share topic partitions for parallel processing."
        )
    },
    {
        "question": "How can you view the current configuration of a Kafka topic?",
        "options": [
            "Use the kafka-topics.sh --describe command",
            "Use the kafka-configs.sh --describe command",
            "Use the zookeeper-shell.sh command to navigate to the topic's configuration znode",
            "Look in the Kafka broker's log files for the topic configuration"
        ],
        "answer": "Use the kafka-configs.sh --describe command",
        "explanation": "Use `kafka-configs.sh --describe` to view configuration properties such as retention, cleanup policy, and compression."
    },
    {
        "question": "What is the default behavior of the kafka-console-consumer when no consumer group is specified?",
        "options": [
            "It joins a random consumer group",
            "It creates a new consumer group with a generated name",
            "It fails with an error indicating that a consumer group must be specified",
            "It consumes messages without joining any consumer group"
        ],
        "answer": "It creates a new consumer group with a generated name",
        "explanation": "Without `--group`, kafka-console-consumer creates a temporary consumer group like `console-consumer-<random>`."
    },
    {
        "question": "How does the kafka-console-consumer behave when you specify the --from-beginning option?",
        "options": [
            "It starts consuming messages from the earliest available offset",
            "It starts consuming from the latest offset",
            "It starts consuming from a specific offset you provide",
            "It starts consuming from a random offset"
        ],
        "answer": "It starts consuming messages from the earliest available offset",
        "explanation": "The `--from-beginning` option tells Kafka to read from the earliest available offset."
    },
    {
        "question": "What happens when you run multiple instances of kafka-console-consumer with the same consumer group?",
        "options": [
            "Each instance receives a copy of every message",
            "They share partitions for parallel consumption",
            "They compete for messages randomly",
            "They consume messages in round-robin fashion"
        ],
        "answer": "They share partitions for parallel consumption",
        "explanation": "Consumers in the same group divide topic partitions among themselves for load balancing."
    },
    {
        "question": "How can you create a topic named 'test' with 3 partitions and replication factor 2?",
        "options": [
            "kafka-topics.sh --create --zookeeper localhost:2181 --topic test --partitions 3 --replication-factor 2",
            "kafka-topics.sh --create --bootstrap-server localhost:9092 --topic test --partitions 3 --replication-factor 2",
            "kafka-console-producer.sh --broker-list localhost:9092 --topic test --partitions 3 --replication-factor 2",
            "kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --partitions 3 --replication-factor 2"
        ],
        "answer": "kafka-topics.sh --create --bootstrap-server localhost:9092 --topic test --partitions 3 --replication-factor 2",
        "explanation": "Use `kafka-topics.sh --create` with `--bootstrap-server` for topic creation."
    },
    {
        "question": "Which command lists all topics in a Kafka cluster?",
        "options": [
            "kafka-topics.sh --list --zookeeper localhost:2181",
            "kafka-topics.sh --list --bootstrap-server localhost:9092",
            "kafka-console-producer.sh --list --broker-list localhost:9092",
            "kafka-console-consumer.sh --list --bootstrap-server localhost:9092"
        ],
        "answer": "kafka-topics.sh --list --bootstrap-server localhost:9092",
        "explanation": "Use `kafka-topics.sh --list` with `--bootstrap-server` to view topics."
    },
    {
        "question": "How can you describe the configuration of a topic named 'test'?",
        "options": [
            "kafka-topics.sh --describe --topic test --zookeeper localhost:2181",
            "kafka-topics.sh --describe --topic test --bootstrap-server localhost:9092",
            "kafka-configs.sh --describe --entity-type topics --entity-name test --zookeeper localhost:2181",
            "kafka-configs.sh --describe --entity-type topics --entity-name test --bootstrap-server localhost:9092"
        ],
        "answer": "kafka-configs.sh --describe --entity-type topics --entity-name test --bootstrap-server localhost:9092",
        "explanation": "Use `kafka-configs.sh --describe` with `--entity-type topics` and `--bootstrap-server`."
    },
    {
        "question": "Which Kafka CLI command is used to produce messages to a topic?",
        "options": [
            "kafka-console-producer.sh",
            "kafka-console-consumer.sh",
            "kafka-topics.sh",
            "kafka-configs.sh"
        ],
        "answer": "kafka-console-producer.sh",
        "explanation": "Use `kafka-console-producer.sh` to send messages to a Kafka topic."
    },
    {
        "question": "How can you consume messages from the beginning of a topic named 'test'?",
        "options": [
            "kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning",
            "kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test",
            "kafka-console-producer.sh --bootstrap-server localhost:9092 --topic test --from-beginning",
            "kafka-console-producer.sh --bootstrap-server localhost:9092 --topic test"
        ],
        "answer": "kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning",
        "explanation": "Add `--from-beginning` to consume from earliest offsets."
    },
    {
        "question": "What is the purpose of the --group option in kafka-console-consumer?",
        "options": [
            "To specify the consumer group ID",
            "To specify the number of consumer instances",
            "To specify the topics to consume",
            "To specify the bootstrap server"
        ],
        "answer": "To specify the consumer group ID",
        "explanation": "The `--group` option defines the consumer group for offset management."
    },
    # Questions 11–20
    {
        "question": "How can you delete a topic named 'test'?",
        "options": [
            "kafka-topics.sh --delete --topic test --zookeeper localhost:2181",
            "kafka-topics.sh --delete --topic test --bootstrap-server localhost:9092",
            "kafka-configs.sh --delete --entity-type topics --entity-name test --bootstrap-server localhost:9092",
            "kafka-console-producer.sh --delete --topic test --bootstrap-server localhost:9092"
        ],
        "answer": "kafka-topics.sh --delete --topic test --bootstrap-server localhost:9092",
        "explanation": "Use `kafka-topics.sh --delete` with `--bootstrap-server` to delete topics."
    },
    {
        "question": "What command resets offsets for a consumer group?",
        "options": [
            "kafka-consumer-groups.sh --reset-offsets",
            "kafka-topics.sh --reset-offsets",
            "kafka-console-consumer.sh --reset-offsets",
            "kafka-configs.sh --reset-offsets"
        ],
        "answer": "kafka-consumer-groups.sh --reset-offsets",
        "explanation": "Offset resets are managed by `kafka-consumer-groups.sh`."
    },
    {
        "question": "How can you check consumer group lag?",
        "options": [
            "kafka-consumer-groups.sh --describe --group <group-id> --bootstrap-server localhost:9092",
            "kafka-topics.sh --describe --group <group-id> --bootstrap-server localhost:9092",
            "kafka-configs.sh --describe --group <group-id> --bootstrap-server localhost:9092",
            "kafka-console-consumer.sh --describe --group <group-id> --bootstrap-server localhost:9092"
        ],
        "answer": "kafka-consumer-groups.sh --describe --group <group-id> --bootstrap-server localhost:9092",
        "explanation": "Use `kafka-consumer-groups.sh --describe` to see consumer lag."
    },
    {
        "question": "Which command increases partitions for a topic?",
        "options": [
            "kafka-topics.sh --alter --topic <topic-name> --partitions <number> --bootstrap-server localhost:9092",
            "kafka-topics.sh --create --topic <topic-name> --partitions <number> --bootstrap-server localhost:9092",
            "kafka-configs.sh --alter --entity-type topics --entity-name <topic-name> --partitions <number> --bootstrap-server localhost:9092",
            "kafka-console-producer.sh --alter --topic <topic-name> --partitions <number> --bootstrap-server localhost:9092"
        ],
        "answer": "kafka-topics.sh --alter --topic <topic-name> --partitions <number> --bootstrap-server localhost:9092",
        "explanation": "Use `kafka-topics.sh --alter` to increase partitions."
    },
    {
        "question": "How can you view the log of a specific Kafka topic?",
        "options": [
            "kafka-log-dirs.sh --describe --topic <topic-name> --bootstrap-server localhost:9092",
            "kafka-console-consumer.sh --topic <topic-name> --from-beginning --bootstrap-server localhost:9092",
            "kafka-topics.sh --describe --topic <topic-name> --bootstrap-server localhost:9092",
            "kafka-console-producer.sh --log --topic <topic-name> --bootstrap-server localhost:9092"
        ],
        "answer": "kafka-console-consumer.sh --topic <topic-name> --from-beginning --bootstrap-server localhost:9092",
        "explanation": "Use `kafka-console-consumer.sh` to view messages (logs)."
    },
    {
        "question": "Which command changes Kafka broker configuration?",
        "options": [
            "kafka-configs.sh --alter --entity-type brokers --entity-name <broker-id> --add-config <key>=<value> --bootstrap-server localhost:9092",
            "kafka-configs.sh --alter --entity-type brokers --entity-name <broker-id> --add-config <key>=<value> --zookeeper localhost:2181",
            "kafka-topics.sh --alter --entity-type brokers --entity-name <broker-id> --add-config <key>=<value> --bootstrap-server localhost:9092",
            "kafka-topics.sh --alter --entity-type brokers --entity-name <broker-id> --add-config <key>=<value> --zookeeper localhost:2181"
        ],
        "answer": "kafka-configs.sh --alter --entity-type brokers --entity-name <broker-id> --add-config <key>=<value> --bootstrap-server localhost:9092",
        "explanation": "Broker configs are modified via `kafka-configs.sh --alter`."
    },
    {
        "question": "How can you reassign partitions in a Kafka cluster?",
        "options": [
            "kafka-reassign-partitions.sh --execute --reassignment-json-file <file-path> --bootstrap-server localhost:9092",
            "kafka-topics.sh --execute --reassignment-json-file <file-path> --bootstrap-server localhost:9092",
            "kafka-console-producer.sh --execute --reassignment-json-file <file-path> --bootstrap-server localhost:9092",
            "kafka-configs.sh --execute --reassignment-json-file <file-path> --bootstrap-server localhost:9092"
        ],
        "answer": "kafka-reassign-partitions.sh --execute --reassignment-json-file <file-path> --bootstrap-server localhost:9092",
        "explanation": "Partition reassignments are handled by `kafka-reassign-partitions.sh`."
    },
    {
        "question": "Which command creates a consumer group in Kafka?",
        "options": [
            "kafka-console-consumer.sh --create-group --group <group-id> --bootstrap-server localhost:9092",
            "kafka-consumer-groups.sh --create --group <group-id> --bootstrap-server localhost:9092",
            "kafka-topics.sh --create-group --group <group-id> --bootstrap-server localhost:9092",
            "Kafka consumer groups are created automatically when a consumer joins"
        ],
        "answer": "Kafka consumer groups are created automatically when a consumer joins",
        "explanation": "Kafka creates consumer groups automatically at first join."
    },
    {
        "question": "How can you move messages from one Kafka topic to another?",
        "options": [
            "kafka-reassign-partitions.sh --source-topic <source> --destination-topic <dest> --bootstrap-server localhost:9092",
            "Use a combination of kafka-console-consumer.sh and kafka-console-producer.sh",
            "kafka-topics.sh --move --source-topic <source> --destination-topic <dest> --bootstrap-server localhost:9092",
            "kafka-console-producer.sh --move --source-topic <source> --destination-topic <dest> --bootstrap-server localhost:9092"
        ],
        "answer": "Use a combination of kafka-console-consumer.sh and kafka-console-producer.sh",
        "explanation": "Use `kafka-console-consumer` to read and `kafka-console-producer` to write."
    },
    {
        "question": "What is the purpose of the --offset option in kafka-console-consumer?",
        "options": [
            "To specify the starting offset for consuming messages",
            "To specify the offset for deletion",
            "To specify offset for producing messages",
            "To reset offset for a consumer group"
        ],
        "answer": "To specify the starting offset for consuming messages",
        "explanation": "`--offset` allows consumption from a specific offset number."
    },
    {
        "question": "Which of the following is stored in Zookeeper for a Kafka cluster? (Select two)",
        "options": [
            "Consumer offsets",
            "Kafka broker information",
            "Topic partition assignments",
            "Topic-level configurations",
            "Producer client IDs"
        ],
        "answer": ["Kafka broker information", "Topic-level configurations"],
        "explanation": "ZooKeeper stores metadata like broker info and topic configurations. Consumer offsets are stored in `__consumer_offsets`."
    },
    {
        "question": "A Kafka topic has 6 partitions and replication factor of 3. How many replicas per partition exist?",
        "options": ["1", "2", "3", "6"],
        "answer": "3",
        "explanation": "Each partition has 3 replicas distributed across brokers (1 leader + 2 followers)."
    },
    {
        "question": "What happens when a Kafka broker goes down?",
        "options": [
            "All replicas are lost",
            "Replicas are redistributed",
            "Replicas become unavailable until restart",
            "Replicas are promoted immediately"
        ],
        "answer": "Replicas become unavailable until restart",
        "explanation": "Replicas on a failed broker become temporarily unavailable. Followers can take over if leaders fail."
    },
    {
        "question": "How does Kafka ensure data consistency?",
        "options": [
            "Two-phase commit",
            "ZooKeeper consensus",
            "Leader-follower replication",
            "Gossip protocol"
        ],
        "answer": "Leader-follower replication",
        "explanation": "Kafka uses a leader-follower model to replicate data and ensure consistency."
    },
    {
        "question": "Which of the following KSQL statements will cause writes to a Kafka topic? (Select two)",
        "options": [
            "CREATE STREAM FROM_TOPIC AS SELECT * FROM source_topic;",
            "CREATE TABLE FROM_TOPIC AS SELECT * FROM source_topic;",
            "SELECT * FROM source_topic EMIT CHANGES;",
            "DESCRIBE source_topic;",
            "SHOW QUERIES;"
        ],
        "answer": ["CREATE STREAM FROM_TOPIC AS SELECT * FROM source_topic;", "CREATE TABLE FROM_TOPIC AS SELECT * FROM source_topic;"],
        "explanation": "In KSQL, CREATE STREAM AS SELECT and CREATE TABLE AS SELECT continuously write output to Kafka topics. SELECT EMIT CHANGES outputs to the console only."
    },
    {
        "question": "What happens when you run a CREATE STREAM statement without an AS SELECT clause in KSQL?",
        "options": [
            "It creates a new stream and writes metadata to the KSQL command topic.",
            "It creates a new stream and starts writing data to it from the KSQL application.",
            "It fails because CREATE STREAM must always include an AS SELECT clause.",
            "It creates a new empty stream but doesn't write anything to Kafka."
        ],
        "answer": "It creates a new stream and writes metadata to the KSQL command topic.",
        "explanation": "CREATE STREAM without AS SELECT registers a stream on an existing Kafka topic, writing metadata to the command topic but not writing new data."
    },
    {
        "question": "What is the purpose of the PARTITIONS clause in a KSQL CREATE TABLE statement?",
        "options": [
            "To specify the number of partitions for the output Kafka topic",
            "To specify the partitioning key for the output Kafka topic",
            "To specify the number of partitions to read from the input Kafka topic",
            "To specify the partitioning key to read from the input Kafka topic"
        ],
        "answer": "To specify the number of partitions for the output Kafka topic",
        "explanation": "PARTITIONS defines how many partitions the output topic will have. The partitioning key is defined separately using the KEY clause."
    },
    {
        "question": "Which query type is not supported by KSQL?",
        "options": [
            "Stream-to-Stream JOINs",
            "Table-to-Table JOINs",
            "Stream-to-Table JOINs",
            "Complex Nested Queries"
        ],
        "answer": "Complex Nested Queries",
        "explanation": "KSQL supports Stream-to-Stream, Stream-to-Table, and Table-to-Table JOINs. Complex nested subqueries are not supported."
    },
    {
        "question": "What is a KSQL table?",
        "options": [
            "A mutable collection of key-value pairs",
            "An immutable, append-only collection of records",
            "A stateful, changelog-based table",
            "A temporary view of streaming data"
        ],
        "answer": "A stateful, changelog-based table",
        "explanation": "A KSQL table stores the latest value for each key, maintaining state via a changelog topic."
    },
    {
        "question": "Which KSQL function is used to convert a string to uppercase?",
        "options": ["UPPER()", "TO_UPPER()", "STRING_UPPER()", "CONVERT_UPPER()"],
        "answer": "UPPER()",
        "explanation": "UPPER() converts strings to uppercase in KSQL."
    },
    {
        "question": "What does the WINDOW clause in a KSQL query specify?",
        "options": [
            "The time frame for aggregations",
            "The filter condition for the query",
            "The key for partitioning the data",
            "The join condition between streams"
        ],
        "answer": "The time frame for aggregations",
        "explanation": "WINDOW defines the time range for time-based aggregations such as tumbling or hopping windows."
    },
    {
        "question": "Which data format is not supported by KSQL for serialization and deserialization?",
        "options": ["JSON", "Protobuf", "Avro", "Thrift"],
        "answer": "Thrift",
        "explanation": "KSQL supports JSON, Protobuf, and Avro. Thrift is not supported."
    },
    {
        "question": "How can you create a stream in KSQL from an existing Kafka topic?",
        "options": [
            "CREATE STREAM stream_name FROM topic_name;",
            "CREATE STREAM stream_name (columns) WITH (kafka_topic='topic_name', value_format='format');",
            "CREATE STREAM stream_name WITH (kafka_topic='topic_name', value_format='format');",
            "CREATE STREAM stream_name AS SELECT * FROM topic_name;"
        ],
        "answer": "CREATE STREAM stream_name (columns) WITH (kafka_topic='topic_name', value_format='format');",
        "explanation": "The correct syntax specifies columns and the topic/format details in the WITH clause."
    },
    {
        "question": "What is the purpose of the PARTITION BY clause in KSQL?",
        "options": [
            "To split the stream into multiple topics",
            "To repartition the data based on a specified column",
            "To create a new table from a stream",
            "To define the output format of the query"
        ],
        "answer": "To repartition the data based on a specified column",
        "explanation": "PARTITION BY changes the partition key of a stream to the specified column."
    },
    {
        "question": "Which KSQL function is used to concatenate two strings?",
        "options": ["CONCAT()", "JOIN()", "MERGE()", "APPEND()"],
        "answer": "CONCAT()",
        "explanation": "The CONCAT() function in KSQL is used to concatenate two strings. JOIN(), MERGE(), and APPEND() are not valid string functions in KSQL."
    },
    {
        "question": "What is the role of the KEY keyword in KSQL table creation?",
        "options": [
            "To define the primary key of the table",
            "To specify the partitioning key of the table",
            "To assign a unique identifier to each record",
            "To create an index on the table"
        ],
        "answer": "To define the primary key of the table",
        "explanation": "The KEY keyword defines the primary key in a KSQL table, which also determines how records are partitioned in Kafka."
    },
    {
        "question": "Which statement is true about KSQL streams?",
        "options": [
            "They store historical data indefinitely",
            "They are append-only collections of immutable records",
            "They can be directly queried for the current state",
            "They do not support windowed aggregations"
        ],
        "answer": "They are append-only collections of immutable records",
        "explanation": "Streams in KSQL represent real-time data flows that are append-only and immutable. They do support windowed aggregations."
    },
    {
        "question": "Which KSQL command is used to terminate a running query?",
        "options": ["DROP QUERY", "STOP QUERY", "TERMINATE", "DELETE QUERY"],
        "answer": "TERMINATE",
        "explanation": "The TERMINATE command is used in KSQL to stop a running query. DROP QUERY, STOP QUERY, and DELETE QUERY are invalid."
    },
    {
        "question": "What is the result of executing the following KSQL query: SELECT * FROM my_stream EMIT CHANGES;?",
        "options": [
            "It creates a new table from the stream",
            "It continuously outputs the current state of the stream",
            "It returns a snapshot of the stream at a point in time",
            "It filters records based on a condition"
        ],
        "answer": "It continuously outputs the current state of the stream",
        "explanation": "SELECT ... EMIT CHANGES continuously outputs real-time updates from the stream as new records arrive."
    },
    {
        "question": "Which clause in KSQL is used to define the duration of a hopping window?",
        "options": ["SIZE", "DURATION", "HOP", "WINDOW"],
        "answer": "SIZE",
        "explanation": "The SIZE clause specifies the duration of a hopping window. Other options are invalid for defining window duration."
    },
    {
        "question": "How can you perform an inner join between two streams in KSQL?",
        "options": [
            "CREATE STREAM new_stream AS SELECT * FROM stream1 INNER JOIN stream2 WITHIN 5 MINUTES ON stream1.key = stream2.key;",
            "CREATE STREAM new_stream AS SELECT * FROM stream1 JOIN stream2 ON stream1.key = stream2.key;",
            "CREATE STREAM new_stream AS SELECT * FROM stream1 LEFT JOIN stream2 WITHIN 5 MINUTES ON stream1.key = stream2.key;",
            "CREATE STREAM new_stream AS SELECT * FROM stream1 CROSS JOIN stream2 ON stream1.key = stream2.key;"
        ],
        "answer": "CREATE STREAM new_stream AS SELECT * FROM stream1 INNER JOIN stream2 WITHIN 5 MINUTES ON stream1.key = stream2.key;",
        "explanation": "Stream-to-stream joins in KSQL require an INNER JOIN and a WITHIN clause defining the time window. Option A is correct."
    },
    {
        "question": "What does the GROUP BY clause do in a KSQL query?",
        "options": [
            "It filters records based on a condition",
            "It partitions the data by a specified key",
            "It aggregates data based on specified columns",
            "It orders the data by a specified column"
        ],
        "answer": "It aggregates data based on specified columns",
        "explanation": "GROUP BY in KSQL aggregates data based on specific columns to perform operations like COUNT, SUM, or AVG."
    },
    {
        "question": "Which keyword is used to create a persistent query in KSQL?",
        "options": ["PERSIST", "CREATE STREAM AS", "CREATE PERSISTENT QUERY", "SAVE"],
        "answer": "CREATE STREAM AS",
        "explanation": "CREATE STREAM AS (CSAS) creates a persistent query in KSQL that continuously writes output to a Kafka topic."
    },
    {
        "question": "Which function is used to calculate the number of records in a KSQL stream?",
        "options": ["COUNT()", "SUM()", "AVG()", "MAX()"],
        "answer": "COUNT()",
        "explanation": "The COUNT() function counts the number of records in a KSQL stream. SUM(), AVG(), and MAX() perform other aggregations."
    },
    {
        "question": "How can you convert a stream into a table in KSQL?",
        "options": [
            "CREATE TABLE table_name AS SELECT * FROM stream_name;",
            "INSERT INTO table_name SELECT * FROM stream_name;",
            "CREATE TABLE table_name FROM stream_name;",
            "CONVERT STREAM stream_name TO TABLE table_name;"
        ],
        "answer": "CREATE TABLE table_name AS SELECT * FROM stream_name;",
        "explanation": "The correct syntax to convert a stream into a table in KSQL is 'CREATE TABLE table_name AS SELECT * FROM stream_name;'. The other options are not valid KSQL syntaxes for this operation."
    },
    {
        "question": "What is the purpose of the 'AVRO' format in KSQL?",
        "options": [
            "To provide a human-readable format for data",
            "To enable complex data types and schema evolution",
            "To ensure data is stored as plain text",
            "To simplify data parsing"
        ],
        "answer": "To enable complex data types and schema evolution",
        "explanation": "The AVRO format is a binary serialization format that supports complex data structures and schema evolution. It’s efficient and widely used with KSQL for rich data handling."
    },
    {
        "question": "Which KSQL function is used to extract the year from a timestamp?",
        "options": [
            "EXTRACTYEAR()",
            "GETYEAR()",
            "YEAR()",
            "EXTRACT(YEAR FROM timestamp)"
        ],
        "answer": "EXTRACT(YEAR FROM timestamp)",
        "explanation": "The EXTRACT(YEAR FROM timestamp) function in KSQL extracts the year from a timestamp. Other forms like EXTRACTYEAR() or GETYEAR() are invalid."
    },
    {
        "question": "How do you handle null values in KSQL?",
        "options": [
            "Use the IS NULL and IS NOT NULL predicates",
            "Use the NULLIFY() function",
            "Replace null values with default values using COALESCE()",
            "Both A and C"
        ],
        "answer": "Both A and C",
        "explanation": "Null values can be handled using IS NULL and IS NOT NULL predicates for filtering, and COALESCE() to replace nulls with default values. NULLIFY() is not a valid function."
    },
    {
        "question": "Which KSQL function calculates the total sum of a column's values?",
        "options": ["SUM()", "TOTAL()", "ADD()", "AGGREGATE()"],
        "answer": "SUM()",
        "explanation": "The SUM() function in KSQL computes the total sum of a column’s numeric values. Other listed options are not valid KSQL functions for this purpose."
    },
    {
        "question": "What is the default retention period for KSQL streams?",
        "options": ["7 days", "1 day", "1 week", "2 days"],
        "answer": "7 days",
        "explanation": (
            "By default, KSQL streams inherit the retention settings from Kafka topics, which is typically 7 days. "
            "You can adjust it with the RETENTION property or topic configuration."
        )
    },
    {
        "question": "How can you filter records in a KSQL stream?",
        "options": ["By using the FILTER clause", "By using the WHERE clause", "By using the HAVING clause", "By using the LIMIT clause"],
        "answer": "By using the WHERE clause",
        "explanation": "Records in a KSQL stream can be filtered using the WHERE clause, which allows conditional selection of rows. FILTER, HAVING, and LIMIT are not used for filtering streams directly."
    },
    {
        "question": "Which KSQL function can be used to format timestamps?",
        "options": ["FORMAT_TIMESTAMP()", "TO_TIMESTAMP()", "DATE_FORMAT()", "TIMESTAMP_FORMAT()"],
        "answer": "DATE_FORMAT()",
        "explanation": "The DATE_FORMAT() function in KSQL formats timestamps into readable date/time strings according to the specified pattern."
    },
    {
        "question": "For a system designed to read data from an external database, perform some transformations, and then store the results in a Kafka topic, which approach is most suitable?",
        "options": [
            "Consumer + Producer",
            "Kafka Connect Source",
            "Kafka Connect Sink",
            "Kafka Streams"
        ],
        "answer": "Kafka Connect Source",
        "explanation": "Kafka Connect Source connectors are used to import data from external systems into Kafka topics. They can perform transformations before publishing data into Kafka."
    },
    {
        "question": "When needing to aggregate real-time data from a Kafka topic, compute running totals, and then publish those totals back to another Kafka topic for further analysis, which tool should you use?",
        "options": [
            "Consumer + Producer",
            "Kafka Connect Source",
            "Kafka Connect Sink",
            "Kafka Streams"
        ],
        "answer": "Kafka Streams",
        "explanation": "Kafka Streams is designed for building real-time data processing applications. It supports stateful operations like aggregations, joins, and windowing, making it ideal for real-time analytics."
    },
    {
        "question": "If the objective is to periodically export data from a Kafka topic to a relational database for long-term storage and analysis, which Kafka component would best fulfill this requirement?",
        "options": [
            "Consumer + Producer",
            "Kafka Connect Source",
            "Kafka Connect Sink",
            "Kafka Streams"
        ],
        "answer": "Kafka Connect Sink",
        "explanation": "Kafka Connect Sink connectors are used to export data from Kafka topics into external systems like relational databases, data warehouses, or search indexes."
    },
    {
        "question": "A financial institution wants to analyze transaction data in real-time to detect fraudulent activities. The transaction data, which includes sensitive information, is initially stored in a mainframe system. Which approach ensures secure, real-time analysis of this data by a Kafka Streams application while complying with data privacy regulations?",
        "options": [
            "Utilize a mainframe connector with Kafka Connect to ingest the transaction data into a Kafka topic. Apply a Kafka Streams application to anonymize sensitive information in the stream before conducting fraud analysis.",
            "Directly connect the mainframe system to the Kafka Streams application using a custom API, ensuring sensitive data is filtered out during the streaming process.",
            "Employ ksqlDB to directly query the mainframe system, apply data anonymization functions to filter out sensitive information, and then write the sanitized data to a Kafka topic for stream processing.",
            "Implement a batch process to extract transaction data periodically from the mainframe, cleanse the data of sensitive information, and then load the sanitized data into Kafka topics for streaming analysis."
        ],
        "answer": "Utilize a mainframe connector with Kafka Connect to ingest the transaction data into a Kafka topic. Apply a Kafka Streams application to anonymize sensitive information in the stream before conducting fraud analysis.",
        "explanation": "Kafka Connect allows secure ingestion from mainframe systems into Kafka. Kafka Streams can then anonymize sensitive information in-flight before analysis, ensuring compliance with privacy regulations."
    },
    {
        "question": "Your organization aims to implement a real-time recommendation engine for e-commerce users based on their browsing behavior. User session data is considered sensitive and must be anonymized before processing. How can the Kafka ecosystem be leveraged to meet these requirements?",
        "options": [
            "Deploy a Kafka Connect Source Connector to capture session data directly into Kafka, using Stream Processing to anonymize user identifiers before aggregating sessions for recommendation analysis.",
            "Use a custom Kafka Producer application to publish session data to a topic, applying a Stream Processor to anonymize and then process the data for generating recommendations.",
            "Implement a Kafka Connect Sink Connector to store session data into a NoSQL database, with a pre-processor to remove sensitive information before ingestion. Use Kafka Streams to read from the database for analysis.",
            "Create a ksqlDB process to pull session data from source systems, apply anonymization functions within ksqlDB, and output the clean data to a Kafka topic for further processing by the Kafka Streams application."
        ],
        "answer": "Deploy a Kafka Connect Source Connector to capture session data directly into Kafka, using Stream Processing to anonymize user identifiers before aggregating sessions for recommendation analysis.",
        "explanation": "Using Kafka Connect Source connectors simplifies ingestion from multiple data sources. Kafka Streams can then handle real-time anonymization and recommendation logic efficiently."
    },
    {
        "question": "An organization is implementing a system to monitor and alert on infrastructure health status in real-time. The system collects metrics from various sources, including some that contain proprietary information. Which approach ensures that only non-proprietary, critical health metrics are analyzed and alerted on?",
        "options": [
            "Use Kafka Connect with appropriate Source Connectors for each metric source, configuring the connectors to filter out proprietary information. Process the filtered metrics stream with Kafka Streams for alerting.",
            "Directly stream all metrics into Kafka using custom Producers, then employ a Kafka Streams application to separate proprietary data from non-proprietary data, and analyze the latter for alerting.",
            "Implement a series of ksqlDB statements to ingest metrics into Kafka, applying filtering logic within ksqlDB to remove proprietary information before streaming processing and alerting.",
            "Configure a Kafka Connect Sink Connector to aggregate all metrics into a centralized database, followed by batch processing to remove proprietary information before streaming the data into Kafka for real-time analysis."
        ],
        "answer": "Use Kafka Connect with appropriate Source Connectors for each metric source, configuring the connectors to filter out proprietary information. Process the filtered metrics stream with Kafka Streams for alerting.",
        "explanation": "Kafka Connect can handle source-level filtering, reducing exposure of sensitive data early in the pipeline. Kafka Streams then processes only relevant metrics for real-time alerting."
    },
    {
        "question": "A multinational corporation is looking to aggregate sales data from multiple regional systems into a centralized Kafka topic for real-time analysis and reporting. The regional systems vary in technology, including SQL databases and cloud-based storage solutions. Which solution enables the efficient and unified ingestion of these diverse data sources into Kafka?",
        "options": [
            "Deploy Kafka Streams applications near each regional system to collect and forward data to the centralized Kafka topic.",
            "Use Kafka Connect with a mix of Source Connectors suitable for each regional system's technology to ingest data directly into Kafka.",
            "Implement custom Kafka Producers embedded within each regional system to push data to the centralized Kafka topic.",
            "Configure a Kafka Connect Sink Connector for each regional system to replicate data into the centralized Kafka topic."
        ],
        "answer": "Use Kafka Connect with a mix of Source Connectors suitable for each regional system's technology to ingest data directly into Kafka.",
        "explanation": "Kafka Connect supports diverse data ingestion through its broad ecosystem of Source Connectors, providing scalability and minimal custom coding."
    },
    {
        "question": "An online media platform wishes to analyze user interactions (clicks, views, and comments) in real-time to dynamically adjust content recommendations. The platform generates a high volume of interaction data, necessitating scalable and real-time processing. What architecture best suits this requirement?",
        "options": [
            "Utilize a Kafka Connect Source Connector to ingest interaction data into Kafka, then process this data with Kafka Streams to update content recommendations in real-time.",
            "Directly stream interaction data into Kafka using a custom API, then use ksqlDB to perform real-time analysis and generate content recommendations.",
            "Implement batch processing jobs to periodically analyze interaction data stored in an external database, and then use Kafka to distribute batch analysis results for content recommendation updates.",
            "Configure Kafka Connect Sink Connectors to collect interaction data into a big data platform first, then process the data using external stream processing tools before updating content recommendations."
        ],
        "answer": "Utilize a Kafka Connect Source Connector to ingest interaction data into Kafka, then process this data with Kafka Streams to update content recommendations in real-time.",
        "explanation": "Kafka Connect handles scalable data ingestion, and Kafka Streams enables low-latency, real-time recommendation logic based on user interactions."
    },
    {
        "question": "A utility company monitors a network of IoT devices deployed across an energy grid. The devices send telemetry data (e.g., power usage, system health) every minute. The company wants to aggregate this data for near-real-time monitoring and anomaly detection. Which Kafka-based solution efficiently achieves this goal?",
        "options": [
            "Configure Kafka Connect Sink Connectors to collect telemetry data from the IoT devices into Kafka, followed by a Kafka Streams application to aggregate and analyze the data.",
            "Use Kafka Connect Source Connectors appropriate for the IoT devices' communication protocols to ingest telemetry data into Kafka, then employ Kafka Streams for data aggregation and anomaly detection.",
            "Develop custom Kafka Producers within the IoT devices to send data directly to Kafka topics, then use external tools to pull and analyze the data from Kafka.",
            "Implement a centralized database to collect IoT telemetry data first, then use Kafka Connect Source Connectors to ingest the data from the database into Kafka for further processing."
        ],
        "answer": "Use Kafka Connect Source Connectors appropriate for the IoT devices' communication protocols to ingest telemetry data into Kafka, then employ Kafka Streams for data aggregation and anomaly detection.",
        "explanation": "Kafka Connect Source Connectors handle reliable ingestion from IoT systems, while Kafka Streams provides real-time processing and anomaly detection capabilities."
    },
    {
        "question": "A digital marketing platform analyzes user activities to send personalized marketing emails. The platform uses Kafka to stream activity data, with fluctuations in data volume throughout the day. To ensure optimal performance during peak data inflow, what strategy should be employed?",
        "options": [
            "Dynamically adjust the number of partitions in the user activities topic based on incoming data volume.",
            "Scale the Kafka Streams application instances up or down in response to the processing load.",
            "Increase or decrease the number of Kafka Connect Source Connector tasks to match the rate of incoming user activity data.",
            "Modify the replication factor of the user activities topic during high load periods to improve data durability and availability."
        ],
        "answer": "Scale the Kafka Streams application instances up or down in response to the processing load.",
        "explanation": "Kafka Streams applications are horizontally scalable. Adding or removing instances allows dynamic scaling to handle variable workloads efficiently."
    },
    {
        "question": "A media company streams live video content, which generates logs of viewer interactions (e.g., play, pause, stop) in real-time. To enhance viewer experience through personalized content and advertisements, they need to analyze these logs in real-time. The logs are stored in NoSQL databases across different geographical locations. Considering the need for low-latency analysis, which setup is most appropriate?",
        "options": [
            "Use Kafka Connect with a custom NoSQL Source Connector for each geographical location to ingest logs into Kafka, then utilize Kafka Streams for real-time analysis and dynamic content delivery.",
            "Directly stream logs from NoSQL databases to Kafka using log-based Change Data Capture (CDC) connectors specific to each NoSQL database type, followed by processing with ksqlDB to generate viewer insights and personalized content recommendations.",
            "Configure a network of MQTT brokers to collect logs from each location, and then use an MQTT Source Connector to consolidate logs into Kafka. Apply a Kafka Streams application to analyze viewer interactions and adjust content recommendations.",
            "Implement a batch ETL process to extract logs from NoSQL databases nightly, load them into Kafka for next-day processing with Kafka Streams, and update content recommendations based on the analysis."
        ],
        "answer": "Directly stream logs from NoSQL databases to Kafka using log-based Change Data Capture (CDC) connectors specific to each NoSQL database type, followed by processing with ksqlDB to generate viewer insights and personalized content recommendations.",
        "explanation": "CDC connectors capture changes as they happen in NoSQL databases, ensuring low-latency data flow into Kafka. Using ksqlDB enables SQL-like real-time analysis for generating insights and recommendations with minimal delay."
    },
    {
        "question": "An online retailer integrates user reviews from their website into Kafka to perform sentiment analysis and adjust product rankings accordingly. Reviews are initially posted to a MongoDB database. To ensure the analysis reflects recent feedback, which configuration ensures the most efficient and timely data flow into Kafka?",
        "options": [
            "Configure MongoDB Source Connector to capture new and updated reviews into Kafka, then use Kafka Streams for sentiment analysis and to adjust product rankings in near-real-time.",
            "Utilize a cron job to export reviews from MongoDB to CSV files at regular intervals, then use File Source Connectors to ingest these files into Kafka, followed by processing with Kafka Streams.",
            "Deploy log-based CDC connectors to stream only the changes (new and updated reviews) from MongoDB into Kafka, leveraging ksqlDB for continuous sentiment analysis and product ranking adjustments.",
            "Directly access the MongoDB API from Kafka Streams applications to fetch new and updated reviews, perform sentiment analysis, and update product rankings without storing reviews in Kafka."
        ],
        "answer": "Deploy log-based CDC connectors to stream only the changes (new and updated reviews) from MongoDB into Kafka, leveraging ksqlDB for continuous sentiment analysis and product ranking adjustments.",
        "explanation": "CDC connectors efficiently capture incremental changes in MongoDB and push them to Kafka in real-time. ksqlDB allows continuous SQL-like analysis to adjust rankings instantly based on sentiment."
    },
    {
        "question": "A financial institution aims to merge transaction data from legacy systems with real-time fraud detection models running on Kafka Streams. The transaction data resides in various legacy databases and must be enriched with real-time fraud signals before being presented on a dashboard. What's the most effective architecture for this use case?",
        "options": [
            "Use JDBC Source Connectors to ingest transaction data from legacy databases into Kafka. Enrich the data using Kafka Streams by joining it with real-time fraud detection signals. Utilize a Kafka Connect Sink Connector to publish the enriched data to the dashboard.",
            "Implement custom Kafka Producers to extract transaction data from legacy systems, enriching the data in-flight with fraud detection signals before producing it to a Kafka topic for dashboard consumption.",
            "Directly connect the legacy databases to Kafka Streams applications using custom database clients. Perform the enrichment with real-time fraud detection signals in the application, then produce the enriched data to a Kafka topic for dashboard visualization.",
            "Leverage Change Data Capture (CDC) connectors to stream transaction data from legacy databases into Kafka. Use Kafka Streams for real-time enrichment with fraud detection signals and ksqlDB to further process and prepare the data for dashboard presentation."
        ],
        "answer": "Leverage Change Data Capture (CDC) connectors to stream transaction data from legacy databases into Kafka. Use Kafka Streams for real-time enrichment with fraud detection signals and ksqlDB to further process and prepare the data for dashboard presentation.",
        "explanation": "CDC connectors minimize latency by capturing data changes in real-time. Kafka Streams enables stream enrichment with fraud detection signals, and ksqlDB helps refine and prepare data for easy dashboard visualization."
    },
    {
        "question": "Where are the Kafka Connect connector configurations stored?",
        "options": [
            "In a separate config file on each Kafka Connect worker",
            "In the Kafka broker's config directory",
            "In Zookeeper under the `/kafka-connect` znode",
            "In a special Kafka topic named `connect-configs`"
        ],
        "answer": "In a special Kafka topic named `connect-configs`",
        "explanation": "Kafka Connect persists connector and task configurations in the internal Kafka topic `connect-configs`, ensuring distributed consistency and recovery support."
    },
    {
        "question": "You want to use Kafka Connect to export data from a Kafka topic to a relational database. Which type of connector should you use?",
        "options": [
            "Source Connector",
            "Sink Connector",
            "Transformation Connector",
            "Import Connector"
        ],
        "answer": "Sink Connector",
        "explanation": "Sink Connectors consume data from Kafka topics and write it to external systems such as databases, files, or search indexes."
    },
    {
        "question": "You need to stream data from a Twitter feed into a Kafka topic for real-time processing. Which Kafka Connect connector type is most appropriate?",
        "options": [
            "Sink Connector",
            "Source Connector",
            "Transformation Connector",
            "Export Connector"
        ],
        "answer": "Source Connector",
        "explanation": "A Source Connector is used to import data from external systems such as Twitter feeds into Kafka topics for further processing."
    },
    {
        "question": "You are using Kafka Connect to move data from a source system into Kafka for real-time processing with Kafka Streams. After processing, the results need to be stored in HDFS for batch analysis. Which combination of connector types will you need?",
        "options": [
            "Source Connector -> Sink Connector",
            "Sink Connector -> Source Connector",
            "Source Connector -> Source Connector",
            "Sink Connector -> Sink Connector"
        ],
        "answer": "Source Connector -> Sink Connector",
        "explanation": "A Source Connector imports data into Kafka, and a Sink Connector exports processed data from Kafka to external systems like HDFS."
    },
    {
        "question": "You are using a JDBC source connector to copy data from a database table to a Kafka topic. The table has 5 columns. How many tasks will be created by the connector?",
        "options": [
            "1",
            "5",
            "It depends on the `max.tasks` configuration of the connector",
            "It depends on the number of partitions in the Kafka topic"
        ],
        "answer": "1",
        "explanation": "A JDBC Source Connector creates one task per table by default, regardless of the number of columns. Parallelism depends on the `max.tasks` setting and how the connector splits tables, not columns."
    },
    {
        "question": "What happens if the `max.tasks` configuration is set to a value less than the number of tables being copied by a JDBC source connector?",
        "options": [
            "The connector will create one task per table, ignoring the `max.tasks` setting",
            "The connector will create tasks up to the `max.tasks` limit, potentially leaving some tables without dedicated tasks",
            "The connector will distribute the tables evenly among the available tasks",
            "The connector will fail with an error due to the insufficient number of tasks"
        ],
        "answer": "The connector will distribute the tables evenly among the available tasks",
        "explanation": "If `max.tasks` is smaller than the number of tables, the JDBC connector distributes tables evenly among tasks to balance workload and maintain complete data ingestion."
    },
    {
        "question": "How can you increase the parallelism of a JDBC source connector to improve the performance of copying data from a database to Kafka?",
        "options": [
            "Increase the `max.tasks` configuration of the connector",
            "Increase the number of partitions in the target Kafka topic",
            "Increase the `tasks.max` configuration of the Kafka Connect workers",
            "Use multiple instances of the JDBC connector, each copying a different subset of tables"
        ],
        "answer": "Increase the `max.tasks` configuration of the connector and use multiple instances of the JDBC connector, each copying a different subset of tables",
        "explanation": "Parallelism can be improved by increasing `max.tasks` for more parallel connector tasks and running multiple connector instances to divide table ingestion across them."
    },
    {
        "question": "What information about Kafka Connect tasks is NOT stored in the `connect-status` topic?",
        "options": [
            "The connector and task configurations",
            "The current status of each connector and task (running, failed, paused, etc.)",
            "The offsets processed by each connector",
            "The worker node each task is assigned to"
        ],
        "answer": "The connector and task configurations",
        "explanation": "The `connect-status` topic stores status information about connectors and tasks, but not their configurations. Connector and task configurations are stored in the `connect-configs` topic. The current status, offsets, and worker assignments are part of the `connect-status` topic."
    },
    {
        "question": "You have a Kafka cluster with 5 brokers and a topic with 10 partitions. You want to consume messages from this topic using a consumer group with 3 consumers. What is the maximum number of partitions that can be assigned to a single consumer?",
        "options": ["3", "4", "5", "10"],
        "answer": "4",
        "explanation": "With 10 partitions and 3 consumers, Kafka will distribute partitions as evenly as possible: 4 + 3 + 3. Therefore, the maximum number of partitions assigned to a single consumer is 4."
    },
    {
        "question": "You have a Kafka cluster with 3 brokers and a topic with 12 partitions. You want to create a consumer group with 4 consumers to consume messages from this topic. How many consumers will be actively consuming messages?",
        "options": ["1", "3", "4", "12"],
        "answer": "4",
        "explanation": "With 12 partitions and 4 consumers, Kafka will evenly assign 3 partitions per consumer. All 4 consumers will be actively consuming messages. If there were fewer partitions than consumers, some would be idle."
    },
    {
        "question": "What is the purpose of the `connect-offsets` topic in Kafka Connect?",
        "options": [
            "It stores the configuration of the connectors.",
            "It stores the status of the connector tasks.",
            "It stores the offsets of the source connectors.",
            "It stores the offsets of the sink connectors."
        ],
        "answer": "It stores the offsets of the source connectors.",
        "explanation": "The `connect-offsets` topic tracks source connector offsets to enable recovery and fault tolerance. If a task fails, Kafka Connect resumes processing from the last committed offset. Sink connectors do not use this topic for offset management."
    },
    {
        "question": "How does Kafka Connect handle the scalability of connectors?",
        "options": [
            "By automatically creating multiple instances of a connector based on the load.",
            "By allowing manual configuration of the number of tasks for each connector.",
            "By dynamically adjusting the number of tasks based on the connector's performance.",
            "By requiring a separate Kafka Connect cluster for each connector."
        ],
        "answer": "By allowing manual configuration of the number of tasks for each connector.",
        "explanation": "Kafka Connect allows scaling through the `tasks.max` configuration parameter, which determines how many tasks can be created for a connector. Each task processes a subset of data, and Kafka Connect distributes them across workers automatically."
    },
    {
        "question": "What happens when a Kafka Connect worker node fails in a distributed Kafka Connect cluster?",
        "options": [
            "All the connectors and tasks running on the failed worker node are permanently lost.",
            "The connectors and tasks are automatically redistributed to the remaining worker nodes.",
            "The failed worker node is replaced with a new worker node, and the tasks are reassigned.",
            "The entire Kafka Connect cluster goes down until the failed worker node is restored."
        ],
        "answer": "The connectors and tasks are automatically redistributed to the remaining worker nodes.",
        "explanation": "When a worker node fails, Kafka Connect detects the failure and redistributes its connectors and tasks to the remaining active workers. The offsets stored in `connect-offsets` ensure processing resumes from the last committed point. The cluster continues operating without interruption."
    },
    {
        "question": "When using Kafka Streams DSL, how can you perform a stateful operation on a KStream?",
        "options": [
            "By using the map operation to modify the stream's values",
            "By using the filter operation to remove unwanted records from the stream",
            "By using the groupByKey operation to group the stream's records by key",
            "By using the mapValues operation to transform the stream's values"
        ],
        "answer": "By using the groupByKey operation to group the stream's records by key",
        "explanation": "To perform a stateful operation on a KStream using Kafka Streams DSL, you use the `groupByKey` operation. This groups records by their keys, producing a KGroupedStream on which stateful operations such as `aggregate`, `reduce`, or `count` can be applied. These operations maintain per-key state. Stateless operations include `map`, `mapValues`, and `filter`."
    },
    {
        "question": "What is the role of the StateStore in Kafka Streams?",
        "options": [
            "To store the intermediate results of stream processing operations",
            "To store the configuration properties for Kafka Streams applications",
            "To store the metadata information about the Kafka cluster",
            "To store the consumer offsets for Kafka Streams applications"
        ],
        "answer": "To store the intermediate results of stream processing operations",
        "explanation": "The StateStore in Kafka Streams stores and manages state required for stateful operations such as aggregations, joins, or windowing. It acts as a local database accessible by stream tasks and is backed by persistent storage (typically RocksDB). StateStores enable fault-tolerant, recoverable state management and are automatically restored from changelog topics if failures occur."
    },
    {
        "question": "You have an e-commerce application that maintains user information. Which of the following data is best suited to be modeled as a KTable in Kafka Streams?",
        "options": [
            "User clickstream data",
            "User order history",
            "User profile information",
            "User session data"
        ],
        "answer": "User profile information",
        "explanation": "User profile information is best represented as a KTable because it models the latest state for each key (user). A KTable represents a changelog where updates overwrite previous values, which suits relatively static data like profiles. Clickstream or order history are continuous event streams better modeled as KStreams. Session data can be modeled as a windowed KTable depending on needs."
    },
    {
        "question": "In an IoT application, you have a stream of sensor readings that need to be processed in real-time. Which of the following is the most suitable way to model this data in Kafka Streams?",
        "options": [
            "As a KTable, with each sensor reading as a key-value pair",
            "As a KStream, with each sensor reading as a record",
            "As a GlobalKTable, with each sensor reading as a key-value pair",
            "As a windowed KTable, with each sensor reading as a key-value pair"
        ],
        "answer": "As a KStream, with each sensor reading as a record",
        "explanation": "Sensor readings in an IoT system are continuous, independent events, best represented as a KStream. KStreams are ideal for real-time event processing with operations like map, filter, and windowing. KTables or GlobalKTables represent stateful views or reference data, not continuous events."
    },
    {
        "question": "You are building a real-time analytics application that tracks user behavior on a website. Which of the following data is most appropriate to be modeled as a KStream in Kafka Streams?",
        "options": [
            "User demographic information",
            "User navigation events",
            "User purchase history",
            "User authentication data"
        ],
        "answer": "User navigation events",
        "explanation": "User navigation events are continuous, real-time records of user activity, making them suitable for a KStream. Each event (click, page view, interaction) is an independent record processed as it arrives. Static data like demographics fit a KTable, while purchase history can be either a KStream or KTable depending on the use case."
    },
    {
        "question": "Which tool is commonly used to monitor Kafka cluster health and performance?",
        "options": ["Nagios", "Prometheus", "Elasticsearch", "Splunk"],
        "answer": "Prometheus",
        "explanation": "Prometheus is widely used for monitoring Kafka cluster health and performance. It collects metrics from Kafka brokers, producers, and consumers and stores them in a time-series database. Prometheus can also be integrated with Grafana for visualization."
    },
    {
        "question": "What is the primary purpose of JMX in the context of Kafka monitoring?",
        "options": [
            "To configure Kafka brokers",
            "To provide real-time logging of Kafka events",
            "To expose Kafka metrics for monitoring",
            "To manage Kafka ACLs"
        ],
        "answer": "To expose Kafka metrics for monitoring",
        "explanation": "JMX (Java Management Extensions) is used to expose Kafka metrics for monitoring. Kafka brokers expose various metrics like broker, topic, and consumer group metrics through JMX, which can be collected by tools such as Prometheus."
    },
    {
        "question": "Which Kafka metric would you monitor to detect message delivery delays in a Kafka cluster?",
        "options": ["MessagesInPerSec", "RequestLatencyMs", "UnderReplicatedPartitions", "BytesOutPerSec"],
        "answer": "RequestLatencyMs",
        "explanation": "`RequestLatencyMs` measures the latency of requests in Kafka. Monitoring this helps detect message delivery delays. Other metrics like `MessagesInPerSec`, `UnderReplicatedPartitions`, and `BytesOutPerSec` focus on throughput or replication, not latency."
    },
    {
        "question": "Which of the following tools can be used to visualize Kafka metrics collected by Prometheus?",
        "options": ["Kibana", "Grafana", "Logstash", "Fluentd"],
        "answer": "Grafana",
        "explanation": "Grafana is used to visualize metrics collected by Prometheus. It provides rich dashboarding capabilities for Kafka performance and cluster health. Kibana is for Elasticsearch, while Logstash and Fluentd handle log processing."
    },
    {
        "question": "What does the Kafka metric UnderReplicatedPartitions indicate?",
        "options": [
            "The number of partitions without a leader",
            "The number of partitions that have fewer replicas than specified",
            "The number of partitions that are not receiving messages",
            "The number of partitions with high message latency"
        ],
        "answer": "The number of partitions that have fewer replicas than specified",
        "explanation": "`UnderReplicatedPartitions` indicates partitions with fewer replicas than their configured replication factor. Monitoring this ensures replication health and data reliability."
    },
    {
        "question": "Which Kafka metric should be monitored to ensure sufficient disk space on Kafka brokers?",
        "options": ["LogEndOffset", "LogSegmentCount", "FreeStorageSpace", "MessageRate"],
        "answer": "FreeStorageSpace",
        "explanation": "`FreeStorageSpace` tracks available disk space on brokers. Monitoring this helps prevent disk exhaustion, which can disrupt Kafka performance or lead to data loss."
    },
    {
        "question": "What is the role of Kafka Exporter in a Kafka monitoring setup?",
        "options": [
            "To collect logs from Kafka brokers",
            "To expose Kafka metrics to Prometheus",
            "To configure Kafka broker settings",
            "To manage Kafka consumer groups"
        ],
        "answer": "To expose Kafka metrics to Prometheus",
        "explanation": "Kafka Exporter collects metrics from Kafka brokers and exposes them in Prometheus-compatible format, enabling Prometheus to scrape and store them for analysis."
    },
    {
        "question": "Which Kafka metric indicates the time it takes for a record to be acknowledged by all in-sync replicas?",
        "options": ["ReplicationLag", "FetchLatency", "ProducerLatency", "ISRTime"],
        "answer": "ReplicationLag",
        "explanation": "`ReplicationLag` measures the delay between a message being written to the leader and acknowledged by all in-sync replicas, which is key for ensuring data consistency and reliability."
    },
    {
        "question": "Why is it important to monitor the RequestRate metric in Kafka?",
        "options": [
            "To measure the number of messages being produced",
            "To measure the number of bytes being consumed",
            "To measure the rate of requests being handled by Kafka brokers",
            "To measure the number of partitions"
        ],
        "answer": "To measure the rate of requests being handled by Kafka brokers",
        "explanation": "`RequestRate` measures how many requests Kafka brokers are handling per second. Monitoring it helps identify high load conditions that can affect broker performance."
    },
    {
        "question": "What does the Kafka metric ConsumerLag indicate?",
        "options": [
            "The number of messages a consumer has consumed",
            "The number of messages a consumer is behind in processing",
            "The time a consumer takes to process a message",
            "The number of partitions a consumer is subscribed to"
        ],
        "answer": "The number of messages a consumer is behind in processing",
        "explanation": "`ConsumerLag` measures how far behind a consumer is from the latest offset. High consumer lag indicates that consumers are not keeping up with producers, which can lead to processing delays."
    },
    {
        "question": "In the Kafka producer API, what is the purpose of the `acks` configuration parameter?",
        "options": [
            "To specify the number of acknowledgments the producer requires the leader to have received before considering a request complete",
            "To specify the number of replicas that must acknowledge a write for the write to be considered successful",
            "To specify the number of times the producer will retry a failed request",
            "To specify the number of partitions a topic must have for the producer to send messages to it"
        ],
        "answer": "To specify the number of acknowledgments the producer requires the leader to have received before considering a request complete",
        "explanation": "The `acks` parameter in the Kafka producer API controls the durability of writes from the producer to the Kafka broker. It specifies how many acknowledgments the producer requires from the leader before considering a request complete. \n\n- `acks=0`: The producer does not wait for any acknowledgment. \n- `acks=1`: The leader writes to its local log and responds immediately. \n- `acks=all`: The leader waits for all in-sync replicas to acknowledge before responding. \n\nHigher `acks` values increase durability at the cost of higher latency."
    },
    {
        "question": "How does the `min.insync.replicas` broker configuration interact with the `acks` producer configuration?",
        "options": [
            "They are completely independent settings",
            "`acks` must always be set to `all` for `min.insync.replicas` to have any effect",
            "`min.insync.replicas` is only relevant if `acks` is set to `1` or `all`",
            "If `acks` is set to `all`, writes will only succeed if the number of in-sync replicas is at least `min.insync.replicas`"
        ],
        "answer": "If `acks` is set to `all`, writes will only succeed if the number of in-sync replicas is at least `min.insync.replicas`",
        "explanation": "The `min.insync.replicas` setting defines the minimum number of replicas that must acknowledge a write for it to be successful. When the producer uses `acks=all`, the leader waits for acknowledgments from all in-sync replicas. If the number of available replicas falls below `min.insync.replicas`, the write fails, ensuring data durability and consistency."
    },
    {
        "question": "What happens if a Kafka producer sends a message with `acks=all` to a topic partition with 3 replicas, but only 2 replicas are currently in-sync?",
        "options": [
            "The write will succeed and the producer will receive an acknowledgment",
            "The write will succeed but the producer will not receive an acknowledgment",
            "The write will be queued until the third replica comes back in-sync",
            "The write will fail and the producer will receive an error"
        ],
        "answer": "The write will fail and the producer will receive an error",
        "explanation": "With `acks=all`, the producer requires acknowledgments from all in-sync replicas. If a replica is out-of-sync and `min.insync.replicas` cannot be satisfied, the leader returns a `NotEnoughReplicasException`, and the write fails. This protects against data loss by ensuring durability across the required number of replicas."
    },
    {
        "question": "Can a producer configured with `acks=all` and `retries=Integer.MAX_VALUE` ever experience data loss?",
        "options": [
            "No, this configuration guarantees no data loss under all circumstances",
            "Yes, if the total number of replicas for a partition drops below `min.insync.replicas`",
            "Yes, if `unclean.leader.election.enable=true` and all in-sync replicas fail",
            "Yes, if the producer crashes after the broker acknowledges the write but before the producer records the acknowledgment"
        ],
        "answer": "Yes, if the total number of replicas for a partition drops below `min.insync.replicas`, Yes, if `unclean.leader.election.enable=true` and all in-sync replicas fail, Yes, if the producer crashes after the broker acknowledges the write but before the producer records the acknowledgment",
        "explanation": "Even with `acks=all` and infinite retries, data loss can occur if: \n1. The number of in-sync replicas falls below `min.insync.replicas` (broker rejects writes). \n2. `unclean.leader.election.enable=true` allows an out-of-sync replica to become leader. \n3. The producer crashes after the broker acknowledges a message but before the acknowledgment is persisted. \n\nThus, these configurations minimize but do not completely eliminate data loss risks."
    },
    {
        "question": "You want to produce messages to a Kafka topic using a Java client. Which of the following is NOT a required configuration for the producer?",
        "options": [
            "`bootstrap.servers`",
            "`key.serializer`",
            "`value.serializer`",
            "`partitioner.class`"
        ],
        "answer": "`partitioner.class`",
        "explanation": "The required configurations for a Kafka producer are `bootstrap.servers`, `key.serializer`, and `value.serializer`. The `partitioner.class` setting is optional; Kafka uses the default partitioner if none is specified."
    },
    {
        "question": "Which of the following is true about the relationship between producers and consumers in Kafka?",
        "options": [
            "Producers and consumers must use the same serialization format",
            "Producers and consumers must be written in the same programming language",
            "Producers and consumers are decoupled by the Kafka topic",
            "Producers must know about the consumers to send messages to them"
        ],
        "answer": "Producers and consumers are decoupled by the Kafka topic",
        "explanation": "Kafka topics serve as an abstraction layer between producers and consumers. Producers write to topics and consumers read from them independently, allowing decoupling of data producers and consumers for scalability and flexibility."
    },
    {
        "question": "What happens if a Kafka producer sends a message to a topic partition and does not receive an acknowledgment from the broker?",
        "options": [
            "The producer will consider the message as successfully sent",
            "The producer will wait indefinitely for the acknowledgment",
            "The producer will retry sending the message based on its retry configuration",
            "The producer will immediately send the next message in the queue"
        ],
        "answer": "The producer will retry sending the message based on its retry configuration",
        "explanation": "If no acknowledgment is received within `request.timeout.ms`, the send is marked as failed. If `retries > 0`, the producer retries after `retry.backoff.ms`. Otherwise, it raises an exception. Retries help improve reliability in transient failures."
    },
    {
        "question": "What is the purpose of the `acks` parameter in Kafka producer configuration?",
        "options": [
            "To specify the number of partitions the producer should write to",
            "To specify the number of replicas that must acknowledge a write for it to be considered successful",
            "To specify the number of times the producer should retry sending a message",
            "To specify the maximum size of a batch of messages"
        ],
        "answer": "To specify the number of replicas that must acknowledge a write for it to be considered successful",
        "explanation": "The `acks` parameter defines the acknowledgment requirement for producer writes: \n- `0`: No acknowledgment (fastest, least reliable). \n- `1`: Leader acknowledgment only. \n- `all`/`-1`: All in-sync replicas must acknowledge (highest durability)."
    },
    {
        "question": "What happens if the `acks` parameter is set to `all` and the minimum in-sync replicas (`min.insync.replicas`) setting is not satisfied?",
        "options": [
            "The producer will retry sending the message until the `min.insync.replicas` requirement is met",
            "The producer will write the message successfully, ignoring the `min.insync.replicas` setting",
            "The producer will receive an error indicating that the `min.insync.replicas` requirement is not met",
            "The producer will wait indefinitely until the `min.insync.replicas` requirement is met"
        ],
        "answer": "The producer will receive an error indicating that the `min.insync.replicas` requirement is not met",
        "explanation": "When `acks=all`, the producer expects acknowledgments from all in-sync replicas. If fewer than `min.insync.replicas` replicas are available, the broker rejects the write and returns an error. This ensures high durability and consistency guarantees."
    },
    {
        "question": "What is the relationship between the `acks` parameter and the `request.required.acks` parameter in Kafka?",
        "options": [
            "They are the same parameter, just with different names",
            "`acks` is used in the producer configuration, while `request.required.acks` is used in the consumer configuration",
            "`acks` is used in the new producer API, while `request.required.acks` is used in the old producer API",
            "They are completely unrelated parameters"
        ],
        "answer": "`acks` is used in the new producer API, while `request.required.acks` is used in the old producer API",
        "explanation": "The `acks` parameter replaced `request.required.acks` in the new Kafka producer API (≥0.8.2). Both control the acknowledgment level of writes, but `request.required.acks` was part of the deprecated old producer API."
    },
    {
        "question": "How does Kafka's zero-copy optimization handle data transformation or modification?",
        "options": [
            "It automatically applies data transformations during the zero-copy process.",
            "It allows custom data transformations to be plugged into the zero-copy mechanism.",
            "It does not support data transformations and sends data as-is.",
            "It performs data transformations after the data is copied into the application's memory."
        ],
        "answer": "It does not support data transformations and sends data as-is.",
        "explanation": "Kafka's zero-copy optimization is designed for efficient data transfer between producer and consumer without performing any transformations or modifications. The producer serializes data before sending, Kafka transfers it as-is using zero-copy from file cache to network, and the consumer deserializes it after receiving. This approach avoids any overhead of transformations during the transfer process, ensuring maximum throughput and efficiency."
    },
    {
        "question": "What is the purpose of the `linger.ms` setting in the Kafka producer configuration?",
        "options": [
            "To specify the maximum time to wait for a response from the Kafka broker",
            "To specify the maximum time to wait before sending a batch of messages",
            "To specify the maximum time to wait for a message to be acknowledged by the Kafka broker",
            "To specify the maximum time to wait for a message to be written to the Kafka topic"
        ],
        "answer": "To specify the maximum time to wait before sending a batch of messages",
        "explanation": "The `linger.ms` setting controls how long the producer waits before sending a batch of messages. By default, messages are sent immediately, but setting a non-zero `linger.ms` allows the producer to accumulate more messages into a batch before sending, improving throughput by reducing the number of requests."
    },
    {
        "question": "How does the `batch.size` setting affect the behavior of the Kafka producer?",
        "options": [
            "It specifies the maximum number of messages that can be sent in a single batch",
            "It specifies the maximum size (in bytes) of a batch of messages",
            "It specifies the minimum number of messages required to form a batch",
            "It specifies the minimum size (in bytes) of a message to be included in a batch"
        ],
        "answer": "It specifies the maximum size (in bytes) of a batch of messages",
        "explanation": "The `batch.size` setting defines the maximum batch size in bytes. Once the accumulated messages reach this size or the `linger.ms` timeout expires, the producer sends the batch. Increasing `batch.size` improves throughput by sending larger batches but increases memory usage."
    },
    {
        "question": "What happens if the Kafka producer exhausts its buffer memory while sending messages?",
        "options": [
            "The producer will block and wait until buffer memory becomes available",
            "The producer will start discarding the oldest messages to free up buffer memory",
            "The producer will start discarding the newest messages to free up buffer memory",
            "The producer will throw an exception and stop sending messages"
        ],
        "answer": "The producer will block and wait until buffer memory becomes available",
        "explanation": "When the producer’s buffer is full, it blocks new send requests until buffer memory is freed as messages are transmitted. This prevents data loss, but may cause increased latency if the broker is slow to acknowledge messages."
    },
    {
        "question": "What is the default value for the `acks` parameter in the Kafka producer configuration?",
        "options": ["0", "1", "all", "none"],
        "answer": "1",
        "explanation": "By default, Kafka producer uses `acks=1`, meaning it waits for an acknowledgment from the leader only. This offers a balance between performance and durability—writes are considered successful once the leader persists them, without waiting for replicas."
    },
    {
        "question": "What happens when the `acks` parameter is set to 'all' in the Kafka producer configuration?",
        "options": [
            "The producer does not wait for any acknowledgment and considers the write successful immediately",
            "The producer waits for the leader replica to acknowledge the write before considering it successful",
            "The producer waits for all in-sync replicas to acknowledge the write before considering it successful",
            "The producer waits for a minimum number of replicas to acknowledge the write before considering it successful"
        ],
        "answer": "The producer waits for all in-sync replicas to acknowledge the write before considering it successful",
        "explanation": "With `acks=all`, the producer waits for acknowledgments from all in-sync replicas (ISRs) before marking the send as successful. This ensures high durability but adds latency compared to `acks=1`."
    },
    {
        "question": "How does the `max.in.flight.requests.per.connection` setting affect the behavior of the Kafka producer when `acks=1`?",
        "options": [
            "It specifies the maximum number of unacknowledged requests allowed per broker connection",
            "It specifies the maximum number of requests that can be sent to the broker concurrently",
            "It specifies the maximum number of messages that can be buffered in the producer's memory",
            "It has no effect when `acks=1`"
        ],
        "answer": "It specifies the maximum number of unacknowledged requests allowed per broker connection",
        "explanation": "The `max.in.flight.requests.per.connection` parameter determines how many requests can be sent concurrently before receiving acknowledgments. Default is 5. Higher values improve throughput but can risk out-of-order delivery if retries occur."
    },
    {
        "question": "What is the purpose of the `enable.idempotence` setting in the Kafka producer configuration?",
        "options": [
            "To ensure that messages are delivered exactly once to the Kafka broker",
            "To enable compression of messages sent by the producer",
            "To specify the maximum size of a batch of messages",
            "To control the acknowledgment behavior of the producer"
        ],
        "answer": "To ensure that messages are delivered exactly once to the Kafka broker",
        "explanation": "Enabling `enable.idempotence` ensures exactly-once delivery to Kafka brokers. The producer assigns sequence numbers to each message so brokers can detect and discard duplicates during retries, preventing duplicate writes in the same session."
    },
    {
        "question": "What happens when `max.in.flight.requests.per.connection` is set to 1 and `enable.idempotence` is set to true in the Kafka producer configuration?",
        "options": [
            "The producer will send messages in batches to improve throughput",
            "The producer will wait for each request to be acknowledged before sending the next request",
            "The producer will retry failed requests automatically",
            "The producer will disable message compression"
        ],
        "answer": "The producer will wait for each request to be acknowledged before sending the next request",
        "explanation": "With `max.in.flight.requests.per.connection=1` and `enable.idempotence=true`, the producer sends one request at a time per connection, ensuring messages are acknowledged in order. This guarantees message ordering and exactly-once semantics but can reduce throughput."
    },
    {
        "question": "How does enabling idempotence affect the performance of the Kafka producer?",
        "options": [
            "It significantly improves the producer's throughput",
            "It has no impact on the producer's performance",
            "It may slightly reduce the producer's throughput",
            "It increases the producer's memory usage"
        ],
        "answer": "It may slightly reduce the producer's throughput",
        "explanation": "Enabling idempotence adds minimal overhead because the producer and broker must track message sequence numbers and producer IDs to ensure exactly-once delivery. The impact on throughput is small compared to the reliability gained."
    },
    {
        "question": "Which configuration is used to define the schema registry URL in Kafka clients?",
        "options": [
            "schema.registry.url",
            "schema.registry.endpoint",
            "schema.registry.address",
            "schema.registry.host"
        ],
        "answer": "schema.registry.url",
        "explanation": "The configuration `schema.registry.url` is used to specify the URL of the Confluent Schema Registry in Kafka clients. This URL is necessary for the clients to connect to the Schema Registry and retrieve the schemas. Options B, C, and D are incorrect as these are not valid configuration properties."
    },
    {
        "question": "What is the primary purpose of a subject in the Confluent Schema Registry?",
        "options": [
            "To group schemas by type (Avro, Protobuf, JSON Schema)",
            "To manage versions of a schema for a specific topic or entity",
            "To specify the schema storage location",
            "To define the security policies for accessing schemas"
        ],
        "answer": "To manage versions of a schema for a specific topic or entity",
        "explanation": "A subject in the Confluent Schema Registry is used to manage schema versions for a specific topic or entity. It allows version control and ensures compatibility. Other options describe unrelated or incorrect functions."
    },
    {
        "question": "How does Confluent Schema Registry ensure compatibility when registering a new schema version?",
        "options": [
            "By comparing the new schema with the latest version only",
            "By comparing the new schema with all previous versions",
            "By comparing the new schema with a user-specified set of previous versions",
            "By ignoring previous versions and only validating the new schema"
        ],
        "answer": "By comparing the new schema with the latest version only",
        "explanation": "The Schema Registry ensures compatibility by comparing the new schema with the latest version, based on the configured compatibility mode (BACKWARD, FORWARD, or FULL). It does not compare with all previous versions or ignore them entirely."
    },
    {
        "question": "What compatibility mode allows a new schema to both read data written by an old schema and write data that can be read by the old schema?",
        "options": [
            "BACKWARD",
            "FORWARD",
            "FULL",
            "NONE"
        ],
        "answer": "FULL",
        "explanation": "FULL compatibility ensures that a new schema can both read data produced by older schemas and write data that older schemas can still read. BACKWARD and FORWARD only ensure one-way compatibility, and NONE disables compatibility checks."
    },
    {
        "question": "Which schema types are supported by Confluent Schema Registry but not by Apache Avro? (Select all that apply)",
        "options": [
            "Protobuf",
            "Thrift",
            "JSON Schema",
            "XML Schema"
        ],
        "answer": ["Protobuf", "JSON Schema"],
        "explanation": "Confluent Schema Registry supports Avro, Protobuf, and JSON Schema. Apache Avro only supports Avro format, not Protobuf or JSON Schema. Thrift and XML Schema are not supported."
    },
    {
        "question": "In the context of Confluent Schema Registry, what is the main advantage of using Avro over JSON Schema?",
        "options": [
            "Avro schemas are human-readable",
            "Avro provides a compact and fast binary serialization format",
            "Avro does not require schema registration",
            "Avro supports all JSON types natively"
        ],
        "answer": "Avro provides a compact and fast binary serialization format",
        "explanation": "Avro’s main advantage is its efficient binary serialization, which makes it faster and more compact compared to JSON Schema. Other options describe incorrect or secondary characteristics."
    },
    {
        "question": "What is the default compatibility mode in Confluent Schema Registry?",
        "options": [
            "BACKWARD",
            "FORWARD",
            "FULL",
            "NONE"
        ],
        "answer": "BACKWARD",
        "explanation": "The default compatibility mode in the Confluent Schema Registry is BACKWARD. This ensures new schemas can read data written by older schema versions."
    },
    {
        "question": "How does the Confluent Schema Registry handle schema evolution?",
        "options": [
            "By automatically converting old schemas to new schemas",
            "By storing all schema versions and applying compatibility checks",
            "By enforcing schema changes directly on the producer side",
            "By modifying the schema directly in the consumer application"
        ],
        "answer": "By storing all schema versions and applying compatibility checks",
        "explanation": "Schema Registry manages schema evolution by storing every version of a schema and enforcing compatibility rules during registration to ensure safe evolution. It doesn’t modify schemas automatically or externally."
    },
    {
        "question": "What happens if a schema fails the compatibility check when being registered in the Confluent Schema Registry?",
        "options": [
            "The schema is registered with a warning",
            "The schema is rejected, and an error is returned",
            "The schema is registered, but compatibility is disabled",
            "The schema is registered with a lower priority"
        ],
        "answer": "The schema is rejected, and an error is returned",
        "explanation": "If a new schema fails compatibility checks, it is rejected outright, and the registry returns an error. This ensures that incompatible schemas do not corrupt existing data flows."
    },
    {
        "question": "Which command-line tool can be used to interact with the Confluent Schema Registry?",
        "options": [
            "kafka-schema-registry",
            "schema-registry-cli",
            "confluent-hub",
            "kafka-schema-cli"
        ],
        "answer": "schema-registry-cli",
        "explanation": "The `schema-registry-cli` is a command-line tool used to manage schemas, subjects, and compatibility settings in Confluent Schema Registry. Other options are incorrect or unrelated."
    },
    {
        "question": "What is the purpose of the Confluent Schema Registry in a Kafka ecosystem?",
        "options": [
            "To store and manage Avro schemas for Kafka messages",
            "To provide a REST API for producing and consuming Kafka messages",
            "To handle authentication and authorization for Kafka clients",
            "To monitor and manage Kafka clusters and their performance"
        ],
        "answer": "To store and manage Avro schemas for Kafka messages",
        "explanation": "The Schema Registry serves as a centralized service for storing and managing Avro schemas for Kafka messages. It enables schema evolution, compatibility checks, and allows producers and consumers to exchange structured data without embedding full schemas in every message."
    },
    {
        "question": "How does the Confluent Schema Registry ensure compatibility between different versions of a schema?",
        "options": [
            "By enforcing strict backward compatibility for all schema changes",
            "By allowing schema changes that are both backward and forward compatible",
            "By automatically generating compatibility reports for schema versions",
            "By using a compatibility setting to define allowed schema evolution rules"
        ],
        "answer": "By using a compatibility setting to define allowed schema evolution rules",
        "explanation": "Schema Registry uses a configurable compatibility setting (BACKWARD, FORWARD, FULL, or NONE) to enforce rules about how schemas may evolve. These settings determine whether new schemas are allowed based on compatibility with previous versions."
    },
    {
        "question": "How can you retrieve the latest version of a schema from the Confluent Schema Registry using its REST API?",
        "options": [
            "Send a GET request to `/subjects/<subject>/versions/latest`",
            "Send a POST request to `/schemas/<subject>/versions/latest`",
            "Send a GET request to `/schemas/<subject>/versions/latest`",
            "Send a POST request to `/subjects/<subject>/versions/latest`"
        ],
        "answer": "Send a GET request to `/subjects/<subject>/versions/latest`",
        "explanation": "The Schema Registry REST API endpoint `/subjects/<subject>/versions/latest` returns the most recent version of a schema for the specified subject, including details like ID, version, and schema definition."
    },
    {
        "question": "What is the purpose of the `kafkastore.topic` configuration in the Confluent Schema Registry?",
        "options": [
            "To specify the Kafka topic where the Schema Registry stores its schema data",
            "To define the compatibility setting for schema evolution",
            "To set the frequency at which the Schema Registry checks for schema updates",
            "To configure the retention period for old schema versions"
        ],
        "answer": "To specify the Kafka topic where the Schema Registry stores its schema data",
        "explanation": "The `kafkastore.topic` property defines the Kafka topic used by the Schema Registry to persist schema information. By default, it uses the `_schemas` topic but can be customized as needed."
    },
    {
        "question": "What is the default compatibility setting in the Confluent Schema Registry for schema evolution?",
        "options": [
            "BACKWARD",
            "FORWARD",
            "FULL",
            "NONE"
        ],
        "answer": "BACKWARD",
        "explanation": "The default compatibility setting is BACKWARD, ensuring that new schemas can read data written with older schemas. This supports safe evolution of producer schemas without breaking existing consumers."
    },
    {
        "question": "How can you change the compatibility setting for a specific subject in the Confluent Schema Registry using its REST API?",
        "options": [
            "Send a PUT request to `/config/<subject>`",
            "Send a POST request to `/config/<subject>`",
            "Send a PUT request to `/compatibility/<subject>`",
            "Send a POST request to `/compatibility/<subject>`"
        ],
        "answer": "Send a PUT request to `/config/<subject>`",
        "explanation": "To modify a subject’s compatibility level, you send a PUT request to `/config/<subject>` with a JSON body specifying the desired setting, for example: `{ \"compatibility\": \"FULL\" }`."
    },
    {
        "question": "What is the impact of removing a required field that has a default value in an Avro schema?",
        "options": [
            "It is a backward compatible change",
            "It is a forward compatible change",
            "It is both a backward and forward compatible change",
            "It is an incompatible change"
        ],
        "answer": "It is a backward compatible change",
        "explanation": "Removing a required field that includes a default value is backward compatible because older readers can fill the missing field using its default value. However, it’s not forward compatible."
    },
    {
        "question": "What compatibility level is maintained when adding a new optional field to an Avro schema?",
        "options": [
            "Backward compatibility",
            "Forward compatibility",
            "Full compatibility",
            "No compatibility"
        ],
        "answer": "Full compatibility",
        "explanation": "Adding a new optional field (one with a default value) maintains both backward and forward compatibility. Older consumers ignore the new field, while newer consumers treat missing values as defaults."
    },
    {
        "question": "What is the effect of changing the data type of a field in an Avro schema?",
        "options": [
            "It is a backward compatible change",
            "It is a forward compatible change",
            "It is both a backward and forward compatible change",
            "It is an incompatible change"
        ],
        "answer": "It is an incompatible change",
        "explanation": "Changing a field’s data type breaks both backward and forward compatibility since producers and consumers expect different serialized formats for that field."
    },
    {
        "question": "In the Confluent Schema Registry, what is the default compatibility setting for new schemas?",
        "options": [
            "BACKWARD",
            "FORWARD",
            "FULL",
            "NONE"
        ],
        "answer": "BACKWARD",
        "explanation": "The default compatibility type is BACKWARD, allowing consumers to read older messages after schema evolution. It’s the safest and most common mode for Kafka-based systems."
    },
    {
        "question": "What is the role of the `ssl.truststore.location` and `ssl.truststore.password` configurations in Kafka?",
        "options": [
            "To specify the location and password of the keystore for storing the broker's private key",
            "To specify the location and password of the truststore for storing trusted client certificates",
            "To specify the location and password of the keystore for storing trusted broker certificates",
            "To specify the location and password of the truststore for verifying broker certificates"
        ],
        "answer": "To specify the location and password of the truststore for verifying broker certificates",
        "explanation": "The `ssl.truststore.location` and `ssl.truststore.password` configurations in Kafka are used to specify the location and password of the truststore for verifying broker certificates. The truststore contains trusted broker certificates, and these settings ensure that clients can verify the broker’s identity for secure SSL/TLS communication."
    },
    {
        "question": "How can you enable SSL/TLS encryption for communication between Kafka brokers?",
        "options": [
            "Set `ssl.enabled.protocols` to `SSL` in the broker configuration",
            "Set `security.inter.broker.protocol` to `SSL` in the broker configuration",
            "Set `ssl.client.auth` to `required` in the broker configuration",
            "Set `ssl.endpoint.identification.algorithm` to `HTTPS` in the broker configuration"
        ],
        "answer": "Set `security.inter.broker.protocol` to `SSL` in the broker configuration",
        "explanation": "To enable SSL/TLS encryption between Kafka brokers, you set `security.inter.broker.protocol` to `SSL`. This ensures all inter-broker communication, including replication and controller messages, are encrypted using SSL/TLS."
    },
    {
        "question": "What is the purpose of the `ssl.client.auth` configuration in Kafka?",
        "options": [
            "To specify the SSL/TLS protocol version to be used for client authentication",
            "To enable or disable SSL/TLS encryption for client connections",
            "To configure the client authentication mode (none, optional, or required)",
            "To set the location of the client certificate for authentication"
        ],
        "answer": "To configure the client authentication mode (none, optional, or required)",
        "explanation": "The `ssl.client.auth` configuration defines the client authentication mode in Kafka. It can be set to `none`, `requested`, or `required` to control whether brokers request or require client certificates during SSL/TLS handshake."
    },
    {
        "question": "What happens when `ssl.client.auth` is set to `required` in the Kafka broker configuration?",
        "options": [
            "Clients are required to provide a valid certificate for authentication",
            "Clients can choose to provide a certificate optionally",
            "Client authentication is disabled, and no certificates are requested",
            "The broker uses the default SSL/TLS protocol version for client authentication"
        ],
        "answer": "Clients are required to provide a valid certificate for authentication",
        "explanation": "When `ssl.client.auth` is set to `required`, the Kafka broker enforces client certificate authentication. Only clients providing valid, trusted certificates can connect to the broker."
    },
    {
        "question": "What is the default value of the `ssl.client.auth` configuration in Kafka?",
        "options": [
            "`none`",
            "`requested`",
            "`required`",
            "`optional`"
        ],
        "answer": "`none`",
        "explanation": "By default, `ssl.client.auth` is set to `none`, meaning client authentication is disabled. Brokers do not request or verify client certificates unless explicitly configured otherwise."
    },
    {
        "question": "What is the purpose of the `sasl.kerberos.service.name` configuration in Kafka?",
        "options": [
            "To specify the Kerberos principal name for the Kafka broker",
            "To set the Kerberos realm for SASL authentication",
            "To configure the Kerberos key distribution center (KDC) hostname",
            "To define the service name used by Kafka brokers for SASL authentication"
        ],
        "answer": "To define the service name used by Kafka brokers for SASL authentication",
        "explanation": "The `sasl.kerberos.service.name` defines the service name that brokers use for Kerberos-based SASL authentication. It typically matches the principal’s service name, usually `kafka`."
    },
    {
        "question": "What is the role of the `sasl.jaas.config` configuration in Kafka SASL authentication?",
        "options": [
            "To specify the path to the JAAS configuration file for SASL authentication",
            "To set the SASL mechanism to be used for authentication (e.g., PLAIN, SCRAM)",
            "To configure the SASL client and server callbacks for authentication",
            "To enable or disable SASL authentication in Kafka"
        ],
        "answer": "To configure the SASL client and server callbacks for authentication",
        "explanation": "The `sasl.jaas.config` property defines the JAAS configuration directly in Kafka’s settings. It includes the login module, principal, and credentials, enabling SASL authentication without a separate JAAS file."
    },
    {
        "question": "What is the purpose of the `sasl.mechanism` configuration in Kafka SASL authentication?",
        "options": [
            "To specify the SASL mechanism to be used for authentication (e.g., PLAIN, SCRAM)",
            "To configure the SASL client and server callbacks for authentication",
            "To set the path to the JAAS configuration file for SASL authentication",
            "To enable or disable SASL authentication in Kafka"
        ],
        "answer": "To specify the SASL mechanism to be used for authentication (e.g., PLAIN, SCRAM)",
        "explanation": "The `sasl.mechanism` defines which SASL mechanism (e.g., PLAIN, SCRAM-SHA-256, GSSAPI) Kafka will use for authentication between clients and brokers."
    },
    {
        "question": "What security protocol does Kafka use by default for communication between clients and brokers?",
        "options": [
            "SSL/TLS",
            "SASL_PLAINTEXT",
            "PLAINTEXT",
            "SASL_SSL"
        ],
        "answer": "PLAINTEXT",
        "explanation": "Kafka uses the `PLAINTEXT` protocol by default, which does not provide encryption or authentication. It should not be used in production environments where security is required."
    },
    {
        "question": "Which security protocol in Kafka provides encryption for data in transit but does not offer authentication?",
        "options": [
            "PLAINTEXT",
            "SASL_PLAINTEXT",
            "SSL",
            "SASL_SSL"
        ],
        "answer": "SSL",
        "explanation": "The `SSL` protocol provides encryption for Kafka communication but does not inherently handle authentication. For both encryption and authentication, `SASL_SSL` is used."
    },
    {
        "question": "What is the purpose of the `process.roles` configuration in KRaft mode?",
        "options": [
            "To specify whether the server acts as a controller, broker, or both",
            "To set the unique identifier for the server",
            "To define the listeners used by the controller",
            "To configure the metrics reporter for the server"
        ],
        "answer": "To specify whether the server acts as a controller, broker, or both",
        "explanation": "In KRaft mode, the `process.roles` configuration specifies whether a server acts as a **controller**, **broker**, or **both**. It determines the role of the node in the Kafka cluster. Examples: `process.roles=broker` (broker-only), `process.roles=controller` (controller-only), and `process.roles=broker,controller` (development only). Other configurations like `node.id`, `controller.listener.names`, or metrics reporters serve different purposes."
    },
    {
        "question": "What is the recommended value for `process.roles` in a production KRaft cluster?",
        "options": [
            "`broker,controller`",
            "`broker` for broker nodes and `controller` for controller nodes",
            "`controller` for all nodes",
            "Leave `process.roles` unconfigured"
        ],
        "answer": "`broker` for broker nodes and `controller` for controller nodes",
        "explanation": "In production, it’s recommended to **separate brokers and controllers**. Set `process.roles=broker` for broker nodes and `process.roles=controller` for controller nodes. This separation ensures better isolation, independent scaling, and reliability. The combined mode (`broker,controller`) is only for testing and not supported in production."
    },
    {
        "question": "What is the purpose of the `controller.quorum.voters` configuration in KRaft mode?",
        "options": [
            "To specify the listeners used by the controllers",
            "To set the minimum number of in-sync replicas for the controller quorum",
            "To define the list of voters in the controller quorum",
            "To configure the metrics reporter for the controllers"
        ],
        "answer": "To define the list of voters in the controller quorum",
        "explanation": "The `controller.quorum.voters` property defines the **list of controller nodes** that participate in the **metadata quorum** and leader election. The syntax is `{id}@{host}:{port}` — for example: `controller.quorum.voters=1@controller1:9093,2@controller2:9093,3@controller3:9093`. Only these nodes can vote in the controller election."
    },
    {
        "question": "What is the minimum number of controllers required for a KRaft cluster?",
        "options": ["1", "2", "3", "4"],
        "answer": "3",
        "explanation": "KRaft requires a **minimum of 3 controllers** to maintain a majority quorum and ensure fault tolerance. With 3 controllers, one can fail and the cluster still maintains a majority (2 out of 3). Fewer than 3 controllers provide no fault tolerance, while 4 or 5 may be used for larger deployments."
    },
    {
        "question": "What happens if a majority of the controllers in a KRaft cluster become unavailable?",
        "options": [
            "The cluster remains operational with reduced performance",
            "The cluster automatically elects a new set of controllers",
            "The cluster becomes unavailable until a majority of controllers are restored",
            "The brokers take over the responsibilities of the controllers"
        ],
        "answer": "The cluster becomes unavailable until a majority of controllers are restored",
        "explanation": "KRaft requires a **majority quorum** for leader election and metadata operations. If a majority of controllers are unavailable, the cluster cannot elect a leader or process metadata, making it unavailable. The brokers cannot take over controller roles, and restoring the majority brings the cluster back online."
    },
    {
        "question": "What is the purpose of the `kafka-storage` tool in KRaft mode?",
        "options": [
            "To configure the storage directories for Kafka brokers",
            "To manage the Kafka consumer offsets",
            "To generate a cluster ID and format storage directories",
            "To monitor the disk usage of Kafka brokers"
        ],
        "answer": "To generate a cluster ID and format storage directories",
        "explanation": "The `kafka-storage` tool in KRaft mode is used to **generate a cluster ID** and **format storage directories**. It ensures each broker/controller directory is properly initialized. Example commands: `kafka-storage random-uuid` (generate ID) and `kafka-storage format -t <cluster-id> -c <config-file>` (format storage)."
    },
    {
        "question": "What is the default location for the Kafka metadata log in KRaft mode?",
        "options": [
            "The first directory specified in the `log.dirs` configuration",
            "The directory specified in the `metadata.log.dir` configuration",
            "The directory specified in the `controller.log.dir` configuration",
            "The Kafka data directory"
        ],
        "answer": "The first directory specified in the `log.dirs` configuration",
        "explanation": "By default, the **metadata log** is stored in the first directory specified in `log.dirs`. If multiple directories are listed, the first is used. You can override this with `metadata.log.dir` if you want to separate metadata from data logs. There’s no `controller.log.dir` in KRaft."
    },
    {
        "question": "What is the purpose of the `kafka-metadata-quorum` tool in KRaft mode?",
        "options": [
            "To manage the Kafka consumer offsets",
            "To generate a cluster ID for the Kafka cluster",
            "To describe the runtime status of the KRaft metadata quorum",
            "To modify the Kafka topic configurations"
        ],
        "answer": "To describe the runtime status of the KRaft metadata quorum",
        "explanation": "The `kafka-metadata-quorum` tool is used to **describe the current status of the KRaft metadata quorum**, showing details such as leader ID, epoch, high watermark, and voters. Example: `kafka-metadata-quorum --bootstrap-server localhost:9092 describe --status` helps monitor quorum health."
    },
    {
        "question": "Which of the following metrics is used to monitor the lag between the active KRaft controller and the last committed record in the metadata log?",
        "options": [
            "`kafka.controller:type=KafkaController,name=ActiveControllerCount`",
            "`kafka.controller:type=ControllerEventManager,name=EventQueueTimeMs`",
            "`kafka.controller:type=KafkaController,name=LastCommittedRecordOffset`",
            "`kafka.controller:type=KafkaController,name=LastAppliedRecordLagMs`"
        ],
        "answer": "`kafka.controller:type=KafkaController,name=LastAppliedRecordLagMs`",
        "explanation": "The metric `kafka.controller:type=KafkaController,name=LastAppliedRecordLagMs` tracks **how far the controller lags behind** the last committed record in the metadata log. For the active controller, this value is zero. For others, it shows delay in applying the latest records."
    },
    {
        "question": "What is the purpose of the `kafka.controller:type=KafkaController,name=OfflinePartitionCount` metric in KRaft mode?",
        "options": [
            "To track the number of partitions without an active leader",
            "To monitor the number of partitions that are under-replicated",
            "To measure the number of partitions not being consumed by any consumer",
            "To count the number of partitions that have exceeded their retention time"
        ],
        "answer": "To track the number of partitions without an active leader",
        "explanation": "`OfflinePartitionCount` measures how many **partitions currently lack a leader**, meaning they are unavailable for reads/writes. A non-zero value signals broker failure or network issues. It’s a key availability metric for cluster health monitoring."
    },
    {
        "question": "What happens when a new broker joins a KRaft cluster and the `controller.quorum.voters` configuration is not updated to include the new broker?",
        "options": [
            "The new broker automatically becomes a voter in the controller quorum",
            "The new broker joins as an observer and does not participate in the controller quorum voting",
            "The new broker is unable to join the cluster until the configuration is updated",
            "The new broker replaces one of the existing voters in the controller quorum"
        ],
        "answer": "The new broker joins as an observer and does not participate in the controller quorum voting",
        "explanation": "When a new broker joins a KRaft cluster, it does not automatically become a voter in the controller quorum unless the `controller.quorum.voters` configuration is updated. Instead, it joins as an observer, meaning it can replicate metadata but does not participate in voting. To make it a voter, its ID and address must be added to the `controller.quorum.voters` configuration and propagated to all nodes."
    },
    {
        "question": "What is the purpose of the `kafka.controller:type=SnapshotEngine,name=SnapshotGenerationTimeoutCount` metric in KRaft mode?",
        "options": [
            "It measures the number of snapshots that were generated successfully within the configured timeout",
            "It indicates the count of snapshots that failed to generate due to a timeout",
            "It represents the number of snapshots that are currently being generated",
            "It tracks the count of snapshots that were generated after exceeding the configured timeout"
        ],
        "answer": "It indicates the count of snapshots that failed to generate due to a timeout",
        "explanation": "The `SnapshotGenerationTimeoutCount` metric tracks how many snapshot generations failed due to exceeding the configured timeout. In KRaft, snapshots help controllers compact metadata logs and speed up recovery. A high value for this metric indicates performance issues or bottlenecks during snapshot generation."
    },
    {
        "question": "In KRaft mode, what happens when a broker is removed from the `controller.quorum.voters` configuration?",
        "options": [
            "The removed broker is immediately disconnected from the cluster",
            "The removed broker continues to operate as a non-voter observer",
            "The removed broker becomes a candidate and triggers a new controller election",
            "The removed broker enters a controlled shutdown process"
        ],
        "answer": "The removed broker continues to operate as a non-voter observer",
        "explanation": "When a broker is removed from `controller.quorum.voters`, it stops being a voting member and becomes an observer. The broker still receives metadata and serves clients but no longer participates in elections or quorum decisions."
    },
    {
        "question": "What is the impact of setting the `controller.quorum.election.backoff.max.ms` configuration to a very high value in KRaft mode?",
        "options": [
            "It increases the frequency of controller elections, improving fault tolerance",
            "It reduces the time taken for a new controller to be elected, minimizing downtime",
            "It prolongs the time taken for a new controller to be elected, potentially increasing downtime",
            "It has no impact on the controller election process"
        ],
        "answer": "It prolongs the time taken for a new controller to be elected, potentially increasing downtime",
        "explanation": "A high value for `controller.quorum.election.backoff.max.ms` increases the waiting period before brokers attempt controller election. This can delay failover and increase downtime after controller failure. The default (1 second) is typically sufficient."
    },
    {
        "question": "What is the purpose of the `kafka.controller:type=QuorumController,name=ActiveControllerCount` metric in KRaft mode?",
        "options": [
            "It indicates the number of active controllers in the KRaft cluster",
            "It represents the number of brokers currently serving as controllers",
            "It measures the count of controllers that have been active since the cluster started",
            "It tracks the number of controller failover events that have occurred"
        ],
        "answer": "It indicates the number of active controllers in the KRaft cluster",
        "explanation": "The `ActiveControllerCount` metric shows how many controllers are currently active. In a healthy KRaft cluster, it should always be 1 — indicating a single leader. A value of 0 or greater than 1 suggests controller election or quorum issues."
    },
    {
        "question": "What is the significance of the `kafka.controller:type=QuorumController,name=LastAppliedRecordTimestamp` metric in KRaft mode?",
        "options": [
            "It indicates the timestamp of the last record appended to the metadata log",
            "It represents the timestamp of the last record replicated to all the controllers",
            "It measures the timestamp of the last record applied by the active controller",
            "It tracks the timestamp of the last record committed by the active controller"
        ],
        "answer": "It measures the timestamp of the last record applied by the active controller",
        "explanation": "This metric shows when the active controller last applied a record from the metadata log. If it's lagging behind the current time, it indicates delays in metadata application — possibly due to load or performance bottlenecks."
    },
    {
        "question": "What is the impact of setting `controller.quorum.fetch.timeout.ms` to a very low value in KRaft mode?",
        "options": [
            "It increases the time the controllers wait for a fetch response from the active controller",
            "It reduces the time the controllers wait for a fetch response from the active controller",
            "It sets the maximum time allowed for a controller to fetch data from the brokers",
            "It determines the frequency at which the controllers fetch data from the active controller"
        ],
        "answer": "It reduces the time the controllers wait for a fetch response from the active controller",
        "explanation": "A low `controller.quorum.fetch.timeout.ms` shortens how long controllers wait for metadata fetch responses. This can improve failure detection speed but may cause false timeouts if set too low. The default is 2000 ms."
    }
]
