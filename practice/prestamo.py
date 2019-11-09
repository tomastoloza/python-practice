import csv

with open('prestamo.txt') as file:
    reader = csv.reader(file)
    sum = 0
    for row in reader:
        sum+=float(row[len(row)-2])

    print(sum)
