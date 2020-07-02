'''Patient Dictionary'''
Patient1 = {'Name' : 'BORIS' , 'age' : 25 , 'Medication': ['Acamol_50', 'Aspirin_100']};
Patient2 = {'Name' : 'YOSSI' , 'age' : 25 , 'Medication': ['Acamol_50', 'Aspirin_100']};
Patient3 = {'Name' : 'MOSHE' , 'age' : 25 , 'Medication': ['Acamol_50', 'Aspirin_100']};
Patient4 = {'Name' : 'OMER' , 'age' : 25 , 'Medication': ['Acamol_50', 'Aspirin_100']};

'''Medication Dictionary'''
Medication1 = {'Name' : 'Acamol_50' , 'Quantity' : 100 , 'Location':[1,1]}
Medication2 = {'Name' : 'Aspirin_100' , 'Quantity' : 100 , 'Location':[1,2]}
Medication3 = {'Name' : 'Paramol_50' , 'Quantity' : 100 , 'Location':[1,3]}

print(Patient3.get('Name'))
print(Medication1.get('Name'))
print(Medication1.get('Quantity' ))
print(Medication1['Name'],Medication1['Quantity'])