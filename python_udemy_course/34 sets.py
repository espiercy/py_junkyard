
#sets are like lists that do not allow duplicate values

set1 = {25, 68, 97, 'udemy', 25}

print(set1)

for temp in set1:
    print(temp)

if 25 in set1:
    print("yea it's there")

#set functions

set2={89,70,'udemy'}

#intersection

inter=set1.intersection(set2)
print(inter)

print(set1.symmetric_difference(set2))

#doesn't change either set!!!
print(set1.union(set2))

print(set1.difference(set2))

print(set2.difference(set1))