#Finicky Counter
#Demonstrates the break and continue statements

count = 0
while True:
    count += 1

#end loop if count greater than 10
    if count > 10:
        break

# skip five
    if count == 5:
        continue

    print(count)

input("Press the enter key to exit.")

#This reminded me of a few things.
#I use break statements pretty frequently
#I really need to get used to the continue operator
#Python is really, really tricky with indentations.
#Definitely prefer brackets.
