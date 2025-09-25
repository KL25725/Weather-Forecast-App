from dotenv import load_dotenv
import os
import requests
load_dotenv()
api_key = os.getenv("OPENWEATHER_API")

def get_data(place, forcast_days=None, topic=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"

    params = {
        "q": place,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(url, params=params)
    data = response.json()
    data_count = 8 * forcast_days
    observing_dicts = data["list"][:data_count]
    return observing_dicts


if __name__ == "__main__":
    print(get_data(place="Tokyo", forcast_days=2, topic="Sky"))