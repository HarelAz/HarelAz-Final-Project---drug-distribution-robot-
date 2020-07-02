from main_code.homing import *
from main_code.GoTo import *

def Testing_Go_To():
    destinastion_Z = int(input("What is the Cell Floor destination?"))
    destinastion_A = int(input("What is the Cell Number on floor destination?"))
    #homing()
    T = go_to(destinastion_Z, destinastion_A, current_position_Z, current_position_A)
    new_current_position_Z = T[0]
    new_current_position_A = T[1]
    print(T)
    print(new_current_position_Z)
    print(new_current_position_A)
    return T
