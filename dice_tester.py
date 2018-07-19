#stats generator - creates 6 scores
import dice as d

#let's give me the ability to run custom tests
run = True

while run:
    print('How many dice do you want to roll?')
    num_rolls = input

rolls = d.roll_dice(5, 6, 4, 2, True)
print(rolls)
