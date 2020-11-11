#%%
"""
Using Python to interact with the operating system, by Google

Week 6 - Bash Scripting

4 Module Review

Qwiklabs Assessment: Editing Files Using Substrings

CONTENTS: << INTRODUCTION >>
          << PRE-REQUISITES >>
          << RE-DIRECTING  >>
          << EXERCISE practicing cat, grep, cut >>
          << THE TEST COMMAND >>
          << CREATE A FILE USING A RE-DIRECTION OPERATOR >>
          << ITERATION >>
          << FIND FILES USING a BASH SCRIPT (exercise 1) >>
          << RENAME FILES USING a PYTHON SCRIPT (exercise 2) >>
          

    
    
<< INTRODUCTION >>
In this lab, you'll change the username of your coworker Jane Doe from "jane" to "jdoe"
 in compliance with company's naming policy. 
The username change has already been done. 
However, some files that were named with Jane's previous username "jane" haven't been updated yet. 
To help with this, you'll write a bash script and a Python script that will take care of the necessary rename operations.

What you'll do:
Practice using the cat, grep, and cut commands for file operations
Use > and >> commands to redirect I/O stream
Replace a substring using Python
Run bash commands in Python

<< PRE-REQUISITES >>
For this lab, you should have a sound knowledge of these Linux commands:

Command     Syntax
cat         cat [file]
grep        grep [pattern] [file-directory],    grep [pattern] [file-location]
cut         cut [options] [file],               cut -d [delimiter] -f [field number]

CAT COMMAND: The cat command allows us to   create single or multiple files, 
                                            view the contents of a file, 
                                            concatenate files (join them together), 
                                            and redirect output in terminal or other files.

GREP COMMAND: (grep=global regular expression print)
               processes text line-by-line and prints any lines that match a specified pattern.
               It is also used to search text and match a string or pattern within a file.

CAT COMMAND: The cut command extracts a given number of characters or columns from a file. 
              A delimiter is a character or set of characters that separate text strings.
              For delimiter separated fields, the - d option is used.
              The -f option specifies the field, a set of fields, or a range of fields to be extracted.


<< RE-DIRECTING  >>
LINUX I/O RE-DIRECTION
Redirection is defined as:
switching standard streams of data, from either a user-specified source or user-specified destination.
(e.g. get the input not from the keyboard but from a file
 e.g. send the output not to the screen but into a file)

>   : to write the output to a file (if file does not exist yet, it will be created). This OVERWRITES file content
>>  : append the output to an existing file. This DOES NOT OVERWRITE file content
<   : use the input that is stored in a file

Linux command: cat > [file]     if files exists, this over-writes it. If file does not exist, this creates it
Linux command: cat >> [file]    appends a word or string to the existing file

<< EXERCISE practicing cat, grep, cut >>
The Scenario:
Your coworker Jane Doe currently has the username "jane" but she needs to change it to "jdoe" 
to comply with your company's naming policy. 
This username change has already been done. 
HOWEVER, some files that were named with Jane's previous username "jane" haven't been updated. 
For example, "jane_profile_07272018.doc" needs to be updated to "jdoe_profile_07272018.doc".

My notes: change all filenames, from "jane" to "jdoe"


1 cd data   # navigate to the directory "data"
2 ~data$ ls # display a list of all files in this directory. The directory contains,among others, a file called "list.txt"
3 ~data$ cat list.txt # see contents of the file "list.txt"
Output:
001 jane /data/jane_profile_07272018.doc
002 kwood /data/kwood_profile_04022017.doc
003 pchow /data/pchow_profile_05152019.doc
004 janez /data/janez_profile_11042019.doc
005 jane /data/jane_pic_07282018.jpg
006 kwood /data/kwood_pic_04032017.jpg
007 pchow /data/pchow_pic_05162019.jpg
008 jane /data/jane_contact_07292018.csv
009 kwood /data/kwood_contact_0404201.csv
010 pchow /data/pchow_contact_05172019.csv

the file "list.txt" contains three columns: line number, username, and full path to the file.

4 grep 'jane' ../data/list.txt # grep searches for the text "jane" in the file list.txt in th directory data.
                                # two dots mean parent directory (or previous directory?)
This returns all the files with the pattern "jane". It also matches the file that has string "janez" within it.

Output:
001 jane /data/jane_profile_07272018.doc
004 janez /data/janez_profile_11042019.doc
005 jane /data/jane_pic_0282018.jpg
008 jane /data/jane_contact_07292018.csv


5 grep ' jane ' ../data/list.txt # I left whitespace before and after the string "jane"!!
                                 # I did this to list the files that contain jane and not janez
Output:
001 jane /data/jane_profile_07272018.doc
005 jane /data/jane_pic_0282018.jpg
008 jane /data/jane_contact_07292018.csv

Next, we'll use the cut command with grep command. 
For cut command, we'll use the whitespace character (‘ ‘) as a delimiter (denoted by -d) since the text strings are separated by spaces within the list.txt file. 
We'll also fetch results by specifying the fields using -f option.

Let's fetch the different fields (columns) using -f flag :

6 grep " jane " ../data/list.txt | cut -d ' ' -f 1 # we are using a Pipe so the output of grep will be the input of cut
                                                   # we defined the delimiter/separator to be the whitespace
                                                  # we defined the field we want, it is f1, the first column only, the line number
Output:
001
005
008

7 grep " jane " ../data/list.txt | cut -d ' ' -f 2 # again we use Pipe
                                                   # again delimiter is the whitespace
                                                   # this time we choose field 2, the second column, the username
Output:
jane
jane
jane

8 grep " jane " ../data/list.txt | cut -d ' ' -f 3 # again we use Pipe
                                                   # again delimiter is the whitespace
                                                   # this time we choose field 3, the third column, the full path to the file
Output:
data/jane_profile_07272018.doc
data/jane_pic_0282018.jpg
data/jane_contact_07292018.csv

9 grep " jane " ../data/list.txt | cut -d ' ' -f 1-3 # this time we choose field -f 1-3, a range of fields together

10 grep " jane " ../data/list.txt | cut -d ' ' -f 1,3 # this time we choose field 1,3 a set of fields together


<< THE TEST COMMAND >>
TEST COMMAND: it tests for the presence of a file
              it checks if a particular file is present in the file system.

The command test is a command-line utility on Unix-like operating systems that evaluates conditional expressions.
The syntax for this command is: test EXPRESSION
We do this by using the -e flag. 
This flag takes a filename as a parameter and returns True if the file exists.

We'll check the existence of a file named jane_profile_07272018.doc using the following command:

1 if test -e ~/data/jane_profile_07272018.doc; then echo "File exists"; else echo "File doesn't exist"; fi
explanation: if the file "jane_profile_07272018.doc" exists in the directory "data", print File exists else File doesn't exist and finally the inverted if (fi)
Output:
File exists

<< CREATE A FILE USING A RE-DIRECTION OPERATOR >>

We will use > to create an empty file simply by specifying the file name. 
The syntax for this is: > [file-name]

Let's create a file named test.txt using the redirection operator.

1 > test.txt # create the file test.txt
2 ls         # with the ls command I see the directory where the new file was placed
Output:
data scripts text.txt

To append any string to the test.txt file, you can use another redirection operator (>>).

3 echo "I am appending text to this test file" >> test.txt # print the result after appending this string to the file "test.txt"
4 cat test.txt # view the contents of the file
Output:
I am appending text into the text file

<< ITERATION >>
Another important aspect of a scripting language is iteration. 
Iteration, in simple terms, is the repetition of a specific set of instructions. 
It's when a set of instructions is repeated a number of times or until a condition is met. 
And for this process, bash script allows three different iterative statements:

FOR LOOP:       A for loop repeats the execution of a group of statements over a set of items.
                a for loop ierates over the elements of a sequence AND performs an operation on each element
WHILE LOOP:     A while loop executes a set of instructions as long as the control condition remains TRUE.
UNTIL LOOP:     An until loop executes a set of instructions as long as the control condition remains FALSE.

Let's now iterate over a set of items and print those items.
Bash for loop:
for i in 1 2 3; do echo $i; done # for element i in sequence: 1 2 3 print element i
Output:
1
2
3


<< FIND FILES USING a BASH SCRIPT (exercise 1) >>
    
 The   list.txt file contains the following:
        001 jane /data/jane_profile_07272018.doc
        002 kwood /data/kwood_profile_04022017.doc
        003 pchow /data/pchow_profile_05152019.doc
        004 janez /data/janez_profile_11042019.doc
        005 jane /data/jane_pic_07282018.jpg
        006 kwood /data/kwood_pic_04032017.jpg
        007 pchow /data/pchow_pic_05162019.jpg
        008 jane /data/jane_contact_07292018.csv
        009 kwood /data/kwood_contact_04042017.csv
        010 pchow /data/pchow_contact_05172019.csv

    

BASH SCRIPT (find all files named "jane" in the list.txt, store them in the oldFiles.txt)
cd ~/scripts                                        # navigate to the directory "scripts"
nano findJane.sh                                    # open the nano editor to create the script "findJane.sh"
                                                    # this script will find all files in the "list.txt" and save then in the file "oldFiles.txt"
#!/bin/bash                                         # type the shebang line for bash scripts
>oldFiles.txt                                       # create the file "oldFiles.txt" by using the re-direction operator >
files=$(grep"jane" ../data/list.txt | cut-d''-f3)   # with "grep" search for "jane" find all files that contain "jane" in the txt.file, with "cut" select space as delimiter and choose field 3 of the filename. Save result in the Variable "files"
for f in $files; do                                 # for each element in the above list
 if [ -e $HOME$f ];then                             # if the file exists in the filesystem (we examine if the files are indeed in the file system)
    echo $HOME$f >> oldFiles.txt;                   # then append the file name in the file "oldFiles.txt"
 fi                                                 # end the if command
 done                                               # end the for loop

Ctrl-o, Enter key, and Ctrl-x                       # save the bash script "findJane.sh"
chmod +x findJane.sh                                # make it executable
./findJane.sh                                       # run it
cat oldFiles.txt                                    # display contents of the file "oldFiles.txt"
                                                    # contents are: /data/jane_profile_07272018.doc and /data/jane_contact_07292018.csv (we have chosen field 3, f3)



 << RENAME FILES USING a PYTHON SCRIPT (exercise 2) >>
 
PYTHON SCRIPT (re-name files named "jane" to "jdoe". Use the bash script's output from above)
cd ~/scripts                                        # navigate to the directory "scripts"
nano changeJane.py                                  # open the nano editor to create the script "changeJane.py "
#!/usr/bin/env python3                              # type the shebang line for python scripts
import sys                                          # import necessary Python module
import subprocess                                   # import necessary Python module


f = open(sys.argv[1], "r")                         # open the file "oldFiles.txt". "oldFiles.txt" is used as an argument for this Python script.  "oldFiles.txt" is stored in the variable sys.argv[1]
                                                   # the below f.readlines(), produces a list, each element of that list is a line of the "oldFiles.txt"
for line in f.readlines():                         # for each element of the list "f.readlines()"
 old_name = line.strip()                           # remove whitespaces from each element of the list and store the output in the Variable "old_name"
 new_name = old_name.replace("jane", "jdoe")       # apply the replace() function on the Variable "old_name", store the output in the Variable "new_name"
 subprocess.run(["mv", old_name, new_name])        # use the run() function of the subprocess module to re-name the files. Here we are using a Linux command (mv) inside a Python script 
f.close()                                          # close the file "oldFiles.txt"

chmod +x changeJane.py                             # make the the script "changeJane.py" executable
./changeJane.py oldFiles.txt                       # run the script "changeJane.py" and pass the file oldFiles.txt as a command line argument (see week 6_3 Advanced Bash Concepts, the example: "we use the random-exit.py as a parameter for the retry.sh" )
cd ~/data                                          # navigate to the directory "data"
ls                                                 # display list of files in the directory "data"
                                                   # "jane" is changed into "jdoe"
"""
