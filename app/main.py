from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from app.pages.router import router as pages_router
from app.weather.router import router as weather_router
from app.user.router import router as user_router
from app.redis_client import init_redis

#uvicorn  app.main:app --host  0.0.0.0 --port 80 --reload
#alembic revision --autogenerate -m "initial"


app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

app.mount("/static", StaticFiles(directory="app/static"), name="static")


app.include_router(pages_router)
app.include_router(weather_router, prefix="/api")
app.include_router(user_router, prefix="/api")

@app.on_event("startup")
async def startup():
    await init_redis()

@app.get("/")
async def redirect_to_pages():
    return RedirectResponse(url="/pages/")

@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    if request.url.path.startswith("/api/"):

        return JSONResponse(status_code=404, content={"detail": str(exc)})
    else:
        return templates.TemplateResponse(
            "exception_page.html",
            {"request": request, "data": {'code': 404, 'details': 'Page not found'}},
            status_code=404
        )
