# camel game
from random import randint

print("Welcome to Camel!")

print("You have stolen a camel to make your way across the great Mobi desert.")

print("The natives want their camel back and are chasing you down! Survive your desert trek and out run the natives.")

done = False
miles_traveled = 0
thirst = 0
camel_tiredness = 0
distance_from_natives = -20
number_of_drinks = 8

while not done:
    print('A. Drink from your canteen.')
    print('B. Ahead moderate speed.')
    print('C. Ahead full speed.')
    print('D. Stop for the night.')
    print('E. Status Check.')
    print('Q. Quit.')
    choice = input('Input your choice: ')
    if choice.upper() == 'Q':
        done = True
    elif choice.upper() == 'E':
        print('Miles Traveled: ', miles_traveled)
        print('Thirst: ', thirst)
        print('Camel Tiredness: ', camel_tiredness )
        print('Distance From Natives', distance_from_natives)
        print('Drinks left in canteen: ', number_of_drinks)
    elif choice.upper() == 'D':
        camel_tiredness = 0
        print('You rest for the night. Your camel is happy and rested.')
        distance_from_natives += randint(7, 14)
    elif choice.upper() == 'C':
        print('You charge your camel ahead at full speed.')
        distance_traveled = randint(10, 20)
        distance_from_natives -= distance_traveled #need to decrement, as this var is negative
        miles_traveled += distance_traveled
        print("You have covered a distance of ", miles_traveled, " miles.")
        thirst += 1
        camel_tiredness += randint(1, 3)
        distance_from_natives += randint(7, 14)
    elif choice.upper() == 'B':
        print('You take it easy on your camel.')
        distance_traveled = randint(5, 12)
        distance_from_natives -= distance_traveled #need to decrement, as this var is negative
        miles_traveled += distance_traveled
        print("You have covered a distance of ", miles_traveled, " miles.")
        thirst += 1
        camel_tiredness += 1
        distance_from_natives += randint(7, 14)
    elif choice.upper() == 'A':
        if number_of_drinks > 0:
            number_of_drinks -= 1
            print('You take a drink.')
            thirst = 0
        else:
            print('You are all out of water')

    if thirst >= 4:
        if thirst <= 6:
            print('You are thirsty.')
        else:
            print('You have died from thirst!')
            done = True

    if not done:
        if camel_tiredness > 5:
            if camel_tiredness < 8:
                print('Your camel is getting tired.')
            else:
                print('Your camel has died from exhaustion.')
                done = True

    if not done:
        if distance_from_natives >= 0:
            print('The natives caught you.')
            done = True
        elif distance_from_natives > -15:
            print('The natives are getting close!')

    if not done:
        if distance_traveled >= 200:
            print('You made it all the way across the desert! Congratulations. You may keep your camel.')

    if not done:
        oasis = randint(0, 4)
        if oasis == 4:
            print('You found an oasis. You drink, refill your canteena, and rest briefly in the shade.')
            thirst = 0
            number_of_drinks = 8
            camel_tiredness = 0
    print()