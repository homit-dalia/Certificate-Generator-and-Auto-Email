import csv

with open('userData.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    for lines in data:
        text = "Hello " + lines[0]
        print (text)