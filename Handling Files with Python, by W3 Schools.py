#%%
"""
Handling Files with Python, by W3 Schools 

File handling is an important part of any web application.
Python has several functions for creating, reading, updating, and deleting files.

1 File Handling
2 Open a File on the Server
3 Read Only Parts of the File
4 Read Lines
5 Close Files
6 Write to an Existing File
7 Overwrite the contents of an existing file
8 Create a New File
9 Delete a File
10 Check if File exists
11 Delete Folder

1 File Handling
    The key function for working with files in Python is the open() function.
    The open() function takes two parameters; filename, and mode.
    There are four different methods (modes) for opening a file:

    "r" - Read - Default value. Opens a file for reading, error if the file does not exist
    "a" - Append - Opens a file for appending, creates the file if it does not exist
    "w" - Write - Opens a file for writing, creates the file if it does not exist
    "x" - Create - Creates the specified file, returns an error if the file exists

    In addition you can specify if the file should be handled as binary or text mode
    "t" - Text - Default value. Text mode
    "b" - Binary - Binary mode (e.g. images)

Syntax
    To open a file for reading it:
    f = open("filepath")
    The code above is the same as:
    f = open("filepath", "rt")
    Because "r" for read, and "t" for text are the default values, you do not need to specify them.
    Note: Make sure the file exists, or else you will get an error.
"""
#%%
f = open("demofile.txt")
#demofile is in the same directory as Python
#contains the text:
#Hello! Welcome to demofile.txt
#This file is for testing purposes.
#Good Luck!    
#%%
"""
2 Open a File on the Server
Assume we have the following file, located in the same folder as Python:
To open the file, use the built-in open() function.
The open() function returns a file object, which has a read() method for reading the content of the file:
"""
#%%
f = open("demofile.txt", "r") #use the built-in open() function.
print(f.read()) # read method reads the whole file

#%%
"""
3 Read Only Parts of the File
By default the read() method returns the whole text, but you can also specify how many characters you want to return:
"""
#%%
f = open("demofile.txt")
print(f.read(5)) #specify how many characters you want to return
 
#%%  
"""
4 Read Lines
You can return one line by using the readline() method:
By calling readline() two times, you can read the two first lines:    
By iterating over the lines of the file, you can read the whole file, line by line:    
"""
#%%
f = open("demofile.txt")
print(f.readline())   
#%%
f = open("demofile.txt")
print(f.readline())
print(f.readline())
#%%
f = open("demofile.txt")
for x in f:  # the for loop iterates over each line of the text 
  print(x)
    
#%%  
"""
5 Close Files
It is a good practice to always close the file when you are done with it.
open/read/close
"""
#%%
f = open("demofile.txt", "r")
print(f.readline())
f.close()

#%%
"""
6 Write to an Existing File
I will use demofile2
I created it by copying the contents of demofile
I will append to demofile2.txt the phrase: Now the file has more content!
So, I have the existing file demofile2.
I will append to it

I add this parameter to the open() function: "a" - Append - will append to the end of the file
Then i will use the write() method, in which I will put the phrase as an argument

all txt files are in C:\Users, where python is too.
"""
#%%
f = open("demofile2.txt", "a") # this will append to the end of the file the following phrase
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt")
print(f.read())

#%%
"""
7 Overwrite the contents of an existing file

first I created demofile3 whose contents are: this is demofile 3
I will delete these contents and write new ones ("Woops! I have deleted the content!")
Note: the "w" method will overwrite the entire file.
"""
#%%
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())
#%%
"""
8 Create a New File

To create a new file in Python, use the open() method, with one of the following parameters:
"x" - Create - will create a file, returns an error if the file exist
"a" - Append - will create a file if the specified file does not exist
"w" - Write - will create a file if the specified file does not exist
"""
#%%
f = open("demofile4.txt", "a")
f.close()
# empty file is created
#%%
f = open("demofile4.txt", "a")
f.write("Append.")
# The word Append is added to the file
#%%
f = open("demofile5.txt", "w")
f.close()
# empty file is created
#%%
f = open("demofile5.txt", "w")
f.write("Write.")
# The word Write is added (there was not anything before to overwrite, text was blank )
#%%
f = open("demofile6.txt", "x")
f.close()
# empty file is created
#%%
"""
9 Delete a File
To delete a file, you must import the OS module, and run its os.remove() function:
I deleted demofile6
"""
#%%
import os
os.remove("demofile6.txt")
# demofile6 was deleted!
#%%
"""
10 Check if File exists
To avoid getting an error, you might want to check if the file exists,
before you try to delete it:  
"""
#%%
import os
if os.path.exists("demofile6.txt"):
  os.remove("demofile6.txt")
else:
  print("The file does not exist") 
# demofile6 was already deleted so I get the output The file does not exist
#%%
import os
if os.path.exists("demofile5.txt"):
  os.remove("demofile5.txt")
else:
  print("The file does not exist") 
# demofil5 was present and now it is deleted!
#%% 
""" 
11 Delete Folder
To delete an entire folder, use the os.rmdir() method:
    Note: You can only remove empty folders.
"""
#%%
import os
os.rmdir("MyFolder")
# the empty MyFolder was deleted
