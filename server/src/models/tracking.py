from sqlalchemy import Column, Integer

from .model import Model


class Tracking(Model):
    __tablename__ = "Trackings"
    id = Column("tracking_id", Integer, primary_key=True)
