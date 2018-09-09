import random as rn, datetime as dt

#rando between 0 and 1
print("Random number between 0 and 1: ", rn.randint(0, 1))

#rando between 1 and 10
print("Random number between 0 and 1: ", rn.randint(1, 10))

year = rn.randint(0, 2099)
month = rn.randint(1, 12)
#don't want to deal with potential issues during leap years...so
day = rn.randint(1, 28)

date = dt.date(year, month, day)

print("Random value from datetime? ", date)