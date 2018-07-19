#Random word printer
#Prints randomly from a list of words
#Evan Piercy
#4.5.15
import random
words = ["type", "vector", "k-means", "random", "bayes", "set",
         "data", "conversion", "sklearn"]

while words:
    word_to_print = random.choice(words)
    #for this program, the remove method associated with lists
    #is utilized instead of the books rather clumsy preference
    #towards returning slices.
    words.remove(word_to_print)
    print(word_to_print, " ")

input("\nAll done. Press enter key to exit.")
