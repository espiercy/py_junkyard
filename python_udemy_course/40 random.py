import random

rand = random.random()
print(rand)

for i in range(5):
    rand = random.random()
    print(rand)

print(random.randrange(1,10000))

print(random.uniform(1,10000))