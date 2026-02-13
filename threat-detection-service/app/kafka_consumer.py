import json
from aiokafka import AIOKafkaConsumer
from app.detector import detect_threat

KAFKA_BOOTSTRAP_SERVERS = "kafka:9092"
TOPIC_NAME = "threat-logs"

consumer = AIOKafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    group_id="threat-detection-group"
)

async def start_consumer():
    await consumer.start()
    try:
        async for msg in consumer:
            log_event = json.loads(msg.value.decode())
            result = detect_threat(log_event)
            print("Threat Detection Result:", result)
    finally:
        await consumer.stop()