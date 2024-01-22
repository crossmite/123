from pydantic import BaseModel, ConfigDict
from datetime import datetime


class Car(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    number: str
    time: datetime
    price: int
