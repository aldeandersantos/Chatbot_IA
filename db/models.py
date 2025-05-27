from sqlalchemy import Column, Integer, String, JSON, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Session(Base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True)
    session_id = Column(String, index=True)
    data = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())