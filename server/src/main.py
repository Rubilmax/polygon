import time
from datetime import datetime, timedelta
from typing import Optional

from fastapi import FastAPI, BackgroundTasks
from starlette.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from sqlalchemy.sql import func

from . import models, schemas


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
    db_url="mysql://polygon_user:polygon_password@127.0.0.1:3306/polygon_db",
)


def save_tracking(start_time: float, timestamp: datetime):
    with db():
        tracking = models.Tracking(
            timestamp=timestamp,
            status_code=200,
            completion_time=time.time() - start_time,
        )

        db.session.add(tracking)
        db.session.commit()


@app.get("/performances", response_model=schemas.Performances)
async def get_performances(
    background_tasks: BackgroundTasks, timeframe_hours: Optional[str] = "24"
):
    start_time = time.time()
    timestamp = datetime.utcnow()
    background_tasks.add_task(save_tracking, start_time, timestamp)

    datetime_origin = timestamp - timedelta(hours=float(timeframe_hours))

    min_completion_time, avg_completion_time, max_completion_time = (
        db.session.query(
            func.min(models.Tracking.completion_time),
            func.avg(models.Tracking.completion_time),
            func.max(models.Tracking.completion_time),
        )
        .filter(models.Tracking.timestamp >= datetime_origin)
        .one()
    )

    return {
        "min_completion_time": min_completion_time,
        "avg_completion_time": avg_completion_time,
        "max_completion_time": max_completion_time,
    }
