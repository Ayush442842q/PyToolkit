import requests

# API Configuration
API_KEY = "055b5a613d4edfed8fc3a92e149d8e35"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
def get_weather(city):
    """Fetches weather data for a given city."""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()
def parse_weather(data):
    """Parses weather data and returns clean dictionary."""
    if data.get("cod") != 200:
        return None
    
    return {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temp": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"]
    }
def display_weather(weather):
    """Displays weather data in a nice format."""
    if not weather:
        print("❌ City not found! Please check the city name.")
        return

    print(f"\n🌍 Weather in {weather['city']}, {weather['country']}")
    print("-" * 40)
    print(f"🌡️  Temperature  : {weather['temp']}°C")
    print(f"🤔 Feels Like   : {weather['feels_like']}°C")
    print(f"💧 Humidity     : {weather['humidity']}%")
    print(f"💨 Wind Speed   : {weather['wind_speed']} m/s")
    print(f"☁️  Description  : {weather['description'].capitalize()}")
    print("-" * 40)
def main():
    """Main function to run the Weather CLI."""
    print("🌤️  PyToolkit Weather CLI")
    print("=" * 40)
    city = input("Enter city name: ").strip()
    if not city:
        print("❌ No city entered.")
        return
    print(f"\n⏳ Fetching weather for '{city}'...")
    data = get_weather(city)
    weather = parse_weather(data)
    display_weather(weather)

if __name__ == "__main__":
    main()
def get_forecast(city):
    """Fetches 5-day weather forecast for a given city."""
    FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(FORECAST_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        print("❌ Network error! Please check your internet connection.")
        return None
    except requests.exceptions.Timeout:
        print("❌ Request timed out! Try again later.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Something went wrong: {e}")
        return None
def display_forecast(data):
    """Displays 5-day weather forecast in a nice format."""
    if not data or data.get("cod") != "200":
        print("❌ Could not fetch forecast data.")
        return

    city = data["city"]["name"]
    country = data["city"]["country"]
    print(f"\n📅 5-Day Forecast for {city}, {country}")
    print("=" * 40)

    seen_dates = []
    for item in data["list"]:
        date = item["dt_txt"].split(" ")[0]
        if date not in seen_dates:
            seen_dates.append(date)
            temp = item["main"]["temp"]
            description = item["weather"][0]["description"]
            humidity = item["main"]["humidity"]
            print(f"📆 {date}")
            print(f"   🌡️  Temp       : {temp}°C")
            print(f"   💧 Humidity   : {humidity}%")
            print(f"   ☁️  Condition  : {description.capitalize()}")
            print("-" * 40)