#!C:\Python34\python.exe
#epiercy
#logToText
#demonstrates writing logs to text files

import logging

logging.basicConfig(filename='myProgramLog.log', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Writing to myProgramLog')
