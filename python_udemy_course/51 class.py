
#create class. You need to begin with an uppercase letter

class Person:
    name=""
    age=0

    def show(self, n, a):
        self.name=n
        self.age=a
        print(self.name, self.age)

#instance of class
p1=Person()
#method call
p1.show('Evan',22)

print(p1.name, p1.age)