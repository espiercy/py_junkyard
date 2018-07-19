#Guess My Number
#
#Computer picks a random number between 1 and 100
#The player tries to guess it and the computer lets
#The player know if the guess is too high, too low
#Or right on the money
#Added step value function
#Book is nonspecific about how to utilize the step value
#I suppose it originally intended the user to be told how
#Far away the initial guess was, or perhaps to use the step function
#As a timer, but it is a waste of time to do so.
#Evan Piercy
#6.1.15

import random

def ask_number(question, low, high, step = 1):

    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

print("Welcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.")

#set the initial values

the_number = random.randint(1,100)
turns = 0;
guess = 0;

#guessing loop
while guess != the_number:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")
    turns +=1;
    guess = ask_number("Guess a number: ", 1, 100)

print("You guessed it! The number was " , the_number)
print("And it only took you " , turns , " tries!\n")
input("\n\nPress the enter key to exit.")
