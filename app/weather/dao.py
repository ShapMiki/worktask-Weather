from sqlalchemy import select, func
from datetime import datetime, timedelta

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.weather.models import Weather
from app.config import settings

class WeatherDAO(BaseDAO):
    model = 'Weather'

    @staticmethod
    async def add_one(user_id: int, city: str, description: str, request_datetime: str):
        async with async_session_maker() as session:
            dt_aware = datetime.fromisoformat(request_datetime.replace("Z", "+00:00"))
            dt_aware += timedelta(hours=settings.hour_zone)
            dt_naive = dt_aware.replace(tzinfo=None)
            new_weather = Weather(
                user_id=user_id,
                city=city,
                description=description,
                request_datatime=dt_naive
            )
            session.add(new_weather)
            await session.commit()
            return new_weather
