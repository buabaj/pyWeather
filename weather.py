#importing required modules
import requests, json

#enter your API key from openweathermap.org here
api_key = 'Your API key goes here'

#base url to store url from api
base_url = "http://api.openweathermap.org/data/2.5/weather?"

#input city name here
city_name = input('Enter city name: ')

complete_url = base_url + 'appid=' + api_key + '&q=' + city_name
response = requests.get(complete_url)
x = response.json()

#checking validity f city name
if x['cod'] != '404':
    y = x['main']
    current_temperature = y['temp']
    current_pressure = y['pressure']
    current_humidity = y['humidity']
    z = x['weather']
    weather_description = z[0]['description']

    print('Temperature (in Kelvin unit) = ' + str(current_temperature) + '\n Atmospheric Pressure (in hPa unit) = ' + str(current_pressure) + '\n Humidity (in percentage) = ' + str(current_humidity) + '\n Weather Description = ' + weather_description)
else:
    print('City Not Found')
