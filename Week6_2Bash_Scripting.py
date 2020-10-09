#%%
"""
Using Python to interact with the operating system, by Google

Week 6 - Bash Scripting

2 Bash Scripting

2.1 Creating Bash Scripts
2.2 Using Variables and Globs
2.3 Conditional Execution in Bash
2.4 Bash Scripting Resources
2.5 Practice Quiz: Bash Scripting


"""
#%%
"""
2.1 Creating Bash Scripts

Bash is a programming language AND also Bash is the most commonly used shell on Linux

Shell: 
    the shell is a program that takes commands from the keyboard and gives them to the operating system to perform
On most Linux systems a program called bash (which stands for Bourne Again SHell, 
    an enhanced version of the original Unix shell program, sh, written by Steve Bourne) acts as the shell program. 
Besides bash, there are other shell programs available for Linux systems. These include: ksh, tcsh and zsh.

Until now we have used Bash commands one by one
Now, we will use many Bash commands inside one script with the extension .sh
We can use Bash to write simple scripts when we need to use a lot of commands.

Why use a Bash script and not Bash commands?
Because we can use many commands at once in a script and not one by one

(e.g. sometimes we need to debug a computer that's not behaving correctly. 
 There are lots of commands that can tell you what's going on in there to help you with your debugging. 
 For example, the ps command can list all the current running processes. 
 The free command can show you the amount of free memory. 
 The uptime command can tell you how long the computer has been on and so on. 
 Anytime you need to debug a computer, you can manually run these commands one by one, 
 followed by as many commands as you can think of that might be helpful. 
 But that already sounds tedious just describing it!
 What if instead, you can run a single command that can gather all these information in just one shot? 
 Well, I have some good news for you. 
 We can do this by creating a Bash script that contains all of the commands that we want to call, one after the other.)

VIDEO WITH LINUX COMMANDS:
    EXAMPLE 1
    Title of the following Bsh script is: gather-information.sh (look at the sh extension!!!)
    #!/bin/bash
    echo "Starting at: $(date)" # print the text Starting at: and run the date command 
    echo                        # print the result  of the previous command
    
    echo "UPTIME"   # print the word UPTIME
    uptime          # run the uptime command
    echo            # print the result of the uptime command
    
    echo "FREE"     # print the word FREE
    free            # run the free command
    echo            # print the result of the free command
    
    echo "WHO"      # print the word WHO
    who             # run the who command
    echo            # print the result of the who command
    
    echo "Finishing at: $(date)" #print the text Finishing at: and run the date command 
    
    Output is:
    Starting at: Thu 09 Jan 2020 08:12:35 AM PST
    UPTIME
    08:12:35 UP 3 DAYS, 20:56, 1 USER, LOAD AVERAGE: 0.07, 0.02, 0.00
    
    FREE
            total       used        free        shared  buff/cache  available  
    Mem:    7841988     1285096     3884428     253228  2672464     5998856
    Swap:   2097148           0     2097148  
    
    WHO
    user    tty7    2020-01-05 11:16 (:0)
    Finishing at: Thu 09 Jan 2020 08:12:35 AM PST 
    
    
    EXPLANATION OF EXAMPLE 1
    above, we call 3 basic commands: uptime, free, who
    uptime: shows how long the computer has been running
    free: shows the amount of unused memory on the current system
    who: lists users currently logged into the computer
    We use the echo command to print some other information
    We leave empty lines to make the output more readable
    We call the date command to print current date
    We place the date command inside parentheses and a preceding dollar sign
    This indicates that the output of the command should be passed to the echo command and be printed to the screen.
    
    In the Output we can see that starting and finishing times are the same because there are so few operations we're doing that it takes a computer less than a second to complete them.

    EXAMPLE 2
    in Example 1 we had one command per line
    that is good practice but we can write them on the same line and separate them by colon ;
    
    #!/bin/bash
    echo "Starting at: $(date)" ;echo

    echo "UPTIME" ;uptime ;echo
    
    echo "FREE" ;free ;echo   
    
    echo "WHO" ;who ;echo
     
    echo "Finishing at: $(date)"
    
    EXPLANATION OF EXAMPLE 2:
    example 2 works exactly like example 1


IN-VIDEO QUESTION
Which command will correctly run a bash script?
1
~$ #!/bin/bash
No, This is the first line of the contents of a .sh or bash file.
2
~$ ./bash.py
No, This is a python script using the .py file extension.
3
~$ ./bash_sample.sh
YES, A bash script is run with the .sh file extension.
4
~$ ./sh.bash
No, A bash script doesn't use a .bash file extension.

My notes:
A Bash script in its first line contains: #!/bin/bash
A bash script has the extension: .sh

"""
#%%
"""
2.2 Using Variables and Globs

Bash is not only a way of executing commands one after the other
Bash is a programming language with variables, new conditional operations, execute loops, defined functions, etc.

VARIABLES IN BASH
Bash lets us use Variables to store values
Environment Variables = they are Variables set in the environment in which the command is executing
In addition to the Environment Variables, we can also define our own Variables
We set Bash Variables using the equals sign (=)
Attention, no space is left e.g. Variable=value, otherwise it is not recognized
When we want to access the value stored in a Bash Variable, we pre-fix the name of the Variable with the dollar sign ($)

Any Variable that you define in your script or in the command line is LOCAL to the environment where you define it. 
If you want commands from that environment to also see the Variable you need to export them using the EXPORT KEYWORD. 


VIDEO WITH LINUX COMMANDS:
    EXAMPLE 1
    The below Bash script is called gather_information.sh
    #!/bin/bash
    echo "Starting at: $(date)" ;echo

    echo "UPTIME" ;uptime ;echo
    
    echo "FREE" ;free ;echo   
    
    echo "WHO" ;who ;echo
     
    echo "Finishing at: $(date)"
    
    What we will do here is to add a line with dashes instead of space 
    The point is to make the output more readable
    The point is to use a Variable and a value in a Bash script

    EXAMPLE 2
    here I modify the script gather_information.sh
    #!/bin/bash
    line="---------------------------"      # Variable is "line", value is "-----"
    echo "Starting at: $(date)" ;echo $line # I added $ and the Variable name

    echo "UPTIME" ;uptime ;echo $line
    
    echo "FREE" ;free ;echo $line   
    
    echo "WHO" ;who ;echo $line
     
    echo "Finishing at: $(date)"
    
    ./gather_information.sh # run the script
    Output is:
    Starting at: Thu 09 Jan 2020 08:12:35 AM PST
    UPTIME
    08:12:35 UP 3 DAYS, 20:56, 1 USER, LOAD AVERAGE: 0.07, 0.02, 0.00
    ---------------------------------
    FREE
            total       used        free        shared  buff/cache  available  
    Mem:    7841988     1285096     3884428     253228  2672464     5998856
    Swap:   2097148           0     2097148  
    ---------------------------------
    WHO
    user    tty7    2020-01-05 11:16 (:0)
    ---------------------------------
    Finishing at: Thu 09 Jan 2020 08:12:35 AM PST

GLOBS IN BASH
To use Globs in Python we have to use the glob module!

Globs are characters that allow us to create list of files
The star(*) and the question mark(?) are the most common globs

using these globs lets us create sequences of filenames that we can use as parameters to the commands we call in our scripts.

Glob star(*)
* returns any amount of characters
In Bash using a star* in the command line will match all filenames that follow the format we have specified

example: echo *.py 
This returns a list with files that their name ends with .py (SUFFIX=ΚΑΤΑΛΗΞΗ)
returns list of filenames in the current directory
we specified that we want all filenames before ".py". So we ask for a list of ALL py files
Output is:
areas.py
capitalize_words.py
charfreq.py
etc.

example: echo c* PREFIX ΠΡΟΘΕΜΑ starts with c
This returns a list with files that their name starts with c 
returns list of filenames in the current directory
we specified that we want all filenames that start with the letter c
Output is:
    capitalize.py
    charfreq.py
    csv_file.txt

example: echo * creates a list of absolutely all files in the current directory!

Glob question mark (?)
the question mark symbol can be used to match exactly one character
one (?) returns one character
we can repeat the ? as many times as we need

example echo ?????.py 
This returns a list of all py files which have 5 characters in their name
returns list of filenames in the current directory
we specified that we want 5-character filenames before ".py".
Output is:
    areas.py
    hello.py
    myapp.py

My Notes:
    star (*) and question mark (?) in Bash remind me of REGEX in Python
"""
#%%
"""
2.3 Conditional Execution in Bash

Note form the In-Video question:
In a Bash script, the if conditional ends with fi (a backwards "if").

My notes: if is the operator, after if we have the condition that equals to True or False

One of the main concepts of programming is being able to branch the execution according to a condition.
E.g., IF the condition is True the program executes A, IF thr condition is False the program executes B

In Python: we use the IF block and the condition is an expression that is examined and is either True or False
In Bash: we also use an IF block but now the condition has to do with the EXIT STATUS of the command.
        we examine the exit status of a command using the dollar sign and question mark ($?)
        in Bash exit value=0 means that the command was executed successfully
        in Bash, if the exit value=0 after the command was executed, this result is considered True
        so, exit value=0 then True
        
 VIDEO WITH LINUX COMMANDS:
     EXAMPLE 1
     cat check_localhost.sh
     Output is:
     #!/bin/bash
     if grep "127.0.0.1" /etc/hosts; then
             echo "Everything ok"
     else
             echo "ERROR!127.0.0.1 is not on /etc/hosts"
    fi
    ./check_localhost.sh
    Output is:
    127.0.0.1   localhost
    Everything ok

    EXPLANATION OF EXAMPLE 1
    lets say we have a Bash file named check_localhost.sh
    this file contains an entry for 127.0.0.1 and we want to verify this
    the grep command will return exit status=0 when it finds just one match,
    and exit status different than 0 if it does not find a match.
    So, we will use the grep command to do this verification
    we start with the if keyword followd by the grep command
    The grep command is used to search text. 
    It searches the given file for lines containing a match to the given strings or words
    We start with the if keyword, followed by the grep command
    If the grep command has exit value=0, it was successful at locating the text
    Note: The computer file hosts is an operating system file that maps hostnames to IP addresses. 
          It is a plain text file.
          It must contain 127.0.0.1
          webopedia: In TCP/IP networks, localhost is the name used to describe the local computer address. Localhost always translates to the loopbackIP address 127.0.0.1.
    At the end of the command we necessarily type ;then
    Then the body of the IF conition is written
    echo print/displays mssages on the screen
    so, if the condition is True(exit status=0 for the grep command)
    we see the first message
    ELSE, if the condition is False we see the second message
    Finally to close the if block we write the fi keyword (mirror opposite of if)
    PLEASE NOTE:
        we absolutely need to write ;then after the command and fi at the end!!!
    Lets execute the Bash script now.
    First line of output is generated by the grep command
    Second line of output is generated by our script
    
    
    EXAMPLE 2
    if test -n "$PATH"; then echo "Your path is not empty"; fi
    Output is:
    Your path is not empty
    
    
    EXPLANATION OF EXAMPLE 2
    TEST COMMAND:
    Test is a command that evaluates the conditions received and 
        exits with zero when they are true and 
        with one when they're false.
    We're using the -n option for the test command
    -n means that the length of STRING is nonzero 
    so if length of string is not zero, True and print Your path is not empty
       if length of string is  zero, False
    
    This is a short script and we do no need indentation:)
    
    Indentation is not mandatory in Bash
    We use it for better readability
    
    In this example PATH is not empty
    
    EXAMPLE 3
    if [-n "$PATH" ]; then echo "Your path is not empty"; fi
    Output is:
    Your path is not empty
    
    EXPLANATION OF EXAMPLE 3
    In ths example the command we are calling is the opening square bracket
    the opening square bracket is an alias for the test command (OMG!!!)
    so, [ = test
    order to call the opening square bracket we need to use a closing square bracket too
    Attention: we need a space before the closing bracket

"""
#%%
"""
2.4 Bash Scripting Resources

Bash Scripting Resources
Check out the following links for more information:

https://ryanstutorials.net/bash-scripting-tutorial/
https://linuxconfig.org/bash-scripting-tutorial-for-beginners
https://www.shellscript.sh
"""

#%%
"""
2.5 Practice Quiz: Bash Scripting


1.
Question 1
Which of the following commands will output a list of all files in the current directory?

1 point

echo ?.py


echo * CORRECT


echo *.py


echo a*

2.
Question 2
Which module can you load in a Python script to take advantage of star [*] like in BASH?

1 point

stdin


ps


Glob CORRECT


Free

3.
Question 3
Conditional execution is based on the _____ of commands.

1 point

environment variables


parameters


exit status CORRECT


test results

4.
Question 4
What command evaluates the conditions received on exit to verify that there is an exit status of 0 when the conditions are true, and 1 when they are false?

1 point

test CORRECT


grep


echo


export

5.
Question 5
The opening square bracket ([), when combined with the closing square bracket (]), is an alias for which command?

1 point

glob


test CORRECT


export


if


"""
