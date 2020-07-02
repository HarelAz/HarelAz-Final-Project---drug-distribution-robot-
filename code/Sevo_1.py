

pwm.start(0)
def Servo_1_SetAngle(angle):
    duty =(180 - angle) / 18 + 2
    GPIO.output(ServoPin, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(ServoPin, False)
    pwm.ChangeDutyCycle(0)