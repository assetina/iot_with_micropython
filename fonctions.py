from machine import Pin
from time import sleep_ms, sleep
import dht
from servo import Servo
from machine import SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
def calcultemp(sensor):
    sensor.measure()
    return sensor
    
    
    
def obstacle(capteur, led):
    if capteur.value()!=1:
        led.on()
        return "on"
    else:
        led.off()
        return "off"
    




def obstacle3(capteur):
    
    if capteur.value()==0:
        value= 0
    else :
        value= 1
    return value
    
    
    
def obstacle1(capteur, led,value):
    
    if capteur.value()==0:
        sleep_ms(500)
        if value==0:
            led.on()
            value= 1
        else :
            led.off()
            value= 0
        return value
    
    
def tourne(capteur,servo,lcd,p):
    if capteur.value()==0:
        lcd.move_to(p,1)
        lcd.putstr("O")
        for i in range(0,181):
            servo.write_angle(i)
            sleep_ms(1)
        sleep(1)
        
        for i in range(180,0,-1):
            servo.write_angle(i)
            sleep_ms(1)
        lcd.move_to(p,1)
        lcd.putstr("C")
    
 
    
#    initialisation(15)
#def initialisation(temp,c1,c2,c3,l1,l2,l3):
 #   sensor = dht.DHT11(Pin(temp))
  #  capteur= Pin(nombre_capteur, Pin.IN)