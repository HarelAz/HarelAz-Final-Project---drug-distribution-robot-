
from main_code.con import *
from main_code.moduless import *
from main_code.motor_status import *



def Home_Servo_1():
    Servo_1_SetAngle(0)


def Home_A():
   # delay = 0.0005
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

    current_position[1] = 0
    return current_position[1]

def Home_Z():
    #delay = 0.00015
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
    current_position[0] = 0
    return current_position[0]


def homing():
    #Home_Servo_1()
    enable_motors()
    current_position[1] = Home_A()
    current_position[0] = Home_Z()
    return current_position


if __name__ == "__main__":
    homing()
    #Home_Servo_1()
    #Home_A()
    #Home_Z()
