from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError
from topics.user_topics import get_user_topics
from topics.post_topics import get_post_topics

KAFKA_SERVER = "kafka:9092"  # Change if needed

def create_all_topics():
    topics_config = get_user_topics() + get_post_topics()

    try:
        admin_client = KafkaAdminClient(bootstrap_servers=KAFKA_SERVER)

        new_topics = [
            NewTopic(
                name=topic["name"],
                num_partitions=topic["partitions"],
                replication_factor=topic["replication_factor"],
            )
            for topic in topics_config
        ]

        admin_client.create_topics(new_topics=new_topics, validate_only=False)
        print("Kafka topics created successfully!")

    except TopicAlreadyExistsError:
        print("Some topics already exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        admin_client.close()
