from fastapi import FastAPI
from pydantic import BaseModel
from app.detector import detect_threat

app = FastAPI(title="Threat Detection Service")


class LogEvent(BaseModel):
    ip: str
    failed_attempts: int = 0
    payload: str = ""


@app.post("/analyze")
def analyze_log(event: LogEvent):
    result = detect_threat(event.dict())
    return result


@app.get("/")
def health_check():
    return {"status": "Threat Detection Service Running"}
