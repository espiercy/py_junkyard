#Who Is Your GrandDaddy
#Uses the Python dictionary data structure to retrieve father names
#From sons name
#Son is the key, father is the value
#Evan Piercy

father_from_son = {'Chris' : 'Andy', 'David' : 'Benjamin',
                   'Jack' : 'Guido', 'Evan' : 'Kevin',
                   'Robert' : 'Bobby', 'Max' : 'Leon',
                   'Kyle' : 'Michael', 'Daniel' : 'Rick',
                   'James' : 'Thomas', 'Arthur' : 'Conan',
                   'Andy':'Andrew','Benjamin':'Benstoffersun',
                   'Guido':'Guillame', 'Kevin':'Kevstoffersun',
                   'Bobby': 'Boberto', 'Leon':'Leonidas',
                   'Michael' : 'Michaelangelo', 'Rick':'Rickonidas',
                   'Thomas': 'Thamas', 'Conan':'Barbarian'}
check =""
print("Welcome to 'Who's Your GrandDaddy. Below is a list of sons. Press X to exit")

while check != 'X':
    print(father_from_son.keys())
    check = input("Press 1 to view fathers. Press 2 to view grandfathers:\n")
    if check =='1':
        input("Enter the name of the son you are looking for: ")
        if son_check in father_from_son:
            print(son_check, "'s father is: ", father_from_son[son_check], "\n")
        else:
            input("That name is not in the dictionary, please try again.")
    elif check == '2':
        son_check = input("Enter the name of the grandson you are looking for:" )
        if son_check in father_from_son:
            if father_from_son[son_check] in father_from_son: 
                print(son_check, "'s grandfather is: ", father_from_son[father_from_son[son_check]], "\n")
            else:
              print("No grandfather found, sorry.")
        else:
              print("That name is not in the dictionary")
    elif check == 'X':
        print('Ok, hope you found what you were looking for.')
    else:
        print("That's not a valid command.")
              
input("Press the enter key to exit.")
    
