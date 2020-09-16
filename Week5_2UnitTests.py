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
