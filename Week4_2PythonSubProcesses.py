#%%
"""
Using Python to interact with the operating system, by Google

WEEK 4 – Managing Data and Processes

2 - PYTHON SUB-PROCESSES

2.1 Running system commands in Python
2.2 Obtaining the output of a System Command
2.3 Advanced Sub-Process management
2.4 Python Sub-processes Cheat-Sheet
2.5 Practice Quiz

"""
#%%
"""
2.1 Running system commands in Python

Until now,we have used file objects to read the contents of files
eg SAQ tool module to check if the disk is full
eg sys module to process standard input, get parameters, or generate an exit code
eg the ping command, to send ICMP packets to a host to check if it's responding

Now we will use a system command, as part of our Python script, to accomplish a task
    The subprocess module of Python, has functions that allow system commands to be executed in Python scripts


return code is the exit status? 0 for successful completion and different than zero for un-successful completion
"""

import subprocess
subprocess.run(['date'])

# this does not work here unfortunately
# I get a big message and File Not Found Error
#
"""
INCORPORATE THE DATE COMMAND IN A PYTHON SCRIPT
USING THE SUBPROCESS MODULE

import subprocess
subprocess.run(["date"])

output is:
Tue 07 Jan 2020 02:34:44 PM PST
CompletedProcess(args=['date'], returncode=0)

Notes:
we import the subprocess module
we use the subprocess.run function (should I say method?) to call the date command
the date command shows the current date
the run function  returns an object of the CompletedProcess type
This object includes information related to the execution of the command. 
From the information that got printed we can see that the returncode of the command was 0 (so the system command "date" was executed successfully)

parent process is our python script?
child process is the system command date?

a secondary enviroνment is created for the child process

while the child process works, the parent process is blocked and cannot work.
when the system command is completed, the child process exits, and flow of control returns to the parent process.
then the python script can continue.

"""
#%%
"""
INCORPORATE THE SLEEP COMMAND IN A PYTHON SCRIPT
USING THE SUBPROCESS MODULE


sleep command
waits for a number of seconds that we tell it, before returning
"""
import subprocess
subprocess.run(['sleep', '2'])

# this does not work here unfortunately
# I get a big message and File Not Found Error

"""
import subprocess
subprocess.run(['sleep', '2'])

output is:
CompletedProcess(args=['sleep', '2'], returncode=0) 

Notes:
we import the subprocess module
we use the subprocess.run function to call the sleep command
the subprocess.run function receives a list (specifically a list of strings)
the list contains, first the name of the command and then any other parameters that we want to pass to that command
so, the list elements after the command name are command-line arguments
(so, the arguments after the name of the command refer to the command?)
In this case, we're requesting sleep to wait for two seconds
    
The command was executed successfully (return code=0)  
    
    
"""

#%%
"""
INCORPORATE THE LS COMMAND IN A PYTHON SCRIPT
USING THE SUBPROCESS MODULE

ls command
lists the files and folders in the current directory 

import subprocess
result = subprocess.run(["ls", "this_file_does_not_exist"]) # list of strings, 1st element or argument is the name of the command
                                                            # 2nd element or argument is the name of the file 

The output is:
ls: cannot access 'this_file_does_not_exist' : No such file or directory

print(result.returncode) # here we apply the return code method on the result and order its display

The output is:
2

Notes:
we tried to use the ls command to list a file that does not exist
so the child process did not get executed
so the return code is 2 (different than zero)
"""
#%%
"""
2.2 Obtaining the output of a System Command

If we want our Python scripts to manipulate 
the output of system command that we're executing, we need to tell the run function to capture it for us. 

This might be helpful when we need to extract information from a command and then use it for something else in our script. 

who command
prints the users currently logged into a computer

so, we have the who command inside a python script
the python script uses the output of the who command to make a list of the users that logged in into a computer

to do that, we will use a parameter capture_output
we will set this parameter to true, when calling the run function

host command
converts a host name to an IP address and vice versa

Heads up! 
This example uses the capture_output parameter of subprocess.run, which was introduced in Python 3.7. 
Please make sure you are running Python 3.7 or later to follow along
"""
#%%
"""
EXAMPLE

import subprocess
result = subprocess.run(["host", "8.8.8.8."], capture_output=True) # the result variable is a completed process instance that we can access
print(result.returncode) # here we check the return code attribute

output is:
0

print(result.stdout) # here we print and operate with the output generated by the command

Output is:
b'8.8.8.8. in-addr .arpa domain name pointer dns.google.\n'



Notes
we use the subprocess module to use the host command in a python script
with the run method of the subprocess module we execute the host command (we tell it to work)
the subprocess.run() takes a list as a parameter
the host command converts an IP address into a host name and vice-versa
we also pass the parameter "capture output=True"  and store the result in a variable so that we can access it

we examine if the host command was executed successfully by using the result.returncode, we get a 0 so it works
we print it to see it in the display

then on the result we apply stdout (.stdout method?)
stdout is a channel between 1)a program and 2)a target of output-a display
STDOUT generally takes the form of text displayed in a terminal
when we use the print function to display information to the screen, we use the STDOUT channel

with stdout applied, we get a b in the beginning of the string
that b tells us that this string is not a proper string for Python. 
It's actually an array of bytes.
1 byte=256 characters
to cover the thousands of characters (e.g. Chinese has 10.000 characters!), we use a type of encoding called character encoding 
Character encodings: 
    -they indicate which sequence of bytes represent which characters
    - encodes characters as bytes.
    - computers only recognize binary data so text must be represented in a binary form. 
    This is accomplished by converting each character (which includes letters, numbers, symbols, and spaces) 
    into a binary code.
    binary code uses only 0 and 1
    Nowadays, most people use UTF-8 encoding, which is part of the Unicode standard that lists all the possible characters that can be represented. 

In our example when we execute the command using run, Python doesn't know which encoding to use to process the output of the command
So Python simply represents the output of the command as a series of bytes
If we want this series of bytes to become a proper string, we can call the DECODE METHOD

DECODE METHOD
This method applies an encoding to transform the bytes into a string. 
By default, it uses a UTF-8 encoding which is what we want. 
So with all that said, let's transform our array of bytes into a string and then split it into several pieces.

import subprocess
result = subprocess.run(["host", "8.8.8.8."], capture_output=True) # the result variable is a completed process instance that we can access
print(result.returncode) # here we check the return code attribute

output is:
0

print(result.stdout) # here we print and operate with the output generated by the command

Output is:
b'8.8.8.8. in-addr .arpa domain name pointer dns.google.\n'

print(result.stdout.decode().split())

Output is:
['8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'dns.google.']

So, now we have applied the decode() method, to the output of the host command,
and we transformed the bytes into a string which we splitted too


Now we can do what we like with the list of strings:)
    For example, we can choose to keep the last element of the list, which is the name that corresponds to the IP that we're looking for
"""
#%%
"""
Above we studied the captured standard output
Now lets study the standard error

import subprocess
result= subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)

the Output is:
1

Notes:
So, we get a 1, so the execution of the command rm failed

 Now, let's check the contents of the stdout and stderr attributes


import subprocess
result= subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)

the Output is:
1

print(result.stdout)
output is:
    b''
print(result.stderr)
output is:
    b"rm: cannot remove 'does_not_exist': No such file or directory\n"
    
Notes:
So we see that the output when applying stdout, is empty
But, the output when applying stderr, is the description of an error!
This is a great example of how standard output and standard error are actually different streams

SUMMARY
we can execute system commands from Python
then we can check whether they succeeded or failed
and we can obtain the output of the system command that was executed inside a Python script

we can capture the standard output(stdout) stream
we can capture the standard error(stderr) stream
"""
#%%
"""
2.3 Advanced Sub-Process management

In the following example we again have a system command inside a python script
Now we will modify the environment that the command "sees"
"""

LINUX OS (available remotely and provided by the course)
$ atom myapp.py  

The Output is:
import os
import subprocess
my_env= os.environ.copy()
my_env["PATH"] = os.pathsep.join(["opt/myapp/", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env)
"""
Notes:
we launch atom editor in the command line by typing atom
we open the python script "myapp.py" with the atom editor

we import the os module that allows us to interact with the operating system(in this case linux)
The OS module in python provides functions for interacting with the operating system.
we import the subprocess module that allows us to use a system command inside a python script

"my_env" is the new environment that we want the command to "see" Question: which exactly is the system command? Is the command called "myapp" and it is inside the python script "myapp.py"?
we want to modify the environment that the child process (system command) sees
ofcourse, we will not modify the original environment, instead we will copy it and then modify the copy


The os.environ in Python, is a mapping object that represents the user’s environmental variables.
It returns a dictionary having user’s environmental variable as key and their values as value.
The OS environ dictionary contains the current environment variables
The os.environ behaves like a python dictionary, so all the common dictionary operations like get and set can be performed.
The os.environ is a non-callable object so it accepts no parameters
By applying .copy() to the os.environ dictionary we create a new dictionary
The change that we're doing in this script is adding one extra directory to the path variable in the new dictionary ofcourse
Remember that the PATH Variable indicates where the operating system will look for the executable programs
By adding one entry to the path, we're telling the OS to look for programs in an additional location
my_env is the dictionary and ["PATH"] is the Key, with = we define the Value for that Key!

The "os.pathsep.join" adds the directory "opt/myapp/" to the existing path variable "PATH"
It takes 2 arguments as it seems, the new directory and the path variable

Then we define the Variable result, and as a value for that Variable we state that:
    it is the product of applying the subprocess.run() method (the subprocess.run runs the system command?!)
    the subprocess.run() method takes 2 arguments*
    we are calling the myapp command (which we have added in the path variable in a previous step?)
    also, we define/set the end parameter to the new environment that we've just prepared. 

* The Subprocess.run Method
The Subprocess.run method takes a list of arguments. 
When the method is called, it executes the command and waits for the process to finish, returning a “CompletedProcess” object in the end. 
The “CompletedProcess” object returns stdout, stderr, original arguments used while calling the method, and a return code. 
Stdout refers to the data stream produced by the command, while stderr refers to any errors raised during execution of the program. 
Any non-zero return code (exit code) would mean error with the command executed in the subprocess.run method.

So to recap, this script is modifying the contents of the path environment variable by adding a directory to it.

"""

"""
2.4 Python Sub-processes Cheat-Sheet

https://docs.python.org/3/library/subprocess.html
subprocess.run(args,
               *, 
               stdin=None, 
               input=None,
               stdout=None,
               stderr=None,
               capture_output=False,
               shell=False,
               cwd=None,
               timeout=None,
               check=False,
               encoding=None,
               errors=None,
               text=None,
               env=None,
               universal_newlines=None,
               **other_popen_kwargs)¶
"""
#%%
"""
2.5 Practice Quiz


Question 1
What type of object does a run function return?

CompletedProcess correct? yes. This object includes information related to the execution of a command.
capture_output
stdout
returncode

Question 2
How can you change the current working directory where a command will be executed?

Use the capture_output parameter.
Use the env parameter. correct?NO. This will define the environment for which the command will operate.
Use the cwd parameter.correct?
Use the shell parameter.

3.
Question 3
When a child process is run using the subprocess module, which of the following are true? (check all that apply)

The child process is run in a secondary environment. correct?
The parent process is blocked while the child process finishes. correct?YES. While the parent process is waiting on the subprocess to finish, it’s blocked, meaning the parent can’t do any work until the child finishes.
The parent process and child process both run simultaneously.
Control is returned to the parent process when the child process ends. correct?YES.After the external command completes its work, the child process exits, and the flow of control returns to the parent.

4.
Question 4
When using the run command of the subprocess module, what parameter, when set to True, allows us to store the output of a system command?

cwd
capture_output correct?YES. The capture_output parameter allows us to get and store the output of the system command we're using.
timeout
shell

5.
Question 5
What does the copy method of os.environ do?

Creates a new dictionary of environment variables correct?YES.  The copy method of os.environ makes a new copy of the dictionary containing the environment variables, making modification easier.
Runs a second instance of an environment
Joins two strings
Removes a file from a directory











"""
