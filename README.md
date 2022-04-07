# Kimberlina
![Kimberlina](http://www.selinoid.com/wp-content/uploads/2021/09/Kimberlina_No_Background-300x300.png)

Kimberlina is a tournament battle bot inspired by Star Wars IG- 227 Hailfire – Class Droid. You can read more information on Kimberlina in the [Mag Pi 116 Issue](https://magpi.raspberrypi.com/issues/116)

## Software
Please keep the [main.py](https://github.com/saornek/Kimberlina/blob/main/main.py) with the main.py name for it to be able to start on boot. 

### Software Explanation
First we will need to import to required libraries.
```sh
from machine import Pin,UART,PWM
from time import sleep
```
---
Secondly, we need to configure the bluetooth port and the pins for the motors and servos.
To configure the bluetooth port:
```sh
#The baud rate might be setup different in your bluetooth module or the other devices code please change accordingly.
uart = UART(0,9600) 
```

To configure the motor ports:
```sh
leftMotorFront = Pin(10, Pin.OUT) #For Left Motor Forward Movement
leftMotorBack = Pin(11, Pin.OUT) #For Left Motor Backward Movement
rightMotorFront = Pin(12, Pin.OUT) #For Right Motor Forward Movement
rightMotorBack = Pin(13, Pin.OUT) #For Right Motor Backward Movement

servoFlip = PWM(Pin(14))
servoPush = PWM(Pin(15))
```
---
Thirdly, we need to adjust the servo settings.
We set up three constants which are in nanoseconds indicating the min position and the max position. These numbers might change according to your servo type and placement.
```sh
MIN = 1000000
MAX = 2000000
```

We then set its initial frequency to 50. 
```sh
servoFlip.freq(50)
servoFlip.duty_ns(MIN)
servoPush.freq(50)
servoPush.duty_ns(MIN)
```
---

Lastly, we await for the commands from the app to start the motors.
```sh
while True:
    if uart.any():
        command = uart.readline()
        if 'a' in command: #Forward Button
            leftMotorFront.high()
            rightMotorFront.high()
```          


## Hardware
### Parts You Need
* Raspberry Pi Pico
* HC-05 Bluetooth Module
* L298N DC Motor Driver
* Step-Down Voltage Regulator
* 3001HB Servo (x2)
* 12v 125RPM DC Motor (x2)
* Ball Caster (x2)
* PLA Filament
* Tough PLA and PLA Filament
* 9mm steel bearing balls

### Connections
![alt text](https://github.com/saornek/Kimberlina/blob/main/KimberlinaCircuit.jpg)
