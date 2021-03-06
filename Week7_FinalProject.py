#%%
"""
WRITING A SCRIPT FROM THE GROUND UP
Steps for coding projects

1.Understand the problem statement
Define what needs to be done
Identify what the given inputs and desired outputs are for that program that we need to write.

2.Research (researching available tools)
Do research on the Python standard library or external modules. 
Remember, we want to avoid reinventing the wheel. 
Most probably others have solved something similar before. 
It is essential to find what resources already exist to help us solve our problem. 
Study the documentation of the modules, classes, and functions that we'll need to use, and their application.
The documentation also includes examples. 
Study these examples and see how they relate to the code that we need to write.

3.Planning (writing a design document)
Once we know what we need to write and what tools we can use to make it work, we should do some planning. 
This means thinking about what data types are useful for our solution, the order of operations that we need to perform, 
and how all the pieces have come together to form our solution. 
Synergy. 
If the problem is complex, it might help to write down the plan for quick reference,
 either on a piece of paper or in a digital document. 
 Writing down the plan helps us focus on how we're going to do things and identify any problems our plan might have. 
 At many companies, it's a common practice to write a design document at this stage, detailing the problem statement, 
 the tools that will be used to solve it, and the plan of attack towards a solution. 
 Having others comment on your design helps make sure that all the twists have been untangled.
 
3. Writing the script 
This step includes not only writing the code, but also checking that the code does what it's supposed to do. 
We do that by both manually testing the code and adding some automatic test. 

Sometimes, it's tempting to just jump right into the coding stage, 
without spending any necessary time to fully understand the problem, research tools, or plan the solution. 
But our experience shows us spending a while getting familiar with what we're trying to do 
and what tools we have available to do it can make a big difference.

My synopsis
1. define the problem
2. find appropriate tools to solve it, find similar work done by others in the past
3. write down a plan, a "design document" with the methodology we will use. Have it reviewed by others
4. write the script, test it to make sure it produces the expected results

PROJECT PROBLEM STATEMENT

One of the servers used by your company runs a service called "ticky". 
This service is an internal ticketing system used by a lot of different teams in the company to manage their work. 
The service logs/records a bunch of events to syslog, both when it runs successfully and when it encounters errors. 

Developers of the service are asking for your help with getting some information out of those logs, 
to better understand how the software is being used and how to improve it. 

You'll write some automation scripts that will process the system log and generate a bunch of reports 
    based on the information extracted from log files. 
    The log lines follow a pattern similar to the ones we've seen before. Something like this.
    
    example of log files:
    May 2 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)
    Jun 1 11:06:48 ubuntu.local ticky: ERROR: Connection to DB failed (username)

When the service runs correctly, 
    it logs an info message to syslog, stating what it's done, the username, and the ticket number related to the event.
When the service encounters a problem, 
    it logs in error message to the syslog, indicating what was wrong and the username that triggered the action that caused the problem. 

The developers of the service want two different reports out of this data. 
    1)The first one is a ranking of errors generated by the system. 
    This means a list of all error messages logged, and how many times each of them was found, 
    not taking into account the users involved. 
    They should be sorted by the most common error to the least common error. 
    2)The second one is a usage statistics for the service. 
    This means, a list of all users that have used the system including how many info messages and 
    how many error messages they've generated. 
    This report should be sorted by username. 
    
To visualize the data in these reports, you want to generate a couple of webpages that'll be served by a web server 
    running on the machine. 
    To do this, you can make use of a script that's already in the system called csv_ to_html.py. 
    This script converts the data in a CSV file into an HTML file containing a table with the data. 
    
Then, put the files in the directory that's used by the webserver to display the webpages. 
The goal is to have one script that can get all the necessary work done automatically, 
    every day without any user interaction. 
This script doesn't need to do all the work itself. 
It can call on other scripts to do individual task and then put the results together. 
In fact, we recommend splitting the task so that each piece can be written and tested separately. 

system log file = syslog
In computing, a log file is a file that records either events that occur in an operating system or other software runs,
 or messages between different users of a communication software. 
Logging is the act of keeping a log. In the simplest case, messages are written to a single log file.
Logging = recording, diary of events


HELP WITH RESEARCH AND PLANNING

We want to find some specific log lines in the sys log file. 
We strongly recommend that you use regular expressions to find them. 
It'll be easier to extract information you want that way. 
To find the regular expression, you can use a website like regex101.com which can help you test your expression. 
Once you have a regex pattern that you think it works, try it out in a Python interpreter 
to verify that it matches the right lines and captures the right information. 

Afterwards, count how many errors are of the same type (one dictionary, sorted from most repeated error to least repeated error)
            count how many info and error messages there are for a given user (2 dictionaries, one for info one for error, sorted by user) 
            Use dictionaries to count.
            Find info on how to sort a dictionary at the "Crash course"

 The output of your Python script should be a couple of CSV files.
 Each of them containing the names of the columns and the data in the order that it needs to be presented. 
 
 Once those files are generated, you'll need to call the CSV html.py script to create HTML files based on CSV data. 
 You'll have access to look at how the script works but the key is to pass two parameters to it. 
 The name of the CSV file to read and the name of the HTML file to be generated. 
 You could do this last step from either a Python script or a bash script. 
 Since the script will be only calling commands and moving files, we recommend doing a bash. 



Synopsis
find certain log lines by using regex
construct dictionaries
convert dictionaries to csv
convert csv to html files

"""

#%%
"""
HOW TO SORT (from Python Crash course)
sort from smallest to largest integer
sort alphabetically
"""
numbers = [4,6,2,7,1] # list
numbers.sort()
print(numbers)
# Output is also a list, [1, 2, 4, 6, 7]

names = ["Carlos", "Ray", "Alex", "Kelly"]
print(names)
# Output is also a list, ['Carlos', 'Ray', 'Alex', 'Kelly']
print(sorted(names))
# Output is also a list, ['Alex', 'Carlos', 'Kelly', 'Ray']

#%%
"""
Qwiklabs
Log Analysis Using Regular Expressions

<<INTRODUCTION>>

Imagine your company uses a server that runs a service called ticky, an internal ticketing system. 
The service logs events to syslog, both when it runs successfully and when it encounters errors.

The service's developers need your help getting some information from those logs 
so that they can better understand how their software is used and how to improve it. 

So, for this lab, you'll write some automation scripts that will process the system log and
 generate reports based on the information extracted from the log files.

What you'll do
Use regex to parse a log file
Append and modify values in a dictionary
Write to a file in CSV format
Move files to the appropriate directory for use with the CSV->HTML converter



<<EXERCISE - 1>> this can be skipped, it is only for practice

We'll be working with a log file named syslog.log, which contains logs related to ticky.

cat syslog.log # display contents of the file "syslog.log"

The log lines follow a pattern similar to the ones we've seen before. Something like this:
May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)
Jun 1 11:06:48 ubuntu.local ticky: ERROR: Connection to DB failed (username)

When the service runs correctly, it logs an INFO message to syslog. 
It then states what it did and states the username and ticket number related to the event. 
If the service encounters a problem, it logs an ERROR message to syslog. 
This error message indicates what was wrong and states the username that triggered the action that caused the problem.

In this section, we'll search and view different types of error messages. 
The error messages for ticky, details the problems with the file with a timestamp for when each problem occurred.

These are a few kinds of listed error:

Timeout while retrieving information
The ticket was modified while updating
Connection to DB failed
Tried to add information to a closed ticket
Permission denied while closing ticket
Ticket doesn't exist

grep ticky syslog.log # with grep we search for the text "ticky" on all log lines. 
                        Output is all log lines containing "ticky"

grep "ERROR" syslog.log # with grep we search for the text "ERROR" on all log lines.
                            Output is all log lines containing "ERROR"
                            
grep "ERROR Tried to add information to closed ticket" syslog.log # this searches for a specific error!
                                                                    To enlist all the ERROR messages of specific kind use the below syntax.
                                                                    Syntax: grep ERROR [message] [file-name]
                                                                    
python3                                     # open a Python shell
import re                                   # import regex module
line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
re.search(r"ticky: INFO: ([\w ]*) ", line) # To match a string stored in line variable, we use the search() method by defining a pattern.
                                           # string we are looking for is "ticky: INFO: ([\w ]*) "
                                           # GET ALL LOG LINES CONTAINING INFO
Output is:
<_sre.SRE_Match object; span=(29, 57), match='ticky: INFO: Created ticket '>

line = "May 27 11:45:40 ubuntu.local ticky: ERROR: Error creating ticket [#1234] (username)"
re.search(r"ticky: ERROR: ([\w ]*) ", line) # # GET ALL LOG LINES CONTAINING ERROR
Output is:
<_sre.SRE_Match object; span=(29, 65), match='ticky: ERROR: Error creating ticket '>
"""
#%%
import re
line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
re.search(r"ticky: INFO: ([\w ]*) ", line)
# output is: Out[4]: <re.Match object; span=(29, 57), match='ticky: INFO: Created ticket '>

line = "May 27 11:45:40 ubuntu.local ticky: ERROR: Error creating ticket [#1234] (username)"
re.search(r"ticky: ERROR: ([\w ]*) ", line)
# Output is: Out[6]: <re.Match object; span=(29, 65), match='ticky: ERROR: Error creating ticket '>



#%%
"""
<<EXERCISE - 2>> this can be skipped, it is only for practice



fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2} # this is an example dictionary
sorted(fruit.items())                                         # sort the elements of the dictionary, by alphabetical order of the Keys
Output is:
[('apples', 5), ('bananas', 7), ('oranges', 3), ('pears', 2)]    

import operator #
sorted(fruit.items(), key=operator.itemgetter(0)) # sort a dictionary based on its Keys, choose argument 0 on the itemegetter()
Output is:
[('apples', 5), ('bananas', 7), ('oranges', 3), ('pears', 2)]

sorted(fruit.items(), key=operator.itemgetter(1)) # sort a dictionary based on its Values, pass the argument 1 to the itemgetter function of the operator module.
                                                  # sorts from smallest to largest
Output is:
[('pears', 2), ('oranges', 3), ('apples', 5), ('bananas', 7)]   

sorted(fruit.items(), key = operator.itemgetter(1), reverse=True) # sort dictionary Values, from largest to smallest
Output is:
[('bananas', 7), ('apples', 5), ('oranges', 3), ('pears', 2)]

exit() # exit the Python shell
"""
"""
My notes for exercise 3:
How to sort a dictionary
How to sort based on Keys
How to sort based on Values with the help of operator
(in a dictionary each element=key:Value)
"""
fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
sorted(fruit.items()) # sort aplhabetically based on keys
# Output is: Out[7]: [('apples', 5), ('bananas', 7), ('oranges', 3), ('pears', 2)]

import operator
sorted(fruit.items(), key=operator.itemgetter(0)) # sort aplhabetically based on keys
# Output is: Out[8]: [('apples', 5), ('bananas', 7), ('oranges', 3), ('pears', 2)]

import operator
sorted(fruit.items(), key=operator.itemgetter(1)) # sort based on Values, smallest to largest
# Output is: Out[9]: [('pears', 2), ('oranges', 3), ('apples', 5), ('bananas', 7)]

import operator
sorted(fruit.items(), key = operator.itemgetter(1), reverse=True) # sort based on Values, largest to smallest
# Output is:Out[10]: [('bananas', 7), ('apples', 5), ('oranges', 3), ('pears', 2)]



"""
<<EXERCISE - 3>> DO NOT SKIP THIS, IT IS ESSENTIAL, IT CREATES THE user-emails.html

We'll now work with a file named "csv_to_html.py. "
This file converts the data in a CSV file into an HTML file that contains a table with the data.

create the csv file "user_emails.csv" and convert it to an html file by using "csv_to_html.py"
 
Let's practice this with an example file "user_emails.csv"

nano user_emails.csv # open the nano editor to create the file "user_emails.csv"
Add the following data into the file:
    Full Name, Email Address
    Blossom Gill, blossom@abc.edu
    Hayes Delgado, nonummy@utnisia.com
    Petra Jones, ac@abc.edu
    Oleg Noel, noel@liberomauris.ca
    Ahmed Miller, ahmed.miller@nequenonquam.co.uk
    Macaulay Douglas, mdouglas@abc.edu
    Aurora Grant, enim.non@abc.edu
    Madison Mcintosh, mcintosh@nisiaenean.net
    Montana Powell, montanap@semmagna.org
    Rogan Robinson, rr.robinson@abc.edu
    Simon Rivera, sri@abc.edu
    Benedict Pacheco, bpacheco@abc.edu
    Maisie Hendrix, mai.hendrix@abc.edu
    Xaviera Gould, xlg@utnisia.net
    Oren Rollins, oren@semmagna.com
    Flavia Santiago, flavia@utnisia.net
    Jackson Owens, jackowens@abc.edu
    Britanni Humphrey, britanni@ut.net
    Kirk Nixon, kirknixon@abc.edu
    Bree Campbell, breee@utnisia.net

Save the file by clicking Ctrl-o, Enter key, and Ctrl-x.

sudo chmod +x csv_to_html.py # make the "csv_to_html.py" executable

sudo chmod  o+w /var/www/html # Give write permission to the directory that would host that HTML page
                              # The script csv_to_html.py takes in two arguments, the CSV file, and location that would host the HTML page generated
                              # "o+w" is the CSV file?  
                              # "/var/www/html" is the directory/location that will host the HTML page generated
                              
                              
./csv_to_html.py user_emails.csv /var/www/html/<html-filename>.html # run the script csv_to_html.py script by passing two arguments: user_emails.csv file and the path /var/www/html/. 
                                                                    # instead of <html-filename>.html please write user_emails.html !
                                                                    This should be the name that you want the HTML file to be created with.
                                                                   
ls /var/www/html     # Navigate to the /var/www/html directory. list all files in this directory
                     # Here, you'll find an HTML file created with the filename you passed to the above script.

Now, to view this HTML page, open any web-browser and enter the following URL in the search bar.
[linux-instance-external-IP]/[html-filename].html

linux-instance-external-IP is provided in the Lab
Also no need for square brackets
    Output is:
        column full name and column e-mail address
You should now be able to visualize the data within the user_emails.csv file on a webpage.
"""



"""
<<GENERATE REPORTS>>

you need to finish Exercise - 3 and name html file as "user_emails.html"
you need to name html files as "error_message.html" and "user_statistics.html"

Create the script "ticky_check.py" that will generate 2 reports
1) The ranking of errors generated by the system: 
    A list of all the error messages logged and how many times each error was found, 
    sorted by the most common error to the least common error. 
    This report doesn't take into account the users involved.
2) The user usage statistics for the service: 
    A list of all users that have used the system, including how many info messages and how many error messages 
    they've generated. 
    This report is sorted by username.

SOLUTION - attention: replace the username with the one provided by the Lab

nano ticky_check.py

#!/usr/bin/env python3
import re
import csv
import operator

error_messages = {}
per_user = {}
logfile =r"/home/<username>/syslog.log" # replace the username with the one provided by the Lab
pattern = r"(INFO|ERROR) ([\w' ]+|[\w\[\]#' ]+) (\(\w+\)|\(\w+\.\w+\))$"

with open(logfile, "r") as f:
	for line in f:
		result = re.search(pattern, line)
		if result is None:
			continue
		if result.groups()[0] == "INFO":
			category = result.groups()[0]
			message = result.groups()[1]
			name = str(result.groups()[2])[1:-1]
			if name in per_user:
				user = per_user[name]
				user[category] += 1
			else:
				per_user[name] = {'INFO':1, 'ERROR':0}
		if result.groups()[0] == "ERROR":
			category = result.groups()[0]
			message = result.groups()[1]
			name = str(result.groups()[2])[1:-1]
			error_messages[message] = error_messages.get(message, 0) + 1
			if name in per_user:
				user = per_user[name]
				user[category] += 1
			else:
				per_user[name] = {'INFO':0, 'ERROR':1}

sorted_messages = [("Error", "Count")] + sorted(error_messages.items(), key = operator.itemgetter(1), reverse=True)
#sorted_messages = [("Error", "Count")] + sorted(error_messages.items(), key = lambda x: x[1], reverse=True)
sorted_users = [("Username", "INFO", "ERROR")] + sorted(per_user.items())[0:8]
#sorted_users = [("Username", "INFO", "ERROR")] + sorted(per_user.items())

with open("error_message.csv", "w") as error_file:
	for line in sorted_messages:
		error_file.write("{}, {}\n".format(line[0], line[1]))

with open("user_statistics.csv", "w") as user_file:
	for line in sorted_users:
		if isinstance(line[1], dict):
			user_file.write("{}, {}, {}\n".format(line[0], line[1].get("INFO"), line[1].get("ERROR")))
		else:
			user_file.write("{}, {}, {}\n".format(line[0], line[1], line[2]))

Save the script (ctrl-O, enter, ctrl-x)
chmod +x ticky_check.py # make it executable
./ticky_check.py # run it
./csv_to_html.py error_message.csv /var/www/html/<html-filename>.html # convert csv to html Replace <html-filename> with the name of your choice.
                                                                      # provide the name "error_message.html"

./csv_to_html.py user_statistics.csv /var/www/html/<html-filename>.html # convert csv to html
                                                                        # provide the name "user_statistics.html"


Now, to view these HTML pages, open any web-browser and enter the following URL in the search bar.
[linux-instance-external-IP]/[html-filename].html
linux-instance-external-IP is provided in the Lab
Also no need for square brackets
"""
