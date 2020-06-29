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
