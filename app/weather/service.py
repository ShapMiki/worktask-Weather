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
            "feels_like": response["main"]["feels_like"],
            "wind_speed": response["wind"]["speed"],
            'now_dt': datetime.utcnow()
        }
        return weather
    except requests.RequestException as e:
        print(e)
        return {"error": str(e)}

"""
async def get_weather(city):
    city = city.replace(" ", "+")
    coordinates_url=f"https://geocode-maps.yandex.ru/v1/?apikey={settings.yandex_geocoder_api_key}&geocode={city}&format=json"

    headers = {
        'X-Yandex-Weather-Key': settings.yandex_weather_api_key
    }
    try:
        response = requests.get(coordinates_url)
        response.raise_for_status()

        coordinates = response.json()["response"]["GeoObjectCollection"][("featureMember")][0]["GeoObject"]["boundedBy"]["Envelope"]["lowerCorner"]
        coordinates = coordinates.split(" ")


        weather_url = (f"https://api.weather.yandex.ru/v2/forecast?lat={coordinates[1]}" +
                       f"&lon={coordinates[0]}&lang=en_US&limit=1" )
        response = requests.get(weather_url, headers=headers)
        response.raise_for_status()
        response = response.json()
        all_weather_fact_data = response["fact"]
        weather = {
            "temp": all_weather_fact_data["temp"],
            "condition": all_weather_fact_data["condition"],
            "feels_like": all_weather_fact_data["feels_like"],
            "wind_speed": all_weather_fact_data["wind_speed"],
            'now_dt': response["now_dt"]
        }

    except requests.RequestException as e:
        return {"error": str(e)}

    return weather
"""
"""
async def main():
    city = "London"
    weather_data = await get_weather(city)
    print(weather_data)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
"""