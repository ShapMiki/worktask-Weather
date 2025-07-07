from pydantic import BaseModel
from datetime import datetime


class WeatherSchema(BaseModel):
    city: str
    weather: str
    temperature: float
    request_datetime: datetime

    class Config:
        orm_mode = True