# Weather App (GUI with Tkinter library)

# Required Libraries
import tkinter as tk
from tkinter import *
import requests
from datetime import datetime

# Api Key

Api_Key = "7c58050b4802ad042224bdde687ecfca"

# Function to get weather city

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + Api_Key + "&q=" + city + "&units=metric"

    response = requests.get(complete_url)
    return response.json()

# Function To show Weater city

def show_weather():
    city = city_entry.get()
    weather= get_weather(city)

    if weather['cod'] == 200:
        temp = weather['main']['temp']
        humidity = weather['main']['humidity']
        pressure = weather['main']['pressure']
        wind = weather['wind']['speed']
        description = weather['weather'][0]['description']
        sunrise = datetime.fromtimestamp(weather['sys']['sunrise']).strftime("%H:%M:%S")
        sunset = datetime.fromtimestamp(weather['sys']['sunset']).strftime("%H:%M:%S")

        weather_info = f'''

        Weather in {city}
        Temperature : {temp} °C
        Humidity : {humidity} %
        Pressure {pressure} hpa
        Wind Speed {wind} m/s
        Description {description}
        Sunrise {sunrise}
        Sunset {sunset}
        
        '''
    else:
        weather_info = "City Not Found!!!"
    

    result_label.config(text=weather_info)



###--------------------- Tkinter GUI--------------------------- ###

# Code to Initialize Tkinter App
root = tk.Tk()
root.title("Mabtoor Mabx Weather App (GUI Based)")
root.geometry("400x450")
root.resizable(0,0)

# Code to create Title, city, city_entry, search Button and Result label (Tkinter Library)
title_label = tk.Label(root, text="Weather App", font=("Helvetica", 18, "bold"))
title_label.pack(pady=10)

city_label = tk.Label(root, text="Enter City:", font=("Helvetica", 18, "bold"))
city_label.pack(pady=5)

city_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
city_entry.pack(pady=5)

search_button = tk.Button(root, text="Get Weather Report", command=show_weather, font=("Helvetica", 12),bg="lightblue")
search_button.pack(pady=10)

result_label = tk.Label(root, text='', font=("Helvetica", 12), justify="left")
result_label.pack(pady=20)

# Code to Run Main Application
root.mainloop()


