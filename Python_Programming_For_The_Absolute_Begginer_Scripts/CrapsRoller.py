#Craps Roller
#Demonstrates random number generation
#As in most cases, very similar to java, only faster
#Evan Piercy
#3.16.15

import random

# generate random numbers 1-6
dieOne = random.randint(1, 6)
dieTwo = random.randrange(6) + 1
# dislike putting numbers in my variable names for some reason

total = dieOne + dieTwo

print("You rolled a " , dieOne , " and a " , dieTwo , " for a total of: " , 
      total , "!")

#One weakness of this book, at least the eNook version (bleaugh, I know, right?)
#Is that it does a very, very poor job of editing those printed strings.
