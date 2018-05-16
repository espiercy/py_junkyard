import random

#basic rolling. Takes amount, sides, and per die modifier...other special cases???
def roll(amount, sides, mod = 0):
    value = 0
    for i in range(amount):
        add_val = random.randint(1, sides) - mod
        if add_val <= 0:
            add_val = 1
        print('roll:', i + 1, 'value:', add_val)
        value += add_val
    return value
