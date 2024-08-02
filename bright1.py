from machine import Pin
from time import sleep

L1= Pin(15, Pin.OUT)
L2= Pin(2, Pin.OUT)
L3= Pin(5, Pin.OUT)
L4= Pin(18, Pin.OUT)
L5= Pin(19, Pin.OUT)
L6= Pin(21, Pin.OUT)
L7= Pin(22, Pin.OUT)

liste=[L1,L2,L3,L4,L5,L6,L7]

for i in range(0,len(liste)-1):
    if i%2 != 0:
        liste[i].on()
        sleep(2)
        liste[i].off()
        sleep(2)
#from machine import Pin

#import connect

#connect.connection('atmyhome','home4internet')

from machine import Pin
lampe= Pin(5, Pin.OUT)
lampe.off()