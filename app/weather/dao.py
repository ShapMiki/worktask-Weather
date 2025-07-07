from sqlalchemy import select, func
from datetime import datetime, timedelta

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.weather.models import Weather
from app.config import settings

class WeatherDAO(BaseDAO):
    model = Weather

    @staticmethod
    async def add_one(user_id: int, city: str, condition: str, temp: float, request_datetime: datetime = datetime.utcnow()):
        async with async_session_maker() as session:
            dt = request_datetime + timedelta(hours=settings.hour_zone)

            new_weather = Weather(
                user_id=int(user_id),
                city=city,
                condition=condition,
                temperature= temp,
                request_datatime=dt
            )

            session.add(new_weather)
            await session.commit()
            return new_weather


    @staticmethod
    async def get_all_history() -> list[dict]:
        async with async_session_maker() as session:
            query = select(Weather).order_by(Weather.request_datatime.desc())
            result = await session.execute(query)
            weathers = result.scalars().all()

            return [
                {
                    "user_id": w.user_id,
                    "city": w.city,
                    "weather": w.condition,
                    "temperature": w.temperature,
                    "request_datetime": w.request_datatime.strftime("%H:%M %d.%m.%Y")
                }
                for w in weathers
            ]
