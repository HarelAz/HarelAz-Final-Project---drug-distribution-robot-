######################### Importing modules #########################
from main_code.confi import * #as #conf
from main_code.moduless import *


######################### Servo_1_SetAngle function #########################
# This function move the servo to desired angle that move the linear actuator
def Servo_1_SetAngle(angle):
    duty = (180 - angle) / 18 + 2
    GPIO.output(Servo_1_Pin, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(Servo_1_Pin, False)
    pwm.ChangeDutyCycle(0)
