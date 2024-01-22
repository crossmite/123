from pydantic import BaseModel, ConfigDict
from datetime import datetime


class Place(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    number: str