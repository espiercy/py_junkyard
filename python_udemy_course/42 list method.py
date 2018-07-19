
num=[25,36,48,97,58]
num2=[45,78]

#delete first index
del num[0]

print(num)

#get number of items in list

size = len(num)
print(size)

#print largest value from list
print(max(num))

#...smallest
print(min(num))

#add a value
num.append(35)

print(num)

num.append(58)
#count how many times an item is present in list.
print(num.count(58))

#add lists together
num.extend(num2)

print(num)

num2.extend(num)
print(num2)

#find a value's index
print(num.index(48))

#pop last value from the list
num.pop()

print(num)

#pop indexed val from the list
num.pop(4)

print(num)

#remove from list by value
num.remove(97)
print(num)

#reverse values in list
num.reverse()
print(num)

#sort list smallest to large
num.sort()

print(num)