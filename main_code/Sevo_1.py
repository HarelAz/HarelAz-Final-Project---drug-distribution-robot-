pwm.start(0)

######################### Servo_1_SetAngle function #########################
def Servo_1_SetAngle(angle):
    duty =(180 - angle) / 18 + 2
    GPIO.output(ServoPin, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(ServoPin, False)
    pwm.ChangeDutyCycle(0)