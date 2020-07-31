from art import tprint
import os
from main_code.conf import *
from main_code.moduless import *
from main_code.homing import *
from Testing.Testing_Go_To import *



testing_menu_list = ['Welcome to Medicine distribution testing: \n please enter you\'re choice:\n',
                     'testing homing',
                     'testing go to Position',
                     'testing engine 3']


def clear_screen():
    delay = 0
    sleep(delay)
    print(chr(27) + "[2J")
    os.system('clear')
    tprint("Medicine distribution")


def testing_menu():
    clear_screen()
    while True:
        menu_choice = print_menu(testing_menu_list)

        if menu_choice == len(testing_menu_list):
            break
        elif menu_choice == 1:

            T = homing()
            current_position_Z = T[0]
            current_position_A = T[1]
        elif menu_choice == 2:

            T = Testing_Go_To(current_position_Z, current_position_A)
            current_position_Z = T[0]
            current_position_A = T[1]
        elif menu_choice == 3:
            continue

        clear_screen()

calibration_menu_list = ['Welcome to calibration main menu: \n please enter you\'re choice:\n',
                  'calibration Z axis',
                  'calibration A axis']

def calibration_menu():
    clear_screen()
    while True:
        menu_choice = print_menu(calibration_menu_list)

        if menu_choice == len(main_menu_list):
            break
        elif menu_choice == 1:
            calibrate_Z()
        elif menu_choice == 2:
            calibrate_A()

        clear_screen()


operation_menu_list = ['Welcome to Medicine distribution operation: \n please enter you\'re choice:\n',
                       'Machine ON',
                       'Patients List',
                       'View drug inventory',
                       'Collect a pill by name',
                       'calibration',
                       'machine off and close',]

def operation_menu():
    clear_screen()
    while True:
        menu_choice = print_menu(operation_menu_list)

        if menu_choice == len(operation_menu_list):
            break
        elif menu_choice == 1:
            homing()
            print(current_position_A)
            print(current_position_Z)
        elif menu_choice == 2:
            continue
        elif menu_choice == 3:
            continue
        elif menu_choice == 4:
            continue
        elif menu_choice == 5:


            continue

        clear_screen()


main_menu_list = ['Welcome to Medicine distribution main menu: \n please enter you\'re choice:\n',
                  'testing',
                  'full operation running']


def main_menu():
    clear_screen()
    print("starting application")

    while True:
        menu_choice = print_menu(main_menu_list)

        if menu_choice == len(main_menu_list):
            break
        elif menu_choice == 1:
            testing_menu()
        elif menu_choice == 2:
            operation_menu()

        clear_screen()


def print_menu(menu_items):
    index = 0
    for menu_item in menu_items:
        if index == 0:
            print(menu_item)
        else:
            print(str(index) + ". for " + menu_item)
        if len(menu_items) - 1 == index:
            print(str(index + 1) + ". for exit.")
        index += 1
    menu_choice = int(input(""))
    return menu_choice


def main():
    main_menu()


if __name__ == "__main__":
    main()
