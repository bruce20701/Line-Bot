from weatherQurey import weatherQurey
from weather import Weather
from datetime import datetime

#模擬在Line打的message
testMessage = "查詢天氣「臺北市」"

#判斷message為查詢天氣就呼叫weatherQurey function
if(testMessage[:4] == "查詢天氣"):
    weather =  Weather(weatherQurey(testMessage[5:8]))
    weather.printWeather()
