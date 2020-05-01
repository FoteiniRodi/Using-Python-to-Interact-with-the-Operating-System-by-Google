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

Absolute Path
An absolute path is a full path to the resource in the file system.
We call it absolute path because it doesn't matter where in the file system our script is running, the absolute path will always lead us to the resource. 

Relative Path
Relative paths use only a portion of a path to show where the resource is located in relation to the current working directory. 
Relative paths are a shortcut that you can use so you don't have to write out the full file path. 
But keep in mind, they only make sense relative to the current location.

1.2     Reading files 

First approach: "open/use/close"
                Open a file 
                Read the file (with the readline method or the read method)
                Close the file
   
create the txt file "spider" containing the kid's poem (place it in the directory where Python is)
then write  -file = open(absolute path* to the txt file) EXPLANATION:create a new file object and assign it to a Variable called 'file'
then write  -print(file.readline())       
the readline() method** lets us read a single line in the file
then write  -print(file.readline()) 
executing this again, gives us the second line of the file contents
then write  -print(file.read())
The read() method*** lets us read all the lines in the file
then write  -file.close()

Notes
* 
I can use the absolute path which is the full name of the path. 
 I can use also the relative path but after placing the txt file in C:\Users\jimko which is the directory where Python is placed.

** 
The Readline () method lets us read a single line in the file.
Each time we call the readline method, the file object updates the current position in the file. So it keeps moving forward. 

***
Read() method
    reads from the current position until the end of the file
    Just like readline, the read method starts reading from wherever we currently are in the file

Advantages and disadvantages of the approach "open/read/close"
+ we can use a file object in other places in our code
- we have to remember to close the file each time


Second approach:    "with" block
                    open the file
                    read the file
                    (file closes automatically)
write   -with open(absolute path of the file) as file:
write   -print(file.readline())
the readline() method reads one line of the text

Advantages and disadvantages of the approach "with" block         
+ we don't have to remember to close the file
- we cannot use a file object in other places in our code, only within the "with" block
"""
#%%
# for the cmd on linux VM write : python 3
file = open("spider.txt") # opens the file
print(file.readline()) # reads only the first line
print(file.readline()) # read only the second line
#%%
print(file.read()) # reads all the lines 
file.close()  # closes the file
#%%
with open("spider.txt") as file:
    print(file.readline())
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
with open ("spider.txt") as file:
    for line in file:
        print(line.upper())
#%%
"""
How to avoid empty lines
     use the strip method before the upper method
     we are iterating line by line, and the strip() command is used to remove extra whitespace.
"""
#%%
with open ("spider.txt") as file:
    for line in file:
        print(line.strip().upper()) # remove newline characters, convert to uppercase
#%%
"""
read the file lines into a list
(create a list, whose elements are the lines of our text file)
"""
#%%
with open ("spider.txt") as file:
    for line in file:
        print(line.strip().upper()) # remove newline characters, convert to uppercase
file  = open("spider.txt")
lines = file.readlines()
file.close()
lines.sort() # lines are sorted alphabetically
print(lines) # we see the newline character : \n


#%%
"""
1.4     Writing files

How to write content into a file
(3 ways, append "a", write "w", create "x")


we use the with block (which closes the file automatically)
we use two arguments and the w is for writing contents into the file
the write method writes contents to the file

Please remember
    file objects can be opened in several different modes
    a mode is similar to a file permission and it governs what we can do with the file we just opened
    1   "r" mode, read-only
        by default, the open function uses the "r" mode, which means read-only (we can only READ the file, nothing else)
        we can skip writing "r" since it is use dby default
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
with open("kitty.txt", "a") as file:
    file.write("The kitty is white.") # the write method writes contents to the file
# the file kitty did not exist but I created it with append-a
#%%
with open("kitty.txt", "a") as file:
    file.write("The kitty is also fluffy.") 
# now the file kitty exists, I appended another phrase at the same line
#%%
with open("doggy.txt", "w") as file:
    file.write("The doggy is golden.")
# the file doggy did not exist but I created it with write-w
#%%
with open("doggy.txt", "w") as file:
    file.write("The doggy is chocolate brown.")
# now the file doggy exists, BUT I deleted its content with the new phrase (the new phrase overwrites the old one!)
#%%
with open("piggy.txt", "x") as file:
    file.write("The piggy is pink.")
# the file piggy did not exist but I created it with "x"
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
guests = open("guests.txt", "w") # this is the file object we create (guests)
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"] #list with first names as its elements

for i in initial_guests: # this is iteration (5 elements so 5 iterations). It is a for loop which goes over every element in the list
    guests.write(i + "\n") # with the write method applied on the file object guests, we add a new line for each element of the list
    
guests.close()
#%%
"""
2 - See the contents of the text file "guests".
To see the contents of the newly created guests.txt file,run the following code.
We use the "with" block approach, that closes the file automatically.
"""
#%%
with open("guests.txt") as guests: 
    for line in guests: # iteration on a text file. It is a for loop which goes over each element=line of the text file
        print(line)     # this prints each line of the txt file (the text file already has a new line character at the end of each line and Python reads that too )
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
new_guests = ["Sam", "Danielle", "Jacob"] # this is a new list

with open("guests.txt", "a") as guests: # now we use the append "a" mode
    for i in new_guests: # iterate over the new list. Add each element=list of the list "new_guests", to the existing text file "guests"
        guests.write(i + "\n") # again insert a new line for every element of the above list
guests.close()
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
checked_out=["Andrea", "Manuel", "Khalid"] # list of people who checked out, we shoud remove these from the text file
temp_list=[] # empty list which we will fill with people that remain

with open("guests.txt") as guests: #open text file guests
    for g in guests: # iterate over the contents of the text file guests (elements of the text file are its lines)
        temp_list.append(g.strip()) # we fill the empty list "temp-list"
                                    # this list will contain each line of the text file guests as an element
                                    # strip removes the inline character ( we do not want space as an element of the new list!)
print(temp_list) # I added this to see the contents of the list. Contains ALL lines of the text files as elements of the list
#%%
with open("guests.txt", "w") as guests:
    for name in temp_list: # iterate over the elements of the temp list (element=first name)
        if name not in checked_out: # if the element of the list "temp_list" IS NOT present in the list "checked_out" then go ahead and write it in the text file  
            guests.write(name + "\n")
            
#%%
"""
6 - See the contents of the updated text file "guests".

To check whether your code correctly removed the checked out guests 
from the guests.txt file, run the following cell.
"""
with open("guests.txt") as guests:
    for line in guests:
        print(line)
#The current names in the guests.txt file should be: 
# Bob, Polly, Sam, Danielle and Jacob.
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
guests_to_check = ['Bob', 'Andrea']
checked_in = [] # create a new list

with open("guests.txt") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for x in guests_to_check:
        if x in checked_in:
            print("{} is checked in".format(x))
        else:
            print("{} is not checked in".format(x))

# We can see that Bob is checked in while Andrea is not.
