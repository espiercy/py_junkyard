#Word Counter
#
#The computer picks a random word and then "counts" it
#The player has to guess the original word
#Fourth challenge, fourth chapter
#Evan Piercy
#3.21.15

import random

# create a sequence of words to choose from
WORDS = ("python" , "jumble" , "easy" , "difficult" , "answer" , "xylophone")
#pick one word randomly from the sequence
word = random.choice(WORDS)
    
#create a variable to use later to see f the guess is correct
correct = word

#count chars in word

count = len(word)

#start game
print("""

    Welcome to Word Count!

Guess the word!
(Press the enter key at the prompt to quit.)
""")

print("There are " , count , " characters in this word.")

guess = input("Your guess: ")

while guess != correct and guess != "":
    print("Sorry, that's not it.")
    guess = input("Your guess: ")

if guess == correct:
    print("That's it! You guessed it!\n")


print("Thanks for playing.")
input("\n\nPress the enter key to exit.")
