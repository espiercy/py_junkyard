#here's a list

list=[45,89,78,'text inside of a list']

print(list[0], list[1], list[2], list[3])

print(list)

list_0=list[0]
list[1] = "This value has been changed by direct access"

print(list[2], list[3], list_0, list[:3])

list1 = list*2

print(list1)