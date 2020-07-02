from time import sleep

import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
ServoPin = 24
GPIO.setup(ServoPin, GPIO.OUT)
pwm=GPIO.PWM(ServoPin, 50)
pwm.start(0)

def SetAngle(angle):
    duty =(180 - angle) / 18 + 2
    GPIO.output(ServoPin, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(ServoPin, False)
    pwm.ChangeDutyCycle(0)
delay = 0
SetAngle(0) 
sleep(delay)
SetAngle(180)
sleep(delay)
SetAngle(0) 
sleep(delay)
