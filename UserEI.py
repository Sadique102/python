#1
"""import json
import requests

#def norris_joke():
request = 'https://api.chucknorris.io/jokes/random'
response = requests.get(request)
if response.status_code == 200:
    print(f"It took: {response.elapsed}s ")
    answer = response.json()
    #joke_text = answer['value']
    print(answer["value"])
    #print(json.dumps(answer, indent=2 ))
        #return joke_text
else:
    print("Failed to fetch Chuck Norris joke")"""

"""random_joke = norris_joke()
print("Random Chuck Norris Joke:")
print(random_joke)"""

#2

import requests

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15  # Conversion formula from Kelvin to Celsius
    return celsius

def get_weather_data(api_key, city_name):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        weather_description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        return weather_description, kelvin_to_celsius(temperature)
    else:
        return None, None

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # Replace 'YOUR_API_KEY' with your actual API key from OpenWeather
    city_name = input("Enter the name of a city: ")

    weather, temperature = get_weather_data(api_key, city_name)

    if weather is not None and temperature is not None:
        print(f"Weather in {city_name}: {weather}")
        print(f"Temperature: {temperature:.2f}°C")
    else:
        print("Failed to fetch weather data. Please check the city name or your API key.")




