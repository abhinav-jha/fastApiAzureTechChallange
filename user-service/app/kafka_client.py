# user_service/kafka_client.py
import requests
from fastapi import HTTPException

KAFKA_SERVICE_URL = "http://kafka-service:8000/publish_event"

def send_event_to_kafka(event_type: str, event_data: dict):
    """Send event to Kafka Service."""
    try:
        response = requests.post(KAFKA_SERVICE_URL, json={"event_type": event_type, "data": event_data})
        response.raise_for_status()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to send event to Kafka")

# Example: Creating a user and sending the event
@app.post("/users/")
async def create_user(user_data: dict):
    # Logic for creating a user (save to DB)
    user = create_user_in_db(user_data)
    
    # Send event to Kafka
    send_event_to_kafka("UserCreated", user)
    
    return {"message": "User created successfully"}
