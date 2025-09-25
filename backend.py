"""
Backend module for Weather App
Fetches forecast data from OpenWeatherMap API.
"""

from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_data(place, forecast_days=None):
    """
    Fetch weather forecast data for a given city.

    Args:
        place (str): City name.
        forecast_days (int): Number of days (1–5).

    Returns:
        list: List of forecast dictionaries from the API.
    """

    if not API_KEY:
        raise ValueError("Missing API key. Set OPENWEATHER_API_KEY in your .env file.")
    if not place.strip():
        raise ValueError("Please enter a city name.")

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    params = {"q": place, "appid": API_KEY, "units": "metric"}

    response = requests.get(url, params=params)
    data = response.json()

    cod = str(data["cod"])
    if cod != "200":
        msg = data["message"]
        if cod == "401":
            raise ValueError(f"{msg}")
        if cod == "404":
            raise ValueError(f"{msg.capitalize()}.")

    data_count = 8 * forecast_days
    observing_dicts = data["list"][:data_count]
    return observing_dicts


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=2))