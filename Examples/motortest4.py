from time import sleep

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
# 
# EN = 16   # EN GPIO Pin
# STEP = 20  # Step GPIO Pin
# DIR = 21   # Direction GPIO Pin
# 
EN = 13   # EN GPIO Pin
STEP = 19  # Step GPIO Pin
DIR = 26   # Direction GPIO Pin

CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 3200   # Steps per Revolution (360 / 7.5)
SPD = 9  #8.88   #step per digre
SPC = 3000    #step per cell

GPIO.setmode(GPIO.BCM)
GPIO.setup(EN, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

step_count = SPC*4
#delay = .0208
delay = .002
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)
#     if delay > 0.005:
#         delay = delay - 0.0002
    print(x)
sleep(.5)

GPIO.output(DIR, CCW)
for x in range(step_count,0):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)
    print(x)

GPIO.cleanup()