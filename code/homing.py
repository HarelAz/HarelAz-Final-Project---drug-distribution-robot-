
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
from time import sleep


def Home_Servo_1():
    Servo_1_SetAngle(0)


def Home_A():
    delay = 0.0005
    while True:
        GPIO.output(DIR, MOTOR_A_DIR_CW)
        i = GPIO.input(endstop_A_Pin)       # read status of pin/port and assign to variable i
        if (i == 1):
            break
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    while (i == 1):
        GPIO.output(DIR, not MOTOR_A_DIR_CW)
        i = GPIO.input(endstop_Z_Pin)
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    correntposition_A = 0
    return(correntposition_A)

def Home_Z():
    delay = 0.00015
    while True:
        i = GPIO.input(endstop_Z_Pin)       # read status of pin/port and assign to variable i
        if (i == 1):
            break
        GPIO.output(DIR, MOTOR_Z_DIR_CW)
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    while (i==1):
        GPIO.output(DIR, not MOTOR_Z_DIR_CW)
        i = GPIO.input(endstop_Z_Pin)
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    correntposition_Z = 0
    return(correntposition_Z)

def homing():
    Home_Servo_1()
    correntposition_A = Home_A
    correntposition_Z = Home_Z
    return(correntposition_A, correntposition_Z)

if __name__ == "__main__":
    Home_Servo_1()
    Home_A()
    Home_Z()
