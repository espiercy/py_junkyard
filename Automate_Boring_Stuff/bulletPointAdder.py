#!C:\Python34\python.exe
#bulletPointAdder.py - Adds Wikipedia bullet points to the start
#of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

#TODO: Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)): #loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add start

text = '\n'.join(lines)

pyperclip.copy(text)
