# kafka_service/kafka_consumer.py
from kafka import KafkaConsumer
import json

KAFKA_BROKER = 'localhost:9092'
KAFKA_TOPIC = 'service-events'
GROUP_ID = 'event-consumer-group'

# Kafka Consumer configuration
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    group_id=GROUP_ID,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Deserialize JSON data
)

def consume_events():
    """Function to consume events from Kafka topic."""
    print("🔄 Consuming events from Kafka...")
    for message in consumer:
        event = message.value
        print(f"📨 Event received: {event['event']} with data: {event['data']}")
        # You can perform any action on the event here (e.g., send notifications)
