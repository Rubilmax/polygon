from datetime import datetime
from pydantic import BaseModel


class Tracking(BaseModel):
    id: int
    status_code: int
    completion_time: float
    request_datetime: datetime

    class Config:
        orm_mode = True
