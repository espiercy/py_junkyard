#Backwards
#Accepts a phrase from the user then prints it backwards
#Evan Piercy
#3.20.15

phrase = input("Enter a phrase: ")

begin = len(phrase) - 1

print("Listing characters: ")
#do not like the counter , but it functions properly
for i in range(begin , -1 , -1):
    print(phrase[i])

input("Press the enter key to exit.")
