from fastapi import APIRouter, Request, Depends, Response, HTTPException

from app.user.dependencies import get_user_id
from app.weather.service import get_weather
from app.weather.dao import WeatherDAO


router = APIRouter(
    prefix="/weather",
    tags=["weather"],
)
@router.get("/current/{city}")
async def get_current_weather(city:str, request: Request, response: Response, user_id: int = Depends(get_user_id)):
    weather = await get_weather(city)
    if not weather:
        return HTTPException(status_code=404, detail="Weather data not found")

    description = f"{weather['temp']}, {weather['condition']}"

    await WeatherDAO.add_one(user_id=user_id, city=city, description=description, request_datetime=weather['now_dt'])

    print("weather", weather)

    return weather


@router.get("/all")
async def get_all_history(request: Request, response: Response):
    # Todo: реализовать
    data = [
        "london, 32℃, sunny - 07.07.2025 11:22",
        "london, 32℃, sunny - 06.07.2025 14:32",
        "london, 32℃, sunny - 01.07.2025 18:56",
        "london, 32℃, sunny - 30.06.2025 3:09",
        "ondon, 32℃, sunny - 29.06.2025 12:00",
        "london, 32℃, sunny - 28.06.2025 16:22",
        "london, 32℃, sunny - 28.06.2025 6:46",
        "london, 32℃, sunny - 27.06.2025 6:26",
        "london, 32℃, sunny - 26.06.2025 9:15",
        "london, 12℃, sunny - 07.07.2025 11:22",
        "london, 2℃, sunny - 06.07.2025 14:32",
        "london, 2℃, sunny - 01.07.2025 18:56",
        "london, 1℃, sunny - 30.06.2025 3:09",
        "ondon, 3℃, sunny - 29.06.2025 12:00",
        "london, 2℃, sunny - 28.06.2025 16:22",
        "london, 1℃, sunny - 28.06.2025 6:46",
        "london, 3℃, sunny - 27.06.2025 6:26",
        "london, 1℃, sunny - 26.06.2025 9:15",
    ]
    return data

@router.get("/self")
async def get_self_history(request: Request, response: Response):
    #Todo: реализовать
    data = [
        "Minsk, 32℃, sunny - 07.07.2025 11:22",
        "vMinsk, 32℃, sunny - 06.07.2025 14:32",
        "Minsk, 32℃, sunny - 01.07.2025 18:56",
        "Minsk, 32℃, sunny - 30.06.2025 3:09",
        "Minsk, 32℃, sunny - 29.06.2025 12:00",
        "Minsk, 32℃, sunny - 28.06.2025 16:22",
        "Minsk, 32℃, sunny - 28.06.2025 6:46",
        "Minsk, 32℃, sunny - 27.06.2025 6:26",
        "Minsk, 32℃, sunny - 26.06.2025 9:15",
        "Minsk, 12℃, sunny - 07.07.2025 11:22",
        "Minsk, 2℃, sunny - 06.07.2025 14:32",
        "Minsk, 2℃, sunny - 01.07.2025 18:56",
        "Minsk, 1℃, sunny - 30.06.2025 3:09",
        "Minsk, 3℃, sunny - 29.06.2025 12:00",
        "Minsk, 2℃, sunny - 28.06.2025 16:22",
        "Minsk, 1℃, sunny - 28.06.2025 6:46",
        "Minsk, 3℃, sunny - 27.06.2025 6:26",
        "Minsk, 1℃, sunny - 26.06.2025 9:15",
    ]
    return data
