
#interesting assignment below, but probably not entirely useful
num1,num2,num3,num4,num5 = [23,56,48,74,58]

num11,num22,num33,num44,num55 = (23,56,48,74,58)

print(num1,num11)

#this method is better:

#notice that static designation. That's telling the compiler that the variable is flexible/can handle multiple values
list0, list1, *list, list_second_to_last, list_last = [23,56,48,74,58,5,4,7]

print(list0, list1, list_second_to_last, list_last)
print(list)

#this all works for tuples. I do not feel obligated to demonstrate...