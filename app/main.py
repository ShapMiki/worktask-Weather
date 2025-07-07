from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from app.pages.router import router as pages_router
from app.weather.router import router as weather_router
from app.user.router import router as user_router

#uvicorn  app.main:app --host  0.0.0.0 --port 80 --reload
#alembic revision --autogenerate -m "initial"
app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")


app.include_router(pages_router)
app.include_router(weather_router, prefix="/api")
app.include_router(user_router, prefix="/api")


@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    return  RedirectResponse(url="/pages/")


