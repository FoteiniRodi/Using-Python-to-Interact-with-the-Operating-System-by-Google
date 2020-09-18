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
