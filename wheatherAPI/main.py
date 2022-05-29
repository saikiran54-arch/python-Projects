import requests

API_KEY = "45075d92f31f9310f4c3eb65677df939"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("enter a city name : ")
response_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(response_url)

if response.status_code == 200:
    data  = response.json()
    # weather
    weather = data['weather'][0]['description']
    print(f"Weather : {weather}")
    # temperature
    # celsius = kelvin - 273.15
    temperature =round(data["main"]["temp"]-273.15,2)
    print(f"Temparture : {temperature} C")
    # wind speed
    # 1 mile = 1.6 km
    wind = round(data['wind']['speed']*1.6)
    print(f"Wind Speed : {wind} km/h")

else:
    print("An error occured")
