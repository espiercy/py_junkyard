#don't need shegang in this instance
#Regex Search -- opens all .txt files in directory, searches
#for any line matching a user-supplied regex...
#meh, good enough

respecchar = ['?', '*', '+', '{', '}', '.', '\\', '^', '$', '[', ']']

_regex = input("Enter a regular expression: ")

if _regex == '' or _regex == ' ':
        _regex = r'\s'
elif _regex in respecchar:
    _regex = r'\'+_regex'

import re
search_regex = re.compile(_regex)

#obviously I need this guy...
import os

#Whatever filepath I run this script from, get that directory
this_directory = os.path.abspath('.')
print(this_directory)

suffix = '.txt' #the guarantor of a text file

#first, let's just open and read every line from all .txt files
#not just in this_directory. Need to call listdir
for filename in os.listdir(this_directory):
    if filename.endswith(suffix):
        #we now have access to every text file in the directory
        #so we check for a regex, though I'm just going to test with contains
        #because I don't have the patience to properly test the regex
        for line in open(filename):
            mo = search_regex.search(line)
            if mo:
                print(line)



