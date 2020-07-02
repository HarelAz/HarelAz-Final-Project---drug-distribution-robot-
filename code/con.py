
'''
Motor A
Motor A is the stepper motor that is responsible for the rotation movment of the axis
'''
#Pins
EN_A = 13   # EN GPIO Pin
STEP_A = 19  # Step GPIO Pin
DIR_A = 26   # Direction GPIO Pin
endstop_A_Pin = 6   # endstop1 GPIO Pin

#Constant
A_MIN_ENDSTOP_INVERTING = 1 # set to 0 to invert the logic of the endstop.
MOTOR_A_DIR_CW = 1     # Clockwise Rotation
#CCW = 0    # Counterclockwise Rotation
Motor_A_steppercell = 470    #step per cell

#PinMod  - set a port/pin as an input/output
GPIO.setup(EN_A, GPIO.OUT)
GPIO.setup(DIR_A, GPIO.OUT)
GPIO.setup(STEP_A, GPIO.OUT)
GPIO.setup(endstop_A_Pin, GPIO.IN)

'''
Motor Z
Motor Z is the stepper motor that is responsible for the Up/Dowm movment of the axis
'''
#Pins
EN_Z = 16   # EN GPIO Pin
STEP_Z = 20  # Step GPIO Pin
DIR_Z = 21   # Direction GPIO Pin
endstop_Z_Pin = 5   # endstop1 GPIO Pin

#Constant
Z_MIN_ENDSTOP_INVERTING = 1 # set to 0 to invert the logic of the endstop.
MOTOR_Z_DIR_CW = 1     # Clockwise Rotation
Motor_Z_steppercell = 6000    #step per cell


#PinMod  - set a port/pin as an input/output
GPIO.setup(EN_Z, GPIO.OUT)
GPIO.setup(DIR_Z, GPIO.OUT)
GPIO.setup(STEP_Z, GPIO.OUT)
GPIO.setup(endstop_Z_Pin, GPIO.IN)  # set a port/pin as an input


'''
Servo 1 is responsible for 
'''
Servo_1_Pin = 24
GPIO.setup(Servo_1_Pin, GPIO.OUT)
pwm=GPIO.PWM(Servo_1_Pin, 50)
'''
Servo 2 is responsible for 
'''
Servo_2_Pin = 23
GPIO.setup(Servo_2_Pin, GPIO.OUT)
pwm=GPIO.PWM(Servo_2_Pin, 50)
'''
RGB Led
'''
RED_PEN = 22   # RED Led GPIO Pin
GREEN_PIN = 27  # GREEN Led GPIO Pin
BLUE_PIN = 17   # BLUE Led GPIO Pin

rgb = Squid(RED_PEN, GREEN_PIN, BLUE_PIN)

'''
Variable
'''
correntposition_A
destinastion_A
delay_home_A = 0.0005
delay_Go_to_A = 0.001


correntposition_Z
destinastion_Z
delay_home_Z = 0.00015
delay_Go_To_Z = 0.00015





