import requests
from datetime import datetime

LAT = 47.0105
LON = 28.8638

def fetch_weather():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={LAT}&longitude={LON}&current_weather=true"
    )

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    weather = data["current_weather"]

    return {
        "latitude": LAT,
        "longitude": LON,
        "temperature": weather["temperature"],
        "windspeed": weather["windspeed"],
        "weather_code": weather["weathercode"],
        "timestamp": datetime.utcnow().isoformat()
    }