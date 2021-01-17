import time
from datetime import datetime

from fastapi_sqlalchemy import db

from .. import models


def create_tracking(start_time: float, request_datetime: datetime, status_code: int):
    with db():
        tracking = models.Tracking(
            request_datetime=request_datetime,
            status_code=status_code,
            completion_time=time.time() - start_time,
        )

        db.session.add(tracking)
        db.session.commit()
