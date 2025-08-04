# 🌦️ Python GUI Weather App

## 📌 Introduction

The **Python GUI Weather App** is a simple and interactive desktop application built using Python's **Tkinter** library. It allows users to fetch and view real-time weather data for any city around the world by entering the city's name. This app leverages the **OpenWeatherMap API** to retrieve accurate and up-to-date weather information.

## 🎯 Features

* 🌍 Search weather by **city name**
* 🌡️ Displays **temperature**, **humidity**, and **pressure**
* 💨 Shows **wind speed** and **weather description**
* 🌅 Provides **sunrise** and **sunset** times
* 🧑‍💻 User-friendly **Graphical User Interface (GUI)**
* 🧩 Built with **Tkinter** (no need for a web browser)

## ⚙️ Workflow

1. User enters the name of a city in the input field.
2. The app sends a request to the **OpenWeatherMap API** using the provided city name.
3. If the city is valid:

   * Weather details are extracted and displayed in a structured format.
   * Information includes temperature, humidity, pressure, wind speed, description, sunrise, and sunset.
4. If the city is not found:

   * The app displays an error message: **"City Not Found!!!"**

## 📚 Libraries Used

| Library    | Purpose                                                              |
| ---------- | -------------------------------------------------------------------- |
| `tkinter`  | To build the GUI (Graphical User Interface)                          |
| `requests` | To make HTTP requests to the OpenWeatherMap API                      |
| `datetime` | To convert Unix timestamps (for sunrise and sunset) to readable time |

## 🚀 How to Run

1. Clone the repository to your local machine.
2. Make sure you have Python installed (preferably version 3.8+).
3. Run the Python script to launch the app interface.
4. Enter any city name and click **"Get Weather Report"** to view the weather.

## 📌 Notes

* Make sure you have an **active internet connection** to fetch live data.
* You will need an API key from [OpenWeatherMap](https://openweathermap.org/api). Replace the default API key with your own if required.
