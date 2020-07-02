def Goto_Z(destinastion_Z, correntposition_Z):

    step_count = destinastion_Z *Motor_Z_steppercell - correntposition_Z
    delay_Go_To_Z
    if (step_count_Z >0):
        GPIO.output(DIR, not MOTOR_Z_DIR_CW)
        for x in range(step_count_Z):
            GPIO.output(STEP, GPIO.HIGH)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
            correntposition_Z = correntposition_Z + 1
            if (GPIO.input(endstop1Pin)):
                break
    else:
        GPIO.output(DIR, MOTOR_Z_DIR_CW)
        step_count_Z = step_count_Z

        for x in range(step_count_Z, -1):
            GPIO.output(STEP, GPIO.HIGH)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
            correntposition_Z = correntposition_Z - 1

    return(correntposition_Z)


def Goto_A(destinastion_A, correntposition_A):
    step_count_A = destinastion_A * Motor_A_steppercell - correntposition_A
    delay_Go_to_A
    if (step_count_A > 0):
        GPIO.output(DIR, not MOTOR_A_DIR_CW)
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
            correntposition_A = correntposition_A + 1

    else:
        GPIO.output(DIR, MOTOR_A_DIR_CW)
        step_count_A = step_count_A

        for x in range(step_count_A, -1):
            GPIO.output(STEP, GPIO.HIGH)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
            correntposition_A = correntposition_A - 1

    return (correntposition_A)


def go_to(destinastion_Z, correntposition_Z, destinastion_A, correntposition_A):
    if (destinastion_Z != correntposition_Z):
        Goto_Z(destinastion_Z, correntposition_Z)
    if (destinastion_A != correntposition_A):
        Goto_A(destinastion_A, correntposition_A)

if __name__ == "__main__":
    destinastion_Z = 1
    destinastion_A = 1
    correntposition_Z = 0
    correntposition_A = 0
    go_to(destinastion_Z, correntposition_Z, destinastion_A, correntposition_A)