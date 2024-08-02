import machine
from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep
from machine import Pin
from time import sleep
import dht
from fonctions import *


I2C_ADDR = 0x27
totalRows = 4
totalColumns = 20

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)     #initializing the I2C method for ESP32
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)       #initializing the I2C method for ESP8266
sensor = dht.DHT11(Pin(15))
c1= Pin(23, Pin.IN)
c2= Pin(5, Pin.IN)
c3= Pin(19, Pin.IN)
led1= Pin(4, Pin.OUT)
led2= Pin(2, Pin.OUT)
led3= Pin(18, Pin.OUT)

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)
with open("fichier.csv", "w") as gf:
    gf.write("temperature:\tHumidite:\tLed1:\tLed2:\tLed3:\t"+"\n")
    while True:
        lcd.clear()
        lcd.putstr("SMART TECHNOLOGY")
        lcd.move_to(0,1)
        lcd.putstr("T:{}".format(calcultemp(sensor).temperature()))
        gf.write(str(calcultemp(sensor).temperature())+"\t")
        lcd.move_to(8,1)
        lcd.putstr("H:{}".format(calcultemp(sensor).humidity()))
        gf.write(str(calcultemp(sensor).humidity())+"\t")
        lcd.move_to(0,2)
        lcd.putstr("led1")
        lcd.move_to(6,2)
        lcd.putstr("led2")
        lcd.move_to(12,2)
        lcd.putstr("led3")
        lcd.move_to(0,3)
        lcd.putstr(obstacle(c1,led1))
        gf.write(str(obstacle(c1,led1))+"\t")
        lcd.move_to(6,3)
        lcd.putstr(obstacle(c2,led2))
        gf.write(str(obstacle(c2,led2))+"\t")
        lcd.move_to(12,3)
        lcd.putstr(obstacle(c3,led3))
        gf.write(str(obstacle(c3,led3))+"\n")
        
    
    
    #lcd.putstr("Lets Count 0-10!")
    #sleep(2)
    #lcd.clear()
    #for i in range(11):
        #lcd.putstr(str(i))
        #sleep(1)
        #lcd.clear()