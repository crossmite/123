from sqlalchemy import Column, String, DateTime, Integer
from database import Base


class CarDB(Base):
    tablename = 'cars'

    id = Column(Integer, primary_key=True, index=True)
    number = Column(String, nullable=False)
    time = Column(DateTime, nullable=False)
    price = Column(Integer, nullable=False)

