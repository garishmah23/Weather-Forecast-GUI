# 🌦️ Weather App using Tkinter

A simple and user-friendly **desktop Weather Application** built using **Python and Tkinter**. The application allows users to enter any city name and fetches real-time weather information using the **OpenWeatherMap API**.

---

## 📌 Features

* 🔍 Search weather by city name
* 🖥️ Simple and user-friendly Tkinter GUI
* 🌡️ Displays temperature
* ☁️ Displays weather condition
* 💧 Displays humidity
* 💨 Displays wind speed
* 🔄 Provides real-time weather updates
* 🌐 Uses OpenWeatherMap API for live weather data

---

## 🛠️ Technologies Used

* **Python**
* **Tkinter** – Graphical User Interface
* **Requests** – API requests
* **OpenWeatherMap API** – Real-time weather data

---

## 📂 Project Structure

```text
weather-app/
│
├── main.py
├── README.md
└── weather_report.txt
```

---

## ▶️ How to Run

### 1️⃣ Install Python

Download and install Python from:

https://www.python.org/

Make sure Python is added to your system PATH during installation.

---

### 2️⃣ Install Required Module

Open the terminal in your project folder and run:

```bash
pip install requests
```

> **Note:** Tkinter is usually included with standard Python installations.

---

### 3️⃣ Get an OpenWeatherMap API Key

Visit:

https://openweathermap.org/api

Then:

1. Create a free account.
2. Generate your API key.
3. Copy the API key.
4. Open `main.py`.
5. Replace `YOUR_API_KEY` with your API key.

Example:

```python
api_key = "YOUR_API_KEY"
```

⚠️ **Important:** Do not upload your real API key to a public GitHub repository. Keep it private or store it in an environment variable.

---

### 4️⃣ Run the Project

Open the terminal and run:

```bash
python main.py
```

The Weather App window will open.

---

## 🖥️ Sample Output

```text
City: Delhi

Temperature: 32°C
Condition: Clear Sky
Humidity: 45%
Wind Speed: 3.5 m/s
```

---

## 📸 Screenshots

### Main GUI

<img width="1215" height="567" alt="weather" src="https://github.com/user-attachments/assets/7fb62d74-8032-429d-a7eb-3ea1bfd6638b" />



### Weather Result

<img width="316" height="237" alt="weather2" src="https://github.com/user-attachments/assets/0a9bdb51-f954-4eb3-8620-fab71ca8b8ed" />


---

## 💡 Future Improvements

* 🌤️ Add weather icons
* 🌙 Add dark mode
* 📅 Add a 7-day weather forecast
* 🎨 Improve the overall UI design
* 📍 Add automatic location detection
* 🌡️ Add Celsius/Fahrenheit conversion
* ⚠️ Improve error handling for invalid city names

---

## 👨‍💻 Author

**Garishma**

---

⭐ If you like this project, consider giving the repository a star!
