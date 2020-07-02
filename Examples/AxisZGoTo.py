from time import sleep
import RPi.GPIO as GPIO
from time import sleep

import RPi.GPIO as GPIO

GPIO.setwarnings(False)

#
EN = 16   # EN GPIO Pin
STEP = 20  # Step GPIO Pin
DIR = 21   # Direction GPIO Pin
endstop1Pin = 5   # endstop1 GPIO Pin
# EN = 13   # EN GPIO Pin
# STEP = 19  # Step GPIO Pin
# DIR = 26   # Direction GPIO Pin
# endstop1Pin = 6   # endstop1 GPIO Pin

CW = 0     # Clockwise Rotation
CCW = 1    # Counterclockwise Rotation


GPIO.setmode(GPIO.BCM)
GPIO.setup(EN, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(endstop1Pin, GPIO.IN)  # set a port/pin as an input
GPIO.output(DIR, CW)

correntposition = 0   

#step_count = SPC*4
#delay = .0208
def Home():
    i = GPIO.input(endstop1Pin)       # read status of pin/port and assign to variable i
    delay = 0.00015
    while True:
        i = GPIO.input(endstop1Pin)       # read status of pin/port and assign to variable i
        if (i == 1):
            break
        GPIO.output(DIR, CW)
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    while (i==1):
        GPIO.output(DIR, CCW)
        i = GPIO.input(endstop1Pin)
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    correntposition = 0
    return(correntposition)
    

def GotoLine(destinastion, correntposition):
    steppercell = 6000
    #correntposition = 0
    step_count = destinastion*steppercell - correntposition 
    delay = 0.00015
    if (step_count>0):
        GPIO.output(DIR, CCW)
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
            correntposition = correntposition + 1
            if (GPIO.input(endstop1Pin)):
                break
    else:
        GPIO.output(DIR, CW)
        step_count = step_count

        for x in range(step_count,-1):
            GPIO.output(STEP, GPIO.HIGH)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
            correntposition = correntposition - 1
        
    print(correntposition)
    return(correntposition)


correntposition = Home()   

while True:
    destinastioncell = int(input("What is the cell number of destinastion?"))
    if(destinastioncell == -1):
        break
    correntposition = GotoLine(destinastioncell, correntposition)
    print(correntposition)
    
    
sleep(.5)
GPIO.cleanup()
