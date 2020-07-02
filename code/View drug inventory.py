import csv

with open('pills.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:

        print(row)


