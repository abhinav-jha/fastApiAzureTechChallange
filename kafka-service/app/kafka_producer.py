# kafka_service/kafka_producer.py
from kafka import KafkaProducer
import json

# Configure the Kafka producer
KAFKA_BROKER = 'localhost:9092'  # Kafka broker address
KAFKA_TOPIC = 'service-events'  # Kafka topic for incoming events

# Create the Kafka producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serializing data as JSON
)

def publish_event(event_type: str, data: dict):
    """Function to send event data to Kafka topic."""
    event = {
        "event": event_type,  # Event name (e.g., PostCreated, UserCreated)
        "data": data          # Payload data (e.g., post or user data)
    }
    
    # Send the event to Kafka
    producer.send(KAFKA_TOPIC, value=event)
    producer.flush()  # Ensure the event is published
    print(f"✅ Event {event_type} published successfully.")
