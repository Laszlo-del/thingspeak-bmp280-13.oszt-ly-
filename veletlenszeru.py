import requests
import time
import random
from gpiozero import PWMLED

blue_led = PWMLED(20)  # Kék LED a GPIO 20 pinhez

# ThingSpeak API kulcs
API_KEY = 'HX1HIJ1Y9Q6CMGTV'

# Adatok küldése a ThingSpeak-re
def send_data_to_thingspeak(temp, pressure):
    url = f'http://localhost/sensor/insert_data.php?temperature={temp}&pressure={pressure}'
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Sikeres adatküldés: Hőmérséklet={temp}, Légnyomás={pressure}")
    else:
        print(f"Sikertelen adatküldés: {response.status_code}")

# Végtelen ciklus 10 másodperces időközönként
while True:
    
    # Véletlenszerű hőmérséklet és nyomás generálása
    temperature = round(random.uniform(15.0, 35.0), 2)  # Példa: 15-35°C között
    pressure = round(random.uniform(980.0, 1030.0), 2)  # Példa: 980-1030 hPa között

    print(f"{temperature:05.2f}*C {pressure:05.2f}hPa")

    # LED kapcsolása a hőmérséklet alapján
    if temperature > 20:
        blue_led.value = 1  # Kék LED bekapcsolása
    else:
        blue_led.value = 0  # Kék LED kikapcsolása
    
    # Adatok küldése
    send_data_to_thingspeak(temperature, pressure)
    
    # 10 másodperces várakozás
    time.sleep(10)
