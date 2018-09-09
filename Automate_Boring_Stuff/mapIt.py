#! python3
#mapIt.py - Launches a map in the browser using an address from the command line or clipboard

import webbrowser as wb, pyperclip as pc, sys

if len(sys.argv) > 1:
    #Get address from command line
    address = ' '.join(sys.argv[1:])
else:
    address = pc.paste()

wb.open('https://www.google.com/maps/place/' + address)
