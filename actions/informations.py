import time
import datetime
from voice.speaker import speak
from voice.listener import listen
import os
import dotenv
import requests
import json

dotenv.load_dotenv()
def timenow():
    now = datetime.datetime.now()
    speak(f"Current Date and Time: {now}")

def weathernow():
    speak("whats your city name ")
    time.sleep(1)
    city = listen()
    print(city)
    api = os.getenv('WEATHER_API_KEY')
    url = f"http://api.weatherapi.com/v1/current.json?key={api}&q={city}&aqi=no"
    response = requests.get(url)
    weather_dec = json.loads(response.text)
    day = "afternoon" if weather_dec["current"]["is_day"] == 1 else "night"
    speak(f'{day}')
    speak(f"Temperature in {city} is {weather_dec['current']['temp_c']} degree celsius.")