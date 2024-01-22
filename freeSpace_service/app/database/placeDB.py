from sqlalchemy import Column, String, DateTime, Integer
from database import Base


class PlaceDB(Base):
    tablename = 'place'

    id = Column(Integer, primary_key=True, index=True)
    number = Column(String, nullable=False)

