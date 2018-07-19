
#vars in functions limited in scope
#the var below is global, can access from anywhere
test=9

def display(temp1):
    print(temp1)

def show(temp2):
    print(temp2)

show(5)
display(6)