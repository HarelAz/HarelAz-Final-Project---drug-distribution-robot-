from main_code.confi import *
from main_code.moduless import *

def calibrate_A():
    Home_A()

    step_count = 0
    GPIO.output(DIR_A, not MOTOR_A_DIR_CW)
    while True:
        i = GPIO.input(endstop_A_Pin)  # read status of pin/port and assign to variable i
        GPIO.output(STEP_A, GPIO.HIGH)
        sleep(delay_home_A)
        GPIO.output(STEP_A, GPIO.LOW)
        sleep(delay_home_A)
        step_count = step_count + 1
        if (i == 1):
            break
    Motor_A_steppercell = step_count / No_Of_Cells_A
    print("The step count is:", step_count)
    print("The step per cell is:", Motor_A_steppercell)
    Home_A()
    return (Motor_A_steppercell)


def calibrate_Z():
    Home_A()
    Home_Z()

    step_count = 0
    GPIO.output(DIR_Z, not MOTOR_Z_DIR_CW)
    while True:
        i = GPIO.input(endstop_Z_Pin)  # read status of pin/port and assign to variable i
        GPIO.output(STEP_Z, GPIO.HIGH)
        sleep(delay_home_Z)
        GPIO.output(STEP_Z, GPIO.LOW)
        sleep(delay_home_Z)
        step_count = step_count + 1
        if (i == 1):
            break
    Motor_Z_steppercell = step_count / No_Of_Cells_Z
    print("The step count is:", step_count)
    print("The step per cell is:", Motor_Z_steppercell)
    Home_Z()
    return (Motor_Z_steppercell)