#!C:\Python34\python.exe
#pw.py project one insecure pwd locker program

import sys
print(sys.version)
import pyperclip

PASSWORDS = {'email':'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog':'VmALvQyKAxiVHG8v01if1MLZ3sdt',
             'luggage':'12345'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first cmd arg is account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
