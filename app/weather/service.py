import requests
from app.config import settings
from datetime import datetime

#openweather
async def get_weather(city: str) -> dict:
    try:
        weather_url = ("https://api.openweathermap.org/data/2.5/" +
                       f"weather?q={city}&APPID={settings.api_key}")
        response = requests.get(weather_url)
        response.raise_for_status()
        response = response.json()

        weather = {
            "temp": round(float(response["main"]["temp"]) - 273.15, 2),
            "condition": response["weather"][0]["main"],
            "feels_like": round(float(response["main"]["feels_like"]) - 273.15, 2),
            "wind_speed": response["wind"]["speed"],
            'now_dt': datetime.utcnow()
        }

        return weather

    except requests.RequestException as e:
        status_code = e.response.status_code
        if status_code == 404:
            raise KeyError("City not found")
        else:
            raise e

"""
async def main():
    city = "London"
    weather_data = await get_weather(city)
    print(weather_data)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
"""