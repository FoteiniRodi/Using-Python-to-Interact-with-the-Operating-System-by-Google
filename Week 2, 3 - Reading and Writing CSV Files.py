
#%%
"""
Using_Python-to_Interact_with_the_OS_
week 2 - Managing files with Python

3 READING AND WRITING CSV FILES
3.1     What is a CSV file?
3.2     Reading CSV Files
3.3     Generating CSV
3.4     Reading and Writing CSV Files with Dictionaries
3.5     CSV Files Cheat Sheet
3.6     Practice Quiz: Reading & Writing CSV Files


SYNOPSIS
3.2 Reading csv files
csv.reader() 
from csv to list
each row of the csv file becomes a list (each csv field becomes an element of the list)
if we have 4 fields in a row of the csv then we get a list with 4 elements
3.3 Generating csv files
csv.writer(), creates the instance writer
from list to csv
each element of the list becomes a row in the csv 
(ofcourse the element of the list can be a dictionary so our row can contain the dictionary: the values of their respective keys)
use the function writer.writerow(row), to write one row at a time or writer.writerows(rows), to write all rows at once
3.4
a) csv.DictReader   from csv to dictionary
b) csv.DictWriter   from dictionary to csv
"""


"""
3.1     What is a CSV file?
parse = αναλύω
Parsing = analyzing a file's content, to correctly structure the data
Parsing a file means analyzing its contents to correctly structure the data, and occurs while reading a file.
Until now we worked with text files (NotePad)
But data comes in a bunch of different formats besides text.
We use a bunch of different file formats to structure, store, and transport data:
    HTML: HTML is a markup format which defines the content of a webpage
    JSON: JSON is a data interchange format commonly used to pass data between computers on networks, especially the internet. 
    CSV: CSV or comma separated values is a very common data format used to store data as segment of text separated by commas. 
Below, we will use the CSV module to process CSV files.
The CSV format lets us easily store and retrieve information that we might need for our scripts 
Think of a CSV file like it's a spreadsheet, where each line corresponds to a row and each comma separated field corresponds to a column.
"""
    
"""
3.2     Reading CSV Files
We just use the reader function from the csv module, to read the contents of the CSV file.
syntax: csv.reader(csvfile, dialect='excel', **fmtparams)

csv module: module which lets us read, create and manipulate CSV files.
csv file
each line is a row and columns are separated by the comma ( a csv field is in fact a column, csv field = column)
each line represents a single data record

we have a csv file with 4 rows.
Each row contains 3 fields separated by a comma
each row corresponds to an employee
1st field is name, 2nd field is phone number and 3rd field is role

"""
# 1 Read an existing csv with csv.reader(), open/read/close approach
import csv                 # import csv module
file = open("example1.csv")   # open the csv file (we create a file object. We open the csv as a file object)
reader = csv.reader(file)     # read the csv file (we use csv.reader() method, and we create the instance reader
                               # the reader instance is our csv file which now we can read
for row in reader:        # Iterate over the  reader. It has 4 rows. Each row is a list which contains 3 elements (the 3 csv fields or columns)
    name, phone, role = row # We unpack the values of the list "row" and assign a Variable to each element.(we already know that element 0 is name, element 1 is phone number etc. )
    print("Name: {}, Phone: {},Role: {}".format(name, phone, role)) # we use the format method to display the results
    print(row) # row here is a list and its elements are the csv fields/columns
file.close() # this is the open, read,close approach so we must close the file in the end

# I open the existing csv file and read it with csv.reader() .I am opening the csv as "reader" instance
# I iterate over the reader (which is essentialy my csv). 
# I iterate over the reader rows, and each row corresponds to a csv row. The reader row is a list and the elements are the contents of the csv fields(columns)


#%%
# 2 Read an existing csv with csv.reader(), with block approach
import csv 
with open("example1.csv") as file:  # open the csv file
    reader = csv.reader(file) # read the csv file
    for row in reader:        # iterate over EACH row of the csv file
        name, phone, role =row      # unpack the elements of the list row (unpack elements/columns/fields of each csv row)
        print("Name: {}, Phone: {},Role: {}".format(name, phone, role)) # print the results with the format method
        print(row) # row here is a list and its elements are the csv fields/columns



#%%
"""
3.3     Generating CSV

We will create a csv file starting from a list.
We already know what the name of the column is ( we have a few columns/csv fields)

We will use the writer function to generate contents for the new csv file
syntax: csvwriter.writerows(rows)

This can be really helpful if you process some data in your script and you must store it in a file.

1   We will store the data that we want to write into the csv, initially into a list.
    (it is a list with 2 elements. Each element is a list too)
2   open a new csv file in "write" mode
3   call the writer function of the CSV module with the new csv file as a parameter.
4   writer.writerow(row)     we write one row at a time
    writer.writerows(rows)   we write all rows at once


"""
# 3 Create new csv with csv.writer() starting from a list

hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]] # list
with open("hosts.csv", "w") as file: # create a new csv file using the "write" mode
    writer = csv.writer(file)        # use the csv.writer() method to write into the new csv file (the Variable writer is now an instance of the csv writer class)
    writer.writerows(hosts)          # the writerows() method writes all row in the csv at once

# one list element becomes one csv row
# in other words, list element corresponds to csv row and vice versa
# here I have 2 list elements so I will create 2 csv rows.
# each element is also a list, the sub-elements of the element will become csv fields in the csv row

# in row 1, I see the element 0 of the initial list *sub-elements of element 0, become csv fields
# in row 2, I see the element 2 of the initial list *sub-elements of element 0, become csv fields
# So, essentially, I transformed a list into a csv file

## in linux command line:
#    cat hosts.csv
#    workstation.local, 192.168.25.46
#    webserver.cloud, 10.2.5.6
#%%
"""
3.4     Reading and Writing CSV Files with Dictionaries

EXAMPLE - Create a dictionary, starting from a csv
We use dictionaries, when the columns (csv field of each row) are too many and we need to remember the name for each column

We use the csv.DictReader class
syntax: csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)
csv.DictReader(), maps the information in each row to a dictionary whose keys are given by the optional fieldnames parameter.(In this example I use the 1st row csv fields as keys)

first row of csv contains the keys
subsequent rows of csv contain the values for each key

(We can then access the data by using the column names instead of the position in the row.)
"""
#%%
# 4 create a dictionary starting from an existing csv with csv.DictReader()
import csv
with open("software.csv") as file: # open the csv file
    reader = csv.DictReader(file)  # read the csv file (create the instance)
    for row in reader:                 # here we iterate over each row of the csv. First row provides the key, subsequent rows provide the values
            print("The software:{} is in version:{}, is in status:{} and  it has {} users". format(row["name"], row["version"], row["status"], row["users"]))
            print(row)              # I added this to see what exactly is the row
            
# I have a csv in which 1st row has column titles and next rows have values
# I open this csv 
# I read the csv with csv.DictReader() and also transform it into a dictionary with keys and values
# csv.DictReader() produces the instance reader
# in the reader I have rows. If I only use file as an argument then by default first csv row contains the keys of the future dictionary
# I have 4 rows in the csv. The 3 rows of it are converted into an ordered dictionary (row = ordered dictionary). An element in a dictionary is the combination Key-value
# row is an ordered dictionary (not exactly a dictionary)     
# reader row corresponds to csv row BUT it also uses first csv row as keys and then the next row as values for these keys
#%%
"""
EXAMPLE - Create a csv, starting from a dictionary
We use dictionaries, when the columns (csv field of each row) are too many and we need to remember the name for each column

We use the csv.DictWriter class
syntax: csv.DictWriter(f, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)

I start with a list.
Each element of the list is a dictionary.
A dictionary contains a key and its corresponding value.
We have 3 dictionaries (our list has 3 elements)
Each dictionary has 4 elements, 4 pairs of key:value or 4 keys
"""

#%%
# 5 Create a csv starting from a dictionary with csv.DictWriter()
import csv
users = [{"name": "Sol Mansi", "username": "solm", "department": "IT Infrastructure", "education": "self-taught"}, 
         {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research", "education": "bachelor"},
         {"name": "Charlie Grey", "username": "greyc", "department": "Development", "education": "master"}] # list. each list element is a dictionary. Each dictionary contains 4 elements. Each dictionary element is composed of Key:value
keys = ["name","username", "department", "education"] # list. each element list is a string. these are they only keys, no values
with open("csv1.csv", "w") as file:               # create a new csv
    writer = csv.DictWriter(file, fieldnames=keys)   # use the DictWriter to create the dictionary. Provide name of the new csv and also provide the csv fieldnames (the keys of the dictionary)
    writer.writeheader()                                # The writeheader() function takes no arguments.Creates the first row of the CSV based on the keys that we provided
    writer.writerows(users)                             # The writerows() function will transform each element of the list into a row (each element is a dictionary. The values of each dictionary will be placed in one row)

# dictionary: each element is comprised of Key-value pair.
# here I have a list with 3 elements
# each list element is a dictionary
# each dictionary contains 4 elements ( 4 pairs of Key-value)


#%%
"""
CSV Files Cheat Sheet
Check out the following links for more information:

https://docs.python.org/3/library/csv.html
https://realpython.com/python-csv/
"""
#%%
"""
3.6     Practice Quiz: Reading & Writing CSV Files
"""

"""
EXERCISE 1
We're working with a list of flowers and some information about each one. 
The "create_file" function writes this information to a CSV file. 
The "contents_of_file" function reads this file into records and returns the information in a nicely formatted block. 
Fill in the gaps of the "contents_of_file" function to turn the data in the CSV file into a dictionary using DictReader.
create a csv
with csv.DictReader() create a dictionary from the csv
"""
#%%
"""Question"""

import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  ___
    # Read the rows of the file into a dictionary
    ___
    # Process each item of the dictionary
    for ___:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))

#%%
"""Answer"""
# 6 Create a new csv by using the write() method to enter data into it
#   Display the contents of the csv by transforming it first into a dictionary with DictReader

import os
import csv

def create_csv(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# function that displays the contents of the csv as text
def display_csv_contents(filename):
  text = ""
  
# call the function that creates the new csv
  create_csv(filename)
  
# open the new csv 
  with open(filename) as file:
      reader = csv.DictReader(file) # open csv as instance, convert it to a dictionary. First csv row will become dictionary Keys. Subsequent csv rows will become dictionary values
      for row in reader: # iterate over each csv row ( row is an ordered dictionary. Alphabetical arrangement of keys)
          text += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
      return text # this is the result we want to extract from the function display_csv_contents

print(display_csv_contents("flowers.csv")) # here we call the function and also print its results by providing the argument which is also the name of the csv we want to create
  
# we create the function create_csv
# this function will create a new csv file with the write() method, based on the information we provide 
# next we create the function display_csv_contents with the purpose to create a text depicting the csv contents
# initially the text is empty
# then inside the function display_csv_contents, I call the function create_csv which produces the new csv
# I open the new csv as reader instance with dictreader. dictreader creates a dictionary
# I iterate over the reader rows. Each reader row is an ordered dictionary 
# OrderedDict(contains 3 elements(pairs Key-value). One csv row corresponds to one OrderedDict
# I attach the iterations results on the empty text string. Way of iteration n=n+1 (attach each iteration result to the previous one. I use new line character for each result)
# The value I want to extract from the function display_csv_contents, is the "text"
# finally I call the function display_csv_contents by providing the argument "flowers.csv" and print it too
# at the same time that I am calling the function display_csv_contents, I also call the function create_csv that creates the csv on which I will work on with the function display_csv_contents


#%%
"""
EXERCISE 2
Using the CSV file of flowers again, 
fill in the gaps of the "contents_of_file" function to process the data 
without turning it into a dictionary. 

How do you skip over the header record with the field names?
"""
#%%
"""Question"""
import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  ___
    # Read the rows of the file
    rows = ___
    # Process each row
    for row in rows:
      ___ = row
      # Format the return string for data rows only

          return_string += "a {} {} is {}\n".format(___)
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))




#%%
"""Answer"""
# 7 Create a new csv by using the write() method to enter data into it
#   Display the contents of the csv by using the reader() 
#  be careful to not print the first csv row that contains the Keys!

def create_csv(filename):
  with open(filename, "w") as file:
    file.write("color,name,flowertype\n")
    file.write("pink,carnation,annual\n")
    file.write("yellow,daffodil,perennial\n")
    file.write("blue,iris,perennial\n")
    file.write("red,poinsettia,perennial\n")
    file.write("yellow,sunflower,annual\n")

def display_csv_contents(filename):
  text = ""
  
  create_csv(filename)
  
  with open(filename) as file:
      reader = csv.reader(file)
      next(reader, None)
      for row in reader:
          color, name, flowertype = row
          text += "a {} {} is {}\n".format(color, name, flowertype)
      return text
  
print(display_csv_contents("flowers.csv"))

          
# we create the function create_csv
# this function will create a new csv file with the write() method, based on the information we provide 
# next we create the function display_csv_contents with the purpose to create a text depicting the csv contents
# initially the text is empty
# then inside the function display_csv_contents, I call the function create_csv which produces the new csv
# I open the new csv as reader instance with csv.reader()   
# each reader row (corresponds to a csv row) and it is a list (elements of the list are the contents of each csv field)
# I use the next(reader, None) in order to ignore the first row of the csv which contains the Keys/Titles of columns-csv fields
# I iterate over the reader rows
# I attach the iterations results on the empty text string. Way of iteration n=n+1 (attach each iteration result to the previous one. I use new line character for each result)
# The value I want to extract from the function display_csv_contents, is the "text"
# finally I call the function display_csv_contents by providing the argument "flowers.csv" and print it too
# at the same time that I am calling the function display_csv_contents, I also call the function create_csv that creates the csv on which I will work on with the function display_csv_contents

# In exercise 6 I created a dictionary from the csv(csv.DictReader) and iterated over the dictionary to construct the text
# In exercise 7 I created list from the csv (csv.reader) and iterated over the list to construct the text
# I changed the sequence of the arguments within the write() method   

#%%
"""
# 8
exercise 3
In order to use the writerows() function of DictWriter() to write a list of dictionaries to each line of a CSV file, what steps should we take? 

answer
-create an instance of the DictWriter() class 
(We have to create a DictWriter() object instance to work with, and pass to it the fieldnames parameter defined as a list of keys.)

-write the fieldnames parameter into the first row, using writeheader()
(The non-optional fieldnames parameter list values should be written to the first row.)

-open the csv file using: with open
(The CSV file has to be open before we can write to it.)
"""
#%%
"""
exercise 4
Which of the following is true about unpacking values into variables when reading rows of a CSV file? (Check all that apply)

- we need the same amount of Variables as there are columns of data in the csv
(We need to have the exact same amount of variables on the left side of the equals sign as the length of the sequence on the right side when unpacking rows into individual variables.)

- rows of a csv can be read using both a csv.reader() and a csv.DictReader()
(Although they read the CSV rows into different datatypes, both csv.reader or csv.DictReader can be used to parse CSV files.)

- an instance of the reader class must be created first
(We have to create an instance of the reader class we are using before we can parse the CSV file.)
"""
#%%
"""
exercise 5
If we are analyzing a file's contents to correctly structure its data, what action are we performing on the file?
Parsing
Parsing a file means analyzing its contents to correctly structure the data. As long as we know what the data is, we can organize it in a way our script can use effectively.
"""

#%%
"""
SYNOPSIS


csv.reader()	converts a csv into a list
    			each row of the csv becomes a list
                if we have 4 fields in the csv, then we have 4 elements in the list
                csv rows = lists
                csv fields in each row = elements of the list

csv.writer()	converts a list into a csv
    			each element of the list becomes a row in the csv


csv.DictReader()	converts a csv into a dictionary (with keys and values)
        			first row of csv provides the keys
        			following rows of csv provide the values for the keys
                    if we have 4 rows in the csv, then we get 3 dictionaries

csv.DictWriter()	converts a dictionary into a csv
        			first row of csv contains the Keys
        			subsequent rows of csv contain the Values
        			if we have 3 dictionaries, we get 4 rows

CSV  and LIST
csv row = list
csv field = list element

CSV and DICTIONARY
csv first row = dictionary Keys
csv subsequent rows = dictionary values
"""
