import json
from aiokafka import AIOKafkaProducer

KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
TOPIC_NAME = "raw-logs"

producer = AIOKafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS
)

async def start_producer():
    await producer.start()

async def stop_producer():
    await producer.stop()

async def send_log(message: dict):
    await producer.send_and_wait(
        TOPIC_NAME,
        json.dumps(message).encode("utf-8")
    )