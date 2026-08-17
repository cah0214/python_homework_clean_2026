import csv
import traceback
import os
import custom_module
from datetime import datetime

# Task 2
def read_employees():
    employees_dict = {}
    rows = []
    try:
        with open("../csv/employees.csv", "r") as employee_file:
            reader = csv.reader(employee_file)

            for index, row in enumerate(reader):
                if index == 0:
                    employees_dict["fields"] = row
                else:
                    rows.append(row)

        employees_dict["rows"] = rows
        return employees_dict
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]}, Func.Name : {trace[2]}, Line No : {trace[1]}, Message : {trace[3]}')

        print(f"Exception type: {type(e).__name__}")
        message = str(e)

        if message:
            print(f"Exception message : {message}")

        print(f"Stack trace: {stack_trace}")

employees = read_employees()
print(employees)


# Task 3 
def column_index(column_name):
    index = employees["fields"].index(column_name)
    return index

employee_id_column = column_index("employee_id")


# Task 4 
def first_name(row_number):
    first_name_column = column_index("first_name")
    name = employees["rows"][row_number][first_name_column]
    return name

# Task 5
def employee_find(employee_id):

    def employee_match(row):
        return int(row[employee_id_column]) ==employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches 

# Task 6
def employee_find_2(employee_id):
    matches = list(
        filter(
            lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]
        )
    )
    return matches

# Task 7
def sort_by_last_name():
    last_name_column = column_index("last_name")
    employees["rows"].sort(
        key=lambda row: row[last_name_column]
    )
    return employees["rows"]

# Task 8
def employee_dict(row):
    employee = {}
    for index, field in enumerate(employees["fields"]):
        if field != "employee_id":
            employee[field] = row[index]
    return employee


#task 9
def all_employees_dict():
    all_employees = {}

    for row in employees["rows"]:
        employee_id = row[employee_id_column]
        all_employees[employee_id] = employee_dict(row)
    return all_employees

print(all_employees_dict())

# Task 10
def get_this_value():
    return os.getenv("THISVALUE")

# Task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

# Task 12
def read_minutes():
    def read_file(filename):
        minutes_dict = {}
        rows = []

        with open(filename, "r") as file:
            reader = csv.reader(file)

            for index, row in enumerate(reader):
                if index == 0:
                    minutes_dict["fields"] = row
                else:
                    rows.append(tuple(row))
        minutes_dict["rows"] = rows
        return minutes_dict

    minutes1 = read_file("../csv/minutes1.csv")
    minutes2 = read_file("../csv/minutes2.csv")

    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

# Task 13
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])

    combined_set = set1.union(set2)
    return combined_set
minutes_set = create_minutes_set()

# Task 14
def create_minutes_list():
    minutes_list = list(minutes_set)

    minutes_list = list(
        map(
            lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),
            minutes_list

        )
    )
    return minutes_list

minutes_list = create_minutes_list()
print(minutes_list)

# Task 15
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])

    converted_list = list(
        map(
            lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")),
            minutes_list
        )
    )

    with open("./minutes.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_list) 

    return converted_list 


