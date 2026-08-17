import csv 

# Task 3

employess = []

with open("../csv/employees.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        employess.append(row)

employee_names = [
    row[1] + " " + row[2] for row in employess[1:] ]

print(employee_names)

names_with_e = [
    name
    for name in employee_names
    if "e" in name
]

print(names_with_e)
