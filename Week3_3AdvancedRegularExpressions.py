
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

Note: use \b to get FULL WORDS!use \b at the begging and end of the pattern to indicate that I want matches that are words, not parts of words!

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
