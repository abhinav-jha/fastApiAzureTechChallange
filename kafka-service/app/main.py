from fastapi import FastAPI
from app.kafka_topics import create_all_topics

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("Creating Kafka topics...")
    create_all_topics()
