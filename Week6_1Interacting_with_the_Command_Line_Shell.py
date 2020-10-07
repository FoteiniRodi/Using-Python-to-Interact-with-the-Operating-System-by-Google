#%%
"""
Using Python to interact with the operating system, by Google

Week 6 - Bash Scripting

1 Interacting with the Command Line Shell

1.1 Intro to Module 6: Bash Scripting
1.2 Basic Linux Commands
1.3 Redirecting Streams
1.4 Pipes and Pipelines
1.5 Signalling Processes
1.6 Reading: Basic Linux Commands Cheat-Sheet
1.7 Reading: Redirections, Pipes and Signals
1.8 Practice Quiz: Interacting with the Command Line
"""

#%%
"""
1.1 Intro to Module 6: Bash Scripting

Bash is another programming language different than the Python programming language.

In this module, we'll broaden our exposure to what the Linux operating system has to offer. 
We will see the most common Linux commands and 
    we'll see how we can connect the input and output streams to files or even to other programs. 
    
We will also use the Bash programming language, why? 
    Because in some cases it is simpler to use Bash rather than Python.
    We can write less code that is more readable and easier to maintain.
    
For example, imagine that you wanted to convert all image files in one directory from PNG to JPEG format. 
There's a command called "convert" that you can use to do this. 
You could definitely do this in Python, by going through all the files in the directory using "os.listdir"
    and can convert using "subprocess.run". 
But it would end up being a really complex script for something that's actually super simple.

In the next videos:
We will use system commands for Linux
we will write scripts with conditionals/loops using the Bash programming language 
We will create scripts using Bash
We will learn when to use Bash and when to use Python
"""

#%%
"""
1.2 Basic Linux Commands
a lot of these commands come from Unix.

I can practice the Linux Commands on Spyder by importing the os module first 
(see my notes Using Python to interact with the operating system-Week 2.2).
The python OS module allows us to interact with the underlying system, whether it is Windows, Linux, Mac, etc.
The python OS module lets us do the same tasks that we can normally do when working with files from the command line
So, we can write and test a script on Windows OS and then run it on Linux OS.
But, please be careful with the paths, they are different among the various OS's

Absolute Path: full path
Relative Path: portion of the Absolute Path

Linux
Command       Description                               
                                                                    
echo          print/display messages to the screen     
cat           show contents of files                    
chmod         change permissions of a file
touch         create an empty file
cp            copy files into an empty directory

ls            list the contents of a directory (shows names of files in a directory)
              list names of files contained in the directory
ls -l         show details of all files in a directory (permissions, users, date, file size)
              we get more information compared to just ls.
              the information is distributed in columns
              ls is the command, -l is the argument. 
              arguments let us change the behavior of commands  
ls -la        show also hidden files               
mkdir         create a new directory (make dir)
cd            change from one directory to another  (change d)   
pwd           print current working directory (for Windows OS, it is getcwd)
mv            rename or move a file
rm            delete a file
rm *          delete all files
rmdir         delete a directory (works only if the directory is empty)
man           command for manual pages to see the documentation, for Unix systems  


Notes: 
Directory = folder in which we place our files
            
Many commands don't print anything when they succeed.
    They only print something if they fail. 
    To check that the cd command succeeded, we can use a command like pwd to print the current working directory.

VIDEO WITH LINUX COMMANDS:

    mkdir mynewdir                                      # create a new directory
    cd mynewdir                                         # change to the directory mynewdir
    ~/mynewdir pwd                                      # print/display the current directory
    Output is: /home/user/mynewdir
    ~/mynewdir cp ../spider.txt .                       # copy the file from the previous directory(..) to the current directory(.)
    ~/mynewdir touch myfile.txt                         # create new file 
    ~/mynewdir ls -l                                    # show contents of directory
    Output is:
    total 4
    -rw-r--r-- 1 user user 0    jan 8 14:41 myfile.txt
    -rw-r--r-- 1 user user 192  jan 8 14:39 spider.txt 
    
    Explanation of the Output:
    -rw-r--r--  permissions of the file
    1           number of nodes pointing to the file
    user user   owner and group to which the file belongs
    0           size of the file in bytes
    jan 8 14:41 date of modification
    myfile.txt  name of the file
    
    ~/mynewdir ls -la                                   # shows hidden files
    Output is:
    total 12
    drwxr-xr-x  2 user user 4096 Jan 8 14:41 .          # one dot means current directory
    drwxr-xr-x 30 user user 4096 Jan 8 14:37 ..         # two dots mean parent directory (or previous directory?)
    -rw-r--r-- 1 user user 0    jan 8 14:41 myfile.txt
    -rw-r--r-- 1 user user 192  jan 8 14:39 spider.txt 
    
    ~/mynewdir mv myfile.txt emptyfile.txt              # rename the "myfile.txt" as "emptyfile.txt"
    ~/mynewdir cp spider.txt yetantoherfile.txt         # create a copy of the "spider.txt" and name it "yetantoherfile.txt"
                                                        # both in mv and cp, 1st parameter is the old file and 2nd parameter is the new file    
    ~/mynewdir ls -l
    Output is:
    total 8
    -rw-r--r-- 1 user user   0 Jan 8 14:41 emptyfile.txt        # renamed file
    -rw-r--r-- 1 user user 192 Jan 8 14:39 spider.txt 
    -rw-r--r-- 1 user user 192 Jan 8 14:45 yetantoherfile.txt   # copy of the spider.txt
    
    ~/mynewdir rm *                                     # delete all files in this directory
    ~/mynewdir ls -l                                    # show details of all files in a directory
    Output is:
    total 0
    ~/mynewdir cd ..                                    # change to the previous directory
    ~ rmdir mynewdir/                                   # delete the empty directory mynewdir
    ~ ls mynewdir
    Output is:
    ls: cannot access 'mynewdir'. No such file or directory

    
My notes from Crash Course Week 4, 4-2 Lists say:                             
The permissions of a file in a Linux system are split into three sets of the permissions:
    read, write, and execute for the owner, group, and others.

#	Permission	               rwx	    Binary

7	read, write and execute	   rwx	    111
6	read and write             rw-	    110
5	read and execute           r-x      101
4	read only                  r--      100
3	write and execute	       -wx      011
2	write only	               -w-      010
1	execute only               --x	    001
0	none	                   ---      000                
                           
    
"""

"""
CREATE A NEW DIRECTORY
Attention: for Linux OS it is mkdir mynewdir
"""
import os
os.mkdir("mynewdir")
# OUTPUT: I see no output but the new directory is created in the same folder as Python
#%%
"""
PRINT THE CURRENT DIRECTORY
Attention: for Linux OS it is pwd
"""
import os
os.getcwd() 
# OUTPUT: 'C:\\Users\\jimko', this is the folder where Python is
#%%
"""
CHANGE FROM ONE DIRECTORY TO ANOTHER
Attention: for Linux OS it is cd mynewdir 
"""
import os
os.chdir("mynewdir")

#%%
"""
COPY A FILE FROM THE PARENT DIRECTORY TO THE NEW DIRECTORY
for Windows OS I could not find an attribute in the os module:(

"""   
#%%
"""
I changed directory again, from mynewdir into C:\\Users\\jimko
"""
import os
os.chdir("C:\\Users\\jimko")

#%%
"""
I confirmed the change by printing the current directory
"""
import os
os.getcwd() 

#%%
"""
1.3 Redirecting Streams

IO STREAM RE-DIRECTING with files

Re-directing output (instead of the screen into a file)
Re-directing input (instead of the keyboard, from a file)
Re-directing error output (instead of the screen into a file)

My notes from Using Python to interact with the operating system-Week 4-1 Data Streams say:
    
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

Now we will combine I/O streams and Bash:
By default we provide input on the keyboard and then see the output and the errors on the screen
Instead of the screen we can re-direct the stream to a different destination! This is called Re-direction
Re-direction is provided by the operating system and is very useful when we want to store the output and the errors
    of a command in a file, instead of just seeind the display on a screen.
To re-direct the output(or the error) of a program to a file we use the SYMBOL >
ATTENTION: each time we perform of redirection of STD out, the destination is overwritten.


Re-direction of Output             
So, we have re-directed the OUTPUT to a file by using symbol > to re-direct for the first time and symbol >> to append
Re-direction of Input
- We can also re-direct the INPUT using the symbol <
  Instead of using the keyboard to send data into a program, we can use the symbol < to read the contents of a file
Re-direction of Error Output
- we can also re-direct ERROR OUTPUT using the symbol 2> to capture errors and diagnostic messages from a program.
  If you're wondering about the number 2, it represents the file descriptor of the SCD Err stream. 
  In this context you can think of a file descriptor as a kind of variable pointing to an IO resource. 
  In this case the STD Err stream. 
  0 and 1 are the file descriptors for SCDIN and SCDOUT. 

Re-direction of Output:       we use the symbol >  to write the output to a file
                              we use the symbol >> to append the output to a file that already has something stored in it
Re-direction of Error Output: we use the symbol 2> to write the error output to a file

Re-direction of Input :       we use the symbol < to use the input that is stored in a file


Please note we can use re-direction in other ways too:
    create a file with the echo command and then  re-direct its output to the file that we want to create.

In-Video question
How do you append the output of a command to a .txt file?
./calculator.py >> result.txt
Great work! A double greater than sign will append a command output to a file.
In fact, the output of the python script calculator.py, will not be displayed on screen but will be saved in the file result.txt

VIDEO WITH LINUX COMMANDS:
    RE-DIRECTING THE OUTPUT INTO A FILE
    cat stdout_example.py                               # cat command, displays the contents of a file
    Output is:
    #!/usr/bin/env python3                              # shebang line
    print("Don't mind me, just a bit of text here...")  # this displays the contents on the screen, it does not re-direct it
    
    ./stdout_example.py                                 # ./ command, runs the file
    Output is:
    Don't mind me, just a bit of text here...           # when the py file is executed we see this on the screen
    
    ./stdout_example.py > new_file.txt                  # Re-direction!
                                                        ./ command AND the symbol >, the output of the script 
                                                        is re-directed into a file called new_file.txt.
                                                        If the file does not exist, it will be created.
    cat new_file.txt                                    # cat command to see the contents of the new file
    Output is:
    Don't mind me, just a bit of text here... 
    
    ./stdout_example.py >> new_file.txt                # Re-direction but in this case it is APPENDING
    cat new_file.txt                                    ./ and symbol >>
    Output is:
    Don't mind me, just a bit of text here...          
    Don't mind me, just a bit of text here...          # the output is appended to the existing output from before  
    
    RE-DIRECTING THE INPUT (using input coming from a file and not from typing on the keyboard)
    cat streams_err.py                                     # with cat we see the contents of the py file
    Output is:
    #!/usr/bin/env python3  
    data = input("This will come from STDIN:")
    print("Now we write it to STDOUT:" + data)
    raise ValueError("Now we generate an error to STDERR")
    
    ./streams_err.py <  new_file.txt                       # the input for the streams_err.py comes from the new_file.txt
    Output is:                                             # we cannot see the input because it comes directly from the new_file.txt
                                                           # usually the input was something we typed on the keyboard but now with symbol < the input comes from the new_file.txt 
                                                           # we can see the input only after it was used by streams_err.py
                                                           # Attention! the input function only reads until it encounters a new line character
                                                           # that is why we see only one of the two lines 
    This will come from STDIN:Now we write it to STDOUT:Don't mind me, just a bit of text here...
    Traceback (most recent call last):
    File "./streams_err.py", line 5, in module
    raise  ValueError("Now we generate an error to STDERR")
    ValueError: Now we generate an error to STDERR
    
    RE-DIRECTING THE ERROR OUTPUT
    ./streams_err.py < new_file.txt 2> error_file.txt      # use input from new_file.txt and store the errors found in the file error_file.txt 
                                                           # so, we do not see any error messages on the screen because they are re-directed to the error_file.txt 
    Output is:
    This will come from STDIN: Now we write it to STDOUT: Don't mind me, just a bit of a text here
    cat error_file.txt                                     # with cat we see the contents of the file error_file.txt 
    Output is:
    File "./streams_err.py", line 5, in module
    raise  ValueError("Now we generate an error to STDERR")
    ValueError: Now we generate an error to STDERR    

    RE-DIRECTING 
    echo "These are the contents of the file" > myamazingfile.txt # echo command displays messages to the screen. here we create a file(a string?) with the echo command and instead of seeing it on the screen we re-direct it into a file 
    cat myamazingfile.txt                                         # we see the contents of the file
    Output is:
    These are the contents of the file

My notes:
>  re-direct output to a file. if it exists it will be overwritten. if it does not exist it will be created
>> re-direct append output to an existing file
2> re-direct error output to a file

< re-direct use input from a certain file
"""

#%%
"""
1.4 Pipes and Pipelines

IO STREAM RE-DIRECTING with Pipe |

Previously we re-directed the output to be stored to a file and re-directed the input to be taken from a file.
(we say re-direct because usually we just see the output on display and enter the input from the keyboard)
Now we will do again re-direction but between programs.


PIPING
we will use Pipes to connect the output of one program to the input of another.
By using Pipes, you can connect multiple scripts, commands, or other programs together into a data processing pipeline.

A Pipe | connects the output of one program to the input of another
This means we can pass data between programs, taking the output of one and making it the input of the next
Using a Pipe | allows us to CREATE NEW COMMANDS by combining the functionality of one command, with the functionality of another 
    without having to store the contents in an intermediate file.


VIDEO WITH LINUX COMMANDS:
    
    EXAMPLE 1
    ls -l | less
    Output is:
    total 3444
    -rw-r--r-- 1 user user 273 Jan 5 14:47 areas.py
    -rw-r--r-- 1 user user 134 Jan 6 11:31 by_department.csv
    -rwxr-xr-x 1 user user  96 May 12 2019 capitalize.py
    
    EXPLANATION OF EXAMPLE 1:
    The output of the command "ls -l" is used as input of the command "less"
    The command "ls -l" provides a list of files in a directory with a lot of details
    The command "less" is a terminal paging program
    So, the list of files is used as input for "less" which displays them 1 page at a time
    We can scroll up or down with the arrow keys, or page up/down
    Once we're done looking at the files, we can quit with Q

    EXAMPLE 2
    cat spider.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head
    Output is:
    7 the
    3 up
    3 spider
    3 and
    2 rain
    2 itsy
    2 climbed
    2 came
    2 bitsy
    1 waterspout.
    
    EXPLANATION OF EXAMPLE 2:
    cat spider.txt     display contents of txt file
    |                  redirect the output into the command tr as input
    tr ' ' '\n'        converts space into a new line, tr means translate
    |                  redirect
    sort               sorts alphabetically
    |                  redirect
    uniq -c            uniq displays each match once, uniq -c also adds number of occurrences as a prefix
    |                  redirect
    sort -nr           sorts numerically, from greatest to smallest
    |                  redirect 
    head               print/display results to STDOUT channel (to the screen). Prints first 10 lines!
    This is a complex command line with many commands linked by the Pipe symbol |, the output of the previous command is used as the input of the next command
    
We can use our Python scripts with the Pipe symbol | too
(to use the output of one script as the input of another script?)
    
    EXAMPLE 3
    cat capitalize.py                       # see contents of the py file
    Output is:
    #!/usr/bin/env python3
    import sys
    for line in sys.stdin:                  # for loop: iterate over each line of the file object
        print(line.strip().capitalize())    # strip: removes newline character from the end of each line. capitalize: capitalize the 1st character of each line
        
    cat haiku.txt                           # see contents of the txt file
    Output is:
    advance your career,
    automating with Python,
    it's so fun to learn
    
    cat haiku.txt | ./capitalize.py         # Use a PIPE to send the output of cat as input for the py file 
    Output is:
    Advance your career,
    Automating with Python,
    It's so fun to learn
    
    ./capitalize.py < haiku.txt             # for this simple task we can use simple re-direction and not pipe re-direction
    Output is:
    Advance your career,
    Automating with Python,
    It's so fun to learn
    
    EXPLANATION OF EXAMPLE 3:
    Python can read the standard input, by using the STDIN file object provided by the sys module
    the STDIN file object is like the file object we obtain with the open() function
    the file object is already open for reading (like if it was in our local library:))
    
    We want to read each line of a text file (input) and then print each line with the first character in uppercase.
    see contents of the py file with the cat command
    In this script we iterate over the contents of the sys.stdin file (this is the file object corresponding to the text file but it is not the text file. Am I correct here?)
    When we iterate over a file object we always go through it line by line
    For each line of the file we use the strip() method to remove the newline character at the end
    then the capitalize() method to capitalize the 1st character of each line
    then we print it out to standard output stdout (our screen)
    Now, let's use a script to capitalize a file that we have in our computer called Haiku.txt.
    see contents of the txt file with the cat command
    
    We will use the py file to capitalize first letter of each line in the txt file
    we will send the output of the cat command on the txt, as input to the py file BY USING A PIPE!
    
    ATTENTION
    we don't necessarily have to use the pipe | in order to use the output of the txt file as an input for the py file!
    we can use the re-direction operator we saw in 1.3 Redirecting Streams and simple re-direction is enough for this task.
    
    BUT if we want this task to be part of a bigger pipeline of commands, then I must use the pipe |
    For example, if we only want to capitalize the lines that match a certain pattern, we can first call grep and then connect it with the pipe to our scripts
    grep: The grep command is used to search text. 
          It searches the given file for lines containing a match to the given strings or words. 
          It is one of the most useful commands on Linux and Unix-like system. 
        
    Advantage of using pipe |
        When a system command doesn't exist with the functionality that you need, 
        you can write a Python script to fill in the gap and include it in your pipeline. 
"""
#%%
"""
1.5 Signalling Processes

while interacting with the Operating System, we have lots of different processes to accomplish what we want
we want these processes to communicate with each other
for example we have a program that starts a back-ground process and wants the process to terminate after a time out
one way of communicating this is through the pipelines we learned in the last video
another way of communicating is through the use of SIGNALS
HOW DO PROCESSES COMMUNICATE BETWEEN THEM?
    through the use of pipelines
    through the use of signals
    
SIGNALS: they are tokens delivered to running processes to indicate a desired action

TOKEN (please see definition 2!) information from https://www.webopedia.com/TERM/T/token
1) In programming languages, a single element of a programming language. For example, a token could be a keyword, an operator, or a punctuation mark.
2) In networking, a token is a special series of bits that travels around a token-ring network. 
   As the token circulates, computers attached to the network can capture it. 
   The token acts like a ticket, enabling its owner to send a message across the network. 
   There is only one token for each network, so there is no possibility that two computers will attempt to transmit messages at the same time.

    A single bit is the smallest unit of information on a machine and can hold only one of two values: 0 or 1.

3) In security systems, a small device the size of a credit card that displays a constantly changing ID code. A user first enters a password and then the card displays an ID that can be used to log into a network. Typically, the IDs change every 5 minutes or so.
A similar mechanism for generating IDs is a smart card.    
4) Another word for USB flash drive.    
    

By using SIGNALS we can tell a program to :
    pause
    terminate
    reload its configuration
    close all open files

Knowing how to send SIGNALS lets us interact with processes and control how the processes behave

VIDEO WITH LINUX COMMANDS:
    
    ping www.example.com  # ping command to send packets to www.example.com to check connectivity between our computer and the website
    Output is:
    PING www.example.com(2606:2800:220:1:248:1893:25c8:1946 (2606:2800:220:1:248:1893:25c8:1946)) 56 data bytes
    64 bytes from 2606:2800:220:1:248:1893:25c8:1946 (2606:2800:220:1:248:1893:25c8:1946): icmp_seq=1 ttl=56
    time =564 ms
    64 bytes from 2606:2800:220:1:248:1893:25c8:1946 (2606:2800:220:1:248:1893:25c8:1946): icmp_seq=2 ttl=56
    time =5.07 ms
    64 bytes from 2606:2800:220:1:248:1893:25c8:1946 (2606:2800:220:1:248:1893:25c8:1946): icmp_seq=3 ttl=56
    time =27.10 ms
    
    ^C                   # CTRL-C
    Output is:
    --- www.example.com ping statistics ---
    21 packets transmitted, 21 received, 0% packet loss, time 50ms
    rtt min/avg/max/mdev = 1.862/34.516/563.820/118.511 ms
    
    ping www.example.com  # run again the ping command
    Output is:
    PING www.example.com(2606:2800:220:1:248:1893:25c8:1946 (2606:2800:220:1:248:1893:25c8:1946)) 56 data bytes
    64 bytes from 2606:2800:220:1:248:1893:25c8:1946 (2606:2800:220:1:248:1893:25c8:1946): icmp_seq=1 ttl=56
    time =564 ms
    64 bytes from 2606:2800:220:1:248:1893:25c8:1946 (2606:2800:220:1:248:1893:25c8:1946): icmp_seq=2 ttl=56
    time =5.07 ms
    
    ^Z                  # CTRL-Z
    Output is:
    [1]+ Stopped ping www.example.com
    
    fg                  # with the fg command we can make the program run again
    ^C                  # CTRL-C
    Output is:
    --- www.example.com ping statistics ---
    36 packets transmitted, 36 received, 0% packet loss, time 50ms
    rtt min/avg/max/mdev = 1.862/34.516/563.820/118.511 ms
    
    1st TERMINAL                                2ND TERMINAL
    ping www.example.com                        ps ax | grep ping
    Output is:                                  Output is:
                                                2576 ? 5l 0:03 /usr/lib/x86_64-linux-gnu/cinnamon-settings-daemon/csd-housekeeping
    PING www.example.com                        4619 pts/1 5+ 0:00 ping www.example.com
    (2606:2800:220:1:248:1893:25c8:1946         4622 pts/0 5+ 0:00 grep --color=auto ping
    (2606:2800:220:1:248:1893:25c8:1946))       kill 4619
    56 data bytes
    64 bytes from 
    2606:2800:220:1:248:1893:25c8:1946 
    (2606:2800:220:1:248:1893:25c8:1946): 
    icmp_seq=1 ttl=56
    time =564 ms
    
    
    
    
    
    
    
    
    
    EXPLANATION 
    ping command sends icmp packets from our machine to the remote host once per second
    The output is the amount of time it takes for every packet to reach its destination and return.
    ping command examines the connectivity
    ping command runs forever unless we interrupt it
    
    type CTRL-C to interrupt (signal=SIGINT)
    the program does not end abruptly, it prints a summary of what it did and what the results were
    Actually, the process received a signal indicating that we wanted it to stop

    re-run the ping command
    type CTRL-Z to interrupt (signal= SIGSTOP)
    the proccess did not finish properly
    This signal causes the program to stop running without actually terminating

    fg command (the program runs again. Also, puts a background job in foreground?)
    type CTRL-C to interrupt
    Output is as above
    
    To send other signal to the process, we can use the command kill
    The kill command sends the signal SIGTERM, that tells the program to terminate
    Kill command is not like CTRL-C or CTRL-Z!
    It is a separate program and we need to run it on a different terminal
    We also need to know the PID of the process to which we want to send a signal
    (PID=process identifier)
    To find out the PID we will use the ps command
    ps command, lists current processes and their PID 
    ps ax command, lists current process in the current computer
    Then, we'll use the grep command to keep lines that contain the text "ping". (grep command, searches for specific text)
    
    Now, we will run "ping" on 1 terminal and find it's PID and "kill" it on another terminal
    
    We see that the PID for the running ping command is 4619
    We can now use this process identifier to send the signal SIGTERM to the process (kill command)
    after typing "kill 4619" in the 2nd terminal, the ping process in the 1st terminal finishes without the display of any messages

    OTHER SIGNALS
    ofcourse we can send other signals to a process
    e.g. send a signal to a program and the program reloads its configuration from disk
    the program does not have to stop, its gets informed about the configuration and continues to run
    e.g. a program that provides web services gets a signal that tells it to finish dealing with any currently open connections and then terminate cleanly once it's done
"""

#%%
"""
1.6 Reading: Basic Linux Commands Cheat-Sheet


This list includes a bunch of different commands that are useful to know when working with Linux. Not all of these commands are covered in the videos, so feel free to investigate them on your own.

MANAGING FILES AND DIRECTORIES
cd directory:           changes the current working directory to the specified one
pwd:                    prints the current working directory
ls:                     lists the contents of the current directory
ls directory:           lists the contents of the received directory
ls -l:                  lists the additional information for the contents of the directory
ls -a:                  lists all files, including those hidden
ls -la:                 applies both the -l and the -a flags
mkdir directory:        creates the directory with the received name
rmdir directory:        deletes the directory with the received name (if empty)
cp old_name new_name:   copies old_name into new_name
mv old_name new_name:   moves old_name into new_name
touch file_name:        creates an empty file or updates the modified time if it exists
chmod modifiers files:  changes the permissions for the files according to the provided modifiers; we've seen +x to make the file executable
chown user files:       changes the owner of the files to the given user
chgrp group files:      changes the group of the files to the given group

OPERATING WITH THE CONTENT OF FILES
cat file:                       shows the content of the file through standard output
wc file:                        counts the amount of characters, words, and lines in the given file; can also count the same values of whatever it receives via stdin
file file:                      prints the type of the given file, as recognized by the operating system
head file:                      shows the first 10 lines of the given file
tail file:                      shows the last 10 lines of the given file
less file:                      scrolls through the contents of the given file (press "q" to quit)
sort file:                      sorts the lines of the file alphabetically
cut -dseparator -ffields file:  for each line in the given file, splits the line according to the given separator and prints the given fields (starting from 1)

ADDITIONAL COMMANDS
echo "message":             prints the message to standard output
date:                       prints the current date
who:                        prints the list of users currently logged into the computer
man command:                shows the manual page of the given command; manual pages contain a lot of information explaining how to use each command (press "q" to quit)
uptime:                     shows how long the computer has been running
free:                       shows the amount of unused memory on the current system

"""
#%%
"""
1.7 Reading: Redirections, Pipes and Signals

MANAGING STREAMS
These are the redirectors that we can use to take control of the streams of our programs

command > file:         redirects standard output, overwrites file
command >> file:        redirects standard output, appends to file
command < file:         redirects standard input from file
command 2> file:        redirects standard error to file
command1 | command2:    connects the output of command1 to the input of command2

OPERATING WITH PROCESSES
These are some commands that are useful to know in Linux when interacting with processes. 
Not all of them are explained in videos, so feel free to investigate them on your own.

ps:         lists the processes executing in the current terminal for the current user
ps ax:      lists all processes currently executing for all users
ps e:       shows the environment for the processes listed
kill PID:   sends the SIGTERM signal to the process identified by PID
fg:         causes a job that was stopped or in the background to return to the foreground
bg:         causes a job that was stopped to go to the background
jobs:       lists the jobs currently running or stopped
top:        shows the processes currently using the most CPU time (press "q" to quit)
"""

#%%
"""
1.8 Practice Quiz: Interacting with the Command Line


1.
Question 1
Which of the following commands will redirect errors in a script to a file?


user@ubuntu:~$ ./calculator.py >> error_file.txt
user@ubuntu:~$ ./calculator.py > error_file.txt
user@ubuntu:~$ ./calculator.py 2> error_file.txt CORRECT
user@ubuntu:~$ ./calculator.py < error_file.txt

2.
Question 2
When running a kill command in a terminal, what type of signal is being sent to the process?

SIGINT
SIGSTOP
SIGTERM CORRECT
PID

3.
Question 3
What is required in order to read from standard input using Python?

echo file.txt
cat file.txt
The file descriptor of the STDIN stream
Stdin file object from sys module CORRECT

4.
Question 4
_____ are tokens delivered to running processes to indicate a desired action.

Signals CORRECT
Methods
Functions
Commands

5.
Question 5
In Linux, what command is used to display the contents of a directory?

rmdir
cp
pwd
ls CORRECT



"""
