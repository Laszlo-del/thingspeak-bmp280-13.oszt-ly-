import requests
import time
import random

# ThingSpeak API kulcs
API_KEY = 'HX1HIJ1Y9Q6CMGTV'

# Adatok küldése a ThingSpeak-re
def send_data_to_thingspeak(temp, humidity):
    url = f'https://api.thingspeak.com/update?api_key={API_KEY}&field1={temp}&field2={humidity}'
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Sikeres adatküldés: Hőmérséklet={temp}, Páratartalom={humidity}")
    else:
        print(f"Sikertelen adatküldés: {response.status_code}")

# Végtelen ciklus 10 másodperces időközönként
while True:
    # Véletlenszerű hőmérséklet és páratartalom generálása
    temperature = round(random.uniform(20.0, 30.0), 2)  # Példa: 20-30°C között
    humidity = round(random.uniform(30.0, 70.0), 2)     # Példa: 30-70% között
    
    # Adatok küldése
    send_data_to_thingspeak(temperature, humidity)
    
    # 10 másodperces várakozás
    time.sleep(10)
