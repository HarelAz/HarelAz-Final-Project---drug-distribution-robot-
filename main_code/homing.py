
from main_code.con import * #as #conf
from main_code.moduless import *
global current_position_A
global current_position_Z
current_position_A = 0
current_position_Z = 0


def Home_Servo_1():
    Servo_1_SetAngle(0)


def Home_A():
    delay = 0.0005
    while True:
        GPIO.output(DIR_A, MOTOR_A_DIR_CW)
        inA = GPIO.input(endstop_A_Pin)  # read status of pin/port and assign to variable i
        if (inA == 1):
            break
        GPIO.output(STEP_A, GPIO.HIGH)
        sleep(delay_home_A)
        GPIO.output(STEP_A, GPIO.LOW)
        sleep(delay_home_A)
    while (inA == 1):
        GPIO.output(DIR_A, not MOTOR_A_DIR_CW)
        inA = GPIO.input(endstop_A_Pin)
        GPIO.output(STEP_A, GPIO.HIGH)
        sleep(delay_home_A)
        GPIO.output(STEP_A, GPIO.LOW)
        sleep(delay_home_A)
    correntposition_A = 0
    return (correntposition_A)


def Home_Z():
    delay = 0.00015
    while True:
        inZ = GPIO.input(endstop_Z_Pin)  # read status of pin/port and assign to variable i
        if (inZ == 1):
            break
        GPIO.output(DIR_Z, MOTOR_Z_DIR_CW)
        GPIO.output(STEP_Z, GPIO.HIGH)
        sleep(delay_home_Z)
        GPIO.output(STEP_Z, GPIO.LOW)
        sleep(delay_home_Z)
    while (inZ == 1):
        GPIO.output(DIR_Z, not MOTOR_Z_DIR_CW)
        inZ = GPIO.input(endstop_Z_Pin)
        GPIO.output(STEP_Z, GPIO.HIGH)
        sleep(delay_home_Z)
        GPIO.output(STEP_Z, GPIO.LOW)
        sleep(delay_home_Z)
    correntposition_Z = 0
    return (correntposition_Z)


def homing():
    #Home_Servo_1()
   # global current_position_A
    #global current_position_Z
    new_current_position_A = Home_A()
    new_current_position_Z = Home_Z()
    return (new_current_position_Z, new_current_position_A)


if __name__ == "__main__":
    homing()
    #Home_Servo_1()
    #Home_A()
    #Home_Z()
