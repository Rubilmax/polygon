from sqlalchemy import Column, Integer, Float, DateTime

from .model import Model


class Tracking(Model):
    __tablename__ = "Trackings"

    id = Column("tracking_id", Integer, primary_key=True, index=True)
    status_code = Column("status_code", Integer)
    completion_time = Column("completion_time", Float)
    request_datetime = Column("request_datetime", DateTime)
