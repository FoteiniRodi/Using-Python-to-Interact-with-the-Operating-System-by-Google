
#%%
"""
Using Python to interact with the operating system, by Google

Week 2 - Managing files with Python

2   MANAGING FILES AND DIRECTORIES
2.1     Working with Files
2.2     More File Information
2.3     Directories
2.4     Files and Directories cheat-sheets 
2.5     Practice quiz

SYNOPSIS

The OS module allows us to interact with the underlying system, whether it is Windows, Linux, Mac, etc.
    So, we can write and test a script on Windows OS and then run it on Linux OS.
    But, please be careful with the paths, they are different among the various OS's
    The OS module lets us do the same tasks that we can normally do when working with files from the command line
    The os.path sub-module and the associated functions,take the info provided by the operating system so that we can use it in our scripts no matter what OS we're running.
    We can check a file size or last modification date without having to know the operating system the machines running or the type of file system that the file is stored in.
How to remove/delete files
        import os
        os.remove("filename") (this is the relative path, the name of the file located in the same directory as Python)
How to rename files
        import os
        os.rename("old name", "new name") 
How to examine if a file exists or not, exists() function
        import os
        os.path.exists("filename") # relative path
        The output is true/false   
        Attention: we use the sub-module os.path
        the exists() function is very useful, as it helps us to not loose any data by mistake!
How to examine if a file exists or not, isfile() function
        import os
        file= "file.dat"
        if os.path.isfile(file):
            print(os.path.isfile(file))
        else:
            print(os.path.isfile(file))
            print("File not found")
How to find the size of a file in bytes
        import os
        os.path.getsize("filename")  
        Attention: if the file does not exist then the getsize() cannot be called
How to find the date and time, that the file was modified
        import os
        os.path.getmtime("filename")  , this only gives us the number of seconds since 01/01/1970 :):),it is a Unix timestamp 
        import datetime
        timestamp = os.path.getmtime("filename")
        datetime.datetime.fromtimestamp(timestamp)  , this gives us year, month, day, hour, minute, second,..       
        datetime module
        datetime class
        fromtimestamp method
How to transform a relative path into an absolute path (abspath function)
         import os
         os.path.abspath("spider.txt")     
         we use the relative path "spider.txt", but this function gives us the absolute path for this file
How to find the current working directory
        getcwd()  , (attention, for Linux we write pwd)
        import os
        print(os.getcwd()) # this displays our current working directory, takes no arguments
How to create a new directory (new folder inside our cwd)
        mkdir()        
        os.mkdir("new_dir") 
        # we can name our new directory/file folder as we wish
        this creates a new file folder named "new_dir" in my current working directory 
How to change the working directory
        chdir()
        os.chdir("new_dir") # we pass the directory we want to go to, as a parameter
        print(os.getcwd())
        # This changes my working directory from ... to  C:\Users\jimko\new_dir
How to remove/delete a directory
        rmdir()
        os.rmdir("new_dir")
        # this removes the new file folder, named "new_dir", from my current working directory C:\Users\jimko
        # also, the directory we want to remove/delete must be empty otherwise we get an error
How to view the contents of a directory (as a python list)
        os.listdir()
        import os
        os.listdir("C:/Users/jimko") # absolute path
        # this creates a list! The elements are strings that originate from the names of the directories and the files inside the working directory
How to find out if something is a file or a directory? (output: True or False)
        NOTE: should I use absolute paths here? Because it does not recognise the directories otherwise!
        os.path.isdir()
        import os
        os.path.isdir("absolute path")
How to Classify the contents of a directory as files or directories
        # apply the function os.listdir(absolute path) to the directory we examine. 
        This creates a list based on the names of the contents of the directory
        # assign the Variable "dir" to the directory we examine
        # apply a FOR LOOP to iterate over the list elements (over the names of the contents) 
        (iterate: examine each list element one by one)
        # apply the os.path.join() function to create a string which concatenates/joins the name of initial directory AND the name of file/directory
        inside the initial directory, into one single name. We give each content a name this way
        # now all the contents of the initial directory have a name (fullname) that: contains their own name and also the name of the initial directory
        # apply an IF CONDITION, for each iteration, specifically the os.path.isdir for each content
        # if content is a directory, then print contentA is directory
        # else, print contentA is file
        The purpose of the os.path.join() function is to create a string containing cross-platform concatenated directories.
        By using os.path.join we can concatenate directories in a way that can be used with other os.path() functions.
        By using the os.path.join function instead of explicitly adding a slash, we can make sure that our scripts work with all operating systems.
"""

"""
2.1     WORKING WITH FILES
To:  rename, delete, move files 
    or to 
    get information about a file, like the time it was last modified or its current size.

For these operations, we'll be using functions provided by the OS module

os.remove       delete a file, use the REMOVE function from the module OS
                syntax: 
                import os
                os.remove("filename.txt") this is the relative path
os.rename       rename a file, use the RENAME function (1st parameter is the old name, 2nd is the new name)
                syntax:
                import os
                os.rename("old name of file.txt", "new name of file.txt")                
os.path.exists  see if a file exists or not
                syntax:
                import os
                os.path.exists("filename.txt")
                the result is True or False
"""
#%%
# Example 1
# How to remove/delete a file from my directory
import os
os.remove("novel.txt") # removes the file from my computer (the file disappears from the directory)
#%%
os.remove("novel.txt") # if we try to remove it again we get an error, and also we can see the name of the file
#%%
# Example 2
# How to rename a file in my directory
import os
os.rename("myfirst_draft.txt", "finished_masterpiece.txt") # we can see the name change in the directory
#%%
"""
# Example 3
how to check if a file exists or not
(use the submodule os.path and then the exists() function. Then we get a True or False)
"""
import os
os.path.exists("finished_masterpiece.txt")
# output is True
#%%
os.path.exists("userlist.txt")
# output is False
#%%
"""
2.2     MORE FILE INFORMATION
We can get a lot more info about our files using functions in os.path module.

to see the file size, use the getsize function
to see when the file was modified, use the getmtime function
"""
# Example 4
# How to see the file size in bytes
import os
os.path.getsize("spider.txt")
# output is 204, that is in bytes
# Attention: if the file does not exist then the getsize() cannot be called and we get a FileNotFoundError 
#%%
# Example 5
# How to see WHEN the file was modified
os.path.getmtime("spider.txt")
# output is 1586031057.4660442, this is a timestamp!
# It represents the number of seconds since January 1st, 1970. 
# we will make it understandable with the code below
import datetime # import the module datetime
timestamp = os.path.getmtime("spider.txt") # assign the Variable timestamp to this huge number produced
datetime.datetime.fromtimestamp(timestamp)
# output is datetime.datetime(2020, 4, 4, 22, 10, 57, 466044)
# datetime module, then datetime class then fromtimestamp method
#A combination of a date and a time. Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.
#%%
"""
in-video question
Some more functions of the os.path sub-module include:
 getsize() and isfile() 
 which get information on the file size and determine if a file exists, 
 respectively. 
 
 In the following code snippet, what do you think will print if the file 
 does not exist?
"""
import os
file= "file.dat"
if os.path.isfile(file):
    print(os.path.isfile(file)) # this returns True if file exists and False if file does not exist
    print(os.path.getsize(file))
else:
	print(os.path.isfile(file))
    print("File not found")

#Correct 
#Awesome! Because the file does not exist, 
#getsize() will never be called and our error message will be printed instead.

#%%
"""
My example for the in-video question
"""
import os
file= "file.dat"
if os.path.isfile(file):
    print(os.path.isfile(file)) # this returns True or False
else:
    print("File not found")

# the IF condition is not true so the result of ELSE condition is displayed
#%%
import os
file= "spider.txt"
if os.path.isfile(file):
    print(os.path.isfile(file)) # this returns True or False
else:
    print("File not found")
# the IF condition is true, so the result of IF condition is displayed
#%%
    # Example 6
    # How to check if a file exists or not (with the isfile() function)
import os
os.path.isfile("file.dat") 
# output is false  
# see also example 3, the exists() function
#%%
"""
How to transform a relative path into an absolute path (abspath function)
absolute and relative paths
The abspath function, takes a file name and turns it into an absolute path
It is useful to access a file no matter what the current directory is
"""
# Example 7
# Transform a relative path of a file to an absolute path
import os
os.path.abspath("spider.txt")
# output is 'C:\\Users\\jimko\\spider.txt'

#%%
"""
2.3 DIRECTORIES

process files that are in a specific directory
python lets us create, delete and browse the contents of directories
find the current working directory
    getcwd() function
    To check which current directory your Python program 
    is executing in, you can use the getcwd method. (Attention,for linux it is pwd, prints the current working directory)

create a directory
    mkdir() function
    same name as both the Windows and Linux
    
change the directory
    chdir() function
    pass the directory I want to change to, as a parameter

remove a directory
    rmdir() function
    this function works only if the directory is empty
    
view the contents of a directory
    os.listdir() function
    returns a list of all files and sub-directories within a directory
    
which file is a file or a directory
    os.path.isdir() function 
    this will tell us which is a file which is a directory

Is the string of a list a directory?
    to see if a string of the list is a directory,  we need to use os.path.join to create the full path

My Notes:   Can I say that the directory essentialy is a file folder?
            And a file is a text file, a csv file etc.?
"""
# Example 8
# Display the name of my current working directory
import os
print(os.getcwd())
# This tells me the name of my current directory in Windows OS)
# output is C:\Users\jimko
#%%
# Example 9
# Create a new empty folder in my current working directory (we provide the name as an argument)
os.mkdir("new_dir")
# this creates a new file named "new_dir" in my current working directory C:\Users\jimko

#%%
# Example 10
# Change my current working directory (provide the name of the directory I want to go to, as an argument)
os.chdir("new_dir")
print(os.getcwd())
# This changes my working directory from C:\Users\jimko to  C:\Users\jimko\new_dir
# output now is C:\Users\jimko\new_dir
#%%
os.chdir("C:/Users/jimko") # I changed to forward slash
print(os.getcwd())
# This changes my working directory from C:\Users\jimko\new_dir back to C:\Users\jimko
#I changed back into my initial working directory C:\Users\jimko
#%%
# Example 11
# Remove/delete a file from my current directory (we provide the name as an argument)
os.rmdir("new_dir")
# this removes the new file named "new_dir" from my current working directory C:\Users\jimko

#%%
# Example 12
# Display the contents of my current working directory as elements of a python list. The elements are strings
import os
os.listdir("C:/Users/jimko")
# This creates a list. The elements of this list are strings. They are the names of the files and folders in my current working directory
#['.anaconda',
# '.astropy',
# '.conda',
# '.condarc']

#%%
"""
Example 13
How to check if something is a file or a directory(folder)
Is it a file or a directory? (output: True or False (True= it is a directory and False=it is not a directory)
"""
import os
os.path.isdir("C:/Users/jimko")

# a file stores data
# a directory(or folder) stores files and other folders
# a directory(folder) is used to organize files in our computer
# folders themselves take up virtually no space on the hard drive
#%%
import os
os.path.isdir("C:/Users/jimko/.anaconda")

#%%
import os
os.path.isdir("C:/Users/jimko/spider.txt")

#%%
"""
Example 14
How to check if the contents of a directory, are files or folders (files or directories)
use the isdir() function and use the join() function to produce a name for each content, recognizable by all Operating Systems
Classify the contents of a directory, as files or directories
"""
import os
os.listdir("C:/Users/jimko")                # this creates a list of strings. Each string is the name of the file/file folder within the directory
dir = "C:/Users/jimko"                      # assign the Variable "dir" to the absolute path of the directory
for element in os.listdir("C:/Users/jimko"):   # FOR LOOP over the list. We iterate over the list contents (we examine each element one by one) 
    fullname = os.path.join(dir, element)      # we apply the join function of the os.path sub-module. It takes 2 arguments. The absolute path of the directory and the name of the file/file folder. The two names are joined in a way that the resulting path is recognized by many Operating Systems. We assign the Variable "fullname" to the result of this function (the joined names) 
    if os.path.isdir(fullname):             #Finally, we use that fullname to call the os.path.isdir function, to check if it's a directory or a file
        print("{} is a directory".format(fullname)) # the if condition is True, it is a directory
    else:                                           # the if condition is False, it is a file
        print("{} is a file".format(fullname))

# *the join function adds a slash bteween two strings / or \ so we can work with all OS's!
#  the join function let's us be independent from the operating system again
        
#%%
"""
2.4 FILES and DIRECTORIES cheat-sheets 

Check out the following links for more information:

https://docs.python.org/3/library/os.html
https://docs.python.org/3/library/os.path.html
https://en.wikipedia.org/wiki/Unix_time
"""

"""
2.5 PRACTICE QUIZ

Question 1
The create_python_script function
    -creates a new python file in the current working directory, 
    -adds the line of comments to it declared by the 'comments' variable, and 
    -returns the size of the new file. 
Fill in the gaps to create a script called "program.py".
"""
#%%
import os                                           # we have to import the OS module so we can use the os.path sub-module later
def create_new_python_file(filename):                 # we create a new function that eventually will tell us the number of bytes for each Python file
    comments = "# Start of a new Python program"    # we introduce a Variable which is a string that will appear at the beginning of our .py file
    with open("program.py", "w") as file:           # we create a python file that did not exist before, we can use the write method (see Week 2, 1.4 Writing files)
        file.write(comments)
    filesize = os.path.getsize(filename)            # we call the function os.path.getsize and assign to its result the Variable "filesize"
    return(filesize)                                # we want our function "create_python_script" to return the number of bytes of our file
    
print(create_new_python_file("program.py"))           # finally, we put our new function to work for a specific Python file
                                                    # we created both a new function and a new python file. 
# please mind the indentation!

# we construct the function "create_new_python_file" with one parameter called "filename".(parameter/Variable: filename)
# we want this function to:      create a new py file in our working directory
#                                add the text "# Start of a new Python program" at the first line of the py file
#                                calculate the size of this py file and return it  (when using return I extract a value from the function. The relevant Variable is "filesize" and its value is 31 as we will see                
# finally, we call the function by providing the argument "program.py". This is the argument/value for the parameter/Variable "filename".
# we want to see the final result after calling the function, so we use the  print() function



#%%
"""
Question 2
The new_directory function 
    -creates a new directory called Python Programs inside the current working directory, 
    -then creates a new empty py file called script, inside the new directory, and 
    -returns a python list of files in that directory. 
Complete the function to create a file "script.py" in the directory "PythonPrograms".

"""
import os
def create_new_directory(directory, filename):             # we create a new function that eventually will produce a list with the contents of the new directory       
    if not os.path.exists(directory):               # if the directory does not exist (which ha-ha is true because we want to create it. This is like "initializing")
        os.mkdir(directory)                         # create the directory
        fullname = os.path.join(directory, filename)# call the os.path.join function in order to join the paths of the directory and the file it contains, into a path that is recognizable by all Operating Systems. To the result of this function, assign the Variable "fullname"
        file = open(fullname, "w")                  # open/read/close approach. create a new file which will be named after the Variable "fullname". The new file is created inside the new directory
        file.close()                                # close the file (here we use the open,read, close approach. Ofcourse we do not read it but create it)
    return os.listdir(directory)                    # we want our function "new_directory" to return a list with the contents of the directory we just created (that is why we use the os.listdir function)

print(create_new_directory("PythonPrograms", "script.py")) #  # finally, we put our new function to work (and we provide the name for the directory and for the one file it contains)

"""
Definitions
file
directory = folder that stores other folders and also files

# a file stores data
# a directory(or folder) stores files and other folders
# a directory(folder) is used to organize files in our computer
# folders themselves take up virtually no space on the hard drive
"""       
