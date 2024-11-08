import requests

API_KEY = "8147e07d9ad23194dda9c55027042278"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    try:
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()  # Parse JSON data
            print(data)
            main = data["main"]
            weather = data["weather"][0]

            print(f"City: {data['name']}")
            print(f"Temperature: {main['temp']}°C")
            print(f"Feels Like: {main['feels_like']}°C")
            print(f"Humidity: {main['humidity']}%")
            print(f"Weather: {weather['description'].capitalize()}")

        else:
            print("City not found or other error:", response.status_code, response.text)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

city_name = input("Enter the city name: ")
get_weather(city_name)
