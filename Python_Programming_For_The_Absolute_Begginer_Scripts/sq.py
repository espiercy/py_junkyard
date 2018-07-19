import math
def pythag(a , b):
    a2b2 = (a*a) + (b*b)
    guess = 1.0
    while(math.fabs((guess * guess) - a2b2) > 0.01):
        guess = (((a2b2 / guess) + guess) / 2)
    return guess
