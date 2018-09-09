#finding the bugs in the program and fixing them

import random

coin_faces = ['heads', 'tails']

guess = ''
while guess not in coin_faces:
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()


toss = random.randint(0, 1) # 0 is tails, 1 is heads
if (toss == 0 and guess == 'tails') or (toss == 1 and guess == 'heads'):
     print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    while guess not in coin_faces:
        print('That\'s not an option!')
        guess = input()
        
    if (toss == 0 and guess == 'tails') or (toss == 1 and guess == 'heads'):
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
