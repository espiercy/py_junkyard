#Fortune Cookie
#First Challenge, Third Chapter
#Program tells one of five fortunes
#Evan Piercy
#3.18.15

#need random
import random

input("I shall guess your fortune. Press enter to break cookie")

fortune = random.randint(1,5)

if fortune == 1:
    print("You're going to die soon!")
elif fortune == 2:
    print("You're going to get an inheritance!")
elif fortune == 3:
    print("You're going to fall in love!")
elif fortune == 4:
    print("You're going to go on an adventure!")
elif fortune == 5:
    print("That wasn't chicken!")
