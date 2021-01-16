from pydantic import BaseModel


class Performances(BaseModel):
    min_completion_time: float
    avg_completion_time: float
    max_completion_time: float
