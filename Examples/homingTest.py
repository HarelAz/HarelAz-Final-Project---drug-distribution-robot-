#Homing test (tcst2103)
from time import sleep

import RPi.GPIO as GPIO  # import RPi.GPIO module

GPIO.setwarnings(False)

EN = 13   # EN GPIO Pin
STEP = 19  # Step GPIO Pin
DIR = 26   # Direction GPIO Pin
endstop1Pin = 6   # endstop1 GPIO Pin

delay = 1
count = 100

#motor
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 3200   # Steps per Revolution (360 / 7.5)
SPD = 9  #8.88   #step per digre
SPC = 3000 

GPIO.setmode(GPIO.BCM)            # choose BCM or BOARD  
GPIO.setup(endstop1Pin, GPIO.IN)  # set a port/pin as an input  

GPIO.setup(EN, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CCW)
#GPIO.setup(port_or_pin, GPIO.OUT) # set a port/pin as an output   
#GPIO.output(port_or_pin, 1)       # set an output port/pin value to 1/HIGH/True  
#GPIO.output(port_or_pin, 0)       # set an output port/pin value to 0/LOW/False  
#for x in range(count):
#sleep(2)  
    #print(i)
#    sleep(delay)
i = GPIO.input(endstop1Pin)       # read status of pin/port and assign to variable i
step_count = SPC*4
#delay = .0208
delay = 0.0001
#for x in range(step_count):
while (i == 0):
    i = GPIO.input(endstop1Pin)       # read status of pin/port and assign to variable i
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)
    X_ABSULUT=0
sleep(.5)
GPIO.cleanup()