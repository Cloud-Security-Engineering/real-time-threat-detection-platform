from pydantic import BaseModel, ConfigDict
from datetime import datetime


class LogEvent(BaseModel):
    service_name: str
    log_level: str
    message: str
    timestamp: datetime

    # Ensures datetime is serialized properly
    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.isoformat()
        }
    )
