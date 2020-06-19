#%%
"""
Using_Python-to_Interact_with_the_OS_
week 2 - Managing files with Python

4 MODULE REVIEW

For this lab, imagine you are an IT Specialist at a medium-sized company. 
The Human Resources Department at your company wants you to find out how many people are in each department. 
You need to write a Python script that reads a CSV file containing a list of the employees in the organization,
 counts how many people are in each department, and then generates a report using this information. 
The output of this script will be a plain text file.

"""
#%%
import csv

def read_employees(filepath): # 1st function
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True) # The main purpose of this dialect is to remove any leading spaces while parsing the CSV file.
    reader = csv.DictReader(open(filepath), dialect='empDialect')         # open the csv file as reader (an instance of the dictreader)
    
    employee_list = [] # empty list, will be populated below
    for row in reader: # here we iterate over each row of the csv. First row iteration provides the key, subsequent row iteration provides the values
        employee_list.append(row) # we construct the employee_list of ordered dictionaries by appending each row after the other
    return employee_list # employee_list contains elements which are ordered dictionaries. 
employee_list = read_employees("employees.csv")
print(employee_list)

def process_data(employee_list): # 2nd function it produces the dictionary 
    department_list = [] # empty list, will be populated below
    for employee_data in employee_list: # iterate over the elements of the employee_list
        department_list.append(employee_data["Department"]) # populate the department_list by choosing from each element(each ordered dictionary) only the first part of each element (the Department)
    department_data = {} # empty dictionary, will be populated below
    for department_name in set(department_list): # set() method, converts iterable elements to distinct elements. Syntax : set(iterable)
        department_data[department_name] = department_list.count(department_name) # creates the Key:value pair for the new dictionary
    return department_data
    
department_data = process_data(employee_list)
print(department_data)  
   
def write_report(dictionary, report_file):
    with open(report_file, "w+") as file: # open and create the text file 
        for k in sorted(dictionary): # iterate over each dictionary element (each Key:value pair). Attention! Iteration happens only over the dictionary Keys
            file.write(str(k) + ":" + str(dictionary[k]) + "\n") # for each iteration write on the text file the Key, then :, then the value of the Key, then the new line character
    file.close()
write_report(department_data, "report.txt") # call the function by providing the name of the new text file to be created

# I have already constructed a csv file, employees.csv
#Department, Username, Full Name
#Development, Audrey, Audrey Miller
#Production, John, John Snow
#Development, Mary, Mary White
#Production, George, George Brown
#IT infrastructure, Anthony, Anthony Gibbs

# 1st FUNCTION "read_employees", creates a list of dictionaries*(a list whose elements are dictionaries. A dictionary contains  Key:value pairs as its elements)
# in earlier Python versions, DictReader produced indeed a list of dictionaries
# currently, DictReader produces by default a list of ordered dictionaries where the keys are ordered as in the header of the csv
# csv.DictReader(), Creates an object (reader) that operates like a regular reader but maps the information in each csv row to a dict whose keys are given by the optional fieldnames parameter.
# create an empty list of employees (a list with elements that are dictionaries)    
# 1st csv row =  Department,Username,Full Name
# 2nd csv row = Development,Audrey, Audrey Miller
# 2nd csv row becomes first element of the list. The element is an ordered dictionary, ('Department', 'Development'), ('Username', 'Audrey'), ('Full Name', 'Audrey Miller')
# iterate over the reader (csv opened as an instance(reader) of the dictreader)
# first iteration provides the Keys to the ordered dictionaries
# subsequent iterations provide values for the Keys and we get the Key:value pair
# 1st iteration (1st csv row) provides Keys
# 2nd iteration (2nd csv row): [OrderedDict([('Department', 'Development'), ('Username', 'Audrey'), ('Full Name', 'Audrey Miller')])

# 3rd iteration (3rd csv row): [OrderedDict([('Department', 'Development'), ('Username', 'Audrey'), ('Full Name', 'Audrey Miller')]), 
#                              OrderedDict([('Department', 'Production'), ('Username', 'John'), ('Full Name', 'John Snow')])]
# finallly the list of ordered dictionaries is: [OrderedDict([('Department', 'Development'), ('Username', 'Audrey'), ('Full Name', 'Audrey Miller')]), 
#                                               OrderedDict([('Department', 'Production'), ('Username', 'John'), ('Full Name', 'John Snow')]), 
#                                               OrderedDict([('Department', 'Development'), ('Username', 'Mary'), ('Full Name', 'Mary White')]), 
#                                               OrderedDict([('Department', 'Production'), ('Username', 'George'), ('Full Name', 'George Brown')]), 
#                                               OrderedDict([('Department', 'IT infrastructure'), ('Username', 'Anthony'), ('Full Name', 'Anthony Gibbs')])]
# so essentially we get a list of ordered dictionaries
# we append each iteration result to the empty list .Each iteration provides an element to the list
# the result of the function we want to extract is the list, we do this by using the return statement
# we assign a Variable to the result of the function and at the same time we call the function by providing the argument(value) "employees.csv". ("employees.csv" is the relative path of an existing csv file)
# we will use this Variable in another function below

# 2nd FUNCTION "process_data" takes as a parameter the result of the 1st function (Variable=employees_list, value=list of ordered dictionaries )
# create an empty list "department_list" 
# i will populate "department_list" only with the elements of the "employee_list" which contain the Key 'Department'
# 1st list element is ordered dictionary. The ordered dictionary contains three sub-elements 
# employee_data["Department"] is list element 1[dictionary sub-element 1(Key)] = value of sub-element 1(Key) it is Development
#                               list element 2[dictionary sub-element 1(Key)] = value of sub-element 1(Key) it is Production
# so the "department_list" looks like this, ["Development", "Production", "Development", "Production", "IT Infrastructure"] and it is a list of strings (elements of list are strings)

# create an empty dictionary "department_data"
# set(iterable), A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
# set(iterable) syntax: the parameter is required. Iterable is a sequence, collection or an iterator object (list, tuple, dictionary etc)
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
# after applying the set() function on the "department_list" we get the set {'IT Infrastructure', 'Production', 'Development'}
# the set contains strings as elements but now we have unique strings and no duplicates
# we iterate over this set
# department_data[department_name] this is the Key of the dictionary department_data and is equal to the corresponding value (remember Key:value pair is the element of dictionaries)
# dictionary[Key] = value. This is like asking what is the value for that Key in the dictionary. Here we use this to construct the dictionary
# list.count(value), The count() method returns the number of elements with the specified value. so for the list "department_list" we want to count the number of elements that are unique
# note that we are iterating over the set(list) where elements are unique and not on the list itself where there are duplicates
# so the result of each iteration is a Key:value pair (a dictionary element). Key is the Department and value is number of apperances of that Department
# we have 3 elements in the set so we do 3 iterations. 1st iteration gives us {"Development":2}, 2nd iteration {"Development":2, "Production:2"}, 3rd iteration {"Development":2, "Production:2", "IT Infrastructure":1}
# # the result of the function we want to extract is the dictionary so we use the return statement for the Variable "department_data"
# Finally we call the function by providing the argument "employee_list" (employee_list is the output of the 1st function)
# Our dictionary looks like this
#{'Production': 2, 'IT infrastructure': 1, 'Development': 2}

# 3rd FUNCTION "write_report", will produce a text file within which, the dictionary "department_data" will be written
# sorted() function applied on the dictionary produces another dictionary where the Keys are alphabetically sorted?I think yes:)
# the text file we create her will have the contents
# Development:2
#IT infrastructure:1
#Production:2
      
