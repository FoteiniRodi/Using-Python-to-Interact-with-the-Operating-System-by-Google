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
