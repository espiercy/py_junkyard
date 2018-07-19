class Father:
    money=100

    def __init__(self):
        print("Inside father constructor")

    def show(self):
        print("show")

class Mother:
    def display(self):
        print("Mother")

#specifies parent class
class Steve(Father,Mother):

    def __init__(self):
        print("Child constructor")

    def show(self):
        print("show child constructor")

s1=Steve()
s1.show()
s1.display()
print(s1.money)