#Property Critter
#Demonstrates Properties
#Evan Piercy
#6.5.15

class Critter(object):
    """A virtual pet."""
    def __init__(self, name):
        print("A new critter has been born!")
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("A critter's name can't be an empty string.")
        else:
            self.__name = new_name
            print("Name change successful")

    def talk(self):
        print("\nHi, I'm ", self.name)

#main
crit = Critter("Poochie")
crit.talk()

print("\nMy critter's name is: ", end= "")
print(crit.name)

print("\nAttempting to change my critter's name to Randolph")
crit.name = "Randolph"

print("\nMy critter's name is: ", end= "")
print(crit.name)

print("Attempting to change my critter's name to the empty string...")
crit.name = ""

print("\nMy critter's name is: ", end= "")
print(crit.name)

input("\n\nPress the enter key to exit.")
