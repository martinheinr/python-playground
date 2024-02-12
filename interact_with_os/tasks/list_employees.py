""" For this lab, imagine you are an IT Specialist at a medium-sized company. 
The Human Resources Department at your company wants you to find out how many people are in each department. 
You need to write a Python script that reads a CSV file containing a list of the employees in the organization, 
counts how many people are in each department, and then generates a report using this information. 
The output of this script will be a plain text file. """

import csv
csv_file_location = "C:\\test_files\\employees.csv"

def read_employees(csv_file_location):

    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_list = []
    with open(csv_file_location) as employees_list:
        employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
        for data in employee_file:
            employee_list.append(data)

    return employee_list

#print(read_employees(csv_file_location))
employee_list = read_employees(csv_file_location)

def process_data(employee_list):
    department_list = []
    for row in employee_list:
        #Append the names of the department that are in the the row 'Department' to the list
        department_list.append(row['Department'])
    #Initialize the dictionairy
    department_data = {}
    #Itterate through the list and for each of the department names (keys) add the value which is basically a count of how many times
    #department name appears on the list
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    print(department_list)
    print(department_data)
    return department_data

dictionary = process_data(employee_list)
#print(dictionary)

def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
    f.close()

#write_report(dictionary, 'C:\\test_files\\report.txt')

