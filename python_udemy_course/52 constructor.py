
#gives starting values to class attributes

class Person:
    name=""
    age=0

    #default name for every object's constructor
    def __init__(self):
        print("Working")
        self.name = input("Enter person's name: ")
        self.age = input("Enter person's age: ")
        print("Values accepted")

    def __repr__(self):
        return self.name + str(self.age)
    def display(self):
        print(self.name,'is',self.age,'years old')

p1=Person()
p1.display()
print(p1)