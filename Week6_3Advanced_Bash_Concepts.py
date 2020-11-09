#%%
"""
Using Python to interact with the operating system, by Google

Week 6 - Bash Scripting

3 Advanced Bash Concepts 

3.1 While Loops in Bash Scripts
3.2 For Loops in Bash Scripts
3.3 Advanced Command Interaction
3.4 Choosing Between Bash and Python
3.5 Practice Quiz - Advanced Bash Concepts
"""
#%%
"""
3.1 While Loops in Bash Scripts

From my notes in "Crash Course on Python":
    
Loops= the computer does repetitive work
    
The While Loops instruct the computer to execute a block of code multiple times, based on the value of a condition.
"while" the condition is met, the while loop gets executed
once the condition is not met, the while loop stops from being executed and the computer continues to the next lines of code

This works in a similar way to branching if statements.
The difference here is that the body of the block can be executed multiple times instead of just once.

Attention: we must absolutely initialize because we may get 1) error or 2) use a starting value for the Variable from a previous block of code!
Attention: we must double-check the condition of the while loop
           the condition must change!(e.g. 1<5 then 2<5 then 3<5)
           if it does not change and it is always met, the while loop will be executed repeatedly without stopping!
    
Example:
    """
#%%
x = 0                                   # Line 1.INITIALIZING we provide the initial value for the Variable x, we start at 0
while x<5:                              # Line 2.we provide the condition for the WHILE LOOP. x must be smaller than 5 for the while loop to get executed
    print("Not there yet, x=" + str(x)) # Line 3.body of the while loop. executed while the condition is met
    x = x +1                            # Line 4 body.INCREMENTATION. we start at 0 and we increment by adding 1
print ("x="+ str(x))                    # Line 5. This gets executed only when the While Loop has ended because the condition stopped being met

#Output is:
#Not there yet, x=0 1st iteration
#Not there yet, x=1 2nd iteration
#Not there yet, x=2 3rd iteration
#Not there yet, x=3 4th iteration
#Not there yet, x=4 5th iteration
#x=5                CONDITION NOT MET AS 5 IS NOT SMALLER THAN 5. WHILE LOOP STOPS BEING EXECUTED, COMPUTER GOES TO NEXT LINE OF CODE
#%%
"""
LINE 1
Initializing 
(define the starting value for the Variable x)
LINE 2
Define the condition for the While Loop 
(when True, allows WHILE LOOP to be executed)
The while loop gets executed for x=0,1,2,3,4 (starting value 0, then 1,2,3,4 but not 5!We have 5 iterations done in the while loop block)
LINE 3 
Body of the While Loop 
(while x<5, display the message: "Not there yet, x= e.g.0" )
LINE 4
Incrementation 
(The Variable changes by increasing by 1 each time)
LINE 5
above we examined 0,1,2,3 here we examine 5. The while loop condition is not met, the while loop stops executing 
This gets executed only when the condition x<5 is met
This is OUTSIDE the While Loop
This gets executed only when the While Loop has ended
It tests the value 5 (x = 5) the first number in the series of 0,1,2,3,4 that does not satisfy the condition of the while loop!
The computer stops executing the while loop and goes to the next line of code

END of  my notes in "Crash Course on Python".

Bash provides looping constructions similar to Python
Ofcourse the bash syntax for loops is different than in Python
while loop: iterate while a condition is true
for loop:   iterate over a sequence of elements

Loops make the computer do repetitive tasks for us, anything from working with a bunch of numbers to processing the contents of a file line by line. 
Our computer doesn't care how many times we ask it to do what we want, it will keep doing them until it's done. 
No coffee breaks:)

SYNTAX FOR THE WHILE LOOP IN BASH
while [ condition ]
do
   command1
   command2
   command3
done  

command1 to command3 will be executed repeatedly till condition is true. 
The argument for a while loop can be any boolean expression. 
Infinite loops occur when the conditional never evaluates to false. 
Here is the while loop one-liner syntax:  
    while [ condition ]; do commands; done
    while control-command; do COMMANDS; done
   
The condition is evaluated before executing the commands. 
If the condition evaluates to true, commands are executed. 
Otherwise, if the condition evaluates to false, the loop is terminated, and the program control will be passed to the command that follows.    
    
    
VIDEO WITH LINUX COMMANDS:
    EXAMPLE 1
    cat while.sh                # show the contents of while.sh  
    Output is:
    #!/bin/bash                 # starting line of code for bash scripts .sh
    n=1                         # Initialization (provide starting value for our Variable n)
    while [ $n -le 5 ]; do      # condition is: if n is less than or equal to 5 then
     echo "Iteration number $n" # print/display this message while the condition is met
     ((n+=1))                   # Incrementation (provide way the value changes. here it increases by 1 each time, n = n +1)
    done
    ./while.sh                  # execute the Bash script 
    Output is:
    Iteration number 1
    Iteration number 2
    Iteration number 3
    Iteration number 4
    Iteration number 5
    
    EXPLANATION OF EXAMPLE 1:
    We use the Variable n to print messages counting from 1 to 5
    we access the value of the Variable n, by preceding n with the dollar sign ($)
    The loop starts with the keyword do and ends with the keyword done
    Incrementation is placed inside TWO parentheses

    Then we execute the Bash script
    
    EXAMPLE 2
    cat random-exit.py                # show contents of random-exit.py 
    Output is:
    #!/usr/bin/env python
    import sys
    import random
    
    value=random.randint(0,3)
    print("Returning: " + str(value))
    sys.exit(value)                   # we tell the script to exit here

    ./random-exit.py                  # run the python script  
    Output is:
    Returning: 1
    ./random-exit.py
    Output is:
    Returning: 2
    ./random-exit.py
    Output is:
    Returning: 3
    
    
    
    EXPLANATION OF EXAMPLE 2:
    For the sys module see week 4.1 Data Streams, Command-Line Arguments and Exit Status
    The sys module provides information about the Python interpreter's constants, functions, and methods
    
    "value" is a random number between 0 and 3 (we use the method randint from the module random to do this)
    this random value is printed/displayed
    the scripts exits with the printed/displayed value
    
    Notes for exit.sys:
    When we run a program in Python, we simply execute all the code in file, from top to bottom. 
    Scripts normally exit when the interpreter reaches the end of the file, BUT 
    we may also call for the program to exit explicitly with the built-in exit functions. 
    One of these exit functions is sys.exit([arg])
    The optional argument arg can be an integer giving the exit or another type of object. If it is an integer, zero is considered “successful termination”.
    Note: A string can also be passed to the sys.exit() method.
    
    
    EXAMPLE 3
    atom retry.sh                      # open the Bash program in the atom editor 
    n=0                                # initialization
    command=$1                         
    while ! $command && [$n -le 5 ];do # condition is 
        sleep $n                       # we first sleep a few seconds
        ((n=n+1))                      # incrementation
        echo "Retry #$n"               # print the value of the Variable n
    done;
    
    EXPLANATION OF EXAMPLE 3
    In Bash, we're getting the value of a command line argument using the $1,
    this is what we use in Bash to access the first command line argument.
    In Bash, with command=$0 we get the name of the file
    In Python, we get the same information using sys.argv[1].
    In Python, by using sys.argv[0] we get the name of the file

    we execute the while loop until either
    the command succeeds or
    the end Variable reaches a value of five
    In other words, if the received command fails, we'll retry up to five times.

    Why do we call the sleep command?
    the idea here is that if the command we're calling is failing due to CPU usage, network or resource exhaustion, 
    it might make sense to wait a bit before trying again. 
    
    My notes:
    ! is the logical "not" qualifier
    && means that if the first command is successful, only then execute the second command
    SO: in the retry.sh we define a Variable "command". This "command" is the random-exit.py 
        we use the random-exit.py as a parameter for the retry.sh
        we are interested in the first argument of the "command" which is hmm random and can be 0,1,2,3. 
        If first argument of the "command" is 0, then exit status is 0, the command has succeeded (we actually simulate a command that sometimes succeeds and sometimes fails OMG:))
    
        The while condition is while ! $command && [$n -le 5 ]
        explanation: while the "command" is not successful (first argument is not 0) then repeat n times with n<=5
        
        I found information on https://tldp.org/LDP/abs/html/exit-status.html#NEGCOND
        
        the retry.sh uses the random-exit.py as a parameter

the Variable "command" inside the retry.sh, refers to the random-exit.py
The random-exit.py produces 0,1,2,3, we need 0 for the "command" to be successful. This is done to simulate a command that sometimes succeeds and sometimes fails.
Finally my understanding for the while loop condition is:
while ! $command && [$n -le 5 ]
while command not successful, only then repeat executing it n times (and n<=5)
In the video it goes like this:
./retry.sh ./random-exit.py
Output is:
Returning:1
Retry #1
then,
Returning:3
Retry #2
then
Returning:2
Retry #3
then
Returning:0
here the while loop is not executed at all
"""
#%%
"""
3.2 For Loops in Bash Scripts

while loop: repeat something WHILE a condition is met

FOR LOOP: iterate over a sequence of elements

Both in Python and Bash, for loops are used to iterate over a sequence of elements. 
The key to for loops is that they let us perform an operation on each of the elements in a sequence. 

In Python, the sequences are data structures like a list or a tuple or a string. 
In Bash, WE CONSTRUCT these sequences just by listing the elements with spaces in between.
In Video question (that shows how to construct a sequence for a FOR LOOP in Bash):
Which “for” conditional line will add users Paul and Jeremy to a user variable?

for users in Paul Jeremy
for user in Paul Jeremy Correct Nice job! The elements Paul and Jeremy are added to the user variable.
for Paul Jeremy in user
for Paul & Jeremy in user

EXAMPLE
VIDEO WITH LINUX COMMANDS:
cat fruits.sh # see contents 
Output is:
#!/bin/bash
for fruit in peach orange apple; do
    echo"I like $fruit!"
done
./fruits.sh # execute
Output is:
    I like peach!
    I like orange!
    I like apple!
    
EXPLANATION
for element in sequence*
print "I like $element"

* sequence is just a list of the elements with spaces in between. 
again in the bash for loop,we use "do" and "done" like in the while loop


previously we used GLOBS like a star* and question mark? to create lists of files
(see week 6, 6.2 Bash Scripting to see theory for globs)
Globs are characters that allow us to create list of files based on the name of the file
example: echo *.py , returns a list of files that their name ends with .py
example echo ?????.py, returns a list of all py files which have 5 characters in their name


These lists are separated by spaces and so 
we can use them in our loops to iterate over a list of files that match a criteria, 
like all the files that end in.PDF, all files that start with IMG or whatever it is that we need.

In other words, I will use GLOBS to create a list of files and then iterate over that list with a bash FOR LOOP

EXAMPLE
I want to migrate files that end with .HTM to another server 
but I have to rename them to end with .html

I can re-name them manually with the mv command but better do it with a short bash script

VIDEO WITH LINUX COMMANDS:
cd old_website/  # change directory (choose the folder old_website)
/old_website$ ls -l # list all files in this directory with details
Output is:
    total 0
    -rw-r--r-- 1user user  may 24 2019 about.HTM
    -rw-r--r-- 1user user  may 24 2019 contact.HTM
    -rw-r--r-- 1user user  may 24 2019 footer.HTM
    -rw-r--r-- 1user user  may 24 2019 header.HTM
    -rw-r--r-- 1user user  may 24 2019 index.HTM

We have 5 files that we need to re-name
So how can we extract the part before the extension?
There is a command called basename that can help us
This command takes a filename and an extension and then returns the name without the extension
BASENAME: receives index.HTM
          returns  index

VIDEO WITH LINUX COMMANDS:
    
basename index.HTM .HTM index
atom                           # open the atom editor
#!/bin/bash                    # write a new bash script called rename.sh
for file in *HTM; do           # for element in sequence at which each element/file ends with .HTM
   name=$(basename "$file" .HTM) # basename command takes a filename and returns only name without the extension. We save the output in the Variable "name"
   mv "$file" "$name.html"       # use the mv command to rename each file (syntax: mv old name new name)
done



I save the rename.sh script in the folder old_website, where the 5 HTM files are located

I will do a for loop to iterate over each element (each HTM file) and perform an operation on each of the elements

the for loop will iterate over all files that end with HTM

We use dollar sign $ and parentheses to call the command and keep the output
We store the output in a Variable called name

We're surrounding our file variable with double-quotes to allow the command to work even if the file has spaces in its name

IT IS GOOD PRACTICE TO PRINT RESULTS BEFORE RENAMING THE FILES!
Whenever you're going to run a script like this that modifies the files in your file system, 
it's a really good idea to first run it without actually modifying the file system. 
So, I will use the echo command before the mv command.
This way I will print the results and do not implement them on the files
instead of actually renaming, our script we'll print the renaming that it plans to do.

VIDEO WITH LINUX COMMANDS:
#!/bin/bash                       
for file in *HTM; do               
   name=$(basename "$file" .HTM)     
   echo mv "$file" "$name.html"           
done

now we will save the script, make it executable with the chmod command and then run it

/old_website~ chmod +x rename.sh
/old_website~ ./rename.sh
Output is:
    mv about.HTM about.html
    mv contact.HTM contact.html
    mv footer.HTM footer.html
    mv header.HTM header.html
    mv index.HTM index.html
    
Finally, lets remove the echo so the files will be actually re-named

/old_website~./rename.sh

we have no output now, but the files are re-named

/old_website~ls -l # this displays a list of all files with details in the directory
Output is:
    total 4
    -rw-r--r-- 1user user  may 24 2019 about.html
    -rw-r--r-- 1user user  may 24 2019 contact.html
    -rw-r--r-- 1user user  may 24 2019 footer.html
    -rw-r--r-- 1user user  may 24 2019 header.html
    -rw-r--r-- 1user user  may 24 2019 index.html

"""
#%%
"""
3.3 Advanced Command Interaction

system log file
In computing, a log file is a file that records either events that occur in an operating system or other software runs,
 or messages between different users of a communication software. 
Logging is the act of keeping a log. In the simplest case, messages are written to a single log file.

The system log file is located on /var/log/syslog
The system log file contains a trove of information about what's going on in the system. 
So it's really important to learn how to get information out of it. 
Let's use the tail command to look at the last 10 lines from the file right now.

VIDEO WITH LINUX COMMANDS:
    tail /var/log/syslog
    Output is:
    Jan 9 09:32:59 ubuntu anacron[5170]: Anacron 2.3 started on 2020-01-09 # I did not copy all 10 lines only first and last
    Jan 9 09:39:03 ubuntu systemd[1]: systemd-hostnamed.service: Suceeded

EXPLANATION
     date and  time of when the entry was added to the file (Jan 9 09:39:03)
     name of the computer (ububtu)
     name and PID of the process that triggered the event (systemd[1])
     the actual event that is being logged/recorded (systemd-hostnamed.service: Suceeded)

Say that we had a computer that was under significant load but we didn't know why, 
and to find out we wanted to check what events are being logged the most or Syslog. 
To do that we need to extract the part of the line that has the actual event without the date and time. 
We can use a command called cut to help us with that. 
This command, let's us take only bits of each line using a field delimiter. 
In this example, we can split the line using spaces. 

VIDEO WITH LINUX COMMANDS:
    tail /var/log/syslog | cut -d' ' -f5-
    Output is:
    ubuntu systemd[1]: systemd-hostnamed.service: Suceeded    
    
EXPLANATION 
we are using a pipe so the output of tail /var/log/syslog will be used as input for the cut command
(the 10 last lines of the log file that is)

cut -d' ' -f5-
-d' ': -d option is used then to use space a a delimiter (delimiter=separator)
-f5- : we keep field number 5 and everything after it
      field 5 is the process and the actual event

VIDEO WITH LINUX COMMANDS:
    cut -d' ' -f5- /var/log/syslog | sort | uniq -c | sort -nr | head
    Output is:
    8 ubuntu dhclient[3203]: DHPREQUEST for 100.83.177.199 on wlp4s0 to 100.100.185.22 port 67 (xid=0x337b618)

EXPLANATION 
we want to get the log lines that are repeated the most, in our system log file
we apply the cut command on all lines of the log file (since we are not using the tail command)
we get the log lines that are repeated the most on top of the results

In the system log file (in /var/log/syslog) there are many-many files.
Now we will use a FOR LOOP to iterate over each file and get the most repeated lines in each file.
This is more complex so we will not use one line of commands, instead we will write a Bash script
The bash script is called "toploglines.sh"
(for loop: iterates over the elements of a sequence and performs an operation on each element)

VIDEO WITH LINUX COMMANDS:
    cat toploglines.sh    # cat command shoes us the contents of the bash script
    Output is:
    #!/bin/bash
    for logfile in /var/log/*log;do
        echo "Processing: $logfile"
        cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
    done
    
EXPLANATION
for logfile in /var/log/*log;do
for element=logfile in sequence=/var/log/*log, all files in /var/log/ that end in log (* is a glob, *log returns a list of files that end in "log")

echo "Processing: $logfile" 
we print the name of the file we are processing 

cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
we use this group of commands to retrieve the 5 most repeating log lines of all log files     

Finally the output will show us:
    1) name of the log file processed (eg. Processing: /var/log/lastlog )
    2) the 5 most repeated log lines of that log file

now lets execute the toploglines.sh
VIDEO WITH LINUX COMMANDS:
    ./toploglines.sh
    Output is: (3:31 of the video)
    
EXPLANATION
Our script shows us the most common lines on each file in var/log.

In Video question:
what are the fields for the cut command?

question= user@ubuntu:~$ tail /var/log/syslog | cut -d' ' -f3-
october 31 10:18:41 CRON[257236]: description of the event

field 1=october
field 2=31
field 3=10:18:41 
field 4=CRON[257236]:
field 5=process and the actual event

in the cut command, -f3- is selected, so we choose field 3 (10:18:41 ) and everything after it
"""  
#%%
"""
3.4 Choosing Between Bash and Python

By using bash scripts, we can very quickly turn a command that operates on just one file into an automated script 
that handles 1,000 files
As we saw with our log file examples, there's a bunch of terminal commands that provide text processing functionality. 
Plenty of them also support regular expressions, allowing us to do some very advanced processing of the data 
in our files. 
When these commands are linked together in a data processing pipeline, they can become a powerful tool for processing 
text data. 
They can give us information we're looking for quickly about the need to write a full script. 
BUT BE CAREFUL NOT TO WRITE UN-READABLE CODE

VIDEO WITH LINUX COMMANDS:
    for i in $(cat story.txt); do B= echo -n "${i:0:1}" | tr "[:lower:]" "[:upper:]" ; echo -n "${B}${i:1}" ; done; echo -e "\n"
    Output is:
    Once Upon A Time There Was An Egg Of A Programming Language Called Python

EXPLANATION
This command line is using some stuff we saw and some other stuff that we didn't look into, 
like how to do indexing on bash strings to turn the first letter of each word into uppercase. 
We can probably agree that this command line is pretty unreadable. 
If there happened to be a bug in it, it would be really hard to figure out how to fix it. 
When a bash command line starts becoming this complex, 
it's a better idea to write a Python script that handles data in a more readable and testable way. 

VIDEO WITH LINUX COMMANDS:
    cat capitalize_words.py
    Output is:
        #!/usr/bin/env python3
        import sys
        for line is sys.stdin:
            words = line.strip(). split()
            print(" ". join([word.capitalize() for word in words]))


EXPLANATION
we take each line of standard input, 
remove the white space, and split it into separate words. 
Then, we use a list comprehension to capitalize each of the words and end up joining them back with spaces and 
printing the output.  

Once we have the script, we can execute it as part of a pipeline like this.     

VIDEO WITH LINUX COMMANDS:
    cat story.txt | ./capitalize_words.py
    Output is:
    Once Upon A Time There Was An Egg Of A Programming Language Called Python



When to choose Bash and when to choose Python:
1) for a simple task use Bash, for a complex task use Python 
It's a good idea to choose bash when we're operating with files and system commands, 
as long as what we're doing is simple enough that the script is self-explanatory. 
As soon as it becomes hard to understand what the script is doing, it's better to write it in a more general scripting 
language like Python.

2) Bash and Linux commands cannot be used on all operating systems
There's another gotcha when it comes to bash and Linux commands, and it's something that we've said before. 
Their availability depends on the platform that we're using. 
Some commands might not be present on certain operating systems. 
Running a bash script can get the job done very quickly on a Linux machine, but it won't work on a Windows machine. 
There, we need to write the same script in PowerShell. 
So if the tasks that you're trying to accomplish is limited to the current server or a fleet of servers, 
all running the same operating system, a simple bash script can get the job done. 
But if your code is complex or it needs to work across platforms, you might be better off using 
the Python standard library or other external modules that provide the same functionality.

 It is better to use Python and its standard library to use when working across multiple platforms.

"""
#%%
"""
3.5 Practice Quiz - Advanced Bash Concepts

1.
Question 1
Which command does the while loop initiate a task(s) after?
do CORRECT Awesome! Tasks to be performed are written after do.
n=1
done
while

2.
Question 2
Which line is correctly written to start a FOR loop with a sample.txt file?
for sample.txt do in file
for file in sample.txt; do CORRECT You nailed it! The contents of sample.txt are loaded into a file variable which will do any specified task.
for sample.txt in file; do
do sample.txt for file

3.
Question 3
Which of the following Bash lines contains the condition of taking an action when n is less than or equal to 9?
while [ $n -le 9 ]; dowhile [ $n -le 9 ]; do CORRECT Right on!. This line will take an action when n is less than or equal to 9.

while [ $n -lt 9 ]; do

while [ $n -ge 9 ]; do

while [ $n -ge 9 ]; do

4.
Question 4
Which of the following statements are true regarding Bash and Python? [Check all that apply]

Complex scripts are better suited to Python. CORRECT Nice work! When a script is complex, it's better to write it in a more general scripting language, like Python.
Bash scripts work on all platforms.
Python can more easily operate on strings, lists, and dictionaries.CORRECT Awesome! Bash scripts aren’t as flexible or robust as having the entire Python language available, with its many different functions to operate on strings, lists, and dictionaries.
If a script requires testing, Python is preferable.CORRECT Right on! Because of the ease of testing and the fact that requiring testing implies complexity, Python is preferable for code requiring verification.

5.
Question 5
The _____ command lets us take only bits of each line using a field delimiter.

cut CORRECT Excellent!  The cut command lets us take only bits of each line using a field delimiter.
echo
mv
sleep

"""
