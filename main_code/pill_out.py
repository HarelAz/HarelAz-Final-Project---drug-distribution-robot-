######################### Importing modules #########################
from main_code.moduless import *
from main_code.confi import *
from main_code.GoTo import *
from main_code.SERVO_ANGLE import *
from pill_detector import *

def load_json(file_name, path="resources/"):
    with open(path + file_name, 'r') as json_file:
        return json.load(json_file)


def load_json_file():
    # load json file intro dict variable
    drugs_list = load_json("drugs_list.json", "./resuorses/")  # load json function return dict
    return drugs_list





def pill_out(drug_name, drug_sum, current_position):
    drugs_list = load_json_file()
    for drug in drugs_list:
        if drug_name == (drugs_list[drug]['drug_name']):
            destinastion_A = (drugs_list[drug]['capsul_location_A'])
            destinastion_Z = (drugs_list[drug]['capsul_location_Z'])
            #print(destinastion_A, destinastion_Z)
            go_to(destinastion_Z, destinastion_A, current_position)
            for drug_num in range(1, drug_sum + 1):
                print(amount_of_pills())
                servo_1_out()
                sleep(2)
                print(amount_of_pills())
#return current_position

if __name__ == "__main__":
    current_position[0] = 0
    current_position[1] = 0
    pill_out('Erythromycin', 1, current_position)
