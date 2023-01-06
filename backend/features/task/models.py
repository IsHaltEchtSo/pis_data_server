from backend.database import Base

from sqlalchemy import Column, Integer, String, Boolean



class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    task_name = Column(String, nullable=False)
    daily = Column(Boolean, default=True)