from sqlalchemy import select, func

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.user.models import User

class UserDAO(BaseDAO):
    model = 'Weather'  # Assuming the model is defined in the same module as this DAO

    @staticmethod
    async def add_one():
        async with async_session_maker() as session:
            new_user = User()
            session.add(new_user)
            await session.commit()
            return new_user


