from datetime import datetime
from pydantic import BaseModel


class Tracking(BaseModel):
    id: int
    status_code: int
    completion_time: float
    timestamp: datetime

    class Config:
        orm_mode = True
