import requests

APPID = "3c90c392a11ec6754331a63c1eb734dd"
CITY = "London"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&units=imperial&appid={APPID}"


def getMainWeather():
    response = requests.get(URL)
    data = response.json()
    return data['main']

def main():
    main_weather = getMainWeather()
    print(main_weather, type(main_weather))

    temp = main_weather["temp"]
    print("The Circus current temperature is:",temp,"F")

main()