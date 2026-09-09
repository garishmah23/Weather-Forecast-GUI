import tkinter as tk
from tkinter import messagebox
import requests

#key
API_key="95e4f0d35040c780130fb219dc9a4639"

#Weather function
def get_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showerror("ERROR","Please Entry the City Name")
        return

    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("ERROR","City Not Found")
            return

        #Data Extraction
        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        #result
        result = (
            f"City: {city_name},{country}\n"
            f"Temperature: {temperature}°C\n"
            f"Humidity: {humidity}%\n"
            f"Weather: {weather}\n"
            f"Wind Speed: {wind_speed}m/s"
        )

        result_label.config(text = result)
        with open("weather_report.txt","w") as file:
            file.write(result)

    except requests.exceptions.ConnectionError:
        messagebox.showerror("Connection Error","No Internet Connection")

    except Exception as e:
        messagebox.showerror("ERROR",str(e))

#GUI 
root = tk.Tk()
root.title("WEATHER APP")
root.geometry("400x350")
root.config(bg="white")

#title
title_label = tk.Label(
    root,
    text = "WEATHER APP",
    font = ("Arial",20,"bold"),
    bg = "white",
    fg = "black"
)
title_label.pack(pady = 15)

#enter city'
city_label= tk.Label(
    root,
    text = "Enter City:",
    font = ("Arial",12,"bold"),
    bg = "white",
    fg = "black"
)
city_label.pack(pady = 5)

#city input
city_entry = tk.Entry(
    root,
    font = ("Arial",14),
    width = 25
)
city_entry.pack(pady = 10)

#button
get_weather_button = tk.Button(
    root,
    text = "Get Weather",
    font = ("Arial",12,"bold"),
    bg="white",
    fg = "black",
    command = get_weather
)
get_weather_button.pack(pady = 10)

#result '
result_label = tk.Label(
    root,
    text = "",
    font = ("Arial",12,"bold"),
    bg = "white",
    fg = "black",
    justify = "left"
)

result_label.pack(pady = 20)

root.mainloop()