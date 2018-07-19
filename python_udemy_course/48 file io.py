#calls to write will erase previous data without append mod!!!
#file = open('test.txt','w') #<--use this if file doesn't exist

#append as opposed to write
file = open('test.txt','a')

file.write("This text is written to the file via 48 file io.py\n")

file.close()