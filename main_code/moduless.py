'''def importing():
    #Importing File
    from code import GoTo
    from code import Servo_1
    from code import config
    from code import homing
'''


# Importing Modules
from main_code.con import *
from main_code.motor_status import *

from main_code.SERVO_ANGLE import *
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
from time import sleep
import numpy as np
from squid import *
#import pyqrcode
#from pyzbar.pyzbar import decode
#from PIL import Image
#import cv2


