'''def importing():
    #Importing File
    from code import GoTo
    from code import Servo_1
    from code import config
    from code import homing
'''


# Importing Modules

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
from art import tprint
from time import *
#import pyqrcode
#from pyzbar.pyzbar import decode
#from PIL import Image

import cv2


from main_code.homing import *
from main_code.NumberOfPills import *