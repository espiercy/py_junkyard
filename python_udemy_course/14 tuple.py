#here's a tuple:

test_tuple=(2,3,56,"text in a tuple")

print(test_tuple)

print(test_tuple[0])

#can't change tuple values
#test[1]="poop"

#empty tuple

empty=()

second_test=test_tuple*3
print(second_test)

new=('new tuple','hi earth')

joined_tuple=test_tuple+new
print(joined_tuple)
print(joined_tuple[1:4])

t1=joined_tuple[1:5]
print(t1)