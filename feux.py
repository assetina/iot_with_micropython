from machine import Pin, PWM
from time import sleep

#def phases(time1,time2):
    #phase1(a,b,ctime1,time2)
    #phase2(a,b,c,time1,time2)
def processus(liste):
    liste1=liste
    #len(liste1)=6
    for j in range(0,len(liste)):
        liste1[j]= Pin(liste[j],Pin.OUT)
        
    phase(liste1[0],liste1[4],liste1[5],liste1[6],liste1[7],10,5,3)
    phase(liste1[3],liste1[1],liste1[2],liste1[6],liste1[7],10,5,3)
        
        
    
    
    
def phase(a,b,c,d,e,time1,time2,time3):
    a.on()
    b.on()
    sleep(time1-time3)
    for i in range(time3):
        b.on()
        d.on()
        sleep(0.5)
        b.off()
        d.off()
        sleep(0.5)
    b.off()
    #c.on()
    #sleep(time2)
    for i in range(time2):
        c.on()
        e.on()
        sleep(0.5)
        c.off()
        e.off()
        sleep(0.5)
    a.off()
    c.off()


def clignoter(d,time):
    for i in range(time):
        d.on()
        sleep(i)
        d.off()
    

#def phase2(a,b,c,time1,time2):
    #feu2[2].on()
    #feu1[1].on()
    #sleep(10)
    #feu1[1].off()
    #feu1[2].on()
    #sleep(5)
    #feu2[2].off()
    #feu1[2].off()
    
