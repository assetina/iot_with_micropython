from time import sleep
from machine import Pin,PWM

LR= Pin(19)
LV= Pin(15)
LB= Pin(5)
Liste1= [LR, LV, LB]
Liste2= ["rouge", "vert", "bleu", "blanc","bleu clair","jaune","violet","noir", "rouge-orange","gold","marron","gris","vert foncé","corail"]
Liste3= [[255,0,0], [0,255,0], [0,0,255], [255,255,255],[0,255,255],[255,255,0],[255,0,255],[0,0,0],[255,69,0],[255,215,0],[165,42,42],[126,126,126],[0,100,0],[255,127,80]]

frequence=5000
def see(colour):
    for i in range(0,len(Liste2)):
        if colour== Liste2[i]:
            for j in range(0,len(Liste3[i])):
                if Liste3[i][j]!=0:
                    pwm0= PWM(Liste1[j],frequence)
                    pwm0.duty(conversion(255,1023,Liste3[i][j]))
                    
                else:
                    pwm0= PWM(Liste1[j],frequence)
                    pwm0.duty(0)
            
            
def conversion(valeur1,valeur2,value):
    return(int(value*valeur2/valeur1)) 
    
