import re

respecchar = ['?', '*', '+', '{', '}', '.', '\\', '^', '$', '[', ']']


def regexstrip(string, _strip):
    if _strip == '' or _strip == ' ':
        _strip = r'\s'
    elif _strip in respecchar:
        _strip = r'\'+_strip'
    print(_strip) #just for troubleshooting 
    re_strip = re.compile('^'+_strip+'*(.+?)'+_strip+'*$')
    print(re_strip) #just for troubleshooting 
    mstring = re_strip.search(string)
    print(mstring) #just for troubleshooting 
    stripped = mstring.group(1)
    print(stripped)
