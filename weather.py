import requests
from datetime import datetime

URL = "https://api.open-meteo.com/v1/forecast"


def fetch_weather(latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "timezone": "Africa/Kampala",
    }

    try:
        response = requests.get(URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("Error: the weather service took too long to respond. Try again.")
    except requests.exceptions.ConnectionError:
        print("Error: could not connect. Check your internet connection.")
    except requests.exceptions.HTTPError as error:
        print(f"Error: the server returned a problem ({error.response.status_code}).")
    except requests.exceptions.RequestException as error:
        print(f"Error: something went wrong with the request: {error}")
    return None


def print_report(city, data):
    try:
        current = data["current"]
        units = data["current_units"]

        temperature = current["temperature_2m"]
        humidity = current["relative_humidity_2m"]
        wind_speed = current["wind_speed_10m"]
        elevation = data["elevation"]
        reported_at = datetime.fromisoformat(current["time"])
    except KeyError as error:
        print(f"Error: the response was missing expected data: {error}")
        return

    nice_time = reported_at.strftime("%d %B %Y, %H:%M")

    if humidity > 80:
        feel = "Very humid"
    else:
        feel = "Comfortable"

    print("=" * 34)
    print(f"  Current Weather Report: {city}")
    print("=" * 34)
    print(f"{'Temperature:':<16}{temperature:.1f} {units['temperature_2m']}")
    print(f"{'Humidity:':<16}{humidity} {units['relative_humidity_2m']}")
    print(f"{'Wind speed:':<16}{wind_speed:.1f} {units['wind_speed_10m']}")
    print(f"{'Elevation:':<16}{elevation:,.0f} metres above sea level")
    print(f"{'Reported at:':<16}{nice_time} (East Africa Time)")
    print(f"{'Feeling:':<16}{feel}")
    print("=" * 34)


weather_data = fetch_weather(0.3163, 32.5822)

if weather_data is not None:
    print_report("Kampala", weather_data)