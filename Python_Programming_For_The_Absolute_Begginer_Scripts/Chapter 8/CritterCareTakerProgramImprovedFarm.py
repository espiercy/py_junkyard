#Critter Caretaker Farm
#A farm of virtual pets to care for
#Allows specification of food/playtime amounts, number of pets
#Chapter 9, Challenge 4
#Evan Piercy
#6.5.15
#Yet again, the original project has been overwritten by one of the earlier ones. At this point, I don't really care.
import random

class Critter(object):
    """A virtual pet."""
    def __init__(self, name, hunger = random.randrange(0,4), boredom = random.randrange(0,4)):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        rep = ("Critter object: \n")
        rep += "name: " + self.name + "\n"
        rep += "hunger: " + str(self.hunger) + "\n"
        rep += "boredom: " + str(self.boredom) + "\n"

        return rep

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m

    def talk(self):
        print("I'm ", self.name, " and I feel ", self.mood, " now.\n")
        self.__pass_time()

    def eat(self, food = 4):
        amount = int(input("How many food pellets do you want to give me: "))
        print("Brruppp. Thank you.")
        self.hunger -= food*amount
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        time = int(input("How long do you want to play with me: "))
        print("Wheee!")
        self.boredom -= fun*time
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    critter_farm = [] #declare array of critter objects

    crit1_name = input("What do you want to name your first critter?: ")
    critter_farm.append(Critter(crit1_name))
    crit2_name = input("What do you want to name your second critter?: ")
    critter_farm.append(Critter(crit2_name))
    crit3_name = input("What do you want to name your third critter?: ")
    critter_farm.append(Critter(crit3_name))
    crit4_name = input("What do you want to name your fourth critter?: ")
    critter_farm.append(Critter(crit4_name))

    choice = None
    while choice != "0":
        print\
        ("""
         Critter Caretaker

        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)

        choice = input("Choice: ")
        print()

        #exit
        if choice == "0":
            print("Good-bye.")

        #listen to your critter
        elif choice == "1":
            for critter in critter_farm:
                critter.talk()

        #feed your critter
        elif choice == "2":
            for critter in critter_farm:
                critter.eat()

        #play with your critter
        elif choice == "3":
            for critter in critter_farm:
                critter.play()

        #secret option
        elif choice == "4":
            for critter in critter_farm:
                print(critter)
                print()

        #some unknown choice
        else:
            print("\nSorry, but ", choice, " isn't a valid choice.")

main()
("\n\nPress the enter key to exit.")
