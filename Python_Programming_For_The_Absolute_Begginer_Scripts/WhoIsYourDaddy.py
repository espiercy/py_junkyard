#Who Is Your Daddy
#Uses the Python dictionary data structure to retrieve father names
#From sons name
#Son is the key, father is the value
#Evan Piercy

father_from_son = {'Chris' : 'Andy', 'David' : 'Benjamin',
                   'Jack' : 'Guido', 'Evan' : 'Kevin',
                   'Robert' : 'Bobby', 'Max' : 'Leon',
                   'Kyle' : 'Michael', 'Daniel' : 'Rick',
                   'James' : 'Thomas', 'Arthur' : 'Conan'}

print("""Welcome to 'Who's Your Daddy.' Below is a list of sons.\n
      Please enter the name of the son in order to view the name of\n
      his father. Type 'X' to exit this program. \n""")

son_check =""

while son_check != 'X':
    #Can improve this interface
    print(father_from_son.keys(),"\n")
    son_check = input("Enter a name to see the son's father or type 'X' to exit program: ")
    if son_check != 'X':
        if son_check in father_from_son:
            print("\n",son_check + "'s father is:", father_from_son[son_check])
            input("\nPress the enter key to continue")
        else:
            input("\nThat name is not in the dictionary, please try again.")

input("Press the enter key to exit.")
    
