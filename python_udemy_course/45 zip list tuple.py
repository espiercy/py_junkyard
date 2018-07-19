
list1=[2,4,569,85]
list2=[20,45,59,805]
list3=[8,7,6,4080]

#here's how to zip...

zip_list=zip(list1, list2, list3)

#cannot print this way...
print(zip_list)

for val1, val2, val3 in zip_list:
    print(val1,val2, val3)

#again, this all works for tuples, but no need to demonstrate