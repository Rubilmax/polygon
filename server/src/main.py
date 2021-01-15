from typing import Optional

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware

from fastapi_sqlalchemy import db
from .models.model import Tracking

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(
    DBSessionMiddleware,
    db_url="mysql://polygon_user:polygon_password@localhost:3306/polygon_db",
)


@app.get("/performances")
def get_performances(timeframe_hours: Optional[str] = "24"):
    return {
        "timeframe": timeframe_hours + " hours",
        "trackings": db.session.query(Tracking).first(),
    }
