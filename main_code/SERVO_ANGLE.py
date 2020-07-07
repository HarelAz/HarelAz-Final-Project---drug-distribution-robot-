from main_code.confi import * #as #conf
from main_code.moduless import *


def Servo_1_SetAngle(angle):

    duty =(180 - angle) / 18 + 2
    GPIO.output(Servo_1_Pin, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(Servo_1_Pin, False)
    pwm.ChangeDutyCycle(0)
