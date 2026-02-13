# app/models.py

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.database import Base


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String, index=True)
    threat_type = Column(String)
    failed_attempts = Column(Integer)
    payload = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())