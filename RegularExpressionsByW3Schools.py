#%%
"""
W3 schools
Python RegEx
Python Regular Expressions

A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.

RegEx Module
Python has a built-in package called re, which can be used to work with Regular Expressions.

Import the re module (import re)
When you have imported the re module, you can start using regular expressions

There are 4 RegEx Functions
The re module offers a set of functions that allows us to search a string for a match:


1 search	    Returns a Match object if there is a match anywhere in the string
search() returns 1 result, 1 match, 1 occurrence
2 findall	    Returns a list containing all matches (list whose elements are ALL occurences of the string we searched for)
findall() returns all results as elements in a list, all matches, all occurrences
3 split	        Returns a list where the string has been split at each match
4 sub	        Replaces one or many matches with a string

Character class[]
-inside Character Class we can place characters, range of characters, numbers, range of numbers
-inside Character Class, special characters are treated like characters
-(also after the raw string, r prefix before the pattern,  special characters are treated like characters
     it is good practice to always use r before the pattern
     with r, Python interpreter shouldn't try to interpret any special characters
examples for Character Class[]
        "[a-m]          with findall(), find all lowercase characters between a and m (range is: abcdefghijklm)
        "[arn]"         with findall(), find the characters a, r, n
        "[^arn]"        with findall(), find all characters EXCEPT the characters a, r, n
        "[0123]"        with findall(), find the numbers 0,1,2,3
        "[0-9]"         with findall(), find the numbers 0123456789
        "[0-9][0-9]"    with findall(), find any two-digit numbers
        "[a-zA-Z]"      with findall(), find all lowercase characters in the range a-z and all uppercase characters in the range A-Z
        "[+]"           with findall(), find any character +
     
     
Special Sequences (they start with \ back-slash)  
A special sequence is a \ followed by one of the characters in the list below, and has a special meaning

Attention! "^x"     find x only when it is at the beginning of a word, BEGINNING
            "[^x]"  find all characters except for x, EXLUSION

    Pattern     Use
    \Aword      find if the text starts with this word
    word\B      find if the text ends with this word
    
    \bain       find if a word in the text starts with "ain"
    ain\b       find if a word in the text ends with "ain"
    
    \Bain       find if "ain" is present in the text
                and EXCLUDE only the words that START with "ain"
    ain\B       find if "ain" is present in the text
                and EXCLUDE only the words that END with "ain"
                
    \d          find all numbers from 0 to 9 in the text
    \D          find all characters in the text EXCEPT numbers from 0 to 9
    
    \s          find all whitespaces in the text
    \S          find all characters in the text EXCEPT whitespaces
    
    \w          find all word-characters (e.g. letters numbers, underscore)
    \W          find all characters EXCEPT word-characters (e.g. find: ! ?)
    
    
    


"""
#%%
# EXAMPLE 1 - search() function
# The search() function searches the string for a match, and returns a Match object if there is a match.
# The Match Object is the x
# A Match Object is an object containing information about the search and the result.
# If no matches are found, the value None is returned
# Search the string to see if it starts with "The" and ends with "Spain"
# If there is more than one match, only the first occurrence of the match will be returned:
import re
text = "The rain in Spain"
x = re.search("^The.*Spain$", text) # starts with "The", ends with "Spain"?
if x:                               # the words are present in the text (if condition is True)
  print("Yes")
else:                               # the words are not present in the text (if condition is False)
  print("No")

# from the module re, I use the search() function to search for certain words in the text
# I get a value after applying that function to my text. I assign that value to the Variable x
# x is an object
#%%
# EXAMPLE 2 - search() function
# Search for the first white-space character in the string(the first blank)
import re
txt = "The rain in Spain"
x = re.search("\s", txt) # search for white-space
print("1st white-space character is in position:", x.start()) # start() finds the position of the 1st white-space


#%%
# EXAMPLE 3 - Match Object and search() function
# What is a Match Object?
# A Match Object is an object containing information about the search and the result.

# print the object directly
# If no matches are found, the value None is returned

import re
txt = "The rain in Spain"
x = re.search("Portugal", txt) # search for the word "Portugal" in the text
print(x) # we print directly the match object. There is no match though so we get None
#%%
# EXAMPLE 4 - Match Object and search() function
# What is a Match Object?
# A Match Object is an object containing information about the search and the result.

# print the object directly
# if matches are found, we get the position of 1st occurence of match and also the whole object

import re
txt = "The rain in Spain"
x = re.search("ai", txt) # search for "ai" in my text
print(x) # we print directly the match object. There is a match so we get the whole object

# I get <re.Match object; span=(5, 7), match='ai'>
# so my first ai object is located in position 5,7? (7 not included)


#.span() returns a tuple containing the start-, and end positions of the match.
#.string returns the string passed into the function
#.group() returns the part of the string where there was a match

#%%
# EXAMPLE 5 - Match Object and search() function / apply .span() to the object

#Print the position (start- and end-position) of the first match occurrence.
#The regular expression looks for any words that starts with an upper case "S":
# Search for an upper case "S" character in the beginning of a word, and print its position
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt) # search for an upper case "S" character in the beginning of a word
print(x.span()) # apply .span to the object. Displays start position of S and end position for the word that starts with S

# I get (12, 17). I understand that 12 is the start position. 
# 17 is the end of the word that starts with capital s I guess (and in fact it is 16:))

#%%
# EXAMPLE 6 - Match Object and search() functio /, apply .string to the object
# Print the string passed into the function
# The string property returns the search string
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt) # search for an upper case "S" character in the beginning of a word
print(x.string)
# prints all text:)
#%%
# EXAMPLE 7 - Match Object and search() function / apply .group() to the object
# Print the part of the string where there was a match.
# Search for an upper case "S" character in the beginning of a word, and print the word
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt) # search for an upper case "S" character in the beginning of a word
print(x.group())
# prints only the word that starts with S
#%%
# EXAMPLE 8 - findall() function 
# Return a list containing every occurrence of "ai"
# The list contains elements, which are all occurrences of the text we searched for
# The RegEx function findall(), returns a list containing all matches
# The list contains the matches in the order they are found.
#f no matches are found, an empty list is returned
import re
txt = "The rain in Spain"
x = re.findall("ai", txt) # we search for the sub-string ai in the text
print(x)

# output is a list with 2 strings, ['ai', 'ai']
#%%
# EXAMPLE 9 - findall() function 
# If no matches are found, an empty list is returned
import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

#%%
# EXAMPLE 10 - split() function
# The split() function returns a list where the string has been split at each match
# split() function creates a list whose elements are words of the text separated by a blank

# Split at each white-space character:
import re
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#%%
# EXAMPLE 11 - split() with maxsplit(how many splits)
# I can choose how many list elements the split() function will produce by using the maxsplit parameter
# So, split my text into 2 strings (do 1 split). 
#Also, do the split at the 1st occurence of the white-space
import re
txt = "The rain in Spain"
x = re.split("\s", txt, 1) # split at 1st white-space, split text, split once
print(x)

#%%
# EXAMPLE 12 - sub() function
# The sub() function replaces the matches with the text of your choice
# Replace every white-space character with the number 9
# syntax is: x = re.sub(pattern, text of our choice, text)

import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt) # substitute all white-space with 9
print(x)

#%%
# EXAMPLE 13 - sub() with count (how many substitutions)
# We can control the number of replacements by specifying the count parameter
# Replace the first two occurrences of a white-space character with the digit 9

import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2) # substitute white-space with 9, only for the first two occurences of white-space
print(x)

#%%
# EXAMPLE 14
"""
range [a-m], with findall(), find all lowercase characters between a and m (range is: abcdefghijklm)
"""
import re
x = re.findall(r"[a-m]", "The rain in Spain")
print(x)
# ['h', 'e', 'a', 'i', 'i', 'a', 'i']

#%%
# EXAMPLE 15
"""
 [arn], with findall(), find the characters a, r, n
"""
import re
x = re.findall(r"[arn]", "The rain in Spain")
print(x)
# ['r', 'a', 'n', 'n', 'a', 'n']

#%%
# EXAMPLE 16
"""
"[0123]"        with findall(), find the numbers 0,1,2,3
"""
import re
x = re.findall(r"[0123]", "The0 rain1 in2 Spain34")
print(x)
# ['0', '1', '2', '3']
#%%
# EXAMPLE 17
"""
"[0-9]"         with findall(), find the ALL numbers 0123456789
"""
import re
x = re.findall(r"[0-9]", "The0 rain1 in2 Spain34")
print(x)
# ['0', '1', '2', '3', '4']
#%%
# EXAMPLE 18
"""
"[0-9][0-9]"    with findall(), find any two-digit numbers
"""
import re
x = re.findall(r"[0-9][0-9]", "The0 rain1 in2 Spain34")
print(x)
# ['34']
#%%
# EXAMPLE 19
"""
 "[a-zA-Z]"      with findall(), find all lowercase characters in the range a-z and all uppercase characters in the range A-Z
"""
import re
x = re.findall(r"[a-zA-Z]", "The0 rain1 in2 Spain34")
print(x)
# ['T', 'h', 'e', 'r', 'a', 'i', 'n', 'i', 'n', 'S', 'p', 'a', 'i', 'n']
#%%
# EXAMPLE 20
"""
"[+]"           with findall(), find any character +

"""
import re
x = re.findall(r"[+]", "The0+rain1+in2+Spain34")
print(x)
# ['+', '+', '+']

#%%
"""
SPECIAL SEQUENCES
"""
# 
#Check if the string starts with "The":
# Returns a match if the specified characters are at the beginning of the STRING
# find if the string starts with The
import re
x = re.findall(r"\AThe", "The rain in Spain")
print(x)
# ['The']
import re
x = re.search(r"\AThe", "The rain in Spain")
print(x)
# <re.Match object; span=(0, 3), match='The'>

#%%
# Returns a match if the specified characters are at the end of the string
# #Check if the string ends with "Spain":

import re
x = re.findall(r"Spain\Z", "The rain in Spain")
print(x)
# ['Spain']
import re
x = re.search(r"Spain\Z", "The rain in Spain")
print(x)
# <re.Match object; span=(12, 17), match='Spain'>

#%%
# Returns a match where the specified characters are at the beginning of a word
# Check if "ain" is present at the beginning of a WORD

# find if a word (inside the string) starts with ain
import re
x = re.findall(r"\bain", "The rain in Spain")
print(x)
# []
import re
x = re.search(r"\bain", "The rain in Spain")
print(x)
# None
#%%
# Returns a match where the specified characters are at the end of a word
#Check if "ain" is present at the end of a WORD:

# find if a word (inside the string) ends with ain
import re
x = re.findall(r"ain\b", "The rain in Spain")
print(x)
# ['ain', 'ain']
import re
x = re.search(r"ain\b", "The rain in Spain")
print(x)
# <re.Match object; span=(5, 8), match='ain'>
#%%%
# Returns a match where the specified characters are present, 
    #but NOT at the beginning of a word
#Check if "ain" is present, but NOT at the beginning of a word:

# find if ain is present and exclude results when ain is in the beginning of the word
import re
x = re.findall(r"\Bain", "ain The rain in Spain")
print(x)
# ['ain', 'ain']
import re
x = re.search(r"\Bain", "ain The rain in Spain")
print(x)
# <re.Match object; span=(5, 8), match='ain'>

#%%%
# Returns a match where the specified characters are present, but NOT at the end of a word
#Check if "ain" is present, but NOT at the end of a word:

# find if ain is present and exclude results when ain is in the end of the word
import re
x = re.findall(r"ain\B", "The rain in Spain")
print(x)
# []
import re
x = re.search(r"ain\B", "The rain in Spain")
print(x)
# None


#%%%
# Returns a match where the string contains digits (numbers from 0-9)
#Check if the string contains any digits (numbers from 0-9):

# find any numbers present in the string
import re
x = re.findall(r"\d", "1The rain in Spain")
print(x)
# ['1']
import re
x = re.search(r"\d", "1The rain in Spain")
print(x)
# <re.Match object; span=(0, 1), match='1'>

#%%
# Returns a match where the string DOES NOT contain digits
#Return a match at every no-digit character:

# find all characters EXCEPT numbers in the string (e.g. letters, whitespaces)
import re
x = re.findall(r"\D", "1The rain in Spain")
print(x)
# ['T', 'h', 'e', ' ', 'r', 'a', 'i', 'n', ' ', 'i', 'n', ' ', 'S', 'p', 'a', 'i', 'n']
import re
x = re.search(r"\D", "1The rain in Spain")
print(x)
# <re.Match object; span=(0, 1), match='T'>

#%%
# Returns a match where the string contains a white space character
#Return a match at every white-space character:
# \s: returns all whitespaces

# find all whitespaces in the string
import re
x = re.findall(r"\s", "The rain in Spain")
print(x)
# [' ', ' ', ' ']

import re
x = re.search(r"\s", "The rain in Spain")
print(x)
# <re.Match object; span=(3, 4), match=' '>

#%%
# Returns a match where the string DOES NOT contain a white space character
#Return a match at every NON white-space character:
# \S: returns all characters except whitespace

# # find all characters EXCEPT whitespaces
import re
x = re.findall(r"\S", "The rain in Spain!")
print(x)
# ['T', 'h', 'e', 'r', 'a', 'i', 'n', 'i', 'n', 'S', 'p', 'a', 'i', 'n', '!']
import re
x = re.search(r"\S", "The rain in Spain!")
print(x)
# <re.Match object; span=(0, 1), match='T'>

#%%
# Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
# Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)

# find all word characters(letters, numbers, underscore_)
import re
x = re.findall(r"\w", "The_rain_ in _Spain10")
print(x)
# ['T', 'h', 'e', '_', 'r', 'a', 'i', 'n', '_', 'i', 'n', '_', 'S', 'p', 'a', 'i', 'n', '1', '0']
# Attention! It finds 10 but as 2 different numbers

import re
x = re.search(r"\w", "The_rain_ in _Spain10")
print(x)
# <re.Match object; span=(0, 1), match='T'>

#%%
# Returns a match where the string DOES NOT contain any word characters
# Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
# \W: returns all characters except for letters

# find all characters EXCEPT word-characters (e.g.find  !, ?, whitespace)
import re
x = re.findall(r"\W", "The_rain_ in _Spain10?")
print(x)
# [' ', ' ', '?']
import re
x = re.search(r"\W", "The_rain_ in _Spain10?")
print(x)
# <re.Match object; span=(3, 4), match=' '>
