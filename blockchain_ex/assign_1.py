#epiercy 8/28/18
#blockchain assign one

#storing name and age
name = input("Enter your name: ")
age = int(input("Enter your age: "))


def print_info():
    """ Prints global vars"""
    print("Name:", name, "Age:", age)


def print_input(name, age):
    """Prints args
    
    Arguments:
        name: your name
        age: your age
    
    """
    print("Name: " + name + " Age: " + str(age))


def get_decades():
    """ Returns global age // 10"""
    return age // 10


print_info()
print_input("Evan", 36)

print("You have lived", get_decades(), "decades!")