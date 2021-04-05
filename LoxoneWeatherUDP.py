#!/usr/bin/python3
import socket
import requests
import json
import time
from datetime import datetime, timedelta
import os

api_key = "" #OpenWeahter Api Key
base_url = "http://api.openweathermap.org/data/2.5/weather?" #Url OpenWeatherMap
city_name = "" #Name of the city
complete_url = base_url + "appid=" + api_key + "&q=" + city_name #Complete OpenWeather URL 
udp_ip = "192.168.0.2"
udp_port = 1888

print("LoxoneWeatherUDP application start at ", datetime.now().strftime('%H:%M:%S'))
while True:
    try:
        WeatherResponse = requests.get(complete_url).json()
        if WeatherResponse["cod"] != "404": 
            msg = ("w_tt="+str(round(WeatherResponse["main"]["temp"] - 273.15, 2))+ #Current temperature in °C
                        ";w_pr="+str(WeatherResponse["main"]["pressure"])+ #Pressure in hPa
                        ";w_fl="+str(round(WeatherResponse["main"]["feels_like"] - 273.15, 2))+ #Current temperature feels like in °C
                        ";w_ws="+str(WeatherResponse["wind"]["speed"])+ #Wind speed in m/s 
                        ";w_hmd="+str(WeatherResponse["main"]["humidity"])) #Current humidity 
            udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udp.sendto(bytes(msg, "utf-8"), (udp_ip, udp_port))
            print("data send to loxone server at", datetime.now().strftime('%H:%M:%S'))
        else:
            print("openweathermap connection error at", datetime.now().strftime('%H:%M:%S'))
    except:
        print("internet connection error at", datetime.now().strftime('%H:%M:%S'))
    time.sleep(180)