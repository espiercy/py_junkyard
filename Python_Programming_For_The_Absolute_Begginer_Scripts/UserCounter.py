#User Counter
#Counts from and to user specified integer, also allowing user to
#Allot increments
#First challege, chapter four
#Evan Piercy
#3.20.15

start = int(input("Where should I start? "))

finish = int(input("Where should I finish? "))

skip = int(input("By how many should I count? "))

print("Counting:")
for i in range(start,finish,skip):
    print(i, end=" ")
input("\n\nPress the enter key to exit.\n")
