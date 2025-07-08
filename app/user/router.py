from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.user.dependencies import get_user_id
from app.weather.dao import WeatherDAO



router = APIRouter(
    prefix="/user",
    tags=["user"],
)

@router.delete("/")
async def delete_history(user_id: int = Depends(get_user_id)):

    if not user_id:
        return JSONResponse(status_code=200, content={"detail": "You don't have history"})

    user_lines = await WeatherDAO.find_one_or_none(user_id=user_id)
    if not user_lines:
        return JSONResponse(status_code=200, content={"detail": "You don't have history"})

    response = JSONResponse(content={"detail": "History deleted"})
    response.delete_cookie(key="user_id", path="/")
    return response