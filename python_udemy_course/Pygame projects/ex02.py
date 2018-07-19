number_correct = 0
total_q = 5


print("When did William The Conqueror Invade Britain?\n1. 500 BC\n2. He never invaded\n3. 1066 AD\n4. 1942 AD")
answer = int(input("Enter the number of the correct response: "))
if(answer == 3):
    print("Correct!")
    number_correct += 1
else:
    print("No, that is not correct.")
    print("The correct answer was: 3. 1066 AD")
print()
print("Approximately When did the Battle of Thermopylae occur?\n1. 700 BC\n2. 480 BC\n3. 800 AD\n4. 1942 AD")
answer = int(input("Enter the number of the correct response: "))
if(answer == 2):
    print("Correct!")
    number_correct += 1
else:
    print("No, that is not correct.")
    print("The correct answer was: 2. 480 BC")
print()
print("Approximately When did the Battle of Agincourt occur?\n1. 1417 AD\n2. 1066 AD\n3. 1415 AD\n4. 1942 AD")
answer = int(input("Enter the number of the correct response: "))
if(answer == 3):
    print("Correct!")
    number_correct += 1
else:
    print("No, that is not correct.")
    print("The correct answer was: 3. 1415 AD")
print()
print("When did WWII begin?\n1. 1943 AD\n2. 1939 AD\n3. 1066 AD\n4. 1942 AD")
answer = int(input("Enter the number of the correct response: "))
if(answer == 2):
    print("Correct!")
    number_correct += 1
else:
    print("No, that is not correct.")
    print("The correct answer was: 2. 1939 AD")
print()
print("When did WWI begin?\n1. 1914 AD\n2. 1911 AD\n3. 1066 AD\n4. 1942 AD")
answer = int(input("Enter the number of the correct response: "))
if(answer == 1):
    print("Correct!")
    number_correct += 1
else:
    print("No, that is not correct.")
    print("The correct answer was: 1. 1914")
print()
percentage = 100 * number_correct / total_q

print("You scored ", percentage,"%" )
