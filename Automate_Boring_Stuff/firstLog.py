#!C:\Python34\python.exe
#epiercy
#making use of python logging for the first time
#I think the book has gone terribly wrong in this example...
#they used (%s%%) instead of merely (%s), which seems to work...
#not the first typo I've come across in this book though

import logging

logging.basicConfig(level=logging.DEBUG, format= ' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' %(n))
    total = 1
    for i in range (1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')
    
