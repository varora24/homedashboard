import json
import requests
import re


api_key = "959d2ea31caab330b01039ed7c0011d1"

URL = "http://api.openweathermap.org/data/2.5/weather?"
city = "Mumbai"

complete_url = URL + "appid=" + api_key + "&q=" + city

response = requests.get(complete_url)
data = response.json()
weatherinfo = []
if data["cod"] != "404":
    y = data["main"]
    current_temperature = y["temp"] - 273.15
    weatherinfo.append(current_temperature)
    current_pressure = y["pressure"]
    weatherinfo.append(current_pressure)
    current_humidiy = y["humidity"]
    weatherinfo.append(current_humidiy)
    z = data["weather"]
    weather_description = z[0]["description"]
    weatherinfo.append(weather_description)
    #print(" Temperature (in kelvin unit) = " +
    #                str(current_temperature) + 
    #      "\n atmospheric pressure (in hPa unit) = " +
    #                str(current_pressure) +
    #      "\n humidity (in percentage) = " +
    #                str(current_humidiy) +
    #      "\n description = " +
    #                str(weather_description))
  
else:
    print(" City Not Found ")