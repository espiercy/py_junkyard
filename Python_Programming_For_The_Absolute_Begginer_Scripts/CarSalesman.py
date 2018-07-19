#Car Salesman
#Third challenge, second chapter
#Drums up a bunch of bogus fees along with a new car

car = float(input("What is the base price of your car? "))

tax = car * .2
licens = car * .1
bogusOne = 500
bogusTwo = 100
airConditioner = 300
antiStopBrakes = 700

total = tax + licens + bogusOne + bogusTwo + airConditioner + antiStopBrakes

print("$" , total , "is your total.")
