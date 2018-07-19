#Trust Fund Buddu - Good
#Demonstrates a logical propriety, that is to say type conversion
#Evan Piercy
#3.15.16

print(
    """
    Trust Fund Buddy

    Totals your monthly spending so that your trust fund doesn't run out
    (and you're forced to get a real job).

    Please enter the requested monthly costs. Sich you're rich, ignore pennies
    and use only dollar amounts.

    """
    )

car = input("Lamborghini Tune-Ups: ")
car = int(car)

rent = input("Manhattan Apartment: ")
rent = int(rent)

jet =input("Private Jet Rental: ")
jet = int(jet)

gifts = input("Gifts: ")
gifts = int(gifts)

food = input("Dining Out: ")
food = int(food)

staff = input("Staff(butlers, chef, driver, assistant): ")
staff = int(staff)

guru = input("Personal Guru and Coach: ")
guru = int(guru)

games = input("Computer Games: ")
games = int(games)

total = car + rent + jet + gifts + food + staff + guru + games

print("\nGrand Total: ", total)

input("\n\nPress the enter key to exit.")
