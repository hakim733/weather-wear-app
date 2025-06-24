import requests
from datetime import datetime

def get_lat_lon(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1}
    response = requests.get(url, params=params)
    data = response.json()
    results = data.get("results")
    if results:
        return results[0]["latitude"], results[0]["longitude"]
    else:
        raise ValueError(f"City '{city}' not found.")

def fetch_weather(city=None, lat=52.52, lon=13.41):
    if city:
        lat, lon = get_lat_lon(city)
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,relative_humidity_2m,windspeed_10m",
        "current_weather": "true",
        "timezone": "auto"
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Use current weather if available
    current = data.get("current_weather", {})
    return {
        "temp": current.get("temperature", 0),
        "humidity": current.get("relative_humidity", 50),  # fallback
        "wind_speed": current.get("windspeed", 5),
        "condition": "Clear"  # Open-Meteo doesn't return condition text directly
    }
