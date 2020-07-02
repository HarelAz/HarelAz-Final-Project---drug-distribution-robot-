from main_code.con import *
from main_code.moduless import *

def Goto_Z(destinastion_Z, current_position_Z):

    step_count_Z = destinastion_Z *Motor_Z_steppercell - current_position_Z
   # delay_Go_To_Z
    if (step_count_Z >0):
        GPIO.output(DIR_Z, not MOTOR_Z_DIR_CW)
        for x in range(step_count_Z):
            GPIO.output(STEP_Z, GPIO.HIGH)
            GPIO.output(STEP_Z, GPIO.LOW)
            sleep(delay_Go_To_Z)
            current_position_Z = current_position_Z + 1
            if (GPIO.input(endstop_Z_Pin)):
                break
    else:
        GPIO.output(DIR_Z, MOTOR_Z_DIR_CW)
        step_count_Z = step_count_Z
        for x in range(step_count_Z, -1):
            GPIO.output(STEP_Z, GPIO.HIGH)
            GPIO.output(STEP_Z, GPIO.LOW)
            sleep(delay_Go_To_Z)
            current_position_Z = current_position_Z - 1

    return(current_position_Z)


def Goto_A(destinastion_A, current_position_A):
    step_count_A = destinastion_A * Motor_A_steppercell - current_position_A
    #delay_Go_to_A
    if (step_count_A > 0):
        GPIO.output(DIR_A, not MOTOR_A_DIR_CW)
        for x in range(step_count_A):
            GPIO.output(STEP_A, GPIO.HIGH)
            GPIO.output(STEP_A, GPIO.LOW)
            sleep(delay_Go_to_A)
            current_position_A = current_position_A + 1

    else:
        GPIO.output(DIR_A, MOTOR_A_DIR_CW)
        step_count_A = step_count_A

        for x in range(step_count_A, -1):
            GPIO.output(STEP_A, GPIO.HIGH)
            GPIO.output(STEP_A, GPIO.LOW)
            sleep(delay_Go_to_A)
            current_position_A = current_position_A - 1

    return (current_position_A)

#go_to(destinastion_Z, current_position_Z, destinastion_A, current_position_A)
def go_to(destinastion_Z, destinastion_A, current_position_Z, current_position_A):
    if (destinastion_Z != current_position_Z):
        new_current_position_Z = Goto_Z(destinastion_Z, current_position_Z)
    if (destinastion_A != current_position_A):
        new_current_position_A = Goto_A(destinastion_A, current_position_A)

    return (new_current_position_Z , new_current_position_A)

if __name__ == "__main__":
    destinastion_Z = 1
    destinastion_A = 2
    current_position_Z = 0
    current_position_A = 0
    go_to(destinastion_Z, destinastion_A)