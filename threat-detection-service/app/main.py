from fastapi import FastAPI
from pydantic import BaseModel
import asyncio

from app.detector import detect_threat
from app.kafka_consumer import start_consumer
from app.database import engine, Base, AsyncSessionLocal
from app.models import Alert
from app.redis_client import redis_client

app = FastAPI(title="Threat Detection Service")


# Create tables on startup
@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    asyncio.create_task(start_consumer())


# Pydantic model
class LogEvent(BaseModel):
    ip: str
    failed_attempts: int = 0
    payload: str = ""


# API endpoint
@app.post("/analyze")
async def analyze_log(event: LogEvent):
    result = detect_threat(event.dict())

    if result["threat_detected"]:
        async with AsyncSessionLocal() as session:
            alert = Alert(
                ip=event.ip,
                threat_detected=True,
                alert_message=",".join(result["alerts"])
            )
            session.add(alert)
            await session.commit()

        redis_client.publish("threat-alerts", str(result))

    return result


@app.get("/")
def health_check():
    return {"status": "Threat Detection Service Running"}
