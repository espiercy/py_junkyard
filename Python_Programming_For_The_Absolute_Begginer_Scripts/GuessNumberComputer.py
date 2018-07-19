#Guess Number, v. Computer
#Fourth Challenge, third chapter
#Game between player and computer to guess a number
#Evan Piercy
#3.18.15

import random

print("Let's play a guessing game. You think of a number between 1 and 100.")

#need var for computer answer

guess = 50
buff = int(guess /2)
tries = 1
response = ""

#response will depend on specific characters from user
#the logic behind the guess is actually tougher than it seems
while response != "y":
    print("My guess is " , guess)
    response = input("Please enter 'h' for higher, 'l' for lower, and 'y' for yes! ")
    if response == "h":
        tries += 1
        guess = int(guess + buff)
        buff = int(buff/2)
    elif response == "l":
        tries += 1
        guess = int(guess - buff)
        buff = int(buff/2)
    elif response == "y":
        print("I got it in " , tries , " tries. The answer is " , guess , ".")
    else:
        print("That's not a possible guess.")

print("Great! My Turn.")
#just copy/paste from previous
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.")

#set the initial values

the_number = random.randint(1,100)
guess = int(input("Take a guess: "))
tries = 1

#guessing loop
while guess != the_number:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")
    guess = int(input("Take a guess: "))
    tries += 1

print("You guessed it! The number was " , the_number)
print("And it only took you " , tries , " tries!\n")
input("\n\nPress the enter key to exit.")
