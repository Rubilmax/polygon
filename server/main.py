from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/performances")
def get_performances(timeframe_hours: Optional[str] = "24"):
    return {"timeframe": timeframe_hours + " hours"}
