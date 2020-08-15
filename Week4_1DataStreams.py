#%%
"""
Using Python to interact with the operating system, by Google

WEEK 4 – Managing Data and Processes

1       DATA STREAMS
1.1     Intro to Module 4: Managing Data and Processes
1.2     Reading Data Interactively
1.3     Standard Streams
1.4     Environment Variables
1.5     Command-Line Arguments and Exit Status
1.6     More about Input Functions
1.7     Practice quiz



"""
#%%
"""
1.1     Intro to Module 4: Managing Data and Processes

In this module, we'll check out concepts that help us interact with the running operating system. 
-We'll kick this off by talking about how to read user data interactively. 
-Then we'll explore the standard input and output data streams provided by the operating system and
 see how we can interact with them both from Python programs and from the system programs. 
-In a lot of our examples, we'll interact with the operating system through the command line.
 So we'll start familiarizing ourselves a bit more with the Linux shell. 
-We'll also talk about how we can execute system commands from Python. 
This allows our scripts to harness the power of the rest of the operating system. 
So it's important that we know how to manipulate the output of these commands and handle any generated errors. 
-We'll wrap up by diving into one important source of information for IT specialist, log files. 
 Now, we'll look at how we can make sense of information these log files provide by using the tools that we've learned throughout the course.

- In this module, we'll learn a lot about different ways our scripts can send and receive data
"""
#%%
"""
1.2     Reading Data Interactively

The input() function allows user input.
syntax is:  input(prompt)
The prompt is a String, representing a default message before the input
I execute the input function
I see the prompt
I respond to the prompt 
Finally, I see the whole message

the input function uses a string typed in by the user
the input function always returns a string.

This function allows us to prompt the user for a certain value that we can then use for our scripts
prompt = προτρέπω, παρακινώ
"""

name = input("Please enter your name: ") # ask the user for input, the user types in his response
print("Hello," + name) # then we use that name to print a greeting

# 1 Please enter your name:
# 2 I type in "Mary" so, "Please enter your name:" Mary
# 3 when I print "I see Hello, Mary"

#%%
"""
the input function always returns a string!
so, if we want the data that we're reading, not to be a string but a number or a date, 
then we need to convert the string to a format that we want. 
the input function always returns a string!
"""
def to_seconds(hours, minutes, seconds): # here we define a function that converts hours, minutes and seconds into SECONDS
    return hours*3600+minutes*60+seconds # 1 hour=3.600 seconds, 1 minute =60 seconds, 1 second =1 second. SYNTAX: return expression
print("welcome to this time converter")

cont = "y" # here I define the Variable cont. Also its value which is y ( We INITIALIZE THE VARIABLE cont)
while(cont.lower() == "y"): # while condition, even if the value for cont is uppercase, I convert it to lowercase
    hours = int(input("enter the number of hours: " )) 
    minutes = int(input("enter the number of minutes: "))
    seconds = int(input("enter the number of seconds: "))
    
    print("That's {} seconds".format(to_seconds(hours, minutes, seconds))) # -
    print()
    cont = input("do you want to do another conversion?[y to continue]")

print("Good bye!")    

# we have a function with 3 parameters (Variables), hours, minutes and seconds
# this function converts hours, minutes, seconds to seconds
# we get the output of this function with the keyword return
# we display the message "welcome to this time converter"

# initialize the variable cont (define it and provide a value for it. The value is a string). cont means continue
# while the variable cont is equal to y or Y
    # hours = integer of input function I NEED THIS BECAUSE INPUT FUCTION ALWAYS PRODUCES A STRING!
    # minutes
    # seconds

# actually the cont variable is used to ask the user if he wants to do another set of conversion
# the cont variable has an input function of its own, to which the user is prompted to respond y,Y 

# if cont is equal to y then this block of code will be re-executed
# so I use a WHILE LOOP
# With the while loop we can execute a set of statements as long as a condition is true.
# while, cont is equal to y, keep asking the user for input
    
# hours, it is a Variable, I get the value from the user with the input function
# also, I convert the product of the input function to a number!

# finally, I call the function "to_seconds" by providing it with arguments (values) and print it with the format method
    
# EXECUTION
   # 1 welcome to this time converter
   # 2 enter the number of hours:
    
    
    
"""
Note
Interactively asking the user for input might not always be the best approach for a problem we're trying to solve
"""

#%%
"""
1.3     Standard Streams

here we will explain how the input of a user at the keyboard is printed at the screen
it is done by using the I/O streams (Input/Output streams)

I/O streams = basic mechanism for performing Input and Output operations

I/O streams are not used only in Python ofcourse
they are used also when we enter a command in the command line (terminal)
we type the command and then we see the result "printed" in our screen (e.g. cat and ls commands)

I/O streams are called streams because data is flowing:)
    input is typed in and output is generated out


Most operating systems provide 3 types of I/O streams:
    1 - STDIN standard input
        a channel between a source of input-keyboard and a program 
        Usually input is in the form of text data from the keyboard
    2 - STDOUT standard output
        a channel between a program and a target of output-a display
        STDOUT generally takes the form of text displayed in a terminal
        when we use the print function to display information to the screen, we use the STDOUT channel
    3 - STERR standard error
        it is like STDOUT, but is used specifically as a channel to show error messages and diagnostics from the program
  
Attention!
STD OUT and STD ERR are both displayed in our screen but they are different channels
we will study this difference later in this course


"""
data = input("This will come from channel STDIN: ")
print("Now we write it to channel STDOUT: " + data)
print("Now we generate an error to channel STDERR: " + data +1)

# Attention: data is text(string) as it is the product of the input function
# we prompt the user to enter data
# user types in the data by using channel STD IN
# then we print the output (display the output on the screen) by using the STD OUT channel
# then we intentionally create an error by concatenating string and number to use the channel STD ERR and see the display of the error and the explanation too

# 1 This will come from channel STDIN:
# i type in Mary
# I see the result of the print function
# Now we write it to channel STDOUT: Mary
# and I get the error message from channel STD ERR
# TypeError: can only concatenate str (not "int") to str

"""
cat 
command to display the contents of a file
we see the contents displayed because of the channel STD OUT

ls
command to display a list of files and folders in the current directory 
if we write ls -z and there is an error, then we see in the display ls: invalid option --'z'
we see the error message because of the channel STD ERR

"""

#%%
"""
1.4     Environment Variables

Environment Variables
    Environment variables, as the name suggests, are variables in your system that describe your environment. 
    The most well known environment variable is probably PATH, which contains the paths to all folders 
    that might contain executables. 
    With PATH, you can write just the name of an executable rather than the full path to it in your terminal 
    since the shell will check the local directory as well as all directories specified in the PATH variable 
    for this executable.( is this relevant to absolute and relative path?)
    There are many different Environment Variables and some are more important than others.
    e.g. the Environment Variable PATH, is very important.

Environment Variables
    Environment variables is the set of key-value pairs for the current user environment. 
    (So, all the environment variables are a dictionary with the name of the variable as the KEY and the value of the variable as the VALUE?)
    They are generally set by the operating system and the current user-specific configurations.
    In Python, you can think of environment variables as a dictionary, 
    where the key is the environment variable name and the value is the environment variable value.
    How to print all the Environment Variables in Python: 
        The os.environ variable is a dictionary-like object. 
        If we print it, all the environment variables name and values will get printed.
        please see example 1
    
    
The OS module in Python, provides functions for interacting with the operating system

os.environ in Python, is a mapping object that represents the user’s environmental variables. 
It returns a dictionary having user’s environmental variable as Key and their values as Value.
"""
#%%
"""example 1
print all Environment Variables in Windows OS
"""
# in Windows and Spyder
import os
print(os.environ)

# OUTPUT IS BELOW
#environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\jimko\\AppData\\Roaming', 'ASL.LOG': 'Destination=file', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'DESKTOP-PI93GNG', 'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\jimko', 'LOCALAPPDATA': 'C:\\Users\\jimko\\AppData\\Local', 'LOGONSERVER': '\\\\DESKTOP-PI93GNG', 'NUMBER_OF_PROCESSORS': '4', 'ONEDRIVE': 'C:\\Users\\jimko\\OneDrive', 'ONEDRIVECONSUMER': 'C:\\Users\\jimko\\OneDrive', 'OS': 'Windows_NT', 'PATH': 'C:\\Users\\jimko\\Anaconda3;C:\\Users\\jimko\\Anaconda3\\Library\\mingw-w64\\bin;C:\\Users\\jimko\\Anaconda3\\Library\\usr\\bin;C:\\Users\\jimko\\Anaconda3\\Library\\bin;C:\\Users\\jimko\\Anaconda3\\Scripts;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files (x86)\\Calibre2\\;C:\\Users\\jimko\\AppData\\Local\\Microsoft\\WindowsApps;', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'AMD64 Family 21 Model 16 Stepping 1, AuthenticAMD', 'PROCESSOR_LEVEL': '21', 'PROCESSOR_REVISION': '1001', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\WINDOWS', 'TEMP': 'C:\\Users\\jimko\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\jimko\\AppData\\Local\\Temp', 'USERDOMAIN': 'DESKTOP-PI93GNG', 'USERDOMAIN_ROAMINGPROFILE': 'DESKTOP-PI93GNG', 'USERNAME': 'jimko', 'USERPROFILE': 'C:\\Users\\jimko', 'VBOX_MSI_INSTALL_PATH': 'C:\\Program Files\\Oracle\\VirtualBox\\', 'WINDIR': 'C:\\WINDOWS', 'CONDA_PREFIX': 'C:\\Users\\jimko\\Anaconda3', 'LANG': 'en', 'SPYDER_ARGS': '[]', 'QT_SCALE_FACTOR': '', 'QT_SCREEN_SCALE_FACTORS': '', 'SPY_EXTERNAL_INTERPRETER': 'False', 'SPY_UMR_ENABLED': 'True', 'SPY_UMR_VERBOSE': 'True', 'SPY_UMR_NAMELIST': '', 'SPY_RUN_LINES_O': '', 'SPY_PYLAB_O': 'True', 'SPY_BACKEND_O': '0', 'SPY_AUTOLOAD_PYLAB_O': 'False', 'SPY_FORMAT_O': '0', 'SPY_BBOX_INCHES_O': 'True', 'SPY_RESOLUTION_O': '72', 'SPY_WIDTH_O': '6', 'SPY_HEIGHT_O': '4', 'SPY_USE_FILE_O': 'False', 'SPY_RUN_FILE_O': '', 'SPY_AUTOCALL_O': '0', 'SPY_GREEDY_O': 'False', 'SPY_JEDI_O': 'False', 'SPY_SYMPY_O': 'False', 'SPY_RUN_CYTHON': 'False', 'SPY_TESTING': 'None', 'SPY_HIDE_CMD': 'True', 'PYTHONPATH': '', 'JPY_INTERRUPT_EVENT': '12480', 'IPY_INTERRUPT_EVENT': '12480', 'JPY_PARENT_PID': '12468', 'TERM': 'xterm-color', 'CLICOLOR': '1', 'PAGER': 'cat', 'GIT_PAGER': 'cat', 'MPLBACKEND': 'module://ipykernel.pylab.backend_inline'})
#%%
""" print all Environment Variables in LINUX OS"""
INPUT: env
OUTPUT: VTE VERSION=5601
        XDG_SEAT_PATH=/org/freedesktop/DisplayManager/Seat0
        etc.
#%%
"""
example 2
print the PATH variable in Windows OS
syntax: print(os.environ.get("environement variable"))
we use the Environ dictionary provided by the OS module
see below why we use the get() method
"""
import os
print(os.environ.get("PATH"))

# the output is:
#C:\Users\jimko\Anaconda3;
#C:\Users\jimko\Anaconda3\Library\mingw-w64\bin;
#C:\Users\jimko\Anaconda3\Library\usr\bin;
#C:\Users\jimko\Anaconda3\Library\bin;
#C:\Users\jimko\Anaconda3\Scripts;
#C:\WINDOWS\system32;C:\WINDOWS;
#C:\WINDOWS\System32\Wbem;
#C:\WINDOWS\System32\WindowsPowerShell\v1.0\;
#C:\WINDOWS\System32\OpenSSH\;
#C:\Program Files (x86)\Calibre2\;
#C:\Users\jimko\AppData\Local\Microsoft\WindowsApps;

#%%
"""
print the PATH variable in Linux OS
echo is a command to print texts in the Linux shell
shell: application that reads and executes all commands
"""
INPUT: echo $PATH
OUTPUT:usr/local/sbin:/user/local/bin:/usr/sbin:/usr/bin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:snap/bin

all the above are directories where the shell will look for programs   
        
#%%
"""
example 3
how to read the contents of the environment variables

I suppose I must provide the correct name of the environment variable:)
    
(in other words how to display the VALUE for a certain KEY
KEY is the environment variable and VALUE is the value of the environment variable.
all of the Environment Variables are a DICTIONARY with key:value pairs)

Why do we use the get() method together with os.environ?
if we use only os.environ then if the KEY (environemental variable) is not present, we will get an error.
by using get() we can avoid that because we can specify what value should be returned when the key is not present.
In other words, the get() method allows us to specify a default value when the key that we are looking for
 is not in the dictionary (dictionary is the collection of the environmental variables).
 The default value will be an empty string
"""
#%%
""" read the contents of certain environment variables in Windows OS""" 
import os

print("HOME: " + os.environ.get("PATH", ""))
print("SHELL: " + os.environ.get("USERDOMAIN", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))

# output is
# for PATH it is HOME: C:\Users\jimko\Anaconda3;C:\Users\jimko\Anaconda3\Library\mingw-w64\bin;C:\Users\jimko\Anaconda3\Library\usr\bin;C:\Users\jimko\Anaconda3\Library\bin;C:\Users\jimko\Anaconda3\Scripts;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;C:\Program Files (x86)\Calibre2\;C:\Users\jimko\AppData\Local\Microsoft\WindowsApps;
# for "USERDOMAIN" it is SHELL: DESKTOP-PI93GNG
# for FRUIT it is an empty string 
# we get nothing for FRUIT because it is a variable that is not defined in the current environment

#%%
""" read the contents of certain environment variables in Linux OS""" 
INPUT: cat variables.py (variables.py is a Python script. The cat command lists the contents of the file in the terminal window)
OUTPUT: #!usr/bin/env python 3
    
#%%
"""
read the contents of certain environment variables in Linux OS when the FRUIT variable is defined
the export keyword 'tells 

INPUT:./variables.py (./ runs the file. variables.py is a Python file )

OUTPUT: HOME: /home/user
        SHELL:  /bin/bash
        FRUIT: (WE GET AN EMPTY STRING FOR THE UND-DEFINED VARIABLE)

INPUT: export FRUIT = Pineapple (the keyword export "tells" the shell that we want the value we introduced to be "seen" by any commands that we call)
INPUT: ./variables.py
OUTPUT: HOME: /home/user
        SHELL:  /bin/bash
        FRUIT:Pineapple
   """ 
#%%
"""
HOMEDRIVE: is where the user's personal files are: downloads, music, documents, etc
"""
import os 
home = os.environ['HOMEDRIVE']
print("HOMEDRIVE:", home) 

#%%
"""
1.5     Command-Line Arguments and Exit Status

Yet another common way of providing information to our programs is through command line arguments

command-line arguments are parameters that are passed into a program when it is started (before it starts)
(arguments written in the command line that are incorporated into a script?)
we can specify the information that we want our program to use before it even starts

It is super common practice to make our scripts receive certain values by command-line arguments
No user input is required

we can access these values using the argv list in the sys module

to be precise sys.argv is a list, which contains the command-line arguments passed to the script. 
The first item of this list contains the name of the script itself. The arguments follow the script name.

The first argument, sys.argv[0], is always the name of the program as it was invoked,
and sys.argv[1] is the first argument you pass to the program.

It’s common that you slice the list to access the actual command line argument:
    import sys
    program_name = sys.argv[0]
    arguments = sys.argv[1:]
    count = len(arguments)


"""

#%%
"""I have the script "parameters.py"
this script only imports the sys module and
prints the sys.argv list

then we call the program (script) without any parameters
the sys.argv list contains only one element, the name of the program we just executed

"""
import sys

print(sys.argv)

# output is: ['']
#%%
"""
now let's call the program/script with additional parameters
"""

#%%
"""
in the linux command line I will write
INPUT: cat parameters.py
OUTPUT: #!/USR/BIN/ENV PYTHON 3
    import sys
    print(sys.argv)
    
then we call the program (script) without any parameters
the sys.argv list contains only one element, the name of the program we just executed
INPUT: ./parameters.py
OUTPUT: ['./parameters.py']
"""
#%%
"""
now let's call the program/script with additional parameters

INPUT: ./parameters.py one two three
OUTPUT: ['./parameters.py', 'one', 'two', 'three']

Now, we see that each of the arguments that we pass, is included as a separate element in the list sys.argv

The list of arguments are stored in the sys module:):)
"""

#%%
"""
concept of Exit Status or Return Code
It provides another source of information between the shell and the program/script (that is executed in the shell)

The Exit Status is the value returned by a program, to the shell
(shell: application that reads and executes all commands)

In all Unix-like operating systems, 
    - the exit status of the process is zero when the process succeeds (ZERO, WHEN THE PROCESS SUCCEEDS)
    - the exit status of the process is different than zero if it fails (DIFFERENT THAT ZERO, WHEN THE PROCESS FAILS)

The actual number returned gives additional info on what kind of error the program encountered.
 Knowing if a command finish successfully or not is helpful information which can be used by a program that's calling a command.
For example, it can use the information to retry the command. If it failed.

To check the exit status of a program, we can use a special variable that lets us see what the exit status of the last executed command was. 
The variable is the question mark variable.

To see the contents we use $?
Let's try this out using the WC command, which counts the number of lines words and characters in a file.
wc command:
    wc means word count
    syntax: wc filename
    provides number of lines, number of words, number of characters and name of file

echo $? command:
    will return the exit status of last command
    Commands on successful completion exit with an exit status of 0
INPUT: wc variables.py
OUTPUT: 7 19 174 variables.py
( we get number of lines, number of words, number of characters and name of file)
    
INPUT: echo $?
OUTPUT: 0 (yupiee!the exit status of the process is zero when the process succeeds )
last output is 0, because the "wc variables.py" ran successfully

INPUT: wc notpresent.py
OUTPUT: wc: notpresent.py: No such file or directory

INPUT: echo $?
OUTPUT:1
last output is 1 (different than 0), because the py file does not exist and the wc command could not be executed


"""
#%%%
"""
the above concerns commands
what happens when we run python scripts?
when a python script runs successfully, then it exits with an exit value of zero
when a python script does not run and it has an error, like type error or value error, it exits with an exit value different than zero

here is an example:
    INPUT: atom create_file.py
"""
import os
import sys

filename=sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("New file created\n")
else:
    print("Error, the file {} already exists!".format(filename))
    sys.exit(1)

"""
This script receives a file name as a command line argument
It first checks if the filename exists or not
When the file does not exits, it creates it by writing a line to it
When the file exists, our script prints an error message, and exits with an exit value of 1

To try this out let's first execute the script and pass a file that doesn't exist.


INPUT: ./create_file.py example
INPUT: echo $?
OUTPUT:0
the py file exists, the program/script is executed and exits with an exit value of 0 (eventhough it was not specified in the code)

Now, let's look at the contents of the file
INPUT: cat example
OUTPUT: new file created
INPUT: ./create_file.py example
OUTPUT: Error, the file example already exists!
INPUT: echo $?
OUTPUT: 1
We get an error because the file already exists and so we get an exit code of one
"""
"""
We'll use command line parameters to tell our programs what we want them to do without having to interact with them and we'll use exit values to know if our command succeeded or failed and then log failures and automatically retry the commands if we need to.
"""

#%%
"""
1.6     More about Input Functions


Summary
Python 2 and Python 3 handle input and raw_input differently.

In Python 2

input(x) is roughly the same as eval(raw_input(x))
raw_input() is preferred, unless the author wants to support evaluating string expressions.
eval() is used to evaluate string expressions.
Standard Library Docs:

https://docs.python.org/2/library/functions.html#input
https://docs.python.org/2/library/functions.html#raw_input
https://docs.python.org/2/library/functions.html#eval
In Python 3

Input handles string as a generic string. It does not evaluate the string as a string expression.
raw_input doesn’t exist, but with some tricky techniques, it can be supported.
eval() can be used the same as Python 2.
Standard Library Docs: 

https://docs.python.org/3/library/functions.html#input
https://docs.python.org/3/library/functions.html#eval
"""

#%%
"""
1.7     Practice quiz

1.Question 1
Which command will print out the exit value of a script that just ran successfully?

echo $PATH
wc variables.py
import sys
echo $? (CORRECT?)

2.Question 2
Which command will create a new environment variable?

env (this is for printing environment variables)
wc (this is for counting lines, words, characters)
input (this is a function not a command)
export (CORRECT?)
(the keyword export "tells" the shell that we want the value we introduced to be "seen" by any commands that we call )

3.Question 3
Which I/O stream are we using when we use the input function to accept user input in a Python script?

STDOUT channel between the program and the target of output (display)
STDERR channel to show error messages and diagnostics from the program
STDIN channel between the source of input (keyboard) and the program (CORRECT?)
SYS (this is a module)
sys — System-specific parameters and functions
This module provides access 
to some variables used or maintained by the interpreter and 
to functions that interact strongly with the interpreter. It is always available.

4.Question 4
What is the meaning of an exit code of 0?

The program ended with an unspecified error.
The program ended with a ValueError.
The program ended with a TypeError.
The program ended successfully.(correct?)

5.Question 5
Which statements are true about  
input and raw_input in Python 2? 
(select all that apply)

input performs basic math operations. (correct?)
raw_input performs basic math operations.
raw_input gets a string from the user. (correct?)
input  gets a string from the user.

all the above I chose were correct

"""
