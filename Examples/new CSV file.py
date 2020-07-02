import csv

with open('prescription.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)

    thewriter.writerow([ 'Number', 'Name', 'ID', 'Acamol'])
    thewriter.writerow([ '1', 'Iossi', '111', '2'])
