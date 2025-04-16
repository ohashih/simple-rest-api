from datetime import datetime
from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String


class User(Base):
    __table__ = "users"
    id = Column(String, primary_key=True)
    name = Column(String(20), nullable=False, default="dafualt_name")
    created_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
