from main_code.confi import *
from main_code.moduless import *

from time import sleep
import RPi.GPIO as GPIO
from time import sleep

import RPi.GPIO as GPIO

GPIO.setwarnings(False)

CW = 0  # Clockwise Rotation
CCW = 1  # Counterclockwise Rotation
SPR = 3200  # Steps per Revolution (360 / 7.5)
SPD = 9  # 8.88   #step per digre
SPC = 300  # step per cell

GPIO.setmode(GPIO.BCM)
GPIO.setup(EN, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(endstop1Pin, GPIO.IN)  # set a port/pin as an input
GPIO.output(DIR, CW)

correntposition = 0


# step_count = SPC*4
# delay = .0208

def calibrateA():
    Home()
    delay = 0.0002
    No_Of_Cells = 20
    step_count = 0
    GPIO.output(DIR, CCW)

    while True:
        i = GPIO.input(endstop1Pin)  # read status of pin/port and assign to variable i
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
        step_count = step_count + 1
        if (i == 1):
            break
    steppercell = step_count / No_Of_Cells
    print("The step count is:", step_count)
    print("The step per cell is:", steppercell)
    return (steppercell)


sleep(.5)
GPIO.cleanup()

from time import sleep
import RPi.GPIO as GPIO
from time import sleep

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
#

#
# EN = 13   # EN GPIO Pin
# STEP = 19  # Step GPIO Pin
# DIR = 26   # Direction GPIO Pin
# endstop1Pin = 6   # endstop1 GPIO Pin

CW = 1  # Clockwise Rotation
CCW = 0  # Counterclockwise Rotation
SPR = 3200  # Steps per Revolution (360 / 7.5)
SPD = 9  # 8.88   #step per digre
SPC = 300  # step per cell

GPIO.setmode(GPIO.BCM)
GPIO.setup(EN, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(endstop1Pin, GPIO.IN)  # set a port/pin as an input
GPIO.output(DIR, CW)

correntposition = 0



def calibrateZ():
    Home()

    step_count = 0
    GPIO.output(DIR_Z, not MOTOR_Z_DIR_CW)

    while True:
        i = GPIO.input(endstop_Z_Pin)  # read status of pin/port and assign to variable i
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay_home_Z)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay_home_Z)
        step_count = step_count + 1
        if (i == 1):
            break
    Motor_Z_steppercell = step_count / No_Of_Cells_Z
    print("The step count is:", step_count)
    print("The step per cell is:", Motor_Z_steppercell)
    return (Motor_Z_steppercell)


# Home()
# correntposition = 0
# Home()
calibrate()

#
# while True:
#     destinastioncell = int(input("What is the cell number of destinastion?"))
#     if(destinastioncell == -1):
#         break
#     correntposition = GotoLine(destinastioncell, correntposition)
#     print(correntposition)
#

sleep(.5)
GPIO.cleanup()

