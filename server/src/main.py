from datetime import datetime, timedelta
from typing import Optional

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from sqlalchemy.sql import func

from . import models, schemas
from .middlewares.tracking import TrackingMiddleware


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
    db_url="mysql://polygon_user:polygon_password@host.docker.internal:3306/polygon_db",
)
app.add_middleware(TrackingMiddleware)


@app.get("/performances", response_model=schemas.Performances)
def get_performances(timeframeHours: Optional[str] = "24"):
    current_datetime = datetime.utcnow()
    datetime_origin = current_datetime - timedelta(hours=float(timeframeHours))

    min_completion_time, avg_completion_time, max_completion_time = (
        db.session.query(
            func.min(models.Tracking.completion_time),
            func.avg(models.Tracking.completion_time),
            func.max(models.Tracking.completion_time),
        )
        .filter(models.Tracking.request_datetime >= datetime_origin)
        .one()
    )

    return {
        "minCompletionTime": min_completion_time,
        "avgCompletionTime": avg_completion_time,
        "maxCompletionTime": max_completion_time,
    }
