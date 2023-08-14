import requests
from twilio.rest import Client
import os


def main():
    # Load environment variables
    weather_api_key = os.environ.get("API_KEY")
    account_sid = os.environ.get("ACCOUNT_SID")
    auth_token = os.environ.get("AUTH_TOKEN")
    my_num = os.environ.get("MY_NUM")

    # Coordinates for location (Hod Hasharon, Israel)
    my_lat = 32.149960
    my_lon = 34.883881

    # Test
    # manchester_lat = 53.480759
    # manchester_lon = -2.242631

    # API endpoint and parameters for OpenWeatherMap
    url_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
    weather_params = {
        "lat": my_lat,
        "lon": my_lon,
        "appid": weather_api_key,
        "exclude": "current,minutely,daily"
    }

    try:
        # Fetch weather data
        response = requests.get(url=url_endpoint, params=weather_params)
        response.raise_for_status()
        weather_data = response.json()

        # Extract hourly weather data for the next 12 hours
        weather_slice = weather_data["hourly"][:12]

        # Check if rain is expected
        will_rain = any(int(hour_data["weather"][0]["id"]) < 700 for hour_data in weather_slice)

        # Send notification if rain is expected
        if will_rain:
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body="It's going to rain today. Remember to bring an ☂️",
                from_=my_num,
                to="+972525523599"
            )
            print("Message sent:", message.status)

    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
