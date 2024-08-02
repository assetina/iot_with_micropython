from machine import Pin, PWM
from time import sleep


frequency= 5000
Led= Pin(19)
pwm0= PWM(Led,frequency)
while True:
    for dc in range(0,1024):
        pwm0.duty(dc)
        sleep(0.005)
    for dc in range(1023,0,-1):
        pwm0.duty(dc)
        sleep(0.005)
