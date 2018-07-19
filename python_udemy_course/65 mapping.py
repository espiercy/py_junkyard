

list1=[10,20,30,40,50]

def calculate( value ):
    return value*2

#to multiply each value by 2, call map function, cast to list. map() takes params function, list

new_list=list(map( calculate, list1))

print(new_list)