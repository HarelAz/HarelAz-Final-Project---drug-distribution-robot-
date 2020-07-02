#endstop test (tcst2103)
from time import sleep

import RPi.GPIO as GPIO  # import RPi.GPIO module

GPIO.setwarnings(False)
endstop1 = 6   # endstop1 GPIO Pin
delay = 1
count = 100
GPIO.setmode(GPIO.BCM)            # choose BCM or BOARD  
GPIO.setup(endstop1, GPIO.IN)  # set a port/pin as an input  
#GPIO.setup(port_or_pin, GPIO.OUT) # set a port/pin as an output   
#GPIO.output(port_or_pin, 1)       # set an output port/pin value to 1/HIGH/True  
#GPIO.output(port_or_pin, 0)       # set an output port/pin value to 0/LOW/False  
for x in range(count):
    i = GPIO.input(endstop1)       # read status of pin/port and assign to variable i  
    print(i)
    sleep(delay)
