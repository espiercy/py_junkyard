#Guess My Number, Modified
#Third challenge, third chapter
#Only allows 7 guesses
#Computer picks a random number between 1 and 100
#The player tries to guess it and the computer lets
#The player know if the guess is too high, too low
#Or right on the money
#Evan Piercy
#3.18.15

import random

print("Welcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible, you only have seven guesses!")

#set the initial values

the_number = random.randint(1,100)
guess = int(input("Take a guess: "))
tries = 1

#guessing loop
while guess != the_number and tries < 7:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")
    guess = int(input("Take a guess: "))
    tries += 1

if guess == the_number:
    print("You guessed it! The number was " , the_number)
    print("And it only took you " , tries , " tries!\n")
else:
    print("You failed! My number was: " , the_number)
input("\n\nPress the enter key to exit.")
