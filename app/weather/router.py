from fastapi import APIRouter, Request, Depends, Response, HTTPException

from app.user.dependencies import get_user_id
from app.weather.service import get_weather
from app.weather.dao import WeatherDAO


router = APIRouter(
    prefix="/weather",
    tags=["weather"],
)
@router.get("/current/{city}")
async def get_current_weather(city:str, user_id: int = Depends(get_user_id)):
    try:
        weather = await get_weather(city)

        await WeatherDAO.add_one(user_id=user_id, city=city, condition=weather['condition'],
                             temp=weather['temp'], request_datetime=weather['now_dt'])

    except KeyError:
        raise HTTPException(status_code=404, detail="Weather data not found for this city")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

    return weather



