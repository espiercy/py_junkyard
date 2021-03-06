#Critter Caretaker Program
#A virtual pet to care for
#Allows specification of food/playtime amounts
#Chapter 9, Challenge 3
#Evan Piercy
#6.5.15
#Yet again, the original project has been overwritten by one of the earlier ones. At this point, I don't really care.
class Critter(object):
    """A virtual pet."""
    def __init__(self, name, hunger = 0, boredom = 0):
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
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)

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
            crit.talk()

        #feed your critter
        elif choice == "2":
            crit.eat()

        #play with your critter
        elif choice == "3":
            crit.play()

        #secret option
        elif choice == "4":
            print(crit)

        #some unknown choice
        else:
            print("\nSorry, but ", choice, " isn't a valid choice.")

main()
("\n\nPress the enter key to exit.")
