"""
Movement Commands:
a - Forward
b - Backward
c - Stop
d - Right 
e - Left 

Extra Commands:
f - Flip Down
g - Push
h - Emergency Button & Reset Button
j - Flip Up
k - Auto Turn
"""


#Libraries
from machine import Pin,UART,PWM
from time import sleep

#Bluetooth Setup
uart = UART(0,9600)

#Motor Setup
leftMotorFront = Pin(10, Pin.OUT) 
leftMotorBack = Pin(11, Pin.OUT)

rightMotorFront = Pin(12, Pin.OUT)
rightMotorBack = Pin(13, Pin.OUT)

#Servo Positions & Setup
MIN = 1000000
MAX = 2000000

servoFlip = PWM(Pin(14))
servoPush = PWM(Pin(15))

servoFlip.freq(50)
servoFlip.duty_ns(MIN)
servoPush.freq(50)
servoPush.duty_ns(MIN)


#Code
print("Waiting For Any Commands")
while True:
    if uart.any():
        command = uart.readline()
        print(command)
        if 'a' in command: #Forward Button
            leftMotorFront.high()
            rightMotorFront.high()
        elif 'b' in command: #Backward Button
            leftMotorBack.high()
            rightMotorBack.high()
        elif 'c' in command: #Stop Button
            leftMotorFront.low()
            rightMotorFront.low()
            leftMotorBack.low()
            rightMotorBack.low()
        elif 'd' in command: #Right Button
            leftMotorFront.low()
            rightMotorFront.low()
            leftMotorBack.low()
            rightMotorBack.low()
            sleep(0.2)
            leftMotorFront.high()
            rightMotorBack.high()
            sleep(1.5)
            leftMotorFront.low()
            rightMotorBack.low()
        elif 'e' in command: #Left
            rightMotorFront.low()
            leftMotorBack.low()
            rightMotorBack.low()
            sleep(0.2)
            leftMotorBack.high()
            rightMotorFront.high()
            sleep(1.5)
            leftMotorBack.low()
            rightMotorFront.low()
        elif 'f' in command: #Flip Down
            servoFlip.duty_ns(MIN)
        elif 'g' in command: #Push
            servoPush.duty_ns(MAX)
            sleep(1)
            servoPush.duty_ns(MIN)
        elif 'h' in command: #Emergency Stop & Reset
            rightMotorFront.low()
            leftMotorBack.low()
            rightMotorBack.low()
            leftMotorFront.low()
            servoFlip.duty_ns(MIN)
            servoPush.duty_ns(MIN)
        elif 'j' in command: #Flip Up
            servoFlip.duty_ns(MAX)
        elif 'k' in command:
            leftMotorBack.high()
            rightMotorFront.high()
