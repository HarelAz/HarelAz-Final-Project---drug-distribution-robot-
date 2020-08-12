######################### Importing modules #########################
from main_code.confi import *
from main_code.moduless import *

######################### Function that move the axis to the wanted Z position #########################
def Goto_Z(destinastion_Z, current_position_Z):
    # Calculate the number of steps to the desired position from the current position
    step_count_Z = destinastion_Z *Motor_Z_steppercell - int(current_position_Z)

    if (step_count_Z > 0): # Move the Z axis in positive direction
        GPIO.output(DIR_Z, not MOTOR_Z_DIR_CW)
        for x in range(step_count_Z):
            GPIO.output(STEP_Z, GPIO.HIGH)
            GPIO.output(STEP_Z, GPIO.LOW)
            sleep(delay_Go_To_Z)
            current_position_Z = current_position_Z + 1
            if (GPIO.input(endstop_Z_Pin)):
                break

    else: # Move the Z axis in negative direction
        GPIO.output(DIR_Z, MOTOR_Z_DIR_CW)
        for x in range(step_count_Z, -1):
            GPIO.output(STEP_Z, GPIO.HIGH)
            GPIO.output(STEP_Z, GPIO.LOW)
            sleep(delay_Go_To_Z)
            current_position_Z = current_position_Z - 1
    return current_position_Z


######################### Function that move the axis to the wanted A position #########################
def Goto_A(destinastion_A, current_position_A):
    # Calculate the number of steps to the desired position from the current position
    step_count_A = destinastion_A * Motor_A_steppercell - current_position_A

    if (step_count_A > 0): # Move the a axis in positive direction
        GPIO.output(DIR_A, not MOTOR_A_DIR_CW)
        for x in range(step_count_A):
            GPIO.output(STEP_A, GPIO.HIGH)
            GPIO.output(STEP_A, GPIO.LOW)
            sleep(delay_Go_to_A)
            current_position_A = current_position_A + 1

    else: # Move the A axis in negative direction
        GPIO.output(DIR_A, MOTOR_A_DIR_CW)
        step_count_A = step_count_A
        for x in range(step_count_A, -1):
            GPIO.output(STEP_A, GPIO.HIGH)
            GPIO.output(STEP_A, GPIO.LOW)
            sleep(delay_Go_to_A)
            current_position_A = current_position_A - 1

    return current_position_A


######################### Go_to function #########################
def go_to(destinastion_Z, destinastion_A, current_position):
    global current_position_Z
    global current_position_A
    current_position_Z = current_position[0]
    current_position_A = current_position[1]
    if (destinastion_Z *Motor_Z_steppercell != current_position_Z):
        current_position[1] = Goto_A(0, current_position_A)
        current_position_A = current_position[1]
    current_position[0] = Goto_Z(destinastion_Z, current_position_Z)
    current_position[1] = Goto_A(destinastion_A, current_position_A)
    return current_position


######################### Testing the Go_to function #########################
if __name__ == "__main__":
    destinastion_Z = 1
    destinastion_A = 2
    current_position_Z = 0
    current_position_A = 0
    go_to(destinastion_Z, destinastion_A)