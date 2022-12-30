from backend.database import Base

from sqlalchemy import Column, Integer, String, Time



class Routine(Base):
    __tablename__ = 'routines'

    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    starttime = Column(Time)

    def __repr__(self) -> str:
        return f"{self.name} at {self.starttime.hour}:{self.starttime.minute}"
