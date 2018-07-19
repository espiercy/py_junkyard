#Pizza Slicer
#Demonstrates string slicing
#Evan Piercy
#3.20.15
#String slicing is a very useful feature provided by python
#Unfortunately, the book has once again fallen into using ASCII art.
#I'm leaving that bit out. Frankly, so should the writer have.

word = "pizza"

print("Enter the beginning and ending index for your slice of 'pizza'.")
print("Press the enter key at 'Start' to exit.")
start = None
while start != "":
    start = (input("\nStart: "))

    if start:
        start = int(start)
        finish = int(input("Finish: "))

        print("word[",start, ":",finish,"] is", end=" ")
        print(word[start:finish])

input("\n\nPress the enter key to exit.")
