#Coin flip
#Second challenge, third chapter
#Evan Piercy
#3.18.15
#Flips a coin 100 times, returns results

import random
print("Flipping a coin 100 times!")
count = 0
heads = 0
tails = 0

while count < 100:
    drop = random.randint(1,2)
    if drop == 1:
        heads += 1
    else:
        tails += 1
    count += 1

print("We got " , heads , " heads and " , tails , "tails.")
input("Press the enter key to exit.")
