from fastapi import FastAPI
from app.models import LogEvent
from app.kafka_producer import start_producer, stop_producer, send_log

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await start_producer()

@app.on_event("shutdown")
async def shutdown_event():
    await stop_producer()

@app.get("/")
async def root():
    return {"message": "Log Ingestion Service Running 🚀"}

@app.post("/logs")
async def ingest_log(log: LogEvent):
    data = log.model_dump(mode="json")
    await send_log(data)
    return {"status": "sent to kafka"}