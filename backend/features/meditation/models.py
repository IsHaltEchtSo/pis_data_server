from backend.database import Base

from sqlalchemy import Column, Integer, String, Text



class Meditation(Base):
    __tablename__ = 'meditations'

    id          = Column(Integer, primary_key = True)
    name        = Column(String, nullable = False)
    description = Column(Text, nullable = False)

    def __repr__(self) -> str:
        return f"{self.name}"
