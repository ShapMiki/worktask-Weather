from fastapi import APIRouter, Request, Depends, Response, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.weather.dao import WeatherDAO
from app.user.dao import UserDAO
from app.user.dependencies import get_user_id
from app.redis_client import get_redis



templates = Jinja2Templates(directory="app/templates")
router = APIRouter(
    prefix="/pages",
    tags=["pages"],
)

@router.get("/")
async def get_main_page(request: Request, response: Response,
                        user_id: int = Depends(get_user_id)):

    response = templates.TemplateResponse("index.html", {"request": request})

    if not user_id:
        new_user = await UserDAO.add_one()
        response.set_cookie(key="user_id", value=str(new_user.id), max_age=31536000, httponly=True)

    return response


@router.get("/history/{history_type}")
async def get_history_page(history_type: str, request: Request,
    user_id: int = Depends(get_user_id)):

    redis = await get_redis()
    data = {}

    if not user_id:
        user_id = 0
        history = []

    if history_type == "self":
        cache_key = f"user:{user_id}:history_page"
        cached_html = await redis.get(cache_key)

        if cached_html:
            return HTMLResponse(content=cached_html)
        if user_id:
            history = await UserDAO.get_personal_history(user_id)
        data['another_history_type'] = "all"

    elif history_type == "all":
        cache_key = "all_history_page"
        cached_html = await redis.get(cache_key)

        if cached_html:
            return HTMLResponse(content=cached_html)

        history = await WeatherDAO.get_all_history()
        data['another_history_type'] = "self"

    else:
        raise HTTPException(status_code=404, detail="History type not found")

    template_response = templates.TemplateResponse(
        "history_page.html",
        {"request": request, "history": history, "data": data}
    )

    await redis.set(cache_key, template_response.body.decode("utf-8"), ex=1)
    return template_response
