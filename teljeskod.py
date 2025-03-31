import requests
import time
from smbus2 import SMBus
from bmp280 import BMP280

# ThingSpeak API kulcs
API_KEY = 'HX1HIJ1Y9Q6CMGTV'

# BMP280 inicializálása
bus = SMBus(1)  # I2C busz (1-es a legtöbb Raspberry Pi modellen)
bmp280 = BMP280(i2c_dev=bus)

# Adatok küldése a ThingSpeak-re
def send_data_to_thingspeak(temp, pressure):
    url = f'https://api.thingspeak.com/update?api_key={API_KEY}&field1={temp}&field2={pressure}'
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Sikeres adatküldés: Hőmérséklet={temp}°C, Nyomás={pressure} hPa")
    else:
        print(f"Sikertelen adatküldés: {response.status_code}")

# Végtelen ciklus 10 másodperces időközönként
while True:
    try:
        temperature = round(bmp280.get_temperature(), 2)  # Hőmérséklet beolvasása
        pressure = round(bmp280.get_pressure(), 2)  # Légnyomás beolvasása

        # Adatok küldése a ThingSpeak-re
        send_data_to_thingspeak(temperature, pressure)

    except Exception as e:
        print(f"Hiba történt: {e}")

    # 10 másodperces várakozás
    time.sleep(10)
