#!forget shebang, idc
# renames filenames with American date format to Euro

import shutil, os, re

#create regex for American Date Format:
#wow. Regex in python is an effing NIGHTMARE!!!
datePattern = re.compile(r"""^(.*?) #all text before the date
    ((0|1)?\d)-     # one or two digits for the month
    ((0|1|2|3)?\d)- # one or two digits for the day...what?!?!
    ((19|20)\d\d)   #four digits for the year
    (.*?)$
    #that last one, all text after date. IDLE is fucking with me...
    """, re.VERBOSE)
#in all fairness, the book does a good job explaining the above regex
#but, in all hilarity, it makes note of invalid dates that this regex would
#accept, such as 4-31...the hilarious part is that the book acknolwedges that it
#is doing this for the sake of simplicity. pfffft

#Loop over the files in the working directory
for amerFilename in os.listdir('.'): #'.' = 'Where we are right now'
    mo = datePattern.search(amerFilename)
    #Skip files without a date
    if mo == None:
        continue
    #Get the different parts of the filename
    #notice how hard it is to count groups manually!
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    #Form the European-style filename
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    #Get the full, absolute file paths
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    #Rename the files
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    #shutil.move(amerfilename, euroFilename) #uncomment after testing
