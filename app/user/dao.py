from sqlalchemy import select, func
from sqlalchemy.orm import joinedload

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.user.models import User
from app.weather.models import Weather



class UserDAO(BaseDAO):
    model = User

    @staticmethod
    async def add_one() -> None:
        async with async_session_maker() as session:
            new_user = User()
            session.add(new_user)
            await session.commit()
            return new_user

    @staticmethod
    async def get_personal_history(user_id: int) -> list[dict]:
        async with async_session_maker() as session:
            query = (
                select(User)
                .options(joinedload(User.weathers))
                .where(User.id == user_id)
            )
            result = await session.execute(query)
            user = result.unique().scalar_one_or_none()

            if not user or not user.weathers:
                return []
            if not user:
                return []

            return [
                {
                    "city": w.city,
                    "weather": w.condition,
                    "temperature": w.temperature,
                    "request_datetime": w.request_datatime.strftime("%H:%M %d.%m.%Y")
                }
                for w in sorted(user.weathers, key=lambda x: x.request_datatime, reverse=True)
            ]

