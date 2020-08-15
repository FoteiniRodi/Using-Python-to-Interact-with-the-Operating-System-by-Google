#%%
"""
Using Python to interact with the operating system, by Google

WEEK 4 – Managing Data and Processes

3       PROCESSING LOG FILES
3.1     What are log files?
3.2     Filtering log files with Regular Expressions
3.3     Making sense out of the data
3.4     Practice quiz

"""

#%%
"""
3.1     What are log files?
log file =  αρχείο καταγραφής, ημερολόγιο
            Τα .log αρχεία μπορούν να ανοίξουν με το Σημειωματάριο (Notepad).
log file is like keeping a calendar of events (date, time, category of event, short description of event, location of event)
"""
#%%
"""
3.2     Filtering log files with Regular Expressions

When working with log files and scripts, 
our first step is usually to open the log files so our code written in the script, can access the contents of the log file.

Usually, in order to open a file, we use the open function,
the open function returns a file object, and then we iterate through each of its lines using a for-loop to locate something


"""
"""
example 1
LINUX OS
#!USR/BIN/ENV PYTHON 3

import sys
logfile = sys.argv[1]
with open(logfile) as f:
    for line in f:
        print(line.strip())
        
contents of the log file "syslog" are below:
    Jul 6 14:01:23 computer.name CRON[29440]: USER (good user)
    Jul 6 14:02:08 computer.name jam_tag=psin[29187]: (UUID:006)
    Jul 6 14:02:09 computer.name jam_tag=psin[29187]: (UUID:006)
    Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty user)
    Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from "0xDEADBEEF"
    Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty user)
    Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty user)

I created the log file by writing the contents in the Notepad      

I can see the contents of the log file with the command
$ cat syslog

The server that generates this log file has been acting strangely and we suspect it's due to a Cron job started by one of the system administrators    
Cron jobs are used to schedule scripts on UNIX-based operating systems
we want to audit the log files and see exactly who's been launching CRON jobs
the lines of the log file that are interesting to us, are the ones that contain the Cron substring
These lines also show the user who started the Cron job wrapped in parentheses
With this info, we can ignore any line without the Cron substring in it

LINUX OS
#!USR/BIN/ENV PYTHON 3

import sys
logfile = sys.argv[1]
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue            #* the "continue" keyword, tells our loop to go to the next element
        print(line.strip())

*So if the line doesn't contain the string "CRON" we'll skip it and go to the next line

Now we can use our knowledge of REGULAR EXPRESSIONS to extract the username
In this example, we'll use:
    -escape characters, 
    -capture groups, and 
    -the end of string anchor (dollar sign $)
Before we add the expression to our script, we'll construct it and test it out in an INTERPRETER.

Interpreter:
import re
pattern = r"USER \((\w+)\)$"

pattern explanation
we know already that the username we are looking for is at the end of the string and also it is enclosed in parentheses.
so:
    we look for the word USER followed by a string wrapped in parentheses 
    we need to escape those parentheses with a backslash (actually we "escape", we ignore 2 parentheses)
    then we use a pair of parentheses because we want to use a capturing group
    \w+             finds sequence of alphanumeric characters separated by whitespace       SPECIAL SEQUENCE
    \w+ with findall(), returns all matches as 
    words with letters, words with letters and numbers, words with letters and numbers and underscores, numbers, underscores that were divided by a space in the text
    see Week 3 Advanced Regular expressions to read about capturing groups!
    finally we use $, to look for a string that is in the end of the line ('ends with'"$)

CAPTURING GROUPS ARE USED FOR EXTRACTION
    here we want to extract the username
    
Interpreter:
import re
pattern = r"USER \((\w+)\)$"
line = "Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)"
result = re.search(pattern, line)
print(result[1]) # this is where the Capturing Group is used, to extract

The Output is: naughty_user
"""
#%%
"""
example 2
WINDOWS OS, Spyder


"""
import sys
with open("syslog.log") as f:
    for line in f:
        if "CRON" not in line:
            continue            #* the "continue" keyword, tells our loop to go to the next element
        print(line.strip())

# the output is:
#Jul 6 14:01:23 computer.name CRON[29440]: USER (good user)
#Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)
#Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)
#Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)
#%%
"""
example 3
testing the regex in WINDOWS OS, Spyder

"""
import re
x = re.search(r"USER \((\w+)\)$", "Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)") 
print(x[1])

# the output is: good_user
# syntax is (r"pattern", "text")


import re
x = re.search(r"USER \((\w+)\)$", "Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)") 
print(x[1])

# the output is:naughty_user
#%%
"""
example 4
the regex works, so we will add it to our script from example 2

"""
import re
import sys
with open("syslog.log") as f:
    for line in f:
        if "CRON" not in line:
            continue            #* the "continue" keyword, tells our loop to go to the next element
        x = re.search(r"USER \((\w+)\)$", line)
        print(x[1])

#%%
"""
in video question
We're using the same syslog, and we want to display
the date, time, and process id that's inside the square brackets. 
We can read each line of the syslog and pass the contents to the show_time_of_pid function*. 
 
Fill in the gaps to extract the date, time, and process id from the passed line, 
and return this format: Jul 6 14:01:23 pid:29440.

so we have all the lines and we are not reading the log file, no need to use a for loop.
we have to define a regex with 2 capturing groups, one will be date and time and second will be the number inside the brackets

"""

import re
def show_time_of_pid(line):
  pattern = r"([a-zA-Z]+ \d+ \d+:\d+:\d+).*\[(\d+)\]"
  result = re.search(pattern, line)
  return "{} pid:{}".format(result[1], result[2])

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440


# PATTERN EXPLANATION
#first parenthesis-capturing group
#[a-zA-Z] : find only the letters in the text
#space
#\d is a special sequence, finds numbers 0-9
#\d+ special sequence with repeating qualifier + which finds one or more repetitions of numbers from 0-9
#\d+, finds the number after Jul
#space
#\d+:\d+:\d+, find 3 consecutive numbers separated by :

# between the two parentheses
# .* Dot is any character except \n newline character, and star states that all characters/patterns before the star must be searched in the text
# in other words we tell the regex to find everything:)

# then escape/ignore the 1st square bracket

#second parenthesis
# \d+, finds one or more repetitions of numbers from 0-9

# then escape/ignore the 2nd square bracket

# then escape/ignore the colon? by using \:
# We can use \ to escape any special characters
# escape = the characters lose their special character meaning and become simple characters


#%%
"""
3.3     Making sense out of the data
see example 4 please
previously we wrote a python script that examined a log file and extracted the username associated with the string cron.
now we want to see how many times does a username associated with the string cron, appears in the results
we will ofcourse use a dictionary
the Key will be the username and the Value will be the number of times that the username appears in the results.
we will also use the get() method

we will find out which usernames start cron jobs in the server and at what frequency
"""
"""
example 5
this python scripts examines the log file syslog 
it finds good_user one time and naughty)_user 3 times
"""
import re
import sys
with open("syslog.log") as f:
    for line in f:
        if "CRON" not in line:
            continue            #* the "continue" keyword, tells our loop to go to the next element
        x = re.search(r"USER \((\w+)\)$", line)
        print(x[1])

# output is
#good_user
#naughty_user
#naughty_user
#naughty_user

#%%
 """
 example 6
 we write the following to create a dictionary
 then we will add these lines of script to the script of example 4
 """
usernames = {} # here we create an empty dictionary
name = "good_user" # here we create the Variable "name" and provide the Value "good_user" for it
usernames[name] = usernames.get(name, 0) +1
print(usernames)

# output is {'good_user': 1}, Key = usernames[name] = "good_user" and Value = usernames.get(name, 0) +1 = 0+1 = 1
# dictionary was empty and we added to it the key-Value pair 'good_user': 1
usernames[name] = usernames.get(name, 0) +1
print(usernames)

# output is {'good_user': 2}, Key = usernames[name] = "good_user" and Value = usernames.get(name, 0) +1 = 0+1+1 = 2
# dictionary already contained the key-Value pair 'good_user': 1, and we added to it another key-Value pair 'good_user': 1
# so the result now is 'good_user': 2
"""
Notes
1st line
create empty dictionary
2nd line
create Variable "name" with Value "good_user"
3rd line
create a Value for the Key
Key is the username 
Value is the number of times that the username appears
usernames[name], is the Key of the dictionary "usernames"
    -How can we create a dictionary from scratch?
    first create empty dictionary
    then, assign values to keys this way: dictionary[key] = value

The get() method returns the value of the item with the specified key.
Syntax of the get() method:
    dictionary.get(keyname, value)
    keyname:	Required. The keyname of the item you want to return the value from
    value:  	Optional. A value to return if the specified key DOES NOT exist.
    Default value None
we'll set the value associated with the key as one more than the current value (+1)
we'll use the get method to get the current value
at 1st execution, the Key good_user does not exist in the dictionary 
    dictionary was empty and we added to it the key-Value pair 'good_user': 1
at 2nd execution, the Key good_user exists in the dictionary with a Value of 1
    we add to this dictionary another key-Value pair 'good_user': 1 and the result now is 'good_user': 2, same Key different Value
"""


#%%
"""
example 7
to the script of example 4 we add the script of example 6
so we not only find the username but also the count of the username
"""
import re
import sys
usernames = {}
with open("syslog.log") as f:
    for line in f:
        if "CRON" not in line:
            continue            #* the "continue" keyword, tells our loop to go to the next element
        x = re.search(r"USER \((\w+)\)$", line)
        if x is None: # see Note below
            continue
        name = x[1] # see Note below
        usernames[name] = usernames.get(name, 0) +1
print(usernames)

# output is {'good_user': 1, 'naughty_user': 3}

"""
Note
before we add any values to the dictionary, we want to check that we actually got a match to our regular expression.
if the regex we wrote does not find a match (None) then continue to the next line of the log file

for the Variable "name" we define that its Value will be the captured group of the regex, which is the username
"""

#%%
"""
3.4     Practice quiz

1.
Question 1
You have created a Python script to read a log of users running CRON jobs. The script needs to accept a command line argument for the path to the log file. Which line of code accomplishes this?

import sys
syslog=sys.argv[1] correct? YES, This will assign the script's first command line argument to the variable "syslog".
print(line.strip())
usernames = {}

2.
Question 2
Which of the following is a data structure that can be used to count how many times a specific error appears in a log?


Search
Continue
Get
Dictionary correct?YES, A dictionary is useful to count appearances of strings.

3.
Question 3
Which keyword will return control back to the top of a loop when iterating through logs?


Continue correct?YES The continue statement is used to return control back to the top of a loop.
Get
With
Search

4.
Question 4
When searching log files using regex, 
which regex statement will search for the alphanumeric word "IP" followed by one or more digits wrapped in parentheses using a capturing group?

r"IP \(\d+\)$"
b"IP \((\w+)\)$"
r"IP \((\d+)\)$" correct?YES  This expression will search for the word "IP" followed by a space and parentheses. It uses a capture group and \d+ to capture any digit characters found in the parentheses.
r"IP \((\D+)\)$" 

5.
Question 5
Which of the following are true about parsing log files? (Select all that apply.)

Load the entire log files into memory.
You should parse log files line by line. correct? YES Since log files can get pretty large, it's a good idea to parse them one line at a time instead of loading the entire file into memory at once.
It is efficient to ignore lines that don't contain the information we need. correct? YES, We can save a lot of time by not parsing lines that don't contain what we need.
We have to open() the log files first. correct? YES Before we can parse our log file, we have to use the open() or with open() command on the file first.




Parsing a file means analyzing its content to correctly structure the data. 

"""

