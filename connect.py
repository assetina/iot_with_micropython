from machine import Pin
import network
from time import sleep


def open():
    lampe= Pin(2, Pin.OUT)
    i=2
    while i>0:
        lampe.on()
        sleep(0.1)
        lampe.off()
        sleep(0.1)
        i-=0.2
        
def connection(username,password):
    sta_if = network.WLAN(network.STA_IF)

    if not sta_if.isconnected():
        print('en cours de connexion...')
        open()
        sta_if.active(True)
        #sta_if.connect('atmyhome', 'home4internet')
        sta_if.connect(username, password)
        while not sta_if.isconnected():
            sta_if.disconnect()
            #pass

    print('connecté:', sta_if.ifconfig())