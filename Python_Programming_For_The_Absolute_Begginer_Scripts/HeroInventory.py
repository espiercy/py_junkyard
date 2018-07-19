#Hero's Inventory
#Demonstrates tuple creation
#Evan Piercy
#3.20.15

#I think this text makes a mistake introducing tuples this way.
#Tuples turn out to be an extraordinarily important data structure
#They really deserve their own chapter.
#When I started my way through this book several years ago, I didn't
#Really know/understand what a 'tuple' was.

#creat empty tuple

inventory = ()

#treat tuple as condition

if not inventory:
    print("You are empty handed!")

input("Press enter key to continue.")

#create a tuple with some items

inventory = ("sword" , "armor" , "shield" , "healing potion")

#print tuple

print("\nThe tuple inventory is: ")
print(inventory)

#print each element
print("\nYour items: ")
for item in inventory:
    print(item)

input("\n\nPress the enter key to exit.")
