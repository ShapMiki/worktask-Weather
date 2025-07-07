from fastapi import Request, HTTPException, Depends, status

from app.user.dao import UserDAO



async def get_user_id(request: Request):
    try:
        user_id = int(request.cookies.get("user_id"))
    except (ValueError, TypeError):
        return None

    if not user_id:
        print("New user")
        return None

    user = await UserDAO.find_one_or_none(id=user_id)

    if not user:
        print("New user")
        return None

    return user_id


