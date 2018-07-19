#create dictionary

fruits= {'mango':576,'grapes':200,'oranges':300,'banana':20,'strawberry':1000}

#get minimum value

print(min(fruits.values()))

#if we want key along with val, use zip function

print(min(zip(fruits.values(),fruits.keys())))
print(min(zip(fruits.keys(),fruits.values())))

print(max(zip(fruits.values(),fruits.keys())))

#sort
print(sorted(zip(fruits.values(),fruits.keys())))

#can also sort by key, just put it first
print(sorted(zip(fruits.keys(),fruits.values())))