import heapq

#can use with sets, dictionaries
list=[25,36,48,96,78]

#get two largest from list
print(heapq.nlargest(2,list))

#get 3...
print(heapq.nlargest(3,list))

#get two smallest from list
print(heapq.nsmallest(2,list))

product = {'milk':56,'water':560,'honey':60,'sugar':160,'tea':269}

print(heapq.nlargest(3, zip(product.values(),product.keys())))

print(heapq.nsmallest(3, zip(product.keys(),product.values())))

print(heapq.nlargest(3, zip(product.keys(),product.values())))