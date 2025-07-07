from fastapi import APIRouter, Request, Depends, Response
from fastapi.templating import Jinja2Templates

from app.weather.dao import WeatherDAO
from app.user.dao import UserDAO
from app.user.dependencies import get_user_id


router = APIRouter(
    prefix="/pages",
    tags=["pages"],
)

templates = Jinja2Templates(directory="app/templates")

@router.get("/")
async def get_main_page(request: Request, response: Response,
                        user_id: int = Depends(get_user_id)):

    response = templates.TemplateResponse("index.html", {"request": request})

    if not user_id:
        new_user = await UserDAO.add_one()
        response.set_cookie(key="user_id", value=str(new_user.id), max_age=31536000, httponly=True)

    return response



@router.get("/history")
async def get_history_page(request: Request, response: Response,
                           user_id: int = Depends(get_user_id)):

    response = templates.TemplateResponse("history_page.html", {"request": request})

    if not user_id:
        new_user = await UserDAO.add_one()
        response.set_cookie(key="user_id", value=str(new_user.id), max_age=31536000, httponly=True)

    return response

    #TODO: Логика истории

