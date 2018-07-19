import os

#let's read and print to screen

fr = open('test.txt', 'r')

str1 = fr.read()

fr.close()

#attributes
print(fr.closed)
print(fr.name)
print(fr.mode)

print(str1)

os.rename('test.txt', 't1.txt')
os.remove('t1.txt')