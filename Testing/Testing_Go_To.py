from main_code.GoTo import *

def Testing_Go_To(current_position):
    destinastion_Z = int(input("What is the Cell Floor destination?"))
    destinastion_A = int(input("What is the Cell Number on floor destination?"))
    go_to(destinastion_Z, destinastion_A, current_position)
