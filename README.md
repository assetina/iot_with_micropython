# Projet : IoT avec MicroPython
Bienvenue dans le dépôt "IoT avec MicroPython" ! Ce projet propose des tutoriels étape par étape pour divers composants et capteurs IoT en utilisant MicroPython sur une carte ESP32. Vous y trouverez des exemples de codes pour contrôler des LEDs, des servos, des rubans LED, des buzzers, des capteurs de température, des capteurs d'obstacle, des modules GPS, la création de serveurs web, et la connexion à Firebase.

# Table des Matières
  *** Introduction
  Matériel Requis
  Configuration de l'Environnement
  Tutoriels
  Contrôler des LEDs
  Contrôler des Servos
  Utiliser des Rubans LED
  Utiliser des Buzzers
  Capteurs de Température
  Capteurs d'Obstacle
  Ecran LCD
  Modules GPS
  Création d'un Serveur Web
  Connexion à Firebase
  Contribuer
  Licence
  Contact ****
# Introduction
Ce dépôt a pour but de fournir des exemples de codes et des explications détaillées pour réaliser des projets IoT avec MicroPython et une carte ESP32. Chaque composant est abordé séparément avec un tutoriel dédié, pour vous permettre d'apprendre à les utiliser et les intégrer dans vos propres projets.

# Matériel Requis
ESP32
LED
Servo moteur
Ruban LED (Neopixel ou WS2812)
Buzzer
Capteur de température (DHT11, DHT22 ou similaire)
Capteur d'obstacle (HC-SR04 ou similaire)
Module GPS (NEO-6M ou similaire)
Câbles et connecteurs
Alimentation (batterie ou adaptateur secteur)
# Configuration de l'Environnement
Installer MicroPython sur l'ESP32 :

Télécharger l'image MicroPython depuis MicroPython.org.
Flasher l'image sur l'ESP32 en utilisant esptool.py ou un autre outil.
Configurer l'IDE :

Utiliser Thonny IDE, uPyCraft, ou tout autre IDE compatible avec MicroPython.
Tutoriels
Contrôler des LEDs
Code :

python
Copier le code
from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

while True:
    led.value(1)
    sleep(1)
    led.value(0)
    sleep(1)
Contrôler des Servos
Code :

python
Copier le code
from machine import Pin, PWM
import time

servo = PWM(Pin(15), freq=50)

def set_angle(angle):
    duty = int((angle / 180) * 1023)
    servo.duty(duty)

while True:
    set_angle(0)
    time.sleep(1)
    set_angle(90)
    time.sleep(1)
    set_angle(180)
    time.sleep(1)
Utiliser des Rubans LED
Code :

python
Copier le code
import machine, neopixel

np = neopixel.NeoPixel(machine.Pin(4), 8)

def clear():
    for i in range(8):
        np[i] = (0, 0, 0)
    np.write()

def set_color(color):
    for i in range(8):
        np[i] = color
    np.write()

clear()
set_color((255, 0, 0))  # Rouge
Utiliser des Buzzers
Code :

python
Copier le code
from machine import Pin
from time import sleep

buzzer = Pin(14, Pin.OUT)

while True:
    buzzer.value(1)
    sleep(0.5)
    buzzer.value(0)
    sleep(0.5)
Capteurs de Température
Code :

python
Copier le code
import dht
from machine import Pin
import time

sensor = dht.DHT11(Pin(4))

while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print('Temperature: %3.1f C' %temp)
    print('Humidity: %3.1f %%' %hum)
    time.sleep(2)
Capteurs d'Obstacle
Code :

python
Copier le code
from machine import Pin, time_pulse_us
import time

trigger = Pin(5, Pin.OUT)
echo = Pin(18, Pin.IN)

def get_distance():
    trigger.value(0)
    time.sleep_us(2)
    trigger.value(1)
    time.sleep_us(10)
    trigger.value(0)
    duration = time_pulse_us(echo, 1)
    distance = (duration / 2) / 29.1
    return distance

while True:
    dist = get_distance()
    print('Distance:', dist, 'cm')
    time.sleep(1)
Modules GPS
Code :

python
Copier le code
from machine import UART
import utime

uart = UART(2, baudrate=9600, tx=17, rx=16)

def read_gps():
    while uart.any() > 0:
        print(uart.readline())

while True:
    read_gps()
    utime.sleep(1)
Création d'un Serveur Web
Code :

python
Copier le code
import network
import socket

ssid = 'votre_ssid'
password = 'votre_password'

ap = network.WLAN(network.AP_IF)
ap.config(essid=ssid, password=password)
ap.active(True)

while not ap.active():
    pass

print('Connection successful')
print(ap.ifconfig())

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(5)

print('Listening on', addr)

def web_page():
    html = """
    <!DOCTYPE html>
    <html>
    <head> <title>ESP Web Server</title> </head>
    <body> <h1>Hello, World!</h1> </body>
    </html>
    """
    return html

while True:
    cl, addr = s.accept()
    print('Client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break
    response = web_page()
    cl.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n')
    cl.send(response)
    cl.close()
Connexion à Firebase
Code :

python
Copier le code
import urequests

url = 'https://your-firebase-database.firebaseio.com/data.json'

def send_data(data):
    response = urequests.post(url, json=data)
    print(response.text)
    response.close()

data = {
    "temperature": 24,
    "humidity": 60
}

send_data(data)
# Contribuer
Les contributions sont les bienvenues ! Merci de suivre les étapes ci-dessous pour contribuer :

Forker le dépôt
Créer une branche de fonctionnalité (git checkout -b fonctionnalite/ma-nouvelle-fonctionnalite)
Commiter les modifications (git commit -am 'Ajoute une nouvelle fonctionnalité')
Pousser vers la branche (git push origin fonctionnalite/ma-nouvelle-fonctionnalite)
Créer une Pull Request
# Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus d'informations.

# Contact
Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue sur le dépôt GitHub.
