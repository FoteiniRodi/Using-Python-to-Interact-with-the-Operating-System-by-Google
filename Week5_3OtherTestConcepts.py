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
