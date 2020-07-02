from RPi import GPIO
from main_code.con import *
from main_code.moduless import *


def disable_motors():
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(13, GPIO.HIGH)


def enable_motors():
    GPIO.output(16, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)


if __name__ == "__main__":
    disable_motors()
    #enable_motors()
