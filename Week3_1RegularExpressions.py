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
