#%%
"""
Using Python to interact with the operating system, by Google
Week 2 - Managing files with Python
1   READING AND WRITING FILES
1.1     Programming with files          
1.2     Reading files                   
1.3     Iterating through Files
1.4     Writing Files
1.5     Reading and Writing Files cheat-sheet
1.6     Practice Notebook: Text files
"""
#%%
"""
1.1     Programming with files
Absolute Path (full path)
An absolute path is a full path to the resource in the file system.
We call it absolute path because it doesn't matter where in the file system our script is running, the absolute path will always lead us to the resource. 
Relative Path (portion of the path)
Relative paths use only a portion of a path to show where the resource is located in relation to the current working directory. 
Relative paths are a shortcut that you can use so you don't have to write out the full file path. 
But keep in mind, they only make sense relative to the current location.
I can use the absolute path which is the full name of the path. 
I can use also the relative path but after placing the txt file in C:\Users\jimko which is the directory where Python is placed.
1.2     Reading files 
Reading files with: the "open/use/close" approach
                    Open a file 
                    Read the file (with the readline method or the read method)
                    Close the file
   
create the txt file "spider" containing the kid's poem (place it in the directory where Python is)
file = open(path to the txt file)   # here we create a new file object and assign to it a Variable called 'file'
print(file.readline())              # here we read the file with the readline() method)
                                    # the readline() method lets us read a single line in the file
print(file.readline())              # executing this again, gives us the second line of the file contents
print(file.read())                  # The read() method lets us read all the lines in the file
file.close()
Readline () method, lets us read a single line in the file.
Each time we call the readline method, the file object updates the current position in the file. So it keeps moving forward. 
Read() method, lets us read all the lines in the file
    reads from the current position until the end of the file
    Just like readline, the read method starts reading from wherever we currently are in the file
Advantages and disadvantages of the approach "open/read/close"
+ we can use a file object in other places in our code
- we have to remember to close the file each time
Reading files with: the  "with" block approach
                    open the file
                    read the file
                    (file closes automatically)
with open(path of the file) as file:
print(file.readline())              #the readline() method reads one line of the text
Advantages and disadvantages of the approach "with" block         
+ we don't have to remember to close the file
- we cannot use a file object in other places in our code, only within the "with" block
"""
#%%
# for the cmd on linux VM write : python 3
# 1
# open-read-close approach
file = open("spider.txt") # opens the file. we create a new file object and assign to it a Variable called 'file'
print(file.readline()) # reads only the first line
print(file.readline()) # reads the second line. we see that it reads from the current position onwards
#%%
file = open("spider.txt") 
print(file.read()) # reads all the lines 
file.close()  # closes the file
#%%
# 2
# with block approach
with open("spider.txt") as file:
    print(file.readline()) # read one line
#%%
with open("spider.txt") as file:
    print(file.read())      # read all lines
#%%
"""
1.3     Iterating through files
File objects can be iterated in the same way as other Python sequences like lists or strings
This is really useful when you want to process a file, line by line
Say for example you want to make a whole line, uppercase before printing it. 
So, we will use a for loop that goes over each line, 
and for each line we will make the characters uppercase with the upper() method
Empty lines explanation:
    the text file already has a new line character at the end of each line. 
    So, when Python reads the file line by line, the line variable will always have a new line character at the end. 
    In other words, the newline character is not removed when calling read line.
    When we ask Python to print the line, the print function adds another new line character, creating an empty line. 
"""
#%%
with open ("spider.txt") as file:
    print(file.read())
#%%
# 3
with open ("spider.txt") as file:
    for line in file:               # for loop. we iterate over each line of the txt file
        print(line.upper())
# unfortunately, eventhough we do convert lower to upper case we also get spaces between the lines
#%%
"""
How to avoid empty lines
     use the strip method before the upper method
     we are iterating line by line, and the strip() command is used to remove extra whitespace.
"""
#%%
# 4
with open ("spider.txt") as file:
    for line in file:
        print(line.strip().upper()) # remove newline characters, convert to uppercase
#we use the strip method before the upper method to remove spaces between the lines
#%%
"""
read the file lines into a list (in other words, transform the text into a Python list. Each line of the text will be an element of the list)
(create a list, whose elements are the lines of our text file)
we open out txt file as an object
then we create a new object, the list. This new object comes from applying the readlines method on the first file object
"""
#%%
# 5
#Convert a txt file into a list.
#Each line of the text becomes an element of the list.
#(In other words, convert lines of a txt file into elements of a list)

file  = open("spider.txt") # open the text file (open it as an object)
listA = file.readlines() # This is the list. The list is a new object, equal to the result of applying the readlines() method on the initial file object
file.close()
listA.sort() # sort alphabetically the lines(elements of the list)
print(listA) # we display the list, with its elements separated by a comma.
            #we also see the newline character \n ,which was already at the end of each line on the txt file


#%%
"""
1.4     Writing files
How to write content into a file
(3 ways, append "a", write "w", create "x")
we use the "with block" (which closes the file automatically)
we use two arguments and the w is for writing contents into the file
the write method writes contents to the file
Please remember
    file objects can be opened in several different modes
    a mode is similar to a file permission and it governs what we can do with the file we just opened
    1   "r" mode, read-only
        by default, the open function uses the "r" mode, which means read-only (we can only READ the file, nothing else)
        we can skip writing "r" since it is used by default
    2   "w" mode, write-only
        when using "w" mode, it means we are opening the file for write-only. 
        This can CREATE a file that did not exist before. But if the file exists, we will OVER-WRITE IT!
        with "w" mode, we cannot read the contents of the file 
    3   "a" mode, append to the end
        use "a" mode, to append content to the end of an existing file
    4   "r+" mode, read-write
        can both read contents and overwrite them
    
example: 
    when opening a log file with events, use append mode because write mode will overwrite it and we will loose its contents!!
    if we absolutely have to use the write mode, then FIRST CHECK IF THE FILE ALREADY EXISTS 
additional mode https://docs.python.org/3/library/functions.html#open
'r'     open for reading (default)
'w'     open for writing, truncating the file first
'x'     open for exclusive creation, failing if the file already exists
'a'     open for writing, appending to the end of the file if it exists
'b'     binary mode
't'     text mode (default)
'+' open for updating (reading and writing)
"""
#%%
# 6
# Create a new txt file with append mode and write method
with open("kitty.txt", "a") as file:
    file.write("The kitty is white.") # the write method writes contents to the file
# the file kitty did not exist but I created it with append-a
#%%
# 7 
#Append content to the end of an existing txt file with append mode and write method
with open("kitty.txt", "a") as file:
    file.write("The kitty is also fluffy.") 
# now the file kitty exists, I appended another phrase at the same line
#%%
#    8
#Create a new txt file with write mode and write method

with open("doggy.txt", "w") as file:
    file.write("The doggy is golden.")
# the file doggy did not exist but I created it with write-w
#%%
#    9
#Over-write the content of an existing txt file with write mode and write method
with open("doggy.txt", "w") as file:
    file.write("The doggy is chocolate brown.")
# now the file doggy exists, BUT I deleted its content with the new phrase (the new phrase overwrites the old one!)
#%%
#    10
#Create a new txt file with x mode and write method
with open("piggy.txt", "x") as file:
    file.write("The piggy is pink.")
# the file piggy did not exist but I created it with "x"
# the file created with x mode, cannot be altered/overwritten?++
#%%
with open("piggy.txt", "x") as file:
    file.write("The piggy is hungry.") 
# now the file piggy exists, and I cannot change it with "x", I get an ERROR

#%%
"""
PRACTICE NOTEBOOK: Reading and Writing Files
Let's say we have a text file containing current visitors at a hotel. 
We'll call it, guests.txt. 
Run the following code to create the file. 
The file will automatically populate with each initial guest's first name on its own line.
1 - create the text file "guests" based on a list
we see no output, but the file is created in the directory where Python is.
we use the open/read/close approach
"""
#%%
# 11.1
# convert a list into a txt file
guests = open("guests.txt", "w") # here we create a new object called "guests". 
                                #"guests" will be a text file. We create it with the write mode and the write method
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"] #this is the list we have, it contains first names as elements

for element in initial_guests: # this is iteration (5 elements so 5 iterations). It is a for loop which goes over every element in the list
    guests.write(element + "\n") # with the write method applied on the file object guests, we add a new line for each element of the list
    
guests.close()

# for each element in the list, write the element and also the new line character
#%%
"""
2 - See the contents of the text file "guests".
To see the contents of the newly created guests.txt file,run the following code.
We use the "with" block approach, that closes the file automatically.
"""
#%%
# 11.2
# display in the Python console the lines of a text file
with open("guests.txt") as file: 
    for line in file:# iteration on a text file. It is a for loop which goes over each element=line of the text file
        print(line)     # this prints each line of the txt file (the text file already has a new line character at the end of each line and Python reads that too )
# we can iterate also on text files. Actually, we iterate over the lines of the text
#%%
"""
3 - Update the text file with new guests
We will add new guests from the list "new_guests", to the existing text file.
The previous output shows that our guests.txt file is correctly populated with each 
initial guest's first name on its own line. Cool!
Now suppose we want to update our file as guests check in and out. 
Fill in the missing code in the following cell to add guests 
to the guests.txt file as they check in.
"""
#%%
# 11.3
# append content to an existing txt file
new_guests = ["Sam", "Danielle", "Jacob"] # this is a new list

with open("guests.txt", "a") as file: # now we use the append "a" mode
    for element in new_guests: # iterate over the new list. Add each element=list of the list "new_guests", to the existing text file "guests"
        file.write(element + "\n") # again insert a new line for every element of the above list
file.close()
# the text file "guests" now, is updated
#%%
"""
4 - See the contents of the updated text file "guests".
To check whether your code correctly added the new guests to the guests.txt file,
run the following cell.
"""
#%%
with open("guests.txt") as guests:
    for line in guests:  # iteration on a text file.
        print(line)
# see above 11.2
#%%
"""
5 - Remove form the text file "guests", the guests who have checked-out
We will remove those guests from the text file, who are in the list "checked-out".
Now let's remove the guests that have checked out already. 
There are several ways to do this, however, the method we use is: 
1 Open the text file in "read" mode.
2 Iterate over each line in the text file and put each guest's name into a Python list (the temp_list)
3 Open the text file once again in "write" mode.
4 Add each guest's name in the Python list to the file one by one.
In other words
1 open the text file in mode read
2 transform the text file into a list
3 open the text file in mode read+write
4 write in the text file the elements of the list EXCEPT for the elements that are present to the checked-out list
"""
#%%
# 11.4
# create the temp_list from the text file "guests" (convert text file to a list)
checked_out=["Andrea", "Manuel", "Khalid"] # list of people who checked out. we will remove these from the text file later
temp_list=[]                                # empty list. We will create it. It will contain all elements from the lists initail_guests and new_guests

with open("guests.txt") as file: # open the text file "guests"
    for line in file:                # iterate over the contents of the text file guests (elements of the text file are its lines)
        temp_list.append(line.strip()) # we fill the empty list "temp-list"
                                    # this list will contain each line of the text file guests as an element
                                    # strip removes the inline character ( we do not want space as an element of the new list!)
print(temp_list) # I added this to see the contents of the temp_list. Contains ALL lines of the text files as elements of the list
# temp_list = initial_guests + new_guests
#%%
# convert the temp_list into a text file but using conditions (if an element is present in the  checked_out list then it will not be converted into a line in the text file)
with open("guests.txt", "w") as file: # open the text file "guests" 
    for element in temp_list: # iterate over the elements of the temp list 
        if element not in checked_out: # if the element of the list "temp_list" IS NOT present in the list "checked_out" then go ahead and write it in the text file  
            file.write(element + "\n")
# we open the guests.txt in write mode and use the write method do essentialy we over-write its old contents with new ones          
#%%
"""
6 - See the contents of the updated text file "guests".
To check whether your code correctly removed the checked out guests 
from the guests.txt file, run the following cell.
"""
with open("guests.txt") as file:
    for line in file:
        print(line)
#The current names in the guests.txt file should be: 
# Bob, Polly, Sam, Danielle and Jacob.
# see above 11.2
#%%
"""
7 - Find out if Bob and Andrea are in the text file "guests" or not
Now let's check whether Bob and Andrea are still checked in. 
How could we do this? 
We'll just read through each line in the file to see if their name is in there. 
1 create a new list that contains the names in question
2 create an empty list where we will place the guests still staying at the hotel
3 open the text file guests
4 iterate over the text file (element iterated is each line. element=name)
5 append to the empty list all guests from text file. Please remove spaces with strip () method!
6 iterate over the list guests_to_check
    if element of this list exists in list checked_in, print "element is checked in
    else (if element of this list DOES NOT exist in list checked_in), print "element is not checked in
"""
#%%
# 11.5 
#Examine if elements of a list are present or not in a text
#(list elements are equivalent to text lines)
#First convert the text to a list
#Then compare the elements of the lists

guests_to_check = ['Bob', 'Andrea']
checked_in = [] # empty list. we will populate it afterwards

with open("guests.txt") as file: # open the text file guests
    for line in file:           # iterate over each line in the text file
        checked_in.append(line.strip()) # populate the list checked_in with the lines of the text but remove newline characters first
    for element in guests_to_check: # iterate over each element of the list "guests_to_check"
        if element in checked_in: # if an element of the list "guests_to_check" is present in the text file (which we converted to the list checked_in)
            print("{} is checked in".format(element)) # then print "element" is checked in
        else:
            print("{} is not checked in".format(element)) # otherwise print "element" is not checked in

# We can see that Bob is checked in while Andrea is not.

#%%
"""
Notes from w3 schools
read() method
The read() method returns the specified number of bytes from the file. Default is -1 which means the whole file.
readline() method
The readline() method returns one line from the file.
readlines() method
The readlines() method returns a list containing each line in the file as a list item.
so, the readlines() method converts at once a text file to a python list
"""

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
#%%
"""
Using_Python-to_Interact_with_the_OS_
week 2 - Managing files with Python
3 READING AND WRITING CSV FILES
3.1     What is a CSV file?
3.2     Reading CSV Files
3.3     Generating CSV
3.4     Reading and Writing CSV Files with Dictionaries
3.5     CSV Files Cheat Sheet
3.6     Practice Quiz: Reading & Writing CSV Files
SYNOPSIS
3.2 Reading csv files
csv.reader() 
from csv to list
each row of the csv file becomes a list (each csv field becomes an element of the list)
if we have 4 fields in a row of the csv then we get a list with 4 elements
3.3 Generating csv files
csv.writer(), creates the instance writer
from list to csv
each element of the list becomes a row in the csv 
(ofcourse the element of the list can be a dictionary so our row can contain the dictionary: the values of their respective keys)
use the function writer.writerow(row), to write one row at a time or writer.writerows(rows), to write all rows at once
3.4
a) csv.DictReader   from csv to dictionary
b) csv.DictWriter   from dictionary to csv
"""


"""
3.1     What is a CSV file?
parse = αναλύω
Parsing = analyzing a file's content, to correctly structure the data
Parsing a file means analyzing its contents to correctly structure the data, and occurs while reading a file.
Until now we worked with text files (NotePad)
But data comes in a bunch of different formats besides text.
We use a bunch of different file formats to structure, store, and transport data:
    HTML: HTML is a markup format which defines the content of a webpage
    JSON: JSON is a data interchange format commonly used to pass data between computers on networks, especially the internet. 
    CSV: CSV or comma separated values is a very common data format used to store data as segment of text separated by commas. 
Below, we will use the CSV module to process CSV files.
The CSV format lets us easily store and retrieve information that we might need for our scripts 
Think of a CSV file like it's a spreadsheet, where each line corresponds to a row and each comma separated field corresponds to a column.
"""
    
"""
3.2     Reading CSV Files
We just use the reader function from the csv module, to read the contents of the CSV file.
syntax: csv.reader(csvfile, dialect='excel', **fmtparams)
csv module: module which lets us read, create and manipulate CSV files.
csv file
each line is a row and columns are separated by the comma ( a csv field is in fact a column, csv field = column)
each line represents a single data record
we have a csv file with 4 rows.
Each row contains 3 fields separated by a comma
each row corresponds to an employee
1st field is name, 2nd field is phone number and 3rd field is role
"""
# 1 Read an existing csv with csv.reader(), open/read/close approach
import csv                 # import csv module
file = open("example1.csv")   # open the csv file (we create a file object. We open the csv as a file object)
reader = csv.reader(file)     # read the csv file (we use csv.reader() method, and we create the instance reader
                               # the reader instance is our csv file which now we can read
for row in reader:        # Iterate over the  reader. It has 4 rows. Each row is a list which contains 3 elements (the 3 csv fields or columns)
    name, phone, role = row # We unpack the values of the list "row" and assign a Variable to each element.(we already know that element 0 is name, element 1 is phone number etc. )
    print("Name: {}, Phone: {},Role: {}".format(name, phone, role)) # we use the format method to display the results
    print(row) # row here is a list and its elements are the csv fields/columns
file.close() # this is the open, read,close approach so we must close the file in the end

# I open the existing csv file and read it with csv.reader() .I am opening the csv as "reader" instance
# I iterate over the reader (which is essentialy my csv). 
# I iterate over the reader rows, and each row corresponds to a csv row. The reader row is a list and the elements are the contents of the csv fields(columns)


#%%
# 2 Read an existing csv with csv.reader(), with block approach
import csv 
with open("example1.csv") as file:  # open the csv file
    reader = csv.reader(file) # read the csv file
    for row in reader:        # iterate over EACH row of the csv file
        name, phone, role =row      # unpack the elements of the list row (unpack elements/columns/fields of each csv row)
        print("Name: {}, Phone: {},Role: {}".format(name, phone, role)) # print the results with the format method
        print(row) # row here is a list and its elements are the csv fields/columns



#%%
"""
3.3     Generating CSV
We will create a csv file starting from a list.
We already know what the name of the column is ( we have a few columns/csv fields)
We will use the writer function to generate contents for the new csv file
syntax: csvwriter.writerows(rows)
This can be really helpful if you process some data in your script and you must store it in a file.
1   We will store the data that we want to write into the csv, initially into a list.
    (it is a list with 2 elements. Each element is a list too)
2   open a new csv file in "write" mode
3   call the writer function of the CSV module with the new csv file as a parameter.
4   writer.writerow(row)     we write one row at a time
    writer.writerows(rows)   we write all rows at once
"""
# 3 Create new csv with csv.writer() starting from a list

hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]] # list
with open("hosts.csv", "w") as file: # create a new csv file using the "write" mode
    writer = csv.writer(file)        # use the csv.writer() method to write into the new csv file (the Variable writer is now an instance of the csv writer class)
    writer.writerows(hosts)          # the writerows() method writes all row in the csv at once

# one list element becomes one csv row
# in other words, list element corresponds to csv row and vice versa
# here I have 2 list elements so I will create 2 csv rows.
# each element is also a list, the sub-elements of the element will become csv fields in the csv row

# in row 1, I see the element 0 of the initial list *sub-elements of element 0, become csv fields
# in row 2, I see the element 2 of the initial list *sub-elements of element 0, become csv fields
# So, essentially, I transformed a list into a csv file

## in linux command line:
#    cat hosts.csv
#    workstation.local, 192.168.25.46
#    webserver.cloud, 10.2.5.6
#%%
"""
3.4     Reading and Writing CSV Files with Dictionaries
EXAMPLE - Create a dictionary, starting from a csv
We use dictionaries, when the columns (csv field of each row) are too many and we need to remember the name for each column
We use the csv.DictReader class
syntax: csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)
csv.DictReader(), maps the information in each row to a dictionary whose keys are given by the optional fieldnames parameter.(In this example I use the 1st row csv fields as keys)
first row of csv contains the keys
subsequent rows of csv contain the values for each key
(We can then access the data by using the column names instead of the position in the row.)
"""
#%%
# 4 create a dictionary starting from an existing csv with csv.DictReader()
import csv
with open("software.csv") as file: # open the csv file
    reader = csv.DictReader(file)  # read the csv file (create the instance)
    for row in reader:                 # here we iterate over each row of the csv. First row provides the key, subsequent rows provide the values
            print("The software:{} is in version:{}, is in status:{} and  it has {} users". format(row["name"], row["version"], row["status"], row["users"]))
            print(row)              # I added this to see what exactly is the row
            
# I have a csv in which 1st row has column titles and next rows have values
# I open this csv 
# I read the csv with csv.DictReader() and also transform it into a dictionary with keys and values
# csv.DictReader() produces the instance reader
# in the reader I have rows. If I only use file as an argument then by default first csv row contains the keys of the future dictionary
# I have 4 rows in the csv. The 3 rows of it are converted into an ordered dictionary (row = ordered dictionary). An element in a dictionary is the combination Key-value
# row is an ordered dictionary (not exactly a dictionary)     
# reader row corresponds to csv row BUT it also uses first csv row as keys and then the next row as values for these keys
#%%
"""
EXAMPLE - Create a csv, starting from a dictionary
We use dictionaries, when the columns (csv field of each row) are too many and we need to remember the name for each column
We use the csv.DictWriter class
syntax: csv.DictWriter(f, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)
I start with a list.
Each element of the list is a dictionary.
A dictionary contains a key and its corresponding value.
We have 3 dictionaries (our list has 3 elements)
Each dictionary has 4 elements, 4 pairs of key:value or 4 keys
"""

#%%
# 5 Create a csv starting from a dictionary with csv.DictWriter()
import csv
users = [{"name": "Sol Mansi", "username": "solm", "department": "IT Infrastructure", "education": "self-taught"}, 
         {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research", "education": "bachelor"},
         {"name": "Charlie Grey", "username": "greyc", "department": "Development", "education": "master"}] # list. each list element is a dictionary. Each dictionary contains 4 elements. Each dictionary element is composed of Key:value
keys = ["name","username", "department", "education"] # list. each element list is a string. these are they only keys, no values
with open("csv1.csv", "w") as file:               # create a new csv
    writer = csv.DictWriter(file, fieldnames=keys)   # use the DictWriter to create the dictionary. Provide name of the new csv and also provide the csv fieldnames (the keys of the dictionary)
    writer.writeheader()                                # The writeheader() function takes no arguments.Creates the first row of the CSV based on the keys that we provided
    writer.writerows(users)                             # The writerows() function will transform each element of the list into a row (each element is a dictionary. The values of each dictionary will be placed in one row)

# dictionary: each element is comprised of Key-value pair.
# here I have a list with 3 elements
# each list element is a dictionary
# each dictionary contains 4 elements ( 4 pairs of Key-value)


#%%
"""
CSV Files Cheat Sheet
Check out the following links for more information:
https://docs.python.org/3/library/csv.html
https://realpython.com/python-csv/
"""
#%%
"""
3.6     Practice Quiz: Reading & Writing CSV Files
"""

"""
EXERCISE 1
We're working with a list of flowers and some information about each one. 
The "create_file" function writes this information to a CSV file. 
The "contents_of_file" function reads this file into records and returns the information in a nicely formatted block. 
Fill in the gaps of the "contents_of_file" function to turn the data in the CSV file into a dictionary using DictReader.
create a csv
with csv.DictReader() create a dictionary from the csv
"""
#%%
"""Question"""

import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  ___
    # Read the rows of the file into a dictionary
    ___
    # Process each item of the dictionary
    for ___:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))

#%%
"""Answer"""
# 6 Create a new csv by using the write() method to enter data into it
#   Display the contents of the csv by transforming it first into a dictionary with DictReader

import os
import csv

def create_csv(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# function that displays the contents of the csv as text
def display_csv_contents(filename):
  text = ""
  
# call the function that creates the new csv
  create_csv(filename)
  
# open the new csv 
  with open(filename) as file:
      reader = csv.DictReader(file) # open csv as instance, convert it to a dictionary. First csv row will become dictionary Keys. Subsequent csv rows will become dictionary values
      for row in reader: # iterate over each csv row ( row is an ordered dictionary. Alphabetical arrangement of keys)
          text += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
      return text # this is the result we want to extract from the function display_csv_contents

print(display_csv_contents("flowers.csv")) # here we call the function and also print its results by providing the argument which is also the name of the csv we want to create
  
# we create the function create_csv
# this function will create a new csv file with the write() method, based on the information we provide 
# next we create the function display_csv_contents with the purpose to create a text depicting the csv contents
# initially the text is empty
# then inside the function display_csv_contents, I call the function create_csv which produces the new csv
# I open the new csv as reader instance with dictreader. dictreader creates a dictionary
# I iterate over the reader rows. Each reader row is an ordered dictionary 
# OrderedDict(contains 3 elements(pairs Key-value). One csv row corresponds to one OrderedDict
# I attach the iterations results on the empty text string. Way of iteration n=n+1 (attach each iteration result to the previous one. I use new line character for each result)
# The value I want to extract from the function display_csv_contents, is the "text"
# finally I call the function display_csv_contents by providing the argument "flowers.csv" and print it too
# at the same time that I am calling the function display_csv_contents, I also call the function create_csv that creates the csv on which I will work on with the function display_csv_contents


#%%
"""
EXERCISE 2
Using the CSV file of flowers again, 
fill in the gaps of the "contents_of_file" function to process the data 
without turning it into a dictionary. 
How do you skip over the header record with the field names?
"""
#%%
"""Question"""
import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  ___
    # Read the rows of the file
    rows = ___
    # Process each row
    for row in rows:
      ___ = row
      # Format the return string for data rows only

          return_string += "a {} {} is {}\n".format(___)
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))




#%%
"""Answer"""
# 7 Create a new csv by using the write() method to enter data into it
#   Display the contents of the csv by using the reader() 
#  be careful to not print the first csv row that contains the Keys!

def create_csv(filename):
  with open(filename, "w") as file:
    file.write("color,name,flowertype\n")
    file.write("pink,carnation,annual\n")
    file.write("yellow,daffodil,perennial\n")
    file.write("blue,iris,perennial\n")
    file.write("red,poinsettia,perennial\n")
    file.write("yellow,sunflower,annual\n")

def display_csv_contents(filename):
  text = ""
  
  create_csv(filename)
  
  with open(filename) as file:
      reader = csv.reader(file)
      next(reader, None)
      for row in reader:
          color, name, flowertype = row
          text += "a {} {} is {}\n".format(color, name, flowertype)
      return text
  
print(display_csv_contents("flowers.csv"))

          
# we create the function create_csv
# this function will create a new csv file with the write() method, based on the information we provide 
# next we create the function display_csv_contents with the purpose to create a text depicting the csv contents
# initially the text is empty
# then inside the function display_csv_contents, I call the function create_csv which produces the new csv
# I open the new csv as reader instance with csv.reader()   
# each reader row (corresponds to a csv row) and it is a list (elements of the list are the contents of each csv field)
# I use the next(reader, None) in order to ignore the first row of the csv which contains the Keys/Titles of columns-csv fields
# I iterate over the reader rows
# I attach the iterations results on the empty text string. Way of iteration n=n+1 (attach each iteration result to the previous one. I use new line character for each result)
# The value I want to extract from the function display_csv_contents, is the "text"
# finally I call the function display_csv_contents by providing the argument "flowers.csv" and print it too
# at the same time that I am calling the function display_csv_contents, I also call the function create_csv that creates the csv on which I will work on with the function display_csv_contents

# In exercise 6 I created a dictionary from the csv(csv.DictReader) and iterated over the dictionary to construct the text
# In exercise 7 I created list from the csv (csv.reader) and iterated over the list to construct the text
# I changed the sequence of the arguments within the write() method   

#%%
"""
# 8
exercise 3
In order to use the writerows() function of DictWriter() to write a list of dictionaries to each line of a CSV file, what steps should we take? 
answer
-create an instance of the DictWriter() class 
(We have to create a DictWriter() object instance to work with, and pass to it the fieldnames parameter defined as a list of keys.)
-write the fieldnames parameter into the first row, using writeheader()
(The non-optional fieldnames parameter list values should be written to the first row.)
-open the csv file using: with open
(The CSV file has to be open before we can write to it.)
"""
#%%
"""
exercise 4
Which of the following is true about unpacking values into variables when reading rows of a CSV file? (Check all that apply)
- we need the same amount of Variables as there are columns of data in the csv
(We need to have the exact same amount of variables on the left side of the equals sign as the length of the sequence on the right side when unpacking rows into individual variables.)
- rows of a csv can be read using both a csv.reader() and a csv.DictReader()
(Although they read the CSV rows into different datatypes, both csv.reader or csv.DictReader can be used to parse CSV files.)
- an instance of the reader class must be created first
(We have to create an instance of the reader class we are using before we can parse the CSV file.)
"""
#%%
"""
exercise 5
If we are analyzing a file's contents to correctly structure its data, what action are we performing on the file?
Parsing
Parsing a file means analyzing its contents to correctly structure the data. As long as we know what the data is, we can organize it in a way our script can use effectively.
"""

#%%
"""
SYNOPSIS
csv.reader()	converts a csv into a list
    			each row of the csv becomes a list
                if we have 4 fields in the csv, then we have 4 elements in the list
                csv rows = lists
                csv fields in each row = elements of the list
csv.writer()	converts a list into a csv
    			each element of the list becomes a row in the csv
csv.DictReader()	converts a csv into a dictionary (with keys and values)
        			first row of csv provides the keys
        			following rows of csv provide the values for the keys
                    if we have 4 rows in the csv, then we get 3 dictionaries
csv.DictWriter()	converts a dictionary into a csv
        			first row of csv contains the Keys
        			subsequent rows of csv contain the Values
        			if we have 3 dictionaries, we get 4 rows
CSV  and LIST
csv row = list
csv field = list element
CSV and DICTIONARY
csv first row = dictionary Keys
csv subsequent rows = dictionary values
"""
#%%
"""
Using_Python-to_Interact_with_the_OS_
week 2 - Managing files with Python
4 MODULE REVIEW
For this lab, imagine you are an IT Specialist at a medium-sized company. 
The Human Resources Department at your company wants you to find out how many people are in each department. 
You need to write a Python script that reads a CSV file containing a list of the employees in the organization,
 counts how many people are in each department, and then generates a report using this information. 
The output of this script will be a plain text file.
"""
#%%
import csv

def read_employees(filepath): # 1st function
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True) # The main purpose of this dialect is to remove any leading spaces while parsing the CSV file.
    reader = csv.DictReader(open(filepath), dialect='empDialect')         # open the csv file as reader (an instance of the dictreader)
    
    employee_list = [] # empty list, will be populated below
    for row in reader: # here we iterate over each row of the csv. First row iteration provides the key, subsequent row iteration provides the values
        employee_list.append(row) # we construct the employee_list of ordered dictionaries by appending each row after the other
    return employee_list # employee_list contains elements which are ordered dictionaries. 
employee_list = read_employees("employees.csv")
print(employee_list)

def process_data(employee_list): # 2nd function it produces the dictionary 
    department_list = [] # empty list, will be populated below
    for employee_data in employee_list: # iterate over the elements of the employee_list
        department_list.append(employee_data["Department"]) # populate the department_list by choosing from each element(each ordered dictionary) only the first part of each element (the Department)
    department_data = {} # empty dictionary, will be populated below
    for department_name in set(department_list): # set() method, converts iterable elements to distinct elements. Syntax : set(iterable)
        department_data[department_name] = department_list.count(department_name) # creates the Key:value pair for the new dictionary
    return department_data
    
department_data = process_data(employee_list)
print(department_data)  
   
def write_report(dictionary, report_file):
    with open(report_file, "w+") as file: # open and create the text file 
        for k in sorted(dictionary): # iterate over each dictionary element (each Key:value pair). Attention! Iteration happens only over the dictionary Keys
            file.write(str(k) + ":" + str(dictionary[k]) + "\n") # for each iteration write on the text file the Key, then :, then the value of the Key, then the new line character
    file.close()
write_report(department_data, "report.txt") # call the function by providing the name of the new text file to be created

# I have already constructed a csv file, employees.csv
#Department, Username, Full Name
#Development, Audrey, Audrey Miller
#Production, John, John Snow
#Development, Mary, Mary White
#Production, George, George Brown
#IT infrastructure, Anthony, Anthony Gibbs

# 1st FUNCTION "read_employees", creates a list of dictionaries*(a list whose elements are dictionaries. A dictionary contains  Key:value pairs as its elements)
# in earlier Python versions, DictReader produced indeed a list of dictionaries
# currently, DictReader produces by default a list of ordered dictionaries where the keys are ordered as in the header of the csv
# csv.DictReader(), Creates an object (reader) that operates like a regular reader but maps the information in each csv row to a dict whose keys are given by the optional fieldnames parameter.
# create an empty list of employees (a list with elements that are dictionaries)    
# 1st csv row =  Department,Username,Full Name
# 2nd csv row = Development,Audrey, Audrey Miller
# 2nd csv row becomes first element of the list. The element is an ordered dictionary, ('Department', 'Development'), ('Username', 'Audrey'), ('Full Name', 'Audrey Miller')
# iterate over the reader (csv opened as an instance(reader) of the dictreader)
# first iteration provides the Keys to the ordered dictionaries
# subsequent iterations provide values for the Keys and we get the Key:value pair
# 1st iteration (1st csv row) provides Keys
# 2nd iteration (2nd csv row): [OrderedDict([('Department', 'Development'), ('Username', 'Audrey'), ('Full Name', 'Audrey Miller')])

# 3rd iteration (3rd csv row): [OrderedDict([('Department', 'Development'), ('Username', 'Audrey'), ('Full Name', 'Audrey Miller')]), 
#                              OrderedDict([('Department', 'Production'), ('Username', 'John'), ('Full Name', 'John Snow')])]
# finallly the list of ordered dictionaries is: [OrderedDict([('Department', 'Development'), ('Username', 'Audrey'), ('Full Name', 'Audrey Miller')]), 
#                                               OrderedDict([('Department', 'Production'), ('Username', 'John'), ('Full Name', 'John Snow')]), 
#                                               OrderedDict([('Department', 'Development'), ('Username', 'Mary'), ('Full Name', 'Mary White')]), 
#                                               OrderedDict([('Department', 'Production'), ('Username', 'George'), ('Full Name', 'George Brown')]), 
#                                               OrderedDict([('Department', 'IT infrastructure'), ('Username', 'Anthony'), ('Full Name', 'Anthony Gibbs')])]
# so essentially we get a list of ordered dictionaries
# we append each iteration result to the empty list .Each iteration provides an element to the list
# the result of the function we want to extract is the list, we do this by using the return statement
# we assign a Variable to the result of the function and at the same time we call the function by providing the argument(value) "employees.csv". ("employees.csv" is the relative path of an existing csv file)
# we will use this Variable in another function below

# 2nd FUNCTION "process_data" takes as a parameter the result of the 1st function (Variable=employees_list, value=list of ordered dictionaries )
# create an empty list "department_list" 
# i will populate "department_list" only with the elements of the "employee_list" which contain the Key 'Department'
# 1st list element is ordered dictionary. The ordered dictionary contains three sub-elements 
# employee_data["Department"] is list element 1[dictionary sub-element 1(Key)] = value of sub-element 1(Key) it is Development
#                               list element 2[dictionary sub-element 1(Key)] = value of sub-element 1(Key) it is Production
# so the "department_list" looks like this, ["Development", "Production", "Development", "Production", "IT Infrastructure"] and it is a list of strings (elements of list are strings)

# create an empty dictionary "department_data"
# set(iterable), A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
# set(iterable) syntax: the parameter is required. Iterable is a sequence, collection or an iterator object (list, tuple, dictionary etc)
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
# after applying the set() function on the "department_list" we get the set {'IT Infrastructure', 'Production', 'Development'}
# the set contains strings as elements but now we have unique strings and no duplicates
# we iterate over this set
# department_data[department_name] this is the Key of the dictionary department_data and is equal to the corresponding value (remember Key:value pair is the element of dictionaries)
# dictionary[Key] = value. This is like asking what is the value for that Key in the dictionary. Here we use this to construct the dictionary
# list.count(value), The count() method returns the number of elements with the specified value. so for the list "department_list" we want to count the number of elements that are unique
# note that we are iterating over the set(list) where elements are unique and not on the list itself where there are duplicates
# so the result of each iteration is a Key:value pair (a dictionary element). Key is the Department and value is number of apperances of that Department
# we have 3 elements in the set so we do 3 iterations. 1st iteration gives us {"Development":2}, 2nd iteration {"Development":2, "Production:2"}, 3rd iteration {"Development":2, "Production:2", "IT Infrastructure":1}
# # the result of the function we want to extract is the dictionary so we use the return statement for the Variable "department_data"
# Finally we call the function by providing the argument "employee_list" (employee_list is the output of the 1st function)
# Our dictionary looks like this
#{'Production': 2, 'IT infrastructure': 1, 'Development': 2}

# 3rd FUNCTION "write_report", will produce a text file within which, the dictionary "department_data" will be written
# sorted() function applied on the dictionary produces another dictionary where the Keys are alphabetically sorted?I think yes:)
# the text file we create her will have the contents
# Development:2
#IT infrastructure:1
#Production:2

#%%
"""
Using Python to interact with the operating system, by Google
WEEK 3 – Regular Expressions
1      REGULAR EXPRESSIONS
1.1    Intro to Module 3: Regular Expressions
1.2    What are regular expressions?
1.3    Why use regular expressions?
1.4    Basic Matching with grep
1.5    Practice Quiz: Regular Expressions
"""
#%%
"""
1.1    Intro to Module 3: Regular Expressions
With regular expressions, we'll be able to find and operate on text in a more flexible way than we have up until this point.
"""
#%%
"""
1.2    What are regular expressions?
A regular expression, also known as regex or regexp, is essentially a SEARCH QUERY  for text that's expressed by string pattern
With RegEx, we search for a regular expression pattern within a text and anything in the text that matches the expression is the result.
RegEx is a search query that matches the regular expression we have specified
In other words, regular expressions allow us to search strings matching a specific pattern inside a text.
RegEx helps us with text processing.
We can pull information from a file.
For example, if I have a file that lists NFS mounts and options and I want to pull only the server name, I can write a regular expression that strips each line of the excess data and returns only a list of the information I need
. We can also use command line tools that know how to apply regexs, like grep, sed, or awk
We'll check out how we can apply the regexs to processing, parsing and extracting meaning from texts read by our scripts. 
"""
#%%
"""
1.3    Why use regular expressions?
why do I need more processing power than just looking for strings in a text which I already know how to do in Python? 
The answer lies in the power and flexibility of regular expressions
"""
# EXAMPLE 1 SEARCH FOR THE NUMBER BETWEEN SQUARE BRACKETS WITH string slicing
# We want to extract the process identifier from this line, which is a number between the square brackets 12345. 
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
position = log.index("[") # index() method to find the 1st [
print(log[position+1:position+6]) # string slicing to get only the 5 characters
#print(position)

# log is our text
# The index() method finds the first occurrence of the specified value and gives us its position as a number
# Syntax: string.index(value, start, end)
# here log.index("[") is 39. The position of [ in the text "log" is 39
# position Variable is equal to 39
# I will apply the slice syntax on our text with regard to the position Variable
# slice syntax:     string[start index: end index]
#                   string[start index of position: end index of position]
# I have a 5 digit number I want to retrieve, so I chose start index of position=1 (0 is the bracket!) and end index of position=7 (end index is also the bracket but by default excluded, so up to 6 )

# One problem is we don't know for sure how long the process ID string will be in all cases.
# someone may use more square brackets
#%%
# EXAMPLE 2 SEARCH FOR THE NUMBER BETWEEN SQUARE BRACKETS WITH regex
# Instead, we could use a regular expression to extract the process ID in a more robust fashion
import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
x = re.search(r"\[(\d+)\]", log)
print(x[1]) # print the 1st occurence of the match object?

# The regular expression is regex = r"\[(\d+)\]"
# r prefix: the 'r' means the the following is a "raw string", ie. backslash characters\ are treated literally instead of signifying special treatment of the following character
# \d	Returns a match where the string contains digits (numbers from 0-9)
# we search for the number sequence between the []

# regex is a more reliable way to search for text

# syntax for search(): search(regex, text)
# x is the match object

#%%
"""
1.4    Basic Matching with grep
we can use regular expressions in the command line
grep is a command line tool that applies regexes (regular expressions)
grep prints any line that matches our query
we will use grep to find words inside the /usr/share/dict/words file
This is a file that some spell-checking programs use to verify if the word exists or not. 
This file contains one word per line. 
We'll start by looking at words that contain the particle thon. Let's see what happens.
grep is a command-line utility for searching plain-text data sets for lines that match a regular expression. 
Its name comes from the ed command g/re/p (globally search for a regular expression and print matching lines), which has the same effect
"""
# EXAMPLE 3
# Use the grep command to search if a string is present, specifically the string "thon"
In Linux command line write the following:
grep thon /usr/share/dict/words # search for matches of thon in the file /usr/share/dict/words

The output is:
Marathon
Phaethon
Python
diphthong
etc
"thon" is highlighted on the words (visual indicator)
the thon search is case sensitive (lowercase and uppercase are treated differently)
#%%
# EXAMPLE 4
# Use the grep command now regardless of case (uppercase or lowercase)
In Linux command line write the following:
grep -i python /usr/share/dict/words

The output is:
    Python
    Python's
    python
    python's
    pythons


#%%
# EXAMPLE 5
# Reserved Characters
# a dot . matches any character
# a dot . is a wildcard ( it is replaced by any character in the results

In Linux command line write the following:
grep l.rts  /usr/share/dict/words # in the l.rts the . can be any character, we will get all existing characters for this position while l_rts remains as the requested pattern

The output is:
    alerts # lerts
    blurts # lurts
    flirts # lirts

#%%
# EXAMPLE 6 caret or circumflex ^ and dollar sign $
# these are called anchor characters
# ^ indicates the beginning
# $ indicates the end
# these characters tell us where in the line the regex should match from
# One thing to remember is that the circumflex and the dollar sign specifically match the start and end of the LINE, not a string
    
 In Linux command line write the following:
     grep ^fruit /usr/share/dict/words # find all words that start with fruit
    
 The output is:
     fruit
     fruit's
     fruitcake
     fruitcakes
     fruited
     fruitful
     etc
    
 In Linux command line write the following:
     grep cat$ /usr/share/dict/words # find all words that end with cat
    
 The output is:
     Muscat
     bobcat
     cat
     copycat
     ducat
     lolcat
     muscat
     etc
    
#%%
"""
1.5    Practice Quiz: Regular Expressions
"""
# EXAMPLE 7 
"""
Question 1
When using regular expressions, 
which of the following expressions uses a reserved character that can represent any single character?
re.findall(f*n, text)
re.findall(fu$, text)
re.findall(^un, text)
re.findall(f.n, text)
Answer
The  reserved character that can represent any single character is the dot
"""
# EXAMPLE 8
"""
Question 2
Which of the following is NOT a function of the Python regex module?
re.findall()
re.search()
re.match()
re.grep()
Answer
grep is a command line tool not a python module method
"""
# EXAMPLE 9
"""
Question 3
The circumflex [^] and the dollar sign [$] are anchor characters. 
What do these anchor characters do in regex?
Answer
They match the start and end of a LINE (not start end of a string)
"""
# EXAMPLE 10 
"""
Question 4
When using regex, some characters represent particular types of characters. 
Some examples are the dollar sign, the circumflex, and the dot wildcard. 
What are these characters collectively known as?
Answer
Special characters
"""
# EXAMPLE 11
"""
Question 5
What is grep?

a command line regex tool

#%%
"""
Using Python to interact with the operating system, by Google
WEEK 3 – Regular Expressions
2 BASIC REGULAR EXPRESSIONS
2.1    Simple Matching in Python
2.2    Wildcards and Character Classes
2.3    Repetition Qualifiers
2.4    Escaping Characters
2.5    Regular Expressions in Action
2.6    Regular Expressions Cheat-Sheet
2.7    Practice Quiz: Basic Regular Expressions
synopsis
    (r"Pattern", Text)     Use
    aza                    find "aza" in the text
    ^x                     finds x only if it is at the beginning of a word
    [^x]                   find all characters except for x, EXLUSION
    p.ng                   find "p.ing" in the text, dot can be any ONE character except \n newline character
    a.e.i                  find "a.e.i" in the text, dot can be any ONE character except \n newline character
    
    (Pattern, Text, re.IGNORECASE) use the re.IGNORECASE parameter to ignore case in the text when looking for a pattern
    
    [Pp]ython              find Python or python in the text. Use a  character class[] with characters in it
    [a-z]way               find any lowercase letter of the alphabet (e.g away, highway, runway)
    cloud[A-Za-z0-9]       find any lowercase or uppercase letter or number(e.g. cloudy, cloudY, cloud9)
    [,.:;?!]               find only these punctuation symbols
    [a-zA-Z]               find only the letters in the text
    [^a-zA-Z]              find all characters EXCEPT letters 
    
    attention ^ outside[] means start, [^] means exclusion
    
    a$                    finds a only in the end of a word
    
Note: SEARCH FUNCTION RETURNS ONLY THE 1ST MATCH, findall() returns all matches as elements of a list
Regular Expression (regex) is meant for pulling out the required information from any text which is based on patterns. 
They are also widely used for manipulating the pattern-based texts which leads to text preprocessing and are very helpful in implementing digital skills like Natural Language Processing(NLP).
REPETITION (e.g. repeated letters before the qualifier )
    r"Pattern"           Use
    pattern*             Star is a repetition qualifier. Finds as many matches as possible of the pattern/character
                         e.g. ab*: finds 'a', 'ab', 'abb' etc. 
                         f* : find zero or more ocurrences of f
    .*                   Dot is any character except \n newline character, and star states that all characters/patterns before the star must be searched in the text
    Py.*n                now the dot does not represent any ONE character, but all possible characters between Py and n (Pygmalion)
                         text=Pygmalion, match = Pygmalion
                         text=Python programming, match is Python programmin
                         star * is greedy
    Py[a-z]*n            now we don't have a dot, but all lowercase letters
                         text = Python programming, match = Python because it stopped at the whitespace which is not a letter
    Py[a-z]*n            find all lowercase letters between Py and n
                         text = Pyn, match = Pyn. Now we see we had zero occurrences before the star, but it is ok
    pattern+             The plus char represents one or more repetitions of the preceding regex. 
                         For example, ab+ will match “abc” or “abbc”, but will not match “ac”.                     
                         The + returns as result the WHOLE STRING that satisfies the condition
                         f+: find ONE or more occurrences of f
                         o+l+: find the sequence 'ol'. Returns the sequence ol
    [aA].*[aA]          find a word that starts with A or a has any characters (return them all) in between and ends with a or A
    pattern?            The question mark symbol is yet another multiplier. 
                        It means either zero or one occurrence of the character before it.
    pattern *           ab*: finds a or ab or abb or abbb (finds zero or more occurrences of the preceding pattern)
    pattern +           ab+: finds ab or abb or abbb (finds one or more occurrences)
                             does not find a!
    pattern ?           ab ?: finds a or ab or abb or abbb (finds zero or more occurrences of the preceding pattern)
    *, +, ?             they are greedy qualifiers. They match as much text as possible
   
    a{3,5}              will match from 3 to 5 'a' characters a{m, n}
                        Omitting m specifies a lower bound of zero, and omitting n specifies an infinite upper bound.
    a{4,}b              will match aaaab or a thousand 'a' characters followed by a b, but not aaab.
    a{6}                will match exactly six 'a' characters, but not five a{m}
    a{3,5}?             This is the non-greedy version of the previous qualifier.
    
    
Egrep command
egrep is a pattern searching command which belongs to the family of grep functions
syntax: egrep “search_string” filename
example: egrep debian samplefile.txt search for the word debian in the text file sample file
ESCAPE CHARACTERS
We can use \ to escape any special characters
escape = the characters lose their special character meaning and become simple characters
e.g. the dot . does not represent any character except newline, and it becomes a simple dot
Using \ ,can get really confusing with backslashes since
 they're also used to define some special string characters. 
 e.g. \n is the new line character (indicates in Python a new line)
 e.g. \t does the same for tabs
 
THEREFORE ATTENTION
when we see a \:
    - it could be escaping a special regex character
    - it could be a special string character
    - i could be used for a few special sequences that we can use to represent predefined sets of characters. 
      For example, \w matches any alphanumeric character including letters, numbers, and underscores.
    
Using raw strings, like we've been doing, helps avoid some of these possible confusion
 because the special characters won't be interpreted when generating the string.
 They will only be interpreted when parsing the regular expression. 
    .com            finds any character (only one) before com. dot is a special character here
    \.com           finds a dot before com. Dot is not a special character here             ESCAPE CHARACTER
    \w              finds single alphanumeric characters                                    SPECIAL SEQUENCE
    \w+             finds sequence of alphanumeric characters separated by whitespace       SPECIAL SEQUENCE
    \d              finds numbers in the text                                               SPECIAL SEQUENCE
    \s              finds wthitespaces, tabs, new line characters                           SPECIAL SEQUENCE
    \b              finds word boundaries                                                   SPECIAL SEQUENCE    
    
    A.*a            finds a word that starts with A and ends with a with any all characters in between e.g. Azerbaja
    ^A.*a$          finds a sequence in the text, A must be first letter in the text, any characetrs in between, must end with a 
    ^[a-zA-Z_][a-zA-Z_0-9]*$    examines validity of Python Variable name (contains letter, number, underscore but does not start with number)
    
"""
#%%
"""
2.1    Simple Matching in Python
we use the module re
this module contains various functions to manipulate strings
It is a good idea to always use rawstrings for the pattern we look for
r prefix is used to make a string a raw string
"""
# EXAMPLE 1
import re
x = re.search(r"aza", "plaza") # search for pattern aza in the string plaza
print(x) # print the match object

#Output is
#<re.Match object; span=(2, 5), match='aza'>
# span tells us where the pattern starts

# the r prefix indicates that this is a rawstring.
# This means that Python interpreter shouldn't try to interpret any special characters
# in this case there are no special characters in the pattern though

#%%
# EXAMPLE 2
import re
x = re.search(r"aza", "bazaar") # search for pattern aza in the string bazaar
print(x) # print the match object
#Output is
#<re.Match object; span=(1, 4), match='aza'>
# here the span attribute is different beacuse the pattern was found in a different position within the string

#%%
# EXAMPLE 3
# What happens if we do not find the pattern?
# we get the value None
import re
x = re.search(r"aza", "maze") # search for pattern aza in the string maze
print(x) # print the match object
#Output is
# None, the pattern we searched is not present in the string
# none is a special value that Python uses that show that there's not an actual value there
# None means that the regex did not find any match

# EXAMPLE 4
import re
x = re.search(r"^x", "xenon xylophone") # search for pattern x,ONLY if it is in the beginning, in the string xenon
print(x) # print the match object
#Output is:
#<re.Match object; span=(0, 1), match='x'>
# search for an x which is in the beginning
# search returns ONE OCCURENCE

# ATTENTION!    ^x finds x only if it is at the beginning of a word
#                 [^x] find all characters except for x, EXLUSION

#%%
import re
x = re.findall(r"^x", "xenon xylophone") # search for pattern x,ONLY if it is in the beginning, in the string xenon
print(x)
# Output is ['x'], so the findall() ignored the second x because it was not in the beginning?
#%%
# EXAMPLE 5
import re
x = re.search(r"p.ng", "penguin") # search for pattern p.ing (p_all existing characters_ng), in the string penguin
print(x) # print the match object
#Output is:
# <re.Match object; span=(0, 4), match='peng'>
# in penguin between p and ng, there is the pattern peng (p_e_ng). dot =e
# position of pattern starts at 0
# search for one character whichever it may be
# character found is e, in the part peng of the word penguin
#%%
# EXAMPLE 6
import re
x = re.search(r"p.ng", "clapping") # search for pattern p.ing (p_all existing characters_ng), in the string clapping
print(x) # print the match object
#Output is:
# <re.Match object; span=(4, 8), match='ping'>
# in clapping between p and ng there is the pattern ping (p_p_ing). dot = p

#%%
# EXAMPLE 7
import re
x = re.search(r"p.ng", "sponge") # search for pattern p.ing (p_all existing characters_ng), in the string sponge
print(x) # print the match object
#Output is
# <re.Match object; span=(1, 5), match='pong'>
# in sPoNGe between p and ng there is the pattern ping (p_o_ng). dot = o

#%%
# EXAMPLE 8
# In-video exercise
"""
Fill in the code to check if the text passed contains the vowels a, e and i, 
with exactly ONE occurrence of any other character in between.
"""
import re
def check_aei (text):
  result = re.search(r"", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True
#%%
import re
def check_aei (text): # parameter is text
  x = re.search(r"a.e.i", text) # # find pattern a.e.i (a, e and i must be separated by ONE character)
  return x != None # return x only when it is different than None
  
# call the function 3 times with 3 arguments (strings. This is the value for the parameter)
# at the same time, print the result of the function call
print(check_aei("academia"))  
# output is: True, the pattern was found
# <re.Match object; span=(2, 7), match='ademi'>
print(check_aei("aerial")) 
# output is: False, the pattern was not found because a and i are not separated by ONE character, they are side by side
# output is None
print(check_aei("paramedic")) 
# output is: True, the pattern was found
#<re.Match object; span=(3, 8), match='amedi'>

# return statement extracts the value from the function
# we exclude values that do not exist at all, eg when searching pattern "a.e.i" in dog. The pattern is simply not present in the text

#%%
# EXAMPLE 9
# to ignore case we use the re.IGNORECASE as a parameter in the search()
import re
x = re.search(r"p.ng", "Pangea", re.IGNORECASE) # ignore the case in the text!
print(x)
# Output is:
# <re.Match object; span=(0, 4), match='Pang'>
# pattern was found, we have a match
# we need the ignorecase to ignore the uppercase P on the text
# if we do not use ignore case the result is None, no match, pattern not found in the text
#%%
"""
2.2    Wildcards and Character Classes
dot is a special character
dot is a wildcard because it can match absolutely any character
Here we will restrict our wilcards to a range of characters
We do this with Character Class[]
Character Classes are written inside square brackets [] and
 let us list the characters we want to match inside of those brackets
"""
# EXAMPLE 10
import re
x = re.search(r"[Pp]ython", "Python") # search for python or Python in the string Python
print(x)                                # [P,p]ython: search for P or p
# Output is:
# <re.Match object; span=(0, 6), match='Python'>
# we have a match, it is Python
# the match is in index 0(in position0) of the string 

#%%
# EXAMPLE 11
# inside the character class[] we can also use a range of characters using a dash -
# here in our pattern we use the range from a to z, [a-z]
# other ranges are: A to Z, [A-Z] and zero to nine, [0-9]
import re
#x = re.search(r"PATTERN", "TEXT")
x = re.search(r"[a-z]way", "The end of the highway") # dash - means, search all lowercase letters between a and z (all the lowercase alphabet)
print(x)  
# Output is:
# <re.Match object; span=(18, 22), match='hway'>

# [a-z]way searches for one lowercase letter before "way"
# we found one 
# the match is hway

#%%
# EXAMPLE 12
import re
#x = re.search(r"PATTERN", "TEXT")
x = re.search(r"[a-z]way", "What a way") # dash - means, search all lowercase letters between a and z (all the lowercase alphabet)
print(x)
# Output is:
# None, we have a space before way, not a lowercase letter

#%%
# EXAMPLE 13
# We can combine as many ranges and symbols as we want, like this.
# we do not have to separate the ranges with a comma or anything else, just write one range next to each other without leaving a space
import re
x = re.search(r"cloud[A-Za-z0-9]", "cloudy") # A-Z find the uppercase, a-z find the lowercase, 0-9 find the number
print(x)
# Output is:
# <re.Match object; span=(0, 6), match='cloudy'>
# we have a match it is cloud-y. It is a lowercase letter

#%%
# EXAMPLE 14
import re
x = re.search(r"cloud[A-Za-z0-9]", "cloud9") # A-Z find the uppercase, a-z find the lowercase, 0-9 find the number
print(x)
# Output is:
# <re.Match object; span=(0, 6), match='cloud9'>
# 

#%%
# EXAMPLE 15
# In-video question
"""
Fill in the code to check if the text passed
    contains punctuation symbols: 
    commas, periods, colons, semicolons, question marks, and exclamation points
"""
import re
def check_punctuation (text):
  result = re.search(r"___", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

#%%
# inside character class[]we do not have to separate the characters with a comma or anything else, just write one range next to each other without leaving a space
import re
def check_punctuation (text):
  x = re.search(r"[,.:;?!]", text)
  return x != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

#%%
# EXAMPLE 16
# use a ^ inside [] of the character class for exclusion
# suppose we want to search for characters that are NOT letters

import re
x = re.search(r"[a-zA-Z]", "This is a sentence with spaces") # find only letters 
print(x)
# <re.Match object; span=(0, 1), match='T'>
import re
x = re.findall(r"[a-zA-Z]", "This is a sentence with spaces") # find only letters 
print(x)
# ['T', 'h', 'i', 's', 'i', 's', 'a', 's', 'e', 'n', 't', 'e', 'n', 'c', 'e', 'w', 'i', 't', 'h', 's', 'p', 'a', 'c', 'e', 's']

import re
x = re.search(r"[^a-zA-Z]", "This is a sentence with spaces") # find all characters EXCEPT letters
print(x)
# <re.Match object; span=(4, 5), match=' '>. Finds the 1st whitespace
import re
x = re.findall(r"[^a-zA-Z]", "This is a sentence with spaces") # find all characters EXCEPT letters
print(x)
# [' ', ' ', ' ', ' ', ' '] Finds all 5 whitespaces

import re
x = re.search(r"[^a-zA-Z ]", "This is a sentence with spaces") # I exclude letters AND whitespace, therefore I do not have a match
print(x)
# None
import re
x = re.findall(r"[^a-zA-Z ]", "This is a sentence with spaces") # I added a space in the unwanted characters within the brackets[]!
print(x)
# []

#%%
# EXAMPLE 17
# use the pipe symbol | to match either one expression or another
# the pipe symbol | provides alternative

import re
x = re.search(r"cat|dog", "I like cats.") # find either cat or dog
print(x)
#<re.Match object; span=(7, 10), match='cat'>
import re
x = re.findall(r"cat|dog", "I like cats.") # find either cat or dog
print(x)
# ['cat']

import re
x = re.search(r"cat|dog", "I like dogs.")
print(x)
# <re.Match object; span=(7, 10), match='dog'>
import re
x = re.findall(r"cat|dog", "I like dogs.")
print(x)
# ['dog']

import re
x = re.search(r"cat|dog", "I like both dogs and cats.")
print(x)
# <re.Match object; span=(12, 15), match='dog'>
import re
x = re.findall(r"cat|dog", "I like both dogs and cats.")
print(x)
# ['dog', 'cat']

#%%
# EXAMPLE 18
"""
the search() function returns ONLY THE 1ST MATCH
if we want all matches, we have to use the findall() function
the findall() function produces a list with all the matches found as its elements
""" 
import re
x = re.findall(r"cat|dog", "I like both dogs and cats.")
print(x)
# Output is: ['dog', 'cat']
#%%
"""
2.3    Repetition Qualifiers
another regex concept = repeated matches
.* (dot and star qualifier) dot is any character except \n newline character and star states that all occurences of its preceding character or pattern should be searched in the text
It's quite common to see expressions that include a dot followed by a star. 
This means that it matches any character repeated as many times as possible including zero. 
star* is a repetition qualifier
The asterisk char represents zero or more repetitions of the preceding character or pattern. 
For example, ah* will match any of “a”, “ah”, “ahh”.
f* find zero or more ocurrences of f
Repetition qualifiers (*, +, ?, {m,n}, etc) 
"""
# EXAMPLE 19
import re
x = re.search(r"Py.*n", "Pygmalion")
print(x)
# Output is
# <re.Match object; span=(0, 9), match='Pygmalion'>
# now the dot wildcard is not only one character but many

#%%
# EXAMPLE 20
"""
star * repetition qualifier is GREEDY
Greediness means that in general, regexes will try to consume as many characters as they can
"""
import re
x = re.search(r"Py.*n", "Python programming")# search for all characters and all their occurrences between Py and n
print(x)

# <re.Match object; span=(0, 17), match='Python programmin'>
# so the match does not stop at the 1st n, but it continued to the last n of the given string

# this is because of the star*, it takes as many characters as possible

# the dot is wildcard for a character
# the star tells the dot to substitute all characters
#%%
# EXAMPLE 21
# if we want the pattern to match letters we should use the character class[]
import re
x = re.search(r"Py[a-z]*n", "Python programming") # SEARCH FOR ALL LOWERCASE between Py and n
print(x)
# <re.Match object; span=(0, 6), match='Python'>
# the range inside the character class [] brackets searches for lowercase letters 

#%%
# EXAMPLE 22
"""
below we have zero occurrences of lowercase letters but star * still works
"""
import re
x = re.search(r"Py[a-z]*n", "Pyn")
print(x)

# <re.Match object; span=(0, 3), match='Pyn'>
# actually there are zero characters between Py and n!

#%%
# EXAMPLE 23
"""
in python and Egrep command we can use two additional repetition qualifiers
+ plus 
? question mark
(* star is also a repetition qualifier)
PLUS CHARACTER: +, 
The plus character matches one or more occurrences of the character that comes before it.
the result is the WHOLE STRING matching the condition
e.g. f+, find one or more occurrences of letter f
e.g o+l+, find one or more occurrences of "ol"
e.g. ab+, find one or more occurrences of "ab"
ab+ will match ‘a’ followed by any non-zero number of ‘b’s; it will not match just ‘a’.
In the example 'a+', the plus char “+” means “one or more” of the previous char.
The plus char represents one or more repetitions of the preceding regex. 
For example, ab+ will match “abc” or “abbc”, but will not match “ac”.
"""
import re
x = re.search(r"o+l+", "goldfish moldfish") # find letter sequence "ol", 
print(x)
# <re.Match object; span=(1, 3), match='ol'>
import re
x = re.findall(r"o+l+", "goldfish moldfish ")
print(x)
# ['ol', 'ol'] + character does not return single letters but the sequence


import re
x = re.search(r"o+l+", "woolly")
print(x)
# <re.Match object; span=(1, 5), match='ooll'>
import re
x = re.findall(r"o+l+", "woolly")
print(x)
# ['ooll']


import re
x = re.search(r"o+l+", "boil") # here o and l are not side by side, we have i between them
print(x)
# None
# there is no value found
# there is no match
import re
x = re.findall(r"o+l+", "boil") # here o and l are not side by side, we have i between them
print(x)
# []

#%%
# EXAMPLE 24
# in-video question
"""
The  function "repeating_letter_a", checks if the text passed includes the letter "a" 
(lowercase or uppercase) at least twice. 
For example, repeating_letter_a("banana") is True,
 while repeating_letter_a("pineapple") is False.
 Fill in the code to make this work.
 
 Are you including both lowercase and uppercase
"a" in the character class, and using the wildcards to match
everything else?
"""
# Question
import re
def repeating_letter_a(text):
  result = re.search(r"___", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

#%%
# Answer
"""
we will seacrh for a word that starts with a and ends with a
we want to find two a's at least
we will find everything between a and a, as many times as it appears in text (that's why we use *)
"""
import re
def repeating_letter_a(text):
  x = re.search(r"[aA].*[aA]", text) # find all a's that are more than 1
  return x != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

# the search() produces a string
# if we have 2 a's, then we have a string. This is what we want to find. True

# string starts with a or A, has characters in between (as many as possible) and ends with a or A

#%%
import re
x = re.search(r"[aA].*[aA]", "banana") # search for a pattern that starts with a or A and ends with a or A
print(x)
# <re.Match object; span=(1, 6), match='anana'>

import re
x = re.findall(r"[aA].*[aA]", "banana") # search for a pattern that starts with a or A and ends with a or A
print(x)
# ['anana']

#%%
import re
x = re.search(r"[aA].*[aA]", "pineapple")
print(x)
# None
# there is not a word that starts with a and ends with a, so no value at all, no match
import re
x = re.findall(r"[aA].*[aA]", "pineapple")
print(x)
# [] only one a, so nothing in between, so no match, no value to return
#%%
#EXAMPLE 25
"""
Repetition Qualifier ?
The question mark symbol is yet another multiplier. 
It means either zero or one occurrence of the character before it.
"""
import re
x = re.search(r"p?each", "To each their own") # find each, also search for 0 or more occurences of p right before each
print (x)
#<re.Match object; span=(3, 7), match='each'>
# we have zero occurences of p, it is ok we have a match
import re
x = re.findall(r"p?each", "To each their own") # find each, also search for 0 or more occurences of p right before each
print (x)
# ['each'] zero occurence of p is acceptable
#%%
import re
x = re.search(r"p?each", "I like peaches") # find each, also search for 0 or more occurences of p right before each
print (x)
# <re.Match object; span=(7, 12), match='peach'>
# now we have 1 occurence of p
import re
x = re.findall(r"p?each", "I like peaches") # find each, also search for 0 or more occurences of p right before each
print (x)
# ['peach']
#%%
"""
2.4    Escaping Characters
We can use \ to escape any special characters
escape = the characters lose their special character and become simple characters
e.g. the dot . does not represent any character except newline and it becomes a simple dot
Using \ ,can get really confusing with backslashes since
 they're also used to define some special string characters. 
 e.g. \n is the new line character (indicates in Python a new line)
 e.g. \t does the same for tabs
 
THEREFORE ATTENTION
when we see a \:
    - it could be escaping a special regex character
    - it could be a special string character
    - i could be used for a few special sequences that we can use to represent predefined sets of characters. 
      For example, \w matches any alphanumeric character including letters, numbers, and underscores.
    
Using raw strings, like we've been doing, helps avoid some of these possible confusion
 because the special characters won't be interpreted when generating the string.
 They will only be interpreted when parsing the regular expression. 
"""
import re
x = re.search(r".com", "welcome") # . dot represents any character
print(x)
# <re.Match object; span=(2, 6), match='lcom'>
# .com pattern finds the match lcom. The dot represents any character

import re
x = re.search(r"\.com", "welcome") #\. backslash dot represents a dot
print(x)
# None
# the actual .com pattern did not find any match

import re
x = re.search(r"\.com", "mydomain.com") #\. backslash dot represents a dot
print(x)
# <re.Match object; span=(8, 12), match='.com'>

#%%
"""
\w is a special sequence
\w finds letters, numbers, underscores
\w does not find spaces
\w with findall() returns all matches as individual letters,numbers,underscores
                  does not return a match for whitespace  
\w+ with findall() returns all matches as words with letters, words with letters and numbers, words with letters and numbers and underscores, numbers, underscores that were divided by a space in the text
"""

import re
x = re.findall(r"\w", "This is an example")
print(x)

import re
x = re.search(r"\w+", "This is an example") 
print(x)
# <re.Match object; span=(0, 4), match='This'>
import re
x = re.findall(r"\w+", "This is an example")
print(x)
# ['This', 'is', 'an', 'example']



import re
x = re.search(r"\w+", "And_this_is_another")
print(x)
# <re.Match object; span=(0, 19), match='And_this_is_another'>
import re
x = re.findall(r"\w+", "And_this_is_another")
print(x)
# ['And_this_is_another']

# with * WHY DO I HAVE A MATCH FOR LAST SPACE THAT IS NOT PRESENT IN THE TEXT???
# when I use + instead of * , I do not get a MATCH for the last space that is not present in the text

#%%
"""
OTHER SPECIAL SEQUENCES
\d for matching numbers
\s for matching whitespace characters like space, tab, new line
\b for word boundaries
"""
import re
x = re.findall(r"\d", "I have 2 dogs")
print(x)
# ['2']
#%%
import re
x = re.findall(r"\s", "I have 2 dogs")
print(x)
# [' ', ' ', ' '], i have a mtach for 3 white-spaces

#%%
import re
x = re.findall(r"\b", "I have 2 dogs")
print(x)
# ['', '', '', '', '', '', '', ''] I have a match for 4 words, each word start and end is indicated with a space
#%%
"""
In-video question
Fill in the code to check if the text passed has
 at least 2 groups of alphanumeric characters (including letters, numbers, and underscores) 
 separated by one or more whitespace characters.
  Are you using escape characters to check for one
or more occurrence of alphanumeric and whitespace characters?
for each group?
"""
# question
import re
def check_character_groups(text):
  result = re.search(r"______", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False

#%%
# answer
import re
def check_character_groups(text):
  result = re.search(r"\w+\s+\w+", text) # pattern is Alphanumeric(s)Space(s)Alphanumeric(s)
  return result != None 

print(check_character_groups("One")) # False because there is no space here
print(check_character_groups("123  Ready Set GO")) # True because there are two AlphanumericSpaceAlphanumeric here. Between 123 and Ready we have two spaces! That is why we need \s+ and not just \s
print(check_character_groups("username user_01")) # True because there is one AlphanumericSpaceAlphanumeric here
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False because alphanumeric are not separated by space but by : and ,

"""
we want to find alphanumerics separated by a space
"""
#%%
# pattern is \w 
import re
x = re.search(r"\w", "123  Ready Set GO")
print(x)
# <re.Match object; span=(0, 1), match='1'>
# returns first single alphanumeric character
import re
x = re.findall(r"\w", "123  Ready Set GO")
print(x)
# ['1', '2', '3', 'R', 'e', 'a', 'd', 'y', 'S', 'e', 't', 'G', 'O']
# returns all single alphanumeric characters
#%%
# pattern is \w+ 
import re
x = re.search(r"\w+", "123  Ready Set GO")
print(x)
# <re.Match object; span=(0, 3), match='123'>
# returns first repetition of alphanumeric character
import re
x = re.findall(r"\w+", "123  Ready Set GO")
print(x)
# ['123', 'Ready', 'Set', 'GO']
# returns all repetitions of alphanumeric characters, we have 4 elements so 4 repetitions of alphanumeric characters
#%%
# pattern w+\s+\w+ searches for the group Alphanumeric(s)Space(s)Alphanumeric(s)
import re
x = re.search(r"\w+\s+\w+", "123  Ready Set GO")
print(x)
# <re.Match object; span=(0, 10), match='123  Ready'>
# returns first group
import re
x = re.findall(r"\w+\s+\w+", "123  Ready Set GO")
print(x)
# ['123  Ready', 'Set GO']
# returns all groups , we have 2 elements so 2 groups




#%%
"""
2.5    Regular Expressions in Action
"""

# we have a list of countries
# which countries names start with a and end with a?
# what pattern should we use?

import re
x = re.search(r"A.*a", "Argentina") # A.*a searches for a word starting with A ending with a, with any. and all* characters in between. * is repetition qualifier
print (x)
# <re.Match object; span=(0, 9), match='Argentina'>

#%%

import re
x = re.search(r"A.*a", "Azerbajan") # A.*a searches for a word starting with A ending with a, with any. and all* characters in between. * is repetition qualifier
print (x)
# <re.Match object; span=(0, 8), match='Azerbaja'>
# this is wrong since Azerbajan does not finish with a
# it is our fault because we did not specify we want the pattern to match the whole string

# now we will make our pattern stricter
# we will specify that A is in the beginning :^A
# and a is in the end: a$
#%%
import re
x = re.search(r"^A.*a$", "Azerbajan") # A.*a searches for a word starting with A ending with a, with any. and all* characters in between. * is repetition qualifier
print (x)
# None, no match, no value
#%%

import re
x = re.search(r"^A.*a$", "Australia") # A.*a searches for a word starting with A ending with a, with any. and all* characters in between. * is repetition qualifier
print (x)
# <re.Match object; span=(0, 9), match='Australia'>

#%%
import re
x = re.findall(r"^A.*a$", "Australia Andorra") # A.*a searches for a word starting with A ending with a, with any. and all* characters in between. * is repetition qualifier
print (x)
#%%
# EXAMINE IF A VARIABLE HAS A VALID NAME
# rules: it can contain any number of numbers, letters, underscores
#        it cannot start with a number
#        it should start with a letter or an underscore

import re
x = re.search(r"^[a-zA-Z_][a-zA-Z_0-9]*$", "_this_is_a_valid_Variable_name") # A.*a searches for a word starting with A ending with a, with any. and all* characters in between. * is repetition qualifier
print (x)
# <re.Match object; span=(0, 30), match='_this_is_a_valid_Variable_name'>
# we have one match
#%%
import re
x = re.search(r"^[a-zA-Z_][a-zA-Z_0-9]*$", "this isn't a valid Variable") # A.*a searches for a word starting with A ending with a, with any. and all* characters in between. * is repetition qualifier
print (x)
# None, no match
# we used a space which is not defined in the pattern
# also space is not allowed in a Variable name
#%%
import re
x = re.search(r"^[a-zA-Z_][a-zA-Z_0-9]*$", "my_Variable1") # A.*a searches for a word starting with A ending with a, with any. and all* characters in between. * is repetition qualifier
print (x)
# <re.Match object; span=(0, 12), match='my_Variable1'>


import re
x = re.search(r"^[a-zA-Z_][a-zA-Z_0-9]*$", "2my_Variable1") # A.*a searches for a word starting with A ending with a, with any. and all* characters in between. * is repetition qualifier
print (x)
# None

#%%
"""
In-video question
Fill in the code to check 
if the text passed looks like a standard sentence, 
meaning that it starts with an uppercase letter, 
followed by at least some lowercase letters or a space, 
and ends with a period, question mark, or exclamation point.
"""
# question
import re
def check_sentence(text):
  result = re.search(r"___", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True
#%%
# answer
import re
def check_sentence(text):
  result = re.search(r"^[A-Z][a-z -]*[.?!]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True

#%%
"""
2.6    Regular Expressions Cheat-Sheet
Check out the following links for more information:
•	https://docs.python.org/3/howto/regex.html
•	https://docs.python.org/3/library/re.html
•	https://docs.python.org/3/howto/regex.html#greedy-versus-non-greedy
Shout out to regex101.com, which will explain each stage of a regex.
"""
#%%
"""
2.7    Practice Quiz: Basic Regular Expressions
"""

"""
question 1
The check_web_address function 
checks if the text passed qualifies as a top-level web address, meaning that 
-it contains alphanumeric characters (which includes letters, numbers, and underscores), 
-as well as periods, dashes, 
-and a plus sign, followed by a period 
-and a character-only top-level domain such as ".com", ".info", ".edu", etc. 
Fill in the regular expression to do that, using escape characters, wildcards, repetition qualifiers, beginning and end-of-line characters, and character classes.
"""
#%%
# question
import re
def check_web_address(text):
  pattern = ___
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

#%%
# answer
import re
def check_web_address(text):
  pattern = r"\.[a-zA-Z]+$" # this pattern searches for letters AFTER  a dot. the pattern must be in the end
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

#%%
import re
x = re.findall(r"\.[a-zA-Z]+$", "gmail.com")
print(x)
# ['gmail.com']
#%%
import re
x = re.findall(r"\.[a-zA-Z]*$", "www@google")
print(x)
# []
#%%
import re
x = re.findall(r"\.[a-zA-Z]*$", "www.Coursera.org")
print(x)
# ['www.Coursera.org']
#%%
import re
x = re.findall(r"\.[a-zA-Z]*$", "My_Favorite-Blog.US")
print(x)

#%%
"""
question 2
The check_time function 
checks for the time format of a 12-hour clock, as follows: 
    the hour is between 1 and 12, with no leading zero, followed by a colon, 
    then minutes between 00 and 59, 
    then an optional space, 
    and then AM or PM, in upper or lower case. 
Fill in the regular expression to do that. 
How many of the concepts that you just learned can you use here?
"""
import re
def check_time(text):
  pattern = ___
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False

#%%
"""
question 3
The contains_acronym function 
checks the text for 
the presence of 2 or more characters or digits surrounded by parentheses, 
with at least the first character in uppercase (if it's a letter),
 returning True if the condition is met, or False otherwise. 
 For example, "Instant messaging (IM) is a set of communication technologies used for text-based communication" should return True since (IM) satisfies the match conditions." Fill in the regular expression in this function:
"""

import re
def contains_acronym(text):
  pattern = r"\([a-zA-Z0-9]*"
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True


#%%
import re
x = re.findall(r"\([a-zA-Z0-9]*", "Instant messaging (IM) is a set of communication technologies used for text-based communication")
print(x)

#%%
import re
x = re.findall(r"\([a-zA-Z0-9]*", "American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")
print(x)

#%%
import re
x = re.findall(r"\([a-zA-Z0-9]*", "Please do NOT enter without permission!")
print(x)


#%%
"""
question 4
What does the "r" before the pattern string in re.search(r"Py.*n", sample.txt) indicate?
answer
"Raw" strings just means the Python interpreter won't try to interpret any special characters and, instead, will just pass the string to the function as it is.
question 5
What does the plus character [+] do in regex?
amswer
matches ONE or more occurrences of the character before it
"""
#%%
"""
question 6
Fill in the code to check if the text passed includes a possible U.S. zip code,
 formatted as follows: 
     exactly 5 digits, and sometimes, but not always, followed by a dash with 4 more digits.
     The zip code 
     needs to be preceded by at least one space, 
     and cannot be at the start of the text.
     
"""
import re
def check_zip_code (text):
  result = re.search(r"\s+[0-9][0-9][0-9][0-9][0-9][-0-90-90-90-9]*", text)
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False

#%%
import re
x = re.findall(r"\s+[0-9][0-9][0-9][0-9][0-9][-0-90-90-90-9]*", "The zip codes for New York are 10001 thru 11104.")
print(x)

#%%
import re
x = re.findall(r"\s+[0-9][0-9][0-9][0-9][0-9][-0-90-90-90-9]*", "90210 is a TV show")
print(x)

#%%
import re
x = re.findall(r"\s+[0-9][0-9][0-9][0-9][0-9][-0-90-90-90-9]*", "Their address is: 123 Main Street, Anytown, AZ 85258-0001.")
print(x)



#%%
#%%
# question 2-FIC THE CODE HERE!!!
import re
def check_time(text):
  pattern = r"[0-9][0-2]*\:[0-5][0-9]\s*[am|AM|pm|PM]+"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False

#%%
# 
import re
x = re.findall(r"[0-9][0-2]*\:[0-59][0-59]\s*[am|AM|pm|PM]+", "12:45pm")
print(x)
# ['12:45pm']
#%%
import re
x = re.findall(r"[0-9][0-2]*\:[0-59][0-59]\s*[am|AM|pm|PM]+", "9:59AM")
print(x)

"""
This makes 92:45am correct. Yours might work but it's not a good code to allow that time.
"""
#%%
import re
x = re.findall(r"[0-9^0^2^3^4^5^6^7^8^9][0-9^0]*\:[0-59][0-59]\s*[am|AM|pm|PM]+", "92:59AM")
print(x)


#%%
import re
x = re.findall(r"[0-9^0^2^3^4^5^6^7^8^9][0-9^0]*\:[0-5][5-9]\s*[am|AM|pm|PM]+", "9:59AM")
print(x)


#%%
import re
x = re.findall(r"[1][0-9]*\:[0-59][0-59]\s*[am|AM|pm|PM]+", "92:59AM")
print(x)

"""
Using Python to interact with the operating system, by Google
WEEK 3 – Regular Expressions
3 ADVANCED REGULAR EXPRESSIONS
3.1        Capturing Groups
3.2        More on Repetition Qualifiers
3.3        Extracting a PID Using regexes in Python
3.4        Splitting and Replacing
3.5        Advanced Regular Expressions Cheat-Sheet
3.6        Practice Quiz: Advanced Regular Expressions
SYNOPSIS
3.1        Capturing Groups
capturing groups uses () parentheses in the pattern in order to match specific information in the text
I can write a very long pattern and then choose what I want to be returned by using parenthesis.
after using capturing groups I can use indexing x[1], x[2] on the match object x to use the matches I have found
for a pattern with 2 parentheses, and a text with 2 strings, search() and print(x) produces one text with 2 strings (the match)
I can print(x[1]) to get the match for the 1st pattern parenthesis 
I can print (x[2]) to get the match for the 2nd pattern parenthesis 
Attention: with x[0] I get the whole match not 1st pattern parenthesis  etc.
Method groups() 
APPLY IT ON THE MATCH OBJECT: x.groups() and get a tuple whose elements are the pattern parentheses/groups. 
          Pattern                                           Use
          r"^(\w*), (\w*)$", "Lovelace, Ada"                2 groups enclosed in parentheses
          r"^([\w \.-]*), ([\w \.-]*)$","Kennedy, John F."  2 groups
                                                            [] used to escape special character. and also to apply the * to each enclosed character
                                                            the beginning^ and the ending$ are applied on the parentheses
                                                    
Note: special characters 1) inside [] and 2) after \, lose their special meaning
3.2        More on Repetition Qualifiers
repetition qualifiers = *, +, ?
numeric repetition qualifiers = {m, n}      finds preceding repeated characters. Repetition now is quantified. (start, end)
                                {5}         find repetition of preceding regex, of exactly 5 characters (exact number)
                                {5,10}      find repetition of preceding regex, of 5 to 10 characters (lower and upper boundary)
                                {5,}        find repetition of preceding regex, of AT LEAST 5 up to unlimited characters (lower boundary. Upper is defined by the text itself!)
                                [,20]       find repetition of preceding regex, of UP TO 20 characters or less (upper boundary. )
        Pattern                                         Use
        r"[a-zA-Z]{5}", "a ghost"                       finds 5 repeating characters (characters can be any aplhabet letter lowercase or uppercase)
        (r"\b[a-zA-Z]{5}\b", "a scary ghost appeared")  finds 5 repeating characters, but only full words not part of words
Note: use \b to get FULL WORDS!use \b at the beginning and end of the pattern to indicate that I want matches that are words, not parts of words!
3.3        Extracting a PID Using regexes in Python
pattern r"\[(\d+)\], we want to find any numbers within []
capturing group is inside the parenthesis
( I can create as many capturing groups as i like
then i can index x based on these capturing groups)
backslash \ is used to treat following characters LITERALLY
so i use\ before [] and another \ before ]. Finallly [, and ], are treated litterally
    
\d is a special sequence, finds numbers 0-9
\d+ special sequence with repeating qualifier + which find one or more repetitions
INDEXING THE MATCH OBJECT
x: match object
if we use capturing groups in the pattern then I can index the x like this:
    x[1] is the 1st capturing group
    x[2] is the 2nd capturing group
3.4        Splitting and Replacing
we can escape characters in 2 ways
use \
place them inside []
methods in the regex module re
search()
findall()
split()         splits our text at specified points
                produces a list. Elements are parts of the text we splitted
                splitting elements are not included in the result, unless we use capturing groups ()
                
                Pattern                                                    Use
                r"[.?!]", "One sentence. Another one? And the last one!"   split the text using 3 splitting elements
                                                                           I will get 4 parts
                                                                           splitting elements do not appear in the results
                r"([.?!])", "One sentence. Another one? And the last one!" split the text using 3 splitting elements
                                                                           I will get 4 parts
                                                                           now the splitting elements appear in the results but independently
sub()           The sub() function replaces the matches with the text of our choice
                syntax is: x = re.sub(pattern, text of our choice, text)
                x = re.sub(r"","", "")
                so we replace something in the text with something we have chosen
                
                Pattern                                                                              Use
                r"[\w.%+-]+@[\w.-]+","REDACTED", "Received an email for go_nuts95@my.example.com"    replace go_nuts95@my.example.com with REDACTED
                r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"                               replace parenthesis 2 with 1, replace parenthesis 1 with 2 (REVERSE ORDER!)
                
| pipe or vertical bar
use the pipe symbol |, to match either one expression or another
This regular expression uses "the" and "a" as delimiters, no matter where they are in the text, 
even in the middle of other words like "Another" and "last".
"""

#%%
"""
3.1        Capturing Groups using () in the pattern separated by comma
until now we searched for a pattern inside a text, found a match and then printed the match.
now we will use the match and use it to do something else
For example, we may want to extract the hostname or a process ID from a log line and use that value for another operation
For that we need to use a concept of regular expressions called capturing groups
CAPTURING GROUPS = portions of the pattern that are enclosed in parentheses
Let's say that we have a list of people's full names. 
These names are stored as last name, comma, first name.
 We want to turn this around and create a string that starts with the first name followed by the last name. 
We can do this using a regular expression with capturing groups. 
re.search(r"pattern", "text") produces x, the match object
for a pattern with 2 parentheses and a text with 2 strings print(x) produces one text with 2 strings (the match)
I can choose string1 and string 2 from x with indexing
beware! x[0] gives me the whole match, x[1] gives me the 1st string of text/1st () of pattern and x[2] gives me 2nd string of text/2nd () of pattern
x.groups() will produce a tuple with 2 elements, the 2 strings of the text
I will not use findall() because this produces a list with 1 tuple as an element:)
"""
import re
x = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada") # two () and comma in the pattern, two parts and comma in the text
print(x)
# <re.Match object; span=(0, 13), match='Lovelace, Ada'>
print(x[1])
# Lovelace, this is 1st group in the pattern, 1st parenthesis
print(x[2])
# Ada, this is 2nd group in the pattern, 2nd parenthesis
 
import re
x = re.findall(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(x)
# [('Lovelace', 'Ada')]
# with parenthesis in the pattern,findall() produces a list with 1 element
# that element is a tuple with 2 elements
# A tuple is a collection which is ordered and unchangeable.
# In Python tuples are written with round brackets.

# so: list with 1 element which is a tuple
# tuple contains 2 elements (from the 2 parentheses in the pattern)
# findall() maybe is not so practical with capturing groups in the pattern

#%%
import re
x = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada") # produce the Match Object

print(x.groups())                                 # apply the method groups() on the Match Object and create a tuple
# ('Lovelace', 'Ada'), this is a TUPLE
# the groups() method applied on the Match Object produces a tuple with the 2 matches as its elements

print(x)
# <re.Match object; span=(0, 13), match='Lovelace, Ada'>

print(x[0]) 
# Lovelace, Ada

print(x[1])
# prints 1st string of the object
# Lovelace

print(x[2])
# prints 2nd string of the object
# Ada

print("{} {}".format(x[2], x[1])) #  format method to change the order from Surname-Name to Name-Surname
# Ada Lovelace

#%%
"""
write a function to 
change the order from Surname-Name to Name-Surname
"""
def rearrange_name(fullname): # fullname is a text, 2 strings separated by a comma
    x = re.search(r"^(\w*), (\w*)$", fullname) # produce the Match Object x: 'fullname'
    if x is None: # if x is None, then we did not find a match (no value), then return fullname as it is
        return fullname
    return "{} {}".format(x[2], x[1]) # else (if x is other than None and we have a match), re-arrange the fullname)
    
rearrange_name("Lovelace, Ada")
# 'Ada Lovelace'
# we produced x with search(), then we used indexing on x to switch the order of the 2 strings
# it looks like we do not need x.groups() ha-ha
rearrange_name("Ritchie, Dennis")
# 'Dennis Ritchie'
rearrange_name("Hopper, Grace M. ")
# 'Hopper, Grace M.
#  'Now the regex did not work because we used the \w* which only matches 
# repetition of letters,numbers,underscores and now in the text we have whitespace and dot!

# ATTENTION 
# we use capturing groups () here which correspong to indexes of the match object x
#%%
"""
In-video question
Fix the regular expression used in the rearrange_name function so that it can match
 middle names, middle initials, as well as double surnames.
 What we need to do here is add the extra characters that we want to allow in the names.
 In this example we'd want to add spaces and dots.
 
CORRECTION
The correct regular expression should be: "^([\w \.-]*), ([\w \.-]*)$"
1st () in pattern:
^ should start with this ()
\w find alphanumeric 
\. find actual dot
- find dash
enclose all above, in [] and use star * to find all repetitions of preceding characters
2nd () in pattern:
same contents in [], again use star*
at the end of parenthesis, use $ to indicate that this should be the end
    
Note: for star* to be applied to all regex, I enclose them in []
Un-escaped, the dot in this expression will match any character. 
In this case it makes the code work, but it is incorrect! 
Since we wanted to match the dot character specifically, we should have escaped the dot in the regular expression. 
"""
import re
def rearrange_name(name):
  result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.") # call the function with an argument
print(name)

#%%
import re
x = re.search(r"^([\w \.-]*), ([\w \.-]*)$", "Kennedy, John F.")
print(x)
# <re.Match object; span=(0, 16), match='Kennedy, John F.'>

import re
x = re.search(r"^([\w \.-]*), ([\w \.-]*)$", "Kennedy, John F.")
print(x.groups())
# ('Kennedy', 'John F.')

#%%
"""
3.2        More on Repetition Qualifiers
"""
import re
x = re.search(r"[a-zA-Z]{5}", "a ghost")
print(x)
# <re.Match object; span=(2, 7), match='ghost'>
# {5} is a NUMERIC repetition qualifier
# it seacrhes for a specific 5 repetition of  letter character in the text
# we have a match, it is 'ghost' which has 5 repetitions of letter character

import re
x = re.search(r"[a-zA-Z]{5}", "a scary ghost appeared")
print(x)
# <re.Match object; span=(2, 7), match='scary'>
# attention! we have more matches but as always search()  returns only the 1st
# so now use the findall() below

import re
x = re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared")
print(x)
# ['scary', 'ghost', 'appea']
# 3 matches 
#%%
"""
What if we wanted to match all the words that are exactly five letters long? 
We can do that using \b,
 which matches word limits at the beginning and end of the pattern, 
 to indicate that we want full words
 
I use \b at the begging and end of the pattern to 
indicate that I want matches that are words, not parts of words!
"""
import re
x = re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared")
print(x)
# ['scary', 'ghost']
# 2 matches because I used \b
# so, appea is exactly 5 characters long but it is not a full word so it is excly=uded from the results

#%%
"""
numeric repetition qualifier
{5}         find repetition of preceding regex of 5 characters (exact number)
{5,10}      find repetition of preceding regex of 5 to 10 characters (lower and upper boundary)
{5,}        find repetition of preceding regex of 5 to unlimited characters (lower boundary. Upper is defined by the text itself!)
[,20]
"""
import re
x = re.findall(r"\w{5,10}", "A scary ghost appeared")
print(x)
# ['scary', 'ghost', 'appeared']
# {5,10} numeric repetition qualifier with lower limit and upper limit

import re
x = re.findall(r"\w{5,10}", "I really like strawberries")
print(x)
# ['really', 'strawberri']
# I did not use \b here so I got part of a word
#%%
import re
x = re.search(r"s\w{,20}", "I really like strawberries")
print(x)
# pattern we look for in the text is:
# letter:s, alphanumeric, zero to 20 repetition length 
# (starts with s, is alphanumeric and is up to 20 alphanumeric characters)
# <re.Match object; span=(14, 26), match='strawberries'>
# strawberries contains alphanumeric characters
# starts with s
# contains 11 characters after s, so it is up to 20
# so it is a match

#%%
"""
In-video question
The long_words function returns all words that are at least 7 characters.
 Fill in the regular expression to complete this function.
"""
# question
import re
def long_words(text):
  pattern = r"\w{7,}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []

#%%
# answer
import re
x = re.findall(r"\w{7,}", "I like to drink coffee in the morning.")
print(x)

#%%
"""
3.3        Extracting a PID Using regexes in Python
pattern r"\[(\d+)\], we want to find any numbers within []
capturing group is inside the parenthesis
( I can create as many capturing groups as i like
then i can index x based on these capturing groups)
backslash \ is used to treat following characters LITERALLY
so i use\before[] and another \before]. Finallly [, and ], are treated litterally
    
\d is a special sequence, finds numbers 0-9
\d+ special sequence with repeating qualifier + which find one or more repetitions
INDEXING THE MATCH OBJECT
x: match object
if we use capturing groups in the pattern then I can index the x like this:
    x[1] is the 1st capturing group
    x[2] is the 2nd capturing group
PID= process ID 
"""
import re
x = re.search(r"\[(\d+)\]", "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")
print(x[1]) # x is the match object, x[1] is the 1st capturing group 
# 12345 
# this is our match, we got it by indexing the match object
# if we just printed x, we would get the string '[12345]'
# we searched for repeating numbers
# () contain the group we are searching for
# we have one group in the pattern and one number in the text
# if we had a text, the match would be the 1st string

#%%
import re
x = re.search(r"\[(\d+)\]", "A completely different string that also has numbers [34567]")
print(x[1])
# 34567

#%%
"""
what if our string had numbers NOT in square brackets?
"""
import re
x = re.search(r"\[(\d+)\]", "99 elephants in a [cage]")
print(x[1])
# error!
# TypeError: 'NoneType' object is not subscriptable

#%%
"""
what can we do when there is no match, no value and ofcourse we cannot index x?
we will build a function 
to extract the process ID WHEN possible
and do something else WHEN NOT possible
"""
def extract_pid(LogLine):
    x = re.search(r"\[(\d+)\]", LogLine)
    if x is None:
        return "no ID"
    return x[1]

print(extract_pid("A completely different string that also has numbers [34567]"))
# output is: 34567

print(extract_pid("99 elephants in a [cage]"))
# print(x) now is NONE so output is: no ID

#%%
import re
x = re.search(r"\[(\d+)\]", "99 elephants in a [cage]")
print(x)

#%%
"""
In-video question
Add to the regular expression used in the extract_pid function, 
to return the uppercase message in parenthesis, after the process id.
use character classes, repetition
qualifiers, and word boundaries to check for the message
following the process id
Attention, inside the capturing group parenthesis I will include what 
I WANT TO APPEAR, in the printing of x indexing
1st capturing group() corresponds to x[1]
2nd capturing group corresponds to x[2] and so on
"""
import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]___"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(___)

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)

#%%
import re
def extract_pid(log_line):
    x = re.search(r"\[(\d+)\]: ([A-Z]*)", log_line)
    if x is None:
        return None
    return "{} ({})".format(x[1], x[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)

# REGEX EXPLANATION
# find the number that is inside the square brackets:
# \d finds numbers from 0-9
# \d+ finds repetition of \d, if there is one or more occurrences in the text
# [\d+] I need the number inside []
# \[\d+\] I need the litteral meaning of square brackets, so I use \ before each bracket

# find the uppercase word after :whitespace
# : [A-Z]
# : [A-Z]* , the star repetition qualifier finds zero or more occurrences in the text
# whole regex is \[\d+\]: [A-Z]*
# if I try to print here i get the match '[12345]: ERROR' from 1st text, which I do not want

# now I will create 2 capturing groups by placing parentheses
# I place 1st () around \d+ to eventually retrieve only the number and not the square brackets!
# I place 2nd () around [A-Z]* to eventually retrieve only the uppercase word and not the : and the whitespace
# later I will use x[1] to retrieve \d+ match
# and I will use x[2] to retrieve [A-Z]* match
#%%
"""
attention, I will use 2 capturing groups in the pattern and then index the match object x
"""
import re
x = re.search(r"\[(\d+)\]:( [A-Z]*)", "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")
print(x) # # <re.Match object; span=(39, 53), match='[12345]: ERROR'>
print(x[1]) # [12345]
print(x[2]) # : ERROR

#%%
"""
3.4        Splitting and Replacing
we can escape characters in 2 ways
use \
place them inside []
methods in the regex module re
search()
findall()
split()         splits our text at specified points
                produces a list. Elements are parts of the text we splitted
                splitting elements are not included in the result, unless we use capturing groups ()
"""

"""
split a text into sentences
sentences end with .?!
we will use .?! as splitting elements
splitting elements are omitted from the results
"""
import re
x = re.split(r"[.?!]", "One sentence. Another one? And the last one!")
print(x)
# ['One sentence', ' Another one', ' And the last one', '']

#%%
"""
split a text into sentences
now use capturing groups () for the splitting elements to appear
"""
import re
x = re.split(r"([.?!])", "One sentence. Another one? And the last one!")
print(x)
# ['One sentence', '.', ' Another one', '?', ' And the last one', '!', '']

#%%
"""
re methods
search
findall
split
sub()           The sub() function replaces the matches with the text of our choice
                syntax is: x = re.sub(pattern, text of our choice, text)
                x = re.sub(r"",r"", "")
                so we replace something in the text with something we have chosen
"""
"""
So we have some logs in our system that included e-mail addresses of users and
 we want to anonymize the data by removing all the addresses
redact = edit (text) for publication/censor or obscure (part of a text) for legal or security purposes.
"""

import re
x = re.sub(r"[\w.%+-]+@[\w.-]+",r"REDACTED", "Received an email for go_nuts95@my.example.com")
print(x)
# Received an email for REDACTED
# this pattern has a small mistake, if there are two dots after @, then it will still
# be recognized as an e-mail address and still be redacted.

#%%
"""
write a function to 
change the order from Surname-Name to Name-Surname
USING SEARCH()
"""
def rearrange_name(fullname): # fullname is a text, 2 strings separated by a comma
    x = re.search(r"^(\w*), (\w*)$", fullname) # produce the Match Object x: 'fullname'
    if x is None: # if x is None, then we did not find a match (no value), then return fullname as it is
        return fullname
    return "{} {}".format(x[2], x[1]) # else (if x is other than None and we have a match), re-arrange the fullname)
    
rearrange_name("Lovelace, Ada")
# 'Ada Lovelace'
# we produced x with search(), then we used indexing on x to switch the order of the 2 strings
# it looks like we do not need x.groups() ha-ha
rearrange_name("Ritchie, Dennis")
# 'Dennis Ritchie'
rearrange_name("Hopper, Grace M. ")
# 'Hopper, Grace M.
#  'Now the regex did not work because we used the \w* which only matches 
# repetition of letters,numbers,underscores and now in the text we have whitespace and dot!

# ATTENTION 
# we use capturing groups () here which correspong to indexes of the match object x

#%%
"""
write a function to 
change the order from Surname-Name to Name-Surname
USING SUB()
"""
import re
x = re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")
print(x)
# Ada Lovelace

# pattern r"^(), ()$"
# 1st parenthesis is 1st group etc.
# 1st group comma whitespace 2nd group (like in the text, string1 comma whitespace string2)
# groups are separated by comma like strings are separated by comma in the text
# 1st group= [\w .-]* it contains a space, why? a space can be present in a string 
# 2nd group= same

# our text r"\2 \1"
# here we re-arrange
# we place string2 then string1 
# also group1 corresponds to string 1 and group2 corresponds to string2

# text: ''string1, string2" which is "Lovelace, Ada"

#%%
"""
In-Video question
We want to split a piece of text by either the word "a" or "the", 
as implemented in the following code. What is the resulting split list?
| pipe or vertical bar
use the pipe symbol |, to match either one expression or another
This regular expression uses "the" and "a" as delimiters, no matter where they are in the text, 
even in the middle of other words like "Another" and "last".
"""
import re
x = re.split(r"the|a", "One sentence. Another one? And the last one!")
print(x)

# ['One sentence. Ano', 'r one? And ', ' l', 'st one!']

# splitting elements are lowercase "the" and lowercase "a"
# splitting elements do not appear in the result
# we get the following parts
#'One sentence. Ano'
#'r one? And '
#' l'
#'st one!'

#%%
"""
3.5        Advanced Regular Expressions Cheat-Sheet
Check out the following link for more information:
https://regexcrossword.com/
"""
#%%
"""
3.6        Practice Quiz: Advanced Regular Expressions
"""
"""
QUESTION 1
We're working with a CSV file, which contains employee information. 
Each record has a name field, followed by a phone number field, and a role field. 
The phone number field contains U.S. phone numbers, and needs to be modified 
to the international format, with "+1-" in front of the phone number. 
Fill in the regular expression, using groups, to use the transform_record function to
 do that.
"""
import re
def transform_record(record):
  new_record = re.sub(___)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer

#%%
#syntax is: x = re.sub(pattern, text of our choice, text)
#                x = re.sub(r"","", "")
import re
x = re.sub(r"([\d-]+)", r"+1-\1", "Sabrina Green,802-867-5309,System Administrator")
print(x)
# i have to use r in the replacing text!!!
#%%
import re
x = re.search(r"([\d-]+)", "Sabrina Green,802-867-5309,System Administrator")
print(x)

# ANSWER
#%%
import re
def transform_record(record):
  new_record = re.sub(r"([\d-]+)", r"+1-\1", record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer

#%%
"""
QUESTION 2
The multi_vowel_words function 
returns all words with 3 or more consecutive vowels (a, e, i, o, u). 
Fill in the regular expression to do that.
"""
import re
def multi_vowel_words(text):
  pattern = ___
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []

#%%
# 3 or more consecutive vowels (a, e, i, o, u)
# I need words so I will use \b
# numeric repetition qualifier! 
import re
x = re.findall(r"[aeiou]{3,}", "Life is beautiful")
print(x)
# WHY \b at the beginning and at the end does not work???

#%%
# solution from mentor is
import re
x = re.findall(r"(\w+[aeiou]{3,}\w+)" , "Life is beautiful")
print(x)
# uses \w+ and not \b to return full words and not part of a word
# \w finds alphanumeric characters (letter, number, underscore)
# maybe this is better because I have uppercase and lowercase

#%%
# answer
import re
def multi_vowel_words(text):
  pattern = r"(\w+[aeiou]{3,}\w+)"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []

#%%
"""
QUESTION 3
When capturing regex groups, what datatype does the groups method return?
A tuple
"""
#%%
"""
QUESTION 4
The transform_comments function 
converts comments in a Python script into those usable by a C compiler. 
This means looking for text that begins with a hash mark (#) 
and replacing it with double slashes (//), which is the C single-line comment indicator. 
For the purpose of this exercise, 
we'll ignore the possibility of a hash mark embedded inside of a Python command, 
and assume that it's only used to indicate a comment. 
We also want to treat repetitive hash marks (##), (###), etc., as a single comment indicator,
 to be replaced with just (//) and not (#//) or (//#). 
 Fill in the parameters of the substitution method to complete this function:
"""
import re
def transform_comments(line_of_code):
  result = re.sub(___)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"

#%%
import re
x = re.search(r"#{1,}", "### Start of program")
print(x)
#%%
import re
x = re.sub(r"#{1,}", r"//", "### Start of program")
print(x)
# // Start of program

#%%
import re
x = re.sub(r"#{1,}", r"//", "  number = 0   ## Initialize the variable")
print(x)
# number = 0   // Initialize the variable

#%%
import re
x = re.sub(r"#{1,}", r"//", "  number += 1   # Increment the variable")
print(x)
#   number += 1   // Increment the variable

#%%
import re
x = re.sub(r"#{1,}", r"//", "  return(number)")
print(x)
#   return(number)

#%%
"""
QUESTION 5
The convert_phone_number function
 checks for a U.S. phone number format:
     XXX-XXX-XXXX 
     (3 digits followed by a dash,3 more digits followed by a dash, and 4 digits), 
and converts it to a more formal format that looks like this:
    (XXX) XXX-XXXX. 
Fill in the regular expression to complete this function.
"""
import re
def convert_phone_number(phone):
  result = re.sub(___)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300


#%%
import re
x = re.search(r"(\d{3})-(\d{3}-)(\d{4})", "My number is 212-345-9999.")
print(x)
print(x[1])
print(x[2])

#%%
import re
x = re.sub(r"(\d{3})-(\d{3}-)(\d{4})", r"(\1) \2\3", "My number is 212-345-9999.")
print(x)

#%%
# answer
import re
def convert_phone_number(phone):
  result = re.sub(r"(\d{3})-(\d{3}-)(\d{4})", r"(\1) \2\3", phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300

#My number is (212) 345-9999.
#Please call (888) 555-1234
#(123) 123-12345
#Phone number of Buckingham Palace is +44 303 123 7300

#%%

"""
Using Python to interact with the operating system, by Google
WEEK 3 – Regular Expressions
4   MODULE REVIEW
Qwiklabs Assessment: Working with Regular Expressions
Introduction
It's time to put your new skills to the test! 
In this lab, 
you'll have to find the users using an old email domain in a big list using regular expressions.
What you'll do
Replacing the old domain name (abc.edu) with a new domain name (xyz.edu).
Storing all domain names, including the updated ones, in a new file.
user_emails.csv
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
INDENTATION IS SUPER IMPORTANT!
"""
import re
import csv


def contains_domain(address, domain):
  """Returns True if the email address contains the given,domain,in the domain position, false if not."""
  domain = r'[\w\.-]+@'+domain+'$'
  if re.match(domain,address):
    return True
  return False


def replace_domain(address, old_domain, new_domain):
  """Replaces the old domain with the new domain in the received address."""
  old_domain_pattern = r'' + old_domain + '$'
  address = re.sub(old_domain_pattern, new_domain, address)
  return address

def main():
  """Processes the list of emails, replacing any instances of the old domain with the new domain."""
  old_domain, new_domain = 'abc.edu', 'xyz.edu'
  csv_file_location = 'user_emails.csv'
  report_file = 'updated_user_emails.csv'
  user_email_list = []
  old_domain_email_list = []
  new_domain_email_list = []

  with open(csv_file_location, 'r') as f:
    user_data_list = list(csv.reader(f))
    user_email_list = [data[1].strip() for data in user_data_list[1:]]

    for email_address in user_email_list:
      if contains_domain(email_address, old_domain):
        old_domain_email_list.append(email_address)
        replaced_email = replace_domain(email_address,old_domain,new_domain)
        new_domain_email_list.append(replaced_email)

    email_key = ' ' + 'Email Address'
    email_index = user_data_list[0].index(email_key)

    for user in user_data_list[1:]:
      for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
        if user[email_index] == ' ' + old_domain:
          user[email_index] = ' ' + new_domain
  f.close()

  with open(report_file, 'w+') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(user_data_list)
    output_file.close()

main()

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

#%%
"""
Using Python to interact with the operating system, by Google
WEEK 4 – Managing Data and Processes
4 MODULE REVIEW
Introduction:
Imagine one of your colleagues is struggling with a program that keeps throwing an error. 
Unfortunately, the program's source code is too complicated to easily find the error there. 
Let's write a script to search the log file called "fishy" for the exact error, 
    then output that error into a separate file* so you can work out what's wrong.
    separate file*: it is called "errors_found.log" and it is produced by the code we will write
What you'll do:
Write a script to search the log file using regex to find for the exact error.
Report the error into a separate file so you know what's wrong for further analysis.
I created the log file "fishy.log" (wrote on the Notepad the contents and saved as .log file)
I tested on Spyder
Log entries are written in this format:
Month Day hour:minute:second mycomputername "process_name"["random 5 digit number"] "ERROR/INFO/WARN" "Error description"
"""
#%%
"""
at first I will write part of the code to produce the list "returned_errors"
this list will serve as an argument for the second function that will produce the file "errors_found.log"
"""

import sys
import os
import re

def error_search(log_file):
    error = input("What is the error? ")
    returned_errors = []
    with open(log_file, mode='r',encoding='UTF-8') as file:
        for log in  file.readlines():
            error_patterns = ["error"]
            for i in range(len(error.split(' '))):
                error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_errors.append(log)
        file.close()
    print(returned_errors)
 
error_search("fishy.log")   # here I call the function by providing the argument, the fishy log file
                            # at the prompt of the input() function I reply error, and I get a list of log lines that contain the string "error". It is only a test so I can see what is the outout until here
                            # the exercise is to reply cron, at the prompt, I will do that later on

#%%
"""
this is the complete code
it produces a new log file based on my response at the prompt
"""
import sys
import os
import re
def error_search(log_file):
    error = input("What is the error? ")
    returned_errors = []
    with open(log_file, mode='r',encoding='UTF-8') as file:
        for log in  file.readlines():
            error_patterns = ["error"]
            for i in range(len(error.split(' '))):
                error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
                if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                    returned_errors.append(log)                
        file.close()
    return returned_errors

def file_output(returned_errors):
    with open(os.path.expanduser('~') + '/errors_found.log', 'w') as file:
        for error in returned_errors:
            file.write(error)
        file.close()  

if __name__ == "__main__":
    log_file = "fishy.log"#sys.argv[1] for working on the Linux OS command line
    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0) 
    
# IT WORKS!!
# I used the fishy log file I copied from the virtual Linux OS command line (which I saw with the cat command)
# A LOG FILE CALLED errors_found WAS CREATED ON MY C: DRIVE

#%%
"""
NOTES
write a function "error_search"
 that takes log_file as a parameter and returns "returned_errors".
Define an input function to receive the type of ERROR that the end-user would like to search and
 assign its result, to a Variable named "error".
The input() function takes the input from the user and then evaluates the expression. 
This means Python automatically identifies whether the user entered a string, a number, or a list. 
If the input provided isn't correct then Python will raise either a syntax error or exception. 
The program flow will stop until the user has given an input.
the input function uses a string typed in by the user
the input function always returns a string.
here we prompt the user to tyoe-in a string and then use that string.
we save the result of the input() function in a Variable called "error"
initialize the list returned_errors 
(we create an empty list which will be populated later
This will enlist all the ERROR logs as specified by the end-user through the input function.)
open the log file "fishy", in reading mode and use 'UTF-8' encoding.
apply the method readlines() to "fishy", this will produce a list in which every element comes from a line of the log file "fishy"
The readlines() method returns a list containing each line in the file as a list item.
ALL() FUNCTION
takes an iterable object as an argument. (iterable, lists, tuples, dictionaries, sets)
if all elements in the iterable object are true, then the all() function returns True
when the element is zero, then it is considered False, and the all() function returns False
when the element is false, then it is considered False, and the all() function returns False
so: 0 is the same as False
If the iterable is empty, then the all() function also returns True
Attention: For dictionaries the all() function checks the keys, not the values.
"""

#%%
"""
Using Python to interact with the operating system, by Google
WEEK 5 -Testing in Python
1 Simple Tests
    1.1 Intro to Module 5: Testing in Python
    1.2 What is testing?
    1.3 Manual Testing and Automated Testing
    1.4 Practice Quiz
"""
#%%
"""
1.1 Intro to Module 5: Testing in Python
Up to now, whenever we wrote Python code, either in the interpreter or on our scripts, 
we've been testing it by manually running it and seeing if it did what we expected it to do. 
Buckle up because that's about the change. 
In this module, we'll dive into how we can create automatic testing that will perform these kinds of checks for us. 
This lets us concentrate on just writing the code instead of checking if any changes that we make to it break the previous functionality. 
It will also help us verify that the features we add do what we expect in lots of possible ways. 
We'll learn about the different kinds of testing that are out there, and how we can use them to make our code more reliable, 
and finally, we'll also learn about how to handle errors and exceptions in Python code. 
How to trap those areas so they don't stop our programs from completing, how to raise errors when necessary, and how to test our code to generate the right kinds of errors. 
That sounds interesting. Now let's get to it.
My notes
So, we will examine the python code we wrote, not by ourselves, but by using automated tests
"""

#%%
"""
1.2 What is testing?
We need to be sure the code works correctly, that it produces the expected results.
When the code is simple, we can test the code manually 
When the code becomes complicated (loops, conditionals, many functions) we will do "software testing"
Software testing 
Software testing is a process of evaluating computer code to determine whether or not it does what you expect it to do. 
When you test a piece of software, you want to find the errors and defects and see where things go wrong. 
With software testing we are looking for errors and defects in our code.
We can write tests by ourselves (the tests are code too)
    these tests will examine the correctness of our code
The field of software testing is pretty broad
we'll explore some fundamental concepts involved like:
    automated testing, 
    unit test, 
    integration test, and 
    test-driven development
Up next, we'll talk about the differences between manual and automated testing
"""

#%%
"""
1.3 Manual Testing and Automated Testing
<< Manual Testing of the code >>
run the code with different parameters and see if it returns the expected values.
command line
Executing a script with different command-line arguments to see how its behavior changed is an example of manual testing. 
interpreter
Using the interpreter to try our code before putting it in a script is another form of manual testing. 
So, we provide the various parameters and we examine to see if the results are the expected ones
<< Automatic testing of the code >>
we write another piece of code which examines the previous code:)
The goal of automatic testing is to automate the process of checking if the returned value matches the expectations. 
Instead of us humans running a function over and over with different parameters and checking the results are
 what we expected them to be, we let the computer do this for us. 
Automatic testing means we'll write code to do the test.     
<< Conclusion >>
Automatic testing of code is far better than manual testing of code
The reason is that with automatic testing we can use a lot of different values known as "test cases"
The more test cases that you include in your test, the better tested your code is 
    and the more you can guarantee that your code does what you expect it to do.
When for some reason the results don't match the expectations, the automatic testing code will RAISE AN ERROR, 
    so we can check the code and find out what's going on. 
There's a bunch of different types of tests that we can write to perform automatic testing. 
    The one that we're going to concentrate on in the next few videos is called unit testing
"""
#%%
"""
1.4 Practice Quiz
1.
Question 1
You can verify that software code behaves correctly using test ___.
Loops
Functions
Arguments
Cases CORRECT? YES The software code should behave the way you expect with as many possible values or test cases.
2.
Question 2
What is the most basic way of testing a script?
Write code to do the tests.
Different parameters with expected results. CORRECT?The most basic way of testing a script is to use different parameters and get the expected results.
Let a bug slip through. 
Codifying tests into the software.
3.
Question 3
When a test is codified into its own software, what kind of test is it?
Unit test
Integration test
Automatic test CORRECT?YES Codifying tests into its own software and code that can be run to verify that our programs do what we expect them to do is automatic testing.
Sanity testing
4.
Question 4
Using _____ simplifies the testing process, allowing us to verify the program's behavior repeatedly with many possible values.
integration tests
test cases CORRECT? YES Test cases automatically test with a range of possible values to verify the program’s behavior.
test-driven development
interpreter
5.
Question 5
The more complex our code becomes, the more value the use of _____ provides in managing errors.
loops
functions
parameters
software testing CORRECT? YES Software testing is the process of evaluating computer code to determine whether or not it does what you expect it to do, and the more complex the code, the more likely failure is.
"""

#%%
"""
Using Python to interact with the operating system, by Google
WEEK 5 -Testing in Python
2 Unit Tests
    2.1 Unit Tests
    2.2 Writing Unit Tests in Python
    2.3 Edge Cases
    2.4 Additional Test Cases
    2.5 Unit Test Cheat-Sheet
    2.6 Help with Jupyter Notebooks
    2.7 Practice Quiz
"""
#%%
"""
2.1 Unit Tests
Unit tests target a specific piece of code and test it.
Unit tests are the most common type of software tests
Unit tests are used to verify that small isolated parts of a program are correct
Unit tests are generally written alongside the code 
    to test the behavior of individual pieces or units like functions or methods
An important characteristic of a unit test is isolation
A Unit test should only test the function or method that's being tested
This ENSURES that:
    any success or failure of the test is caused by the behavior of the unit in question and 
    DOES NOT RESULT from some external factor like the network being down or a database server being unresponsive
So, we are testing a specific method or function of the code itself and  NOT an external factor that has nothing to do with our code!
<< Please see below an EXAMPLE of how to call a function directly in the command line using the keyword "from" >>
 The purpose of the keyrword "from" is to use it inside the testing script I will write in order to test my initial script
in the Linux OS command line we call the function we want to test WITHOUT having to write the module name
(it is like calling the function under testing, "directly")
debugging = the process of identifying and removing errors from the code
EXAMPLE 1a
# shebang line in Linux OS command line: #!/usr/bin/env python3
# we open to see the py file rearrange.py with the cat command: cat rearrange.py
# import re
# def rearrange_name(name):
#     result = re.search(r"^([\w .]*), ([\w .]*)$", name)
#     return "{} {}".format(result[2], result[1])
syntax for the code above:
re.search(pattern, text)
the "result" is the output, after applying the method search() of the re module of python, and re means regex
I prefer to use the Match Object x form W3 schools, so I will re-phrase the above code
As we see we use the capturing groups concept (see 2 sets of parentheses) and 
   then we "choose" the 2 capturing groups with x[1] and x[2] as if we were doing indexing (give an index to retrieve what we want) 
"""
#%%
"""
here I am re-phrasing the code in order to use the Match Object x 
the function "rearrange_name" changes the sequence of the surname, name into name,surname
"""
import re
def rearrange_name(name):
    x = re.search(r"^([\w .]*), ([\w .]*)$", name)
    print("{} {}".format(x[2], x[1]))
rearrange_name("Lovelace, Ada") # I wrote this argument MANUALLY!! I am calling the function "rearrange_name" by providing the argument Lovelace,Ada

# Output is; Ada Lovelace, so perfect, it works
#%%
"""
EXAMPLE 1b
we will use the keyword "from" in the Linux OS command line
this way we can use the function rearrange_name at the command line, and ofcourse test it by providing an argument
in Linux OS command line write: 
#python3
#from rearrange import rearrange_name
as we see the rearrange is the MODULE that contains the rearrange_name FUNCTION
By importing it in this way, we can call the function without having to write the module name each time we want to call it, like this.
#rearrange_name("Lovelace, Ada") # I wrote this argument MANUALLY!!
# output is: 'Ada Lovelace'
"""

#%%
"""
2.2 Writing Unit Tests in Python
In video question
What module can you load to use a bunch of testing methods for your unit tests?
Answer: the "unittest" module.
        This module provides a TestCase class with a bunch of testing methods.
        
so,
we have the rearrange.py script, it contains the function "rearrange_name", which re-arranges the order from last name, first name to the opposite.
previously, we tested the script manually by providing the argument "Lovelace, Ada" and runned the script to see if it changed the order.
    It did change the order, but we tested MANUALLY by providing an argument
now, we will write another script called "rearrange_test.py" that will TEST the script rearrange.py
    now, we will test AUTONATICALLY, we will not provide the arguments for the function under testing, instead the computer will do that for us
    we need a code that runs the test and verifies the output
"""
#%%
"""
so, lets write the rearrange_test.py script that will test the rearrange.py script!
WRITE the shebang line in Linux OS command line: #!/usr/bin/env python3
we will test the function "rearrange_name" of the module "rearrange"
My question: when did rearrange become a module?!!! WE treat the rearrange.py as a module? Yes we do, see above the example with the keyword "from"
WRITE: from rearrange import rearrange_name # here we import the function to be tested "from" the py file "rearrange? yes we do
Now we are ready to start writing the tests.
To help us with that, Python provides a module called "unittest". 
This module includes a number of classes and methods that let us easily create unit tests for our code. 
The first thing we'll do is import the unit test module we'll need for testing.
The "unittest" module provides a test case class ("TestCase" class) with a bunch of testing methods ready to use
we will create our own class by inherits from "TestCase" class, thus inheriting all those existing testing methods.
The class that we will create, we'll name it  "TestRearrange" class
WRITE: import unittest
WRITE: class TestRearrange(unittest.TestCase):
    
so, we create a new class that inherits testing methods from the class TestCase of the module unittest
    
Any methods we define in our TestRearrange class that start with the prefix test 
    will automatically become tests that can be run by the testing framework. 
So we're ready to write our first test case.   
WRITE:      def  test_basic(self): # this is a method called "test_basic"
                testcase = 'Lovelace, Ada'
                expected = 'Ada, Lovelace'
                self.assertEqual(rearrange_name(testcase), expected)
With this method which we've called test_basic, we kick off by setting up our expected inputs and outputs.
We then use the assertEqual method provided to us by the TestCase class we inherited from,
    to verify that what we expected is exactly what we got. 
The assertEqual method basically says both of my arguments are equal. 
    If that statement's true, then the test passes. 
    If it's false, the test fails and an error is printed to the screen when the test is run.
WRITE: unittest.main()
the unittest.main() function which will run the test for us.
"""
#%%%
"""
I made two py files
rearrange.py, script to be tested
rearrange_test.py, script used to do the testing
Indeed, I use the first script as a "module"
Save both on my C drive
when I run the rearrange_test.py, it tests/examines the rearrange.py
The output I get is: 
Ran 1 test in 0.050s
OK
"""
#%%
""" rearrange.py"""

import re
def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    return "{} {}".format(result[2], result[1])

#%%
"""rearrange_test.py """
from rearrange import rearrange_name
import unittest
class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()

#%%
"""
2.3 Edge Cases
In the previous example we only used one test case (one value, one argument).
we tested if testcase Lovelace, Ada was changed into expected Ada, Lovelace and the test was successful, the initial code worked correctly.
But we need more test cases to use in our testing script
For example lets see what happens when test case = "" empty string and also expected=""
We're saying that we expect our function to return an empty string whenever it sees an empty string.
See below the initial code and the test code 
we run the rearrange_test1.py to test the code on rearrange.py and we get an error
TypeError: 'NoneType' object is not subscriptable
We have just discovered an Edge Case!
Edge Case
Edge cases are inputs to our code that produce unexpected results, 
    and are found at the extreme ends of the ranges of input we imagine our programs will typically work with. 
Edge cases usually need special handling in scripts in order for the code to continue to behave correctly.
In our rearranging example, we can handle this edge case 
    by performing a simple check of the result variable before operating with it.
    
    
we run the rearrange_test1.py to test the code on rearrange1.py the test is successful and our original code works as expected
we added an if condition in our original script to deal with a result that is None
es, our test passed. We fixed a bug in our code, and by adding an automatic test, we can make sure that it won't happen again.
In our specific case, returning the original value makes sense when we can't rearrange it.
Remember that it's bad for automation to fail silently. Other kinds of edge cases usually include things like passing zero to a function that expects a number, or negative numbers, or extremely large numbers. These types of conditions are good to consider when writing your test, since they can cause your code to crash or behave in unexpected ways.    
My Notes:
    so, edge cases are test cases that we must think of and incorporate them in our test code and then examine our inital code
    I provide the test case and the expected and based on that the test code is testing if the initial code is working correctly.
    but I must think of test case examples? Are not any test cases ready in the TestCase class of the unittest module?
"""
#%%
""" rearrange.py"""

import re
def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    return "{} {}".format(result[2], result[1])
#%%
""" rearrange1.py"""

import re
def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result is None:
        return ""
    return "{} {}".format(result[2], result[1])
#%%
"""rearrange_test1.py """
from rearrange import rearrange_name # I can examine rearrange and also rearrange1
import unittest
class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)
             
unittest.main()

# when we run this code for rearrange.py we get the error
# TypeError: 'NoneType' object is not subscriptable

# when we run this code for rearrange1 .py we get the output
# Ran 2 tests in 0.003s
# OK

#%%
"""
2.4 Additional Test Cases
in rearrange_test.py we have one test case
in rearrange_test1.py we have two test cases
now we will write rearrange_test2.py and will add one more test case
the collection of test cases is called a suite
our initial code is searching with a regex for the last and first name
    then returns first name then last name
    
if the first name contains space and other chars like first name= Grace M. , last name=Hopper
so now, we will write one more test case when we have a double first name in the text we are examining with our initial code
Also we will write the rearrange_test3.py and will add one more test case, to see what happens when there is only one name like Voltaire!
"""
#%%
"""rearrange_test2.py """
from rearrange1 import rearrange_name # I can examine rearrange and also rearrange1
import unittest
class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)
    def test_double_name(self):        
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)
             
unittest.main()

# I examine rearrange1.py with the test code rearrange_test2.py
# the output is
#Ran 3 tests in 0.004s
#OK

#%%
"""rearrange_test3.py """
from rearrange1 import rearrange_name # I can examine rearrange and also rearrange1
import unittest
class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)
    def test_double_name(self):        
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)
    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase), expected)
            
unittest.main()

# I examine rearrange1.py with the test code rearrange_test3.py
#Ran 4 tests in 0.006s
#
#FAILED (failures=1)

"""
In Spyder I get the message FAILED failures=1 but no more info
in the video:
    FAIL: test_one_name # it tells me which function failed
    Assertion Error ""!="Voltaire" # empty string is not equal to Voltaire string
It looks like our function returned an empty string instead of the original name. 
That's because there's a bug in our code. !
So let's go to rearrange1.py and find the bug then write rearrange2.py
"""
#%%
""" rearrange1.py"""

import re
def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result is None:
        return ""
    return "{} {}".format(result[2], result[1])

"""
When we checked if the result was none, we returned an empty string, which made our previous test pass. 
What's happening now is that we're passing a name that doesn't include a comma, which makes a result variable none, and so the function is returning an empty string. The fix for this is pretty simple. 
Instead of returning an empty string when the result is none, we'll return the original name variable.
"""
#%%
""" rearrange2.py"""

import re
def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])



#%%
"""rearrange_test3.py """
from rearrange2 import rearrange_name # I can examine rearrange and also rearrange1 and also rearrange2.py
import unittest
class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)
    def test_double_name(self):        
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)
    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase), expected)
            
unittest.main()

"""
Now that I have fixed the bug in the initial code
I examine rearrange2.py with rearrange_test3.py
and the output is
Ran 4 tests in 0.008s
OK
Bingo! We fixed all the bugs and all our tests passed. 
One of the great things about running tests in a suite like this, 
    is that we now know that all the test cases we wrote were handled correctly. 
Our code works for basic names, empty strings, double names, and single names.
If we found another case that made our tests break, we could add it to the suite, fix the bug, and then run the whole suite again, being assured that all the other cases are still working. 
My notes:
    so essentially, i write code to test my initial code
    in the test code, I use keyword "from" to examine the initial code and keyword "import" to examine a specific function of the initial code
    then I use the module unittest and its class TestCase to create the suite with my tests (which are functions)
"""

#%%
"""
2.5 Unit Test Cheat-Sheet
Frankly, the unit testing library for Python is fairly well documented, but it can be a bit of a dry read. 
Instead, we suggest covering the core module concepts, and then reading in more detail later.
Best of Unit Testing Standard Library Module (the module unittest)
The unittest module provides a rich set of tools for constructing and running tests
The unittest module can be used from the command line to run tests from modules, classes or even individual test methods
Understand a Basic Example: 
    https://docs.python.org/3/library/unittest.html#basic-example
Understand how to run the tests using the Command Line: 
    https://docs.python.org/3/library/unittest.html#command-line-interface
Understand various Unit Test Design Patterns: 
    https://docs.python.org/3/library/unittest.html#organizing-test-code
Understand the uses of setUp, tearDown; setUpModule and tearDownModule
Understand basic assertions:
These methods are used instead of the assert statement so
     the test runner can accumulate all test results and produce a report.
Method                      Checks that	
assertEqual(a, b)           a == b	                to check for an expected result
assertNotEqual(a, b)        a != b	
assertTrue(x)               bool(x) is True	        to verify a condition
assertFalse(x)              bool(x) is False	    to verify a condition
assertIs(a, b)              a is b	
assertIsNot(a, b)           a is not b	
assertIsNone(x)             x is None	
assertIsNotNone(x)          x is not None	
assertIn(a, b)              a in b	
assertNotIn(a, b)           a not in b
assertIsInstance(a, b)      isinstance(a, b)	
assertNotIsInstance(a, b)	  not isinstance(a, b)
Understand more specific assertions such as assertRaises: 
    https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises
"""
#%%
"""
2.6 Help with Jupyter Notebooks
We've aimed to make our Jupyter notebooks easy to use. But, if you get stuck, you can find more information here.
If you still need help, the discussion forums are a great place to find it! Use the forums to ask questions and source answers from your fellow learners.
If you want to learn more about Jupyter Notebooks as a technology, check out these resources:
Jupyter Notebook Tutorial, by datacamp.com
How to use Jupyter Notebooks, by codeacademy.com
Teaching and Learning with Jupyter, by university professors using Jupyter
"""

#%%
"""
2.7 Practice Quiz
Practice Notebook - Unit Tests and Edge Cases
Below we have some code that makes a list of specific letters found in any string. 
If you run it, you can see what it does.
"""

import re 
  
my_txt = "An investment in knowledge pays the best interest."

def LetterCompiler(txt):
    result = re.findall(r'([a-c]).', txt)
    return result

print(LetterCompiler(my_txt))

# OUTPUT IS ['a', 'b']
# syntax: look for the regex a-c in the text txt
# we call and also print the function with the argument "my_txt"
# we are searching for lowercase letters from a to c
# there is one a and one b, we see them in the output as elements of a list
# Note: SEARCH FUNCTION RETURNS ONLY THE 1ST MATCH, findall() returns all matches as elements of a list

#%%
"""
From the output, you can see that the LetterCompiler( ) function finds all matches for the letters a through c 
in an input string if followed by another character and returns them as a list of strings, 
with each string representing one match. Nice.
But can we be sure that this function will always do what we expect it to do? 
We need to write code to help us catch mistakes, errors and bugs. 
This code should automate the process of checking if the returned value of our code matches 
the expectations by dynamically feeding into it test cases. 
Since we're dynamically feeding in different strings, it would be prudent to create unit tests for our code. 
We can use the module unittest for this.
Fill in the blanks below to create an automatic unit test that verifies whether input strings have the correct list
 of string matches.
"""

import unittest

class TestCompiler(unittest.TestCase):

    def test_basic(self):
        testcase = "The best preparation for tomorrow is doing your best today."
        expected = ['b', 'a', 'a', 'b', 'a']
        self.assertEqual(LetterCompiler(testcase), expected)

"""
Now that your automatic test is coded, you need to call the unittest.main( ) function to run the test. 
It is important to note that the configuration for running unit tests in Jupyter 
    is different than running unit tests from the command line. 
Running unittest.main( ) in Jupyter will result in an error. 
You can see this by runnig the following cell to execute your automatic test.
"""
unittest.main()
"""
E
======================================================================
ERROR: /home/jovyan/ (unittest.loader._FailedTest)
----------------------------------------------------------------------
AttributeError: module '__main__' has no attribute '/home/jovyan/'
----------------------------------------------------------------------
Ran 1 test in 0.001s
FAILED (errors=1)
An exception has occurred, use %tb to see the full traceback.
SystemExit: True
Yikes! SystemExit: True means an error occurred, as expected. 
The reason is that unittest.main( ) looks at sys.argv. 
In Jupyter, by default, the first parameter of sys.argv is what started the Jupyter kernel 
    which is not the case when executing it from the command line. 
This default parameter is passed into unittest.main( ) as an attribute when you don't explicitly pass it
    attributes and is therefore what causes the error about the kernel connection file not being a valid attribute. 
Passing an explicit list to unittest.main( ) prevents it from looking at sys.argv.
Let's pass it the list ['first-arg-is-ignored'] for example. 
In addition, we will pass it the parameter exit = False to prevent unittest.main( ) from shutting down 
    the kernel process. 
Run the following cell with the argv and exit parameters passed into unittest.main( ) to rerun your automatic test.
"""
unittest.main(argv = ['first-arg-is-ignored'], exit = False)

"""
----------------------------------------------------------------------
Ran 1 test in 0.091s
OK
<unittest.main.TestProgram at 0x7f7bb0400d68>
Did your automatic test pass? Was OK the result? 
If not, go back to your automatic test code and make sure you filled in the blanks correctly. 
If your automatic test passed, great! 
You have successfully filled in the gaps to create an automatic test that verifies whether 
    input strings have the correct list of string matches.
This is great work so far, but your automatic test includes only one test case. 
You need to make it grow. 
You can feed in more strings as test cases to test whether your code works in the general case. 
But you should also see what happens when you give it some input that 
    you might not expect it to run into under normal operations.
Edge cases are inputs to code that produce unexpected results, 
    and are found at the extreme ends of the ranges of input we imagine programs will typically work with. 
Can you use the cell below to write some edge cases? 
We've already filled in another test case for you! 
As it is, this test will run fine. 
Can you come up with at least one test case that you think could result in a wrong return value? 
No wrong answers! Feel free to play around.
"""
class TestCompiler2(unittest.TestCase):
    
    def test_two(self):
        testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)

# EDGE CASES HERE

unittest.main(argv = ['first-arg-is-ignored'], exit = False)

"""
----------------------------------------------------------------------
Ran 2 tests in 0.072s
OK
Did you find any edge cases? 
If not, continue working on it. 
Choosing test cases can be an exercise in creativity. 
Coming up with different ways a code might break can be super fun! 
When you have found an edge case, think about special handling in your script in order for your code to 
    continue to behave correctly.
If you are out of ideas: Try removing the spaces and figure out why they were in the example testcase. 
Does that give you an idea for other tests?
When you have found at least one edge case, you are all done with this notebook. 
You should take a moment to reflect on what you've done so far. 
It's super impressive and it's going to fit nicely in your IT toolkit.
"""

"""
My notes:
    I CREATED THE PY FILE quizPythonOS_5_2
    import re 
    my_txt = "An investment in knowledge pays the best interest."
    def LetterCompiler(txt):
        result = re.findall(r'([a-c]).', txt)
        return result
    print(LetterCompiler(my_txt))
    
    Then, I CREATED THE PY FILE quizPythonOS_5_2_test
    from quizPythonOS_5_2 import LetterCompiler # from the py file then import the specific function
    import unittest
    class TestCompiler(unittest.TestCase):
    def test_basic(self):
        testcase = "The best preparation for tomorrow is doing your best today."
        expected = ['b', 'a', 'a', 'b', 'a']
        self.assertEqual(LetterCompiler(testcase), expected)
    unittest.main() # UNTIL HERE OUTPUT IS Ran 5 tests in 0.199s, OK (MY NOTES 5 letters so 5 tests?I am putting the function LetterCompiler to work with the test case as its argument. Then I check if the output is equal to "expected" )
    
    THEN I ADDED ONE MORE TEST CASE
    from quizPythonOS_5_2 import LetterCompiler # from the py file then import the specific function
    import unittest
    class TestCompiler(unittest.TestCase):
    def test_basic(self):
        testcase = "The best preparation for tomorrow is doing your best today."
        expected = ['b', 'a', 'a', 'b', 'a']
        self.assertEqual(LetterCompiler(testcase), expected) 
    def test_two(self):
        testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)
    
    unittest.main() # UNTIL HERE OUTPUT IS Ran 6 tests in 0.218s, OK
    
"""

#%%
"""
Using Python to interact with the operating system, by Google
WEEK 5 -Testing in Python
3 Other Test Concepts
    3.1 Black Box vs. White Box
    3.2 Other Test Types
    3.3 Test-Driven Development
    3.4 More About Tests
    3.5 Practice Quiz
"""
#%%
"""
 3.1 Black Box vs. White Box
We've explored unit test in detail, unti tests are both simple to write and are very powerful way to catch bugs. 
But there's a lot more to software testing. 
One interesting concept is whether our test is a white-box test or a black-box test. 
We can write unit tests that are either white or black-box, depending on which testing methodology is chosen.
One way isn't strictly better than the other since each gives you a different path to make your code more reliable. 
Not everything is so black and white or as we'd say in the coding world, binary. 
As an IT specialist, you may need to test that software written by others behaves the way you expect it to. 
To do this, you can use the combination of black-box and white-box test.
Let's say that you have an online catalog of products that are sold by your company. 
    you can have white-box tests that calls the different functions used by that page, checking that the prices are displayed in the right currency, that the description is correctly wrapped and so on.
    you can have a black-box test that verifies that the details for a product are displayed when you open the page for a specific product. 
WHITE BOX TESTING
also called clear-box or transparent testing
relies on the test creators knowledge of the software being tested to construct the test cases.
the test creator knows how the code works and can write test cases that use the understanding to make sure that everything is performing the way it's expected to
White-box tests are helpful because a test writer can use their knowledge of the source code to create tests that cover most of the ways that the program behaves.
If unit tests are run alongside or after the code has been developed, the test cases are made with a knowledge of how software works. 
    They are white-box tests.
BLACK BOX TESTING
the software being tested is treated like an opaque box.
the tester doesn't know the internals of how the software works. 
Black-box tests are written with an awareness of what the program is supposed to do, its requirements or specifications, but not how it does it. 
For example, a simple black-box test could be to verify that when you type www.google.de in your browser, the Google Search page for Germany is returned. 
You might not know how Google's servers process your request but you know what the end result should be. 
Black-box tests are useful because they don't rely on the knowledge of how the system works. 
    This means their test cases are less likely to be biased by the code. 
    They usually cover situations not anticipated by the programmer who originally wrote the script. 
If the unit tests are created before any code is written based on specifications of what the code is supposed to do, they can be considered black-box unit test.
Black-box tests have no knowledge of the code.
when using Black-box tests, the code is not transparent
"""
#%%
"""
3.2 Other Test Types
UNIT TEST
Unit tests should focus on one specific unit, a functional method that being tested. 
This allows the test to verify that the unit provides expected functionality regardless of the rest of the environment.
unit tests shouldn't cross boundaries to do things like make a network request or integrate with an API or database
(API: Application Programming Interface, is a set of definitions and protocols that allow technology products and services to communicate with each other via the internet.)
Isolation ensures that any success or failure of a unit test is caused by the behavior of the unit in question, and doesn't result from some external factor.
INTEGRATION TEST
Integration tests verify that the interactions between the different pieces of code in integrated environments are working the way we expect them to.
the goal of an integration test is to verify that these interactions work and make sure the whole system works as you expect it to.
Integration tests, usually take the individual modules of code that unit tests have verified, then combine them into a group to test. 
Depending on what our program does, and how it interacts with the rest of the systems involved, we might need to create a separate TEST ENVIRONMENT for our test. 
Which runs a test version of our software that we're trying to verify. 
We might be able to run our test against the actual version of our system that's running, but that's only if our code doesn't make any changes to the production environment. 
Whenever your company is deploying a system that's somewhat complex, having integration tests will help make sure that all the pieces come together the way you expect them to. 
These tests usually take a bit more work to set up because you'll need to make sure that you have the test versions of all relevant systems. 
But they might help catch issues that unit tests won't text, so the extra effort is definitely worth it. 
For example, if the service you're trying to test interacts with a database, you want to set up a separate test database with a test user and a test tables. 
This lets you run all tests you need in an environment that you can control without risking modifying the production database. 
Verifying an automation script works well with the overall system and external entities
REGRESSION TEST
A variant of unit tests are regression tests. 
They're usually written as part of a debugging and troubleshooting process to verify that an issue or error has been fixed once it's been identified. 
Say our script has a bug and we're trying to fix it. 
A good approach to doing this would be at first to write a test that fails by triggering the buggy behavior, then fix the bug so that a test passes. 
Regression tests are useful part of a test suite because they ensure that the same mistake doesn't happen twice. 
The same bug can't be reintroduced into the code because introducing it will cause the regression test to fail. 
A test that is written after a bug has been identified in order to ensure the bug doesn't show up again later
SMOKE TEST
this test finds out if the program can run in its basic form before undergoing more refined test cases.
Smoke tests sometimes called build verification tests, get their name from a concept that comes from testing hardware equipment. 
Plug in the given piece of hardware and see if smoke starts coming out of it. 
When writing software smoke test serve as a kind of sanity check to find major bugs in a program. 
Smoke tests answer basic questions like, does the program run? 
These tests are usually run before more refined testing takes place. 
Since if the software fails the smoke test you can be pretty sure none of the other tests will pass either. 
As they say where there's smoke there's fire. 
For a web service the smoke test would be to check if there's a service running on the corresponding port. 
For an automation script, the smoke test would be to run it manually with some basic input and check that the script finishes successfully.
LOAD TEST
Other types of tests our load tests. 
These tests verify that the system behaves well when it's under significant load. 
To actually perform these tests will need to generate traffic to our application simulating typical usage of the service. 
These tests can be super-helpful when deploying new versions of our applications to verify that performance does not degrade. 
For example, we might want to measure the response time of our website while there are 100 requests per second on our pages, or a 1000, or 10,000. 
The actual numbers will depend on the expectations of how much traffic our website will receive.
used to verify the software’s ability to behave well under significantly stressed testing conditions
TEST SUITE
Taking together a group of tests of one or many kinds is commonly referred to as a test suite. 
A good diversity of test types can create a more robust test suite that helps ensure your scripts and automation, do what you tell them to. 
"""

#%%
"""
3.3 Test-Driven Development
You might expect that most testing happens after the code has been written. 
This seems like a natural progression. 
First you write your script then you write tests that verify that the script does what you want it to do. 
But this isn't always the best approach. 
A process called test-driven development or TDD calls for creating the test before writing the code. 
The test-driven development cycle typically involves first writing a test then running it to make sure it fails.
Once you've verified it fails, you write the code that will satisfy the test then run the tests again. 
If it passes you can continue on to the next part of your program. 
If it fails you Debug and run the test again. 
The cycle is repeated for each new feature of your script.
Remember that good tests help make any automation and script you write more robust, resilient, and less buggy
Many companies take testing a step further and combine it with our version control systems and development processes. 
When engineers submit their code, it's integrated into the main repository and tests are automatically run against it to spot bugs and errors in a process called Continuous Integration. 
Although useful, setting up a continuous integration process can be a big undertaking. 
Will talk more about it in a later course. 
In the meantime, if you use unit tests to validate the code you write, you're already on your way to a more reliable and robust automation.
Testing, while developing code may increase the code completion time.This is the only disadvantage of TDD Test-Driven Development
My notes:
    so, I write the script piece by piece while testing at the same time
"""

#%%
"""
3.4 More About Tests
Check out the following links for more information:
https://landing.google.com/sre/sre-book/chapters/monitoring-distributed-systems/
https://landing.google.com/sre/sre-book/chapters/testing-reliability/
https://testing.googleblog.com/2007/10/performance-testing.html
https://www.guru99.com/smoke-testing.html
https://www.guru99.com/exploratory-testing.html
https://testing.googleblog.com/2008/09/test-first-is-fun_08.html
"""
#%%
"""
3.5 Practice Quiz
Practice Quiz: Other Test Concepts
TOTAL POINTS 5
1.
Question 1
In what type of test is the code not transparent?
1 point
Test-driven development
White-box test
Smoke test
Black-box test CORRECT
2.
Question 2
Verifying an automation script works well with the overall system and external entities describes what type of test?
1 point
Regression test
Load test
Integration test CORRECT
Smoke test
3.
Question 3
_____ ensures that any success or failure of a unit test is caused by the behavior of the unit in question, and doesn't result from some external factor.
1 point
Regression testing
Integration
Isolation CORRECT
White-box testing
4.
Question 4
A test that is written after a bug has been identified in order to ensure the bug doesn't show up again later is called _____
1 point
Load test
Black-box test
Smoke test
Regression test CORRECT
5.
Question 5
What type of software testing is used to verify the software’s ability to behave well under significantly stressed testing conditions?
1 point
Load test CORRECT
Black-box test
Smoke test
Regression test
"""

#%%
"""
Using Python to interact with the operating system, by Google
WEEK 5 -Testing in Python
4 Errors and Exceptions
    4.1 The Try-Except Construct
    4.2 Raising Errors
    4.3 Testing for Expected Errors
    4.4 Handling Errors Cheat-Sheet
    4.5 Practice Quiz
"""
#%%
"""
4.1 The Try-Except Construct
how to handle errors when they're raised by the functions that we call
In-Video question
When a try block is not able to execute a function, 
which of the following return examples will an exception block most likely NOT return?
Answer="Error". Awesome! An exception is not meant to produce an error, but to bypass it.
When writing Python code, the interpreter generates errors.
TypeError
Indexerror
ValueError
etc.
Up to now whenever the interpreter threw one of these errors we changed our code to avoid the error.
Until now we have corrected our code by using a condition to avoid the error.
The errors cause our program to stop.
See example 1 to see the use of conditions
See Example 2 to see the use of the Try-Except Construct
"""


"""
Example 1
Say you had a function that opened a file and did some processing on it. 
we are using five if conditions to avoid errors
BUT there could be other situations that could cause the open function to raise an error.
Therefore using numerous if conditions is not logical, instead we will use the TRY-EXCEPT CONSTRUCT
"""
def read_file(filename):
    if not os.path.exists(filename): # if condition when the file does not exist
        return " "
    if not os.path.isfile(filename): 
        return " "
    if not os.access(filename, os.R_OK ): ## the user doesn't have permissions to read the file
        return " "
    if is_locked(filename): # the file is locked by different process and can't be opened right now
        return " "
    if is_not_accessible(filename):
        return " "

"""
Example 2
the function "character_frequency" counts the frequency of each character in the given file
In this example, are calling the open function inside a try-except block
The Try-Except block first tries to do the operation that we want, which in this case is to open the file. 
If there's an error, it then goes into the accept part of the block that matches the error 
    and does whatever cleanup is necessary. 
Here we have only one except block, for the OSError error type, but there could be more blocks 
    if the functions called could raise other types of errors. 
So, when writing a try-except block, the important thing to remember is that
    the code in the except block is only executed if one of the instructions in the try block raise an error of the matching type. 
In this case, in the except-block, we're returning "None" to indicate to the calling code that 
    the function wasn't able to do what was requested of it. 
Returning "None" when something fails is a common pattern but not the only one.
We could also decide to set a variable to some base value like zero for numbers, empty string for strings, 
    empty list for list, and so on. 
It all depends on what our function does and what we need to get that work done. 
The important point is that when we have an operation that might raise an error 
    we want handle that failure gracefully by using the try-except block. 
The operation could be opening a file, converting a value to a different format, executing a system command, 
    sending data over the network or any other action that might fail and isn't trivial to check with a conditional. 
To use a try-except block, we need to be aware of the errors that functions that we're calling might raise. 
This information is usually part of the documentation of the functions. 
Once we know this, we can put the operations that might raise errors as part of the try block, 
    and the actions to take when errors are raised as part of a corresponding except block.
My Notes 
TRY:    includes functions that might raise errors
EXCEPT: code here gets executed ONLY when an error is raised
        we can have multiple except blocks to deal with multiple types of errors raised in the try block
So, I place my function in the Try block.
    -if it does not raise an Error, everything works well and the Except block does not get executed
    -if it does raise an Error, then there is a problem in the code, the Except block is executed and I see "None" 
    which is typically used to indicate that code is not working
"""
def character_frequency(filename):
    # first try to open the file:
    try:
        f = open(filename)
    except OSError:
        return None
    #Now process the file:
    characters = {} # dictionary
    for line in f: # iterate over each line in the file
        for char in line: # iterate over each character in each line
            characters[char] = characters.get(char, 0) + 1 # now construct the dictionary
    f.close() # close the file
    return characters # return the dictionary 
    

#%%
"""
4.2 Raising Errors
Previously, we handled errors that were produced/raised by a function.
We placed the function inside the Try block and if it produced an error then the Accept block was activated 
    to show us the message "None" so we can understand something is wrong with the code
Now, we want to produce/raise an error by ourselves
By now, we've seen how we can handle errors when the code we call generates them
     and now we will see how we can raise our own errors when we want our code to signal that something hasn't gone well.
Keyword RAISE
Keyword "raise",    it is used to generate an error.
keyword ASSERT
Keyword "assert",   it is used to produce a message when a conditional is false.
                    it provides a reason when an error occurs after a function is called
Assertions will get removed from our code if we ask the interpreter to optimize it to run faster. 
So as a rule: 
    we should use RAISE to check for conditions that we expect to happen during normal execution of our code and 
    we should use ASSERT to verify situations that aren't expected but that might cause our code to misbehave.
In-Video question
What keyword can help to provide a reason for which an error has occurred in a function?
Answer: "assert"
raise generates an error
assert provides an explanation for the error
"""

"""
Example 1
This code works as long as the provided values are sensible. 
What would happen if the minlen variable is zero or negative number? 
Our function will allow an empty username as valid which doesn't make much sense. 
To prevent this from happening, we can add an extra check to our function 
    which will verify the receipt parameters are sane.
"""
"""
I create the  py file "validations", I saved it in on my C drive
(I will create another py file with testing code, to test the validations.py code!)
"""
def validate_user(username, minlen):
    if len(username) < minlen: # if length of username is smaller than defined minimum length, RETURN the value False
        return False
    if not username.isalnm(): # if the username does not contain alphanumeric characters, RETURN the value False
        return False
    return True # else RETURN the value True

"""
function takes 2 parameters: username and minlen
minlen is the minimum length the username can have, minimum number of characters in the username
if length of username is smaller than defined minimum length, RETURN the value False, not acceptable
we want the username to contain letters and numbers, in other words to be alphanumeric
if username is not alphanumeric then RETURN the value False, not acceptable
The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
else, if length of username is = or > than minimum length and if username is alphanumeric then everything is OK
    and RETURN True, acceptable
"""

#%%
"""
Example 2
Now I will use the keyword RAISE when the argument/test case is a username with a length smaller than 1
if length is <1 then this way an error will be raised to let us know
"""
"""
I update the py file validations.py
"""
def validate_user(username, minlen):
    if minlen < 1:
        raise ValueError("minlen must be at least 1") # keyword RAISE
    if len(username) < minlen: # if length of username is smaller than defined minimum length, RETURN the value False
        return False
    if not username.isalnm(): # if the username does not contain alphanumeric characters, RETURN the value False
        return False
    return True # else RETURN the value True

"""
if minimum length is smaller than 1 then raise a ValueError saying that minlen must be at least 1
"""
#%%
"""
I created the py file with testing code, "validations_test.py"
and I will try various test cases/arguments to test the code in validations.py 
PLEASE NOTE that I am not using the unittest method and the class TestCase and a suite of test cases here
I will just enter arguments and see the results that the testing script gives when testing my initial script!
"""
from validations import validate_user
validate_user("", -1)

# For these values I get the output ValueError: minlen must be at least 1
# This is normal since I used invalid arguments
# the function validate_user successfully raised an error

from validations import validate_user
validate_user("", 1)

# For these values I get the output False

from validations import validate_user
validate_user("myuser", 1)

# For these values I get the output AttributeError: 'str' object has no attribute 'isalnm'
# I get an error because I have only letters and not letters+numbers 

from validations import validate_user
validate_user(88, 1)

# For these values I get the output TypeError: object of type 'int' has no len()
# because the username is an integer and not alphanumeric, so its length cannot be calculated

from validations import validate_user
validate_user([], 1)

# For these values I get the output False

from validations import validate_user
validate_user(["name"], 1)

# For these values I get the output
# AttributeError: 'list' object has no attribute 'isalnm'

"""
An alternative to the keyword raise is the keyword assert
The keyword ASSERT tries to verify that a conditional expression is true, and if it's false
    it raises an assertion error with the indicated message. 
Let's add an assertion to our function.
we will update the validations.py again 
"""

"""
update again the  validations.py
"""
def validate_user(username, minlen):
    assert type(username) == str, "username must be a string"
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen: # if length of username is smaller than defined minimum length, RETURN the value False
        return False
    if not username.isalnm(): # if the username does not contain alphanumeric characters, RETURN the value False
        return False
    return True # else RETURN the value True

"""
test the updated validations.py
with validations_test.py
"""
from validations import validate_user
validate_user([3], 1)

# I get the output, AssertionError: username must be a string

#%%
"""
4.3 Testing for Expected Errors
In general when using unit tests (examining the output of a certain function, 
     a certain isolated part of our code), we must come up with a lot of test cases.
     This way we can foretell and prevent problems in our code
PREVIOUSLY, we wrote a script and then another script to test the first one.
in the testing script, I defined the test case and the expected and used 
    the assertEqual method to see if test case equals the expected
    ( self.assertEqual(rearrange_name(testcase), expected) )
NOW in the testing script I use a slightly different syntax
    the assertEqual method:
    syntax:
        self.assertEqual(function(chosen arguments), type of error)
    we provide the test case and then the expected error, eg False, True etc.
    example: self.assertEqual(validate_user("validuser", 3), True)
    the assertRaises method:
    syntax:
        self.assertRaises(type of error, function(chosen arguments))
    we provide the type of error expected, then the function with the chosen arguments
    example: self.assertRaises(ValueError, validate_user, "user", -1)
    
    In this case, we need to first pass the error that we expect the function to raise. 
    Then the function name, followed by any parameters that need to be passed to that function
    Behind the scenes, this method is calling the function that we want to test using the try except block 
    and checking that it does raise the error that we said it would raise. 
Both assertEqual and assertRaises are methods provided by the unittest module
In-Video question
When using the assertRaises method, what is passed first?
Answer: Error. Way to go! The expected error is passed first.
"""
"""
this is the testing script validations_test1
to distinguish it from the previous testing script
"""
import unittest
from validations import validate_user

class TestValidatedUser(unittest.TestCase):
    def test_valid(self): # I name the function according to the test I do
        self.assertEqual(validate_user("validuser", 3), True) # I instruct the computer to consider these arguments as True, as acceptable results

    def test_too_short(self):
        self.assertEqual(validate_user("inv", 5), False) # inv is 3 chars, the minlen is 5, so I characterize this as False and tell it to the computer
        
    def test_invalid_characters(self):
        self.assertEqual(validate_user("invalid_user", 1), False)

    def test_invalid_minlen(self):
        self.assertRaises(ValueError, validate_user, "user", -1)

unittest.main()

"""
in the video, 4 tests are done and it is OK
when I do it on Spyder I get the output
Ran 4 tests in 0.019s
FAILED (errors=2)
I did not investigate this further
"""

#%%
"""
4.4 Handling Errors Cheat-Sheet
Handling Errors Cheat-Sheet
Raise allows you to throw an exception at any time.
https://docs.python.org/3/tutorial/errors.html#raising-exceptions
Assert enables you to verify if a certain condition is met and throw an exception if it isn’t.
https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement
https://stackoverflow.com/questions/5142418/what-is-the-use-of-assert-in-python
The standard library documentation is kind of unclear. Basically `assert <something false>` will raise AssertionError, which the caller may need to handle.
In the try clause, all statements are executed until an exception is encountered.
https://docs.python.org/3/tutorial/errors.html#handling-exceptions
Except is used to catch and handle the exception(s) that are encountered in the try clause.
https://docs.python.org/3/library/exceptions.html#bltin-exceptions
Other interesting Exception handling readings:
https://doughellmann.com/blog/2009/06/19/python-exception-handling-techniques/
"""

#%%
"""
4.5 Practice Quiz
"""

"""
Below we have a function that removes an item from an input list. Run it to see what it does.
"""
my_list = [27, 5, 9, 6, 8]

def RemoveValue(myVal):
    my_list.remove(myVal)
    return my_list

print(RemoveValue(27)) # I call the function with an argument and I print/display the result of the function with that argument

# OUTPUT IS [5, 9, 6, 8]

"""
We used the RemoveValue() function to remove the number, 27 from the given list. Great! 
The function seems to be working fine. 
However, there is a problem when we try to call the function on the number 27 again. 
Run the following cell to see what happens.
"""
print(RemoveValue(27))

# OUTPUT IS ValueError: list.remove(x): x not in list

"""
From the above output we see that our function now raises a ValueError. 
This is because we are trying to remove a number from a list that is not in the list. 
When we removed 27 from the list the first time, it was no longer available in the list to be removed a second time. 
Python is letting us know that the number 27 no longer makes sense for our RemoveValue() function.
We'd like to take control of the error messaging here and pre-empt this error. 
pre-empt: προλαβαίνω, προδικάζω, anticipate, forestall, prevent, foretell
Fill in the blanks below to raise a ValueError in the RemoveValue() function if a value is not in the list. 
You can have the error message say something obvious like "Value must be in the given list".
"""
#%%
def RemoveValue(myVal):
    if myVal not in my_list:
        raise ValueError("Value must be in the given list")
    else:
        my_list.remove(myVal)
    return my_list

print(RemoveValue(27))

"""
Did your error message print correctly? 
Was the output something like: ValueError: Value must be in the given list? 
If not, go back to the previous cell and make sure you filled in the blanks correctly. 
If your error message did print correctly, great! 
You are on your way to mastering the basics of handling errors and exceptions.
"""
#%%
"""
Now, let's look at a different function. 
Below we have a function that sorts an input list alphabetically. Run it to see what it does.
"""
my_word_list = ['east', 'after', 'up', 'over', 'inside']

def OrganizeList(myList):
    myList.sort()
    return myList

print(OrganizeList(my_word_list))

# OUTPUT IS ['after', 'east', 'inside', 'over', 'up']

"""
We used the OrganizeList() function to sort a given list alphabetically. 
The function seems to be working fine. 
However, there is a problem when we try to call the function on a list containing number values. 
Run the following cell to see what happens.
"""
my_new_list = [6, 3, 8, "12", 42]
print(OrganizeList(my_new_list))

# OUTPUT IS TypeError: '<' not supported between instances of 'str' and 'int'
#%%
"""
From the above output we see that our function now raises a TypeError. 
This is because the OrganizeList() function makes sense for lists that are filled with only strings. 
Take control of the error messaging here and pre-empt this error by filling in the blanks below 
    to add an assert type argument that verifies whether the input list is filled with only strings. 
You can have the error message say something like "Word list must be a list of strings".
"""
def OrganizeList(myList):
    for item in myList:
        assert type(myList) == str, "Word list must be a list of strings"
    myList.sort()
    return myList

print(OrganizeList(my_new_list))

# OUTPUT IS AssertionError: Word list must be a list of strings

"""
Did your error message print correctly? 
Was the output something like: AssertionError: Word list must be a list of strings? 
If not, go back to the previous cell and make sure you filled in the blanks correctly. 
If your error message did print correctly, excellent! 
You are another step closer to mastering the basics of handling errors and exceptions.
"""
#%%
"""
Let's look at one last code block. 
The Guess() function below takes a list of participants, assigns each a random number from 1 to 9, 
    and stores this information in a dictionary with the participant name as the key. 
It then returns True if Larry was assigned the number 9 and False if this was not the case. 
Run it to see what it does.
"""
import random

participants = ['Jack','Jill','Larry','Tom']

def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
    if my_participant_dict['Larry'] == 9:
        return True
    else:
        return False
    
print(Guess(participants))

# OUTPUT IS SOMETIMES TRUE AND SOMETIMES FALSE, SINCE THE NUMBER ASSIGNMENT TO THE NAME IS DONE RANDOMLY
#%%
"""The code seems to be working fine. 
However, there are some things that could go wrong, so find the part that might throw an exception and 
    wrap it in a try-except block to ensure that you get sensible behavior. 
Do this in the cell below. 
Code your function to return None if an exception occurs.
"""
# Revised Guess() function
import random
def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
    try:
        if my_participant_dict['Larry'] == 9:
            return True
    except:
        return None
        
print(Guess(participants))
 
# OUTPUT IS SOMETIMES TRUE AND SOMETIMES NONE
# when the try block raises an error, the the except block will be executed and I get None
# when the try block does not raise an error, the except block will not be executed   and i get True         
                
"""
Call your revised Guess() function with the following participant list.
"""
participants = ['Cathy','Fred','Jack','Tom']
print(Guess(participants))

#%%
# Revised Guess() function
participants = ['Cathy','Fred','Jack','Tom']
import random
def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
    try:
        
        if my_participant_dict['Larry'] == 9:
            return True
    except:
        return None
        
print(Guess(participants))

# OUTPUT IS ALWAYS NONE (larry is not in the list)

"""
Was the above output None? 
If not, go back to the code block containing your revised Guess() function and make edits so that the output is None for the previous code block. 
If the above output was indeed None, congratulations! 
You've mastered the basics of handling errors and exceptions in Python and you are all done with this notebook!
"""

#%%
"""
Using Python to interact with the operating system, by Google
WEEK 5 -Testing in Python
5 Module Review - Implementing Unit Testing
PART ONE (LINUX COMMAND LINE)
Introduction
Imagine one of your IT coworkers just retired and left a folder of scripts for you to use. 
One of the scripts, called emails.py, matches users to an email address and lets us easily look them up! 
For the most part, the script works great — you enter in an employee's name and their email is printed to the screen. 
But, for some employees, the output doesn't look quite right. 
Your job is to add a test to reproduce the bug, make the necessary corrections, and verify that 
    all the tests pass to make sure the script works! Best of luck!
What you'll do
Write a simple test to check for basic functionality
Write a test to check for edge cases
Correct code with a try/except statement
"""
#%%
"""
PRE-REQUISITES
First, you need to find the .csv file called user_emails.csv, 
    which contains user names and their respective email addresses within the data directory. 
Navigate to this directory using the following command:
"""
cd ~/data
"""
List the files using the following command:
"""
ls

"""
You should now see a file named user_emails.csv. 
To view the contents of the user_emails.csv file, enter the following command:
"""
cat user_emails.csv

"""
Your IT coworker has also left a script named emails.py within the scripts directory.
Use the following command to navigate to the scripts directory:
"""
cd ~/scripts

"""
Now list the contents within the scripts directory using the following command:
"""
ls

"""
Here, you will find the script named emails.py. 
This script aims to match users to their respective email addresses.
You can view the file using the following command:
"""
cat emails.py

"""
This script consists of two functions: 
    populate_dictionary(filename) and find_email(argv). 
The function populate_dictionary(filename) reads the user_emails.csv file and populates a dictionary with
     name/value pairs. 
The other function, find_emails(argv), searches the dictionary created in the previous function
     for the user name passed to the function as a parameter. 
     It then returns the associated email address. 
     
This script accepts employee's first name and last name as command-line arguments and outputs their email address.
The script accepts arguments through the command line. 
These arguments are stored in a list named sys.argv. 
The first element of this list, i.e. argv[0], is always the name of the file being executed. 
So the parameters, i.e., first name and last name, are then stored in argv[1] and argv[2] respectively.
"""
"""
emails.py
"""
#!/usr/bin/env python3

import sys
import csv

def populate_dictionary(filename):
  """Populate a dictionary with name/email pairs for easy lookup."""
  email_dict = {}
  with open(filename) as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    for row in lines:
      name = str(row[0].lower())
      email_dict[name] = row[1]
  return email_dict

def find_email(argv):
  """ Return an email address based on the username given."""
  # Create the username based on the command line input.
  fullname = str(argv[1] + " " + argv[2])
  # Preprocess the data
  email_dict = populate_dictionary('/home/student-02-16fc612dee9b/data/user_emails.csv')
  # Find and print the email
  return email_dict.get(fullname.lower())

def main():
  print(find_email(sys.argv))

if __name__ == "__main__":
  main()




"""
Let's test the script now.
Since you know the contents of the user_emails.csv file, 
    choose any name to be passed as a parameter, or you can use the following name:
"""
python3 emails.py Blossom Gill

"""
This will give you the email address associated with the Full Name passed as parameters. 
In this case, the name is Blossom Gill and the email ID associated with this name is blossom@abc.edu.
print screen
student-00-c24eec123753@linux-instance:~/scripts$ python3 emails.py Blossom Gill
"""
"""
INTRODUCTION TO TEST CASES
Writing a test encourages you to think through the script's design and goals before writing the code. 
This keeps you focused and lets you create better designs. 
If you learn how to easily test your scripts, you'll be able to create code that's better defined and cohesive.
In this lab, we will write tests and correct bugs within the existing script.
In this section, we will write a basic test case and see how it works. 
A test case is an individual unit of testing that checks for a specific response to a particular set of inputs.
Use the following command to create a new file (in scripts directory) to write our test cases:
"""
nano ~/scripts/emails_test.py 

"""
The file should now open in edit mode. 
This script's primary objective is to write test cases that correct bugs in the existing emails.py script.
We will use the unittest package for this.
Add the following shebang line and import the necessary packages:
"""
#!/usr/bin/env python3
import unittest

"""
The package unittest supports 
    test automation, 
    sharing of setup and shutdown code for tests, 
    aggregation of tests into collections, and 
    independence of the tests from the reporting framework. 
This module also provides classes that make it simple to support these qualities for a set of tests.
The following import statement allows a Python file to access the script from another Python file. 
In this case, we will import the function find_email, which is defined in the script emails.py.
"""
from emails import find_email

"""
Now let's create a class:
"""
class EmailsTest(unittest.TestCase):

"""
Classes are a way to bundle data and functionality together. 
Creating a new class creates a new type of object, which further allows new instances of that type to be made.
Another important aspect of the unittest module is the test runner. 
A test runner is a component that orchestrates the execution of tests and provides the outcome to the user.
A test case is created by subclassing unittest.TestCase. 
Let's write our first basic test case, test_basic.
"""
def test_basic(self):
    testcase = [None, "Bree", "Campbell"]
    expected = "breee@abc.edu"
    self.assertEqual(find_email(testcase), expected)
if __name__ == '__main__':
  unittest.main()

"""
Here, variable test case contains the parameters to be passed to the script emails.py. 
As we mentioned, the script file is the first element of input parameters through command line using argv. 
Since we already imported the function find_email from emails.py earlier, 
    we will pass None in place of the script file and call it later in the script. 
Adding to None, we will pass a first name and last name as parameters.
The variable stores the expected value to be returned by emails.py. 
The method assertEqual passes the test case to the function find_email, 
    which we imported earlier from emails.py, and checks whether it generates the expected output.
Save the file by clicking Ctrl-o, Enter key, and Ctrl-x.
We will run this file through the command line here. 
To do this, we will give the file permissions for execution.
"""
chmod +x emails_test.py

"""
Now, let's run our first test case using the following command:
"""
./emails_test.py

"""
The output shows the number of tests run and its associated output.
ran 1 test in 0.01s
OK
The test case passed. 
This was a basic test case to show how test cases with Python work. 
In the next section, we will write a few more test cases covering other possibilities.
"""

"""
TEST CASE 1" MISSING PARAMETERS
Imagine a scenario where the user doesn't give either their first name or last name.
 What do you think the output would be in this case?
Lets try this out. 
Choose any first or last name of your choice or use the following name to be passed to emails.py as a parameter:
"""
python3 emails.py Kirk

"""
I get and IndexError: list index out of range
This now gives us an error. 
The script doesn't take just one parameter as input and so it produces an error.
Let's now write a test case to handle this type of error. 
This test case should pass just the first name to the script.
"""
nano emails_test.py

"""
Add the test case test_one_name just after the first test case.
Pro tip: Note down the name of the test cases. Knowing the names will be helpful in running individual tests.
"""
def test_one_name(self):
    testcase = [None, "John"]
    expected = "Missing parameters"
    self.assertEqual(find_email(testcase), expected)

"""
The file emails_test.py should now look like this:
"""
#!/usr/bin/env python3

import unittest
from emails import find_email

class TestFile(unittest.TestCase):
  def test_basic(self):
    testcase = [None, "Bree", "Campbell"]
    expected = "breee@abc.edu"
    self.assertEqual(find_email(testcase), expected)

  def test_one_name(self):
    testcase = [None, "John"]
    expected = "Missing parameters"
    self.assertEqual(find_email(testcase), expected)

if __name__ == '__main__':
  unittest.main()

"""
Save the file by clicking Ctrl-o, Enter key, and Ctrl-x.
Now run the second test using the following command:
"""
./emails_test.py

"""
(Another way to run a particular function within the script is 
    to specify the class name and the function name you want to run. 
This helps us run individual tests without having to run all the test cases in the test script again.)
This now returns the following output:
    Ran 2 tests in 0.01 s
    FAILED(Errors=1)
    
The output shows the function that caused the error and the description related to the error. 
It returned IndexError, which is raised while attempting to access an index that's outside the bounds of a list. 
This error occurs because the script emails.py takes in two parameters, the first and last name. 
We need to handle this type of incomplete inputs within the script. 
We need to decide what the correct output should be. 
Let's say, in this case, your script should output "Missing parameter".
Let's now fix the code. 
The last test case showed that the script fails if only one parameter is passed. 
We would now handle these types of incomplete inputs given to the script file emails.py.
There are two ways to solve this issue:
    Use a try/except clause to handle IndexError.
    Check the length of input parameters before traversing the user_emails.csv file for the email address.
    
You can use either of the above methods, but remember that test cases should pass and the script should return
    "Missing parameters" in this case.
We will use the try/except clause here to solve this issue. 
Try/except blocks are used for exceptions and error handling. 
Since exceptions are detected during execution of a script/program, error handling in Python is done 
    using exceptions that are caught in try blocks and handled in except blocks.
Let's dive into how try/except blocks work:
    First, we execute the try clause.
    If no exception occurs, the except clause is ignored.
    If an exception occurs during the execution of the try clause, the rest of the try clause is then skipped.
    It then attempts to match the type with the exception named after the except keyword. 
    If this matches, the except clause is executed. 
    If it doesn't, the control is passed on to outer try statements. 
    If no handler is found, it's an unhandled exception and the execution stops with an error message.
    
A try statement may have more than one except clause to specify handlers for different exceptions. 
In our case, the exception error we need to handle is IndexError.
Let's move forward by adding a try/except clause to the script emails.py.
"""
nano emails.py

"""
We will add the complete code block within the function find_email(argv), which is within the try block, 
    and add an IndexError exception within the except block. 
This means that the execution will start normally with any number of parameters given to the script. 
If the function find_email(argv) receives the required number of parameters, it will return the email address. 
And if the function doesn't receive the required number of parameters, it will throw an IndexError exception 
    and the except clause which handles IndexError exception would then execute.
Add the body of the function find_emails(argv) within the try block and add an except block:
"""
def find_email(argv):
  """ Return an email address based on the username given."""
  # Create the username based on the command line input.
  try:
    fullname = str(argv[1] + " " + argv[2])
    # Preprocess the data
    email_dict = populate_dictionary('/home/<username>/data/user_emails.csv')
    # Find and print the email
    return email_dict.get(fullname.lower())
  except IndexError:
    return "Missing parameters"

"""
The complete file emails.py should now look like this:
"""
#!/usr/bin/env python3

import sys
import csv


def populate_dictionary(filename):
  """Populate a dictionary with name/email pairs for easy lookup."""
  email_dict = {}
  with open(filename) as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    for row in lines:
      name = str(row[0].lower())
      email_dict[name] = row[1]
  return email_dict

def find_email(argv):
  """ Return an email address based on the username given."""
  # Create the username based on the command line input.
  try:
    fullname = str(argv[1] + " " + argv[2])
    # Preprocess the data
    email_dict = populate_dictionary('/home/{{ username }}/data/user_emails.csv')
    # Find and print the email
    return email_dict.get(fullname.lower())
  except IndexError:
    return "Missing parameters"

def main():
  print(find_email(sys.argv))

if __name__ == "__main__":
  main()

"""
Save the file by clicking Ctrl-o, Enter key, and Ctrl-x.
Now run the test cases within the file email_test.py again:
"""
./emails_test.py

"""
You should now see that both the test cases ran successfully and an OK message appeared.
"""

"""
TEST CASE 2: RANDOM EMAIL ADDRESS
Let's find some other edge cases. 
We'll search for an employee that doesn't exist. 
Can you expect the output the script would give? 
The expected output in such a case should be "No email address found". 
Let's see how the script reacts to this case 
    by adding a test case in the file emails_test.py just after the second test case.
Open the file emails_test.py.
"""
nano emails_test.py

"""
Add the following test case after the previous test case:
"""
def test_two_name(self):
    testcase = [None, "Roy","Cooper"]
    expected = "No email address found"
    self.assertEqual(find_email(testcase), expected)

"""
The file should now look like this:
"""
#!/usr/bin/env python3

import unittest
from emails import find_email


class EmailsTest(unittest.TestCase):
  def test_basic(self):
    testcase = [None, "Bree", "Campbell"]
    expected = "breee@abc.edu"
    self.assertEqual(find_email(testcase), expected)

  def test_one_name(self):
    testcase = [None, "John"]
    expected = "Missing parameters"
    self.assertEqual(find_email(testcase), expected)

  def test_two_name(self):
    testcase = [None, "Roy","Cooper"]
    expected = "No email address found"
    self.assertEqual(find_email(testcase), expected)

if __name__ == '__main__':
  unittest.main()

"""
Save the file by clicking Ctrl-o, Enter key, and Ctrl-x.
Run the test script using:
"""
./emails_test.py

"""
The test case failed! 
This means the script doesn't output the message "No email address found" 
    if we search for an employee that doesn't exist.
Let's edit the script emails.py to return a message saying 
    "No email address found" where users searched for don't exist.
Can you guess the statement where the function find_email(argv) actually fetches the email address of the user? 
The method email_dict.get(full): does the job. 
This method fetches the email address from the list if found, and if not, it returns None.
We need to add an if-else loop here,
    which will return the email address only if the method email_dict.get(username) returns a valid email address. 
If it doesn't, it will return the message "No email address found".
To do this, edit the script file using:
"""
nano emails.py

"""
Locate the statement return email_dict.get(fullname.lower()): 
    within the script under the function find_email(argv) and replace it with the following block of code:
"""
if email_dict.get(fullname.lower()):
      return email_dict.get(fullname.lower())
    else:
      return "No email address found"

"""
The file should now look like this:
"""
#!/usr/bin/env python3

import csv
import sys


def populate_dictionary(filename):
  """Populate a dictionary with name/email pairs for easy lookup."""
  email_dict = {}
  with open(filename) as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    for row in lines:
      name = str(row[0].lower())
      email_dict[name] = row[1]
  return email_dict

def find_email(argv):
  """ Return an email address based on the username given."""
  # Create the username based on the command line input.
  try:
    fullname = str(argv[1] + " " + argv[2])
    # Preprocess the data
    email_dict = populate_dictionary('/home/{{ username }}/data/user_emails.csv')
     # If email exists, print it
    if email_dict.get(fullname.lower()):
      return email_dict.get(fullname.lower())
    else:
      return "No email address found"
  except IndexError:
    return "Missing parameters"

def main():
  print(find_email(sys.argv))

if __name__ == "__main__":
  main()
  
"""
Save the file by clicking Ctrl-o, Enter key, and Ctrl-x.
Now, run the test case to check if the script still produces an error.
"""
python3 emails_test.py

"""
Since we've handled the IndexError exception, the test case should now pass.
OUTPUT SHOULD BE
Ran 3 tests in 0.01s
OK
You can also run the script emails.py 
    by passing some random names (that aren't present in user_emails.csv) and check the output.
                                                                   
"""
python3 emails.py Roy Cooper

"""
This should now give the following output:
    No email address found
"""

#%%
"""
PART 2 (SOLUTION ON "SPYDER")
"""
#%%
"""
This is "emails2.py"
I will try to re-write the 2nd function because 
I am not providing employee's first name and last name as command-line arguments here on Spyder.
(I will do that on the virtual LINUX OS command line)
I will save this and test it with another script called emails2_test.py
"""
import sys
import csv

def populate_dictionary(filename):
  """Populate a dictionary with name/email pairs for easy lookup."""
  email_dict = {} # define empty dictionary to be populated
  with open(filename) as csvfile: # open the csv file 
    lines = csv.reader(csvfile, delimiter = ',') # create the object lines
    for row in lines: # for each row in the csv
      name = str(row[0].lower())
      email_dict[name] = row[1] # email_dict[name] is the Key and row[1] is the Value
  return email_dict # the dictionary is created and will be used in the following function

# print(populate_dictionary("user_emails.csv")) i can use this line of code to see/display/print the dictionary produced by this function

def find_email(fullname):
    
  
  """ Return an email address based on the username given."""
  try: # add this later
      email_dict = populate_dictionary("user_emails.csv")      
        # Find and print the email
      #return email_dict.get(fullname.lower()) # lower() transforms all letters to lowercase. REPLACE THIS FOR THE 3RD TEST
      if email_dict.get(fullname.lower()): # REPLACEMENT LINE 1 OF 4
          return email_dict.get(fullname.lower())
      else:
          return "No email address found" # REPLACEMENT LINE 4 OF 4
          
  except: # add this later
      return "Missing parameters" # add this later
  
# 1st test: "test_basic"    
#print(find_email("Blossom Gill")) 
#I can use this line of code to see/display/print the e-mail of Blossom Gill
# so I provide the argument "Blossom Gill" and I get the output "blossom@abc.edu"
  
# 2nd test: "test_one_name"
#print(find_email("Kirk")) # when trying "Kirk" as an argument the OUTPUT IS None, 2nd test: "test_one_name"

# 3rd test: "test_two_name"

#%%
"""
This is "emails2_test.py"
I will use this to test the emails2.py
Ofcourse I have created the file user_emails.csv (I copied it from the command line of the virtual machine of linux os)
I have 3 files on my c drive (where Python is located too)
1- user_emails.csv, 
2- emails2.py( I copied that too from linux os VM cmd) and 
3- emails2_test.py
"""
from emails2 import find_email # from the emails2.py file import the function "find_email"
import unittest

class EmailsTest(unittest.TestCase): # Now let's create a class:
     def test_basic(self): #     I will name this test as "test_basic"
         testcase = "Bree Campbell"
         expected = "breee@abc.edu"
         self.assertEqual(find_email(testcase), expected)
         
     def test_one_name(self):
         testcase = None, "John"
         expected = "Missing parameters"
         self.assertEqual(find_email(testcase), expected)
         
     def test_two_name(self):
         testcase = "Roy Cooper"
         expected = "No email address found"
         self.assertEqual(find_email(testcase), expected)
         
    
unittest.main()

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





















