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
