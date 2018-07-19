#Word Jumble Hint
#
#The computer picks a random word and then "jumbles" it
#The player has to guess the original word
#Modified to give a hint
#Third challenge, chapter 4
#Evan Piercy
#3.21.15

import random

# create a sequence of words to choose from
WORDS = ("python" , "jumble" , "easy" , "difficult" , "answer" , "xylophone")
HINTS = ("A big snake" , "All mixed up" , "simple" , "not easy" , "response" , "musical percussion instrument")
#pick one word randomly from the sequence
word = random.choice(WORDS)

if word == "python":
    hint = HINTS[0]
elif word == "jumble":
    hint = HINTS[1]
elif word == "easy":
    hint = HINTS[2]
elif word == "difficult":
    hint = HINTS[3]
elif word == "answer":
    hint = HINTS[4]
elif word == "xylophone":
    hint = HINTS[5]
    
#create a variable to use later to see f the guess is correct
correct = word

#creat a jumbled version of the word

jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]

#start game
print("""

    Welcome to Word Jumble!

Unscramble the letters to make a word.
    Press 'h' for a hint!
(Press the enter key at the prompt to quit.)
""")

print("The jumble is: " , jumble)

guess = input("Your guess: ")

while guess != correct and guess != "":
    if guess == 'h':
        print(hint)
    else:
        print("Sorry, that's not it.")
    guess = input("Your guess: ")
    

if guess == correct:
    print("That's it! You guessed it!\n")


print("Thanks for playing.")
input("\n\nPress the enter key to exit.")
