from pydantic import BaseModel


class Performances(BaseModel):
    minCompletionTime: float
    avgCompletionTime: float
    maxCompletionTime: float
