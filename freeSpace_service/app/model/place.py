from pydantic import BaseModel, ConfigDict



class Place(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    number: str