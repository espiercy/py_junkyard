# delete a list#here's a list

list=[45,89,78,'text inside of a list']

print(list[0], list[1], list[2], list[3])

print(list)

list_0=list[0]
list[1] = "This value has been changed by direct access"

print(list[2], list[3], list_0, list[:3])

list1 = list*2

print(list1)

#delete list
del list1

#declare empty list
empty_list=[]

#join lists, does not change original list
new_list = ["instructor",30]

joined_list= list+new_list
print(joined_list)