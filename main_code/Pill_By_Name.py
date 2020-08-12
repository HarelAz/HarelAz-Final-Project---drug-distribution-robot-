######################### Importing modules #########################
from main_code.moduless import *
from main_code.confi import *
from main_code.pill_out import *

def load_json(file_name, path="resources/"):
    with open(path + file_name, 'r') as json_file:
        return json.load(json_file)


def load_json_file():
    # load json file intro dict variable
    patients_list = load_json("patients_list.json", "../resuorses/")  # load json function return dict
    return patients_list





def pill_by_number(selected_patient, current_position):
    patients_list = load_json_file()

    #print(patients_list[selected_patient]['drugs_list'])

    # loop over dict keys patient list drugs_list

#    for drug_number in patients_list:

    drug_amount = len(patients_list[selected_patient]['drugs_list'])
    print(drug_amount)
    #print(patients_list[selected_patient]['drugs_list'][drug_number]['drug_name'])

    for drug_number in range(1, drug_amount+1):
        drug_name = patients_list[selected_patient]['drugs_list'][str(drug_number)]['drug_name']
        drug_sum = patients_list[selected_patient]['drugs_list'][str(drug_number)]['amount']
        pill_out(drug_name, drug_sum, current_position)


def print_patients_list():
    patients_list = load_json_file()

    # loop over dict keys patient list drugs_list
    for patient in patients_list:
        print(patient, ")", patients_list[patient]['first_name'], patients_list[patient]['last_name'],
              patients_list[patient]['id'])


def pill_by_name(current_position):
    print_patients_list()
    selected_patient = (input("What is the patients number?"))
    #print(selected_patient)
    pill_by_number(selected_patient, current_position)



if __name__ == "__main__":
    pill_by_name()
