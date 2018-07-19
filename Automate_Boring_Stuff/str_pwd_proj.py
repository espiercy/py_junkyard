import re

def strong_pwd_check(pwd):
    if len(pwd) < 8: #check length first
        return False

    digit_regex = re.compile(r'\d+') #check for at least one digit

    if digit_regex.findall(pwd) == []:
        return False

    upper_regex = re.compile(r'[A-Z]') #check for an uppercase letter

    if upper_regex.findall(pwd) == []:
        return False

    lower_regex = re.compile(r'[a-z]') #check for an uppercase letter

    if lower_regex.findall(pwd) == []:
        return False

    return True
