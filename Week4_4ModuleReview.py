#%%
"""
Using Python to interact with the operating system, by Google

WEEK 4 – Managing Data and Processes

4 MODULE REVIEW

Introduction:
Imagine one of your colleagues is struggling with a program that keeps throwing an error. 
Unfortunately, the program's source code is too complicated to easily find the error there. 
The good news is that the program outputs a log file you can read! (the log file produced is called "errors_found")
Let's write a script to search the log file called "fishy" for the exact error, 
    then output that error into a separate file* so you can work out what's wrong.
    separate file*: it is called "errors_found.log" and it is produced by the code we will write

What you'll do:

Write a script to search the log file using regex to find for the exact error.
Report the error into a separate file so you know what's wrong for further analysis.


I created the log file "fishy.log" (wrote on the Notepad the contents and saved as .log file)
I tested on Spyder

Log entries are written in this format:
Month Day hour:minute:second mycomputername "process_name"["random 5 digit number"] "ERROR/INFO/WARN" "Error description"
"""
#%%
"""
at first I will write part of the code to produce the list "returned_errors"
this list will serve as an argument for the second function that will produce the file "errors_found.log"
"""

import sys
import os
import re

def error_search(log_file):
    error = input("What is the error? ")
    returned_errors = []
    with open(log_file, mode='r',encoding='UTF-8') as file:
        for log in  file.readlines():
            error_patterns = ["error"]
            for i in range(len(error.split(' '))):
                error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_errors.append(log)
        file.close()
    print(returned_errors)
 
error_search("fishy.log")   # here I call the function by providing the argument, the fishy log file
                            # at the prompt of the input() function I reply error, and I get a list of log lines that contain the string "error". It is only a test so I can see what is the outout until here
                            # the exercise is to reply cron, at the prompt, I will do that later on

#%%
"""
this is the complete code
it produces a new log file based on my response at the prompt
"""
import sys
import os
import re
def error_search(log_file):
    error = input("What is the error? ")
    returned_errors = []
    with open(log_file, mode='r',encoding='UTF-8') as file:
        for log in  file.readlines():
            error_patterns = ["error"]
            for i in range(len(error.split(' '))):
                error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
                if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                    returned_errors.append(log)                
        file.close()
    return returned_errors

def file_output(returned_errors):
    with open(os.path.expanduser('~') + '/errors_found.log', 'w') as file:
        for error in returned_errors:
            file.write(error)
        file.close()  

if __name__ == "__main__":
    log_file = "fishy.log"#sys.argv[1] for working on the Linux OS command line
    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0) 
    
# IT WORKS!!
# I used the fishy log file I copied from the virtual Linux OS command line (which I saw with the cat command)
# A LOG FILE CALLED errors_found WAS CREATED ON MY C: DRIVE

#%%
"""
NOTES
write a function "error_search"
 that takes log_file as a parameter and returns "returned_errors".

Define an input function to receive the type of ERROR that the end-user would like to search and
 assign its result, to a Variable named "error".
The input() function takes the input from the user and then evaluates the expression. 
This means Python automatically identifies whether the user entered a string, a number, or a list. 
If the input provided isn't correct then Python will raise either a syntax error or exception. 
The program flow will stop until the user has given an input.
the input function uses a string typed in by the user
the input function always returns a string.
here we prompt the user to tyoe-in a string and then use that string.
we save the result of the input() function in a Variable called "error"


initialize the list returned_errors 
(we create an empty list which will be populated later
This will enlist all the ERROR logs as specified by the end-user through the input function.)

open the log file "fishy", in reading mode and use 'UTF-8' encoding.

apply the method readlines() to "fishy", this will produce a list in which every element comes from a line of the log file "fishy"
The readlines() method returns a list containing each line in the file as a list item.


ALL() FUNCTION
takes an iterable object as an argument. (iterable, lists, tuples, dictionaries, sets)
if all elements in the iterable object are true, then the all() function returns True
when the element is zero, then it is considered False, and the all() function returns False
when the element is false, then it is considered False, and the all() function returns False
so: 0 is the same as False
If the iterable is empty, then the all() function also returns True
Attention: For dictionaries the all() function checks the keys, not the values.
"""
