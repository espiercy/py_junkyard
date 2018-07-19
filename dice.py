#epiercy 5/16/18
#module should contain all dice-rolling logic
#all funcs except roll_dice to remain private(?)

import random

#validation? #what if the caller wants to play with individual rolls?
#that is an excellent reason for classification
#this is where I will do work on individual die rolls, as needed
def roll_dice(num_rolls, num_sides, per_roll_mod=0,
    rolls_to_drop=0, drop_lowest=True): #need to break this into components
    roll_vals = mult_roll(num_rolls, num_sides) #roll values
    roll_vals.sort()
    if per_roll_mod != 0: #pass to another function
        roll_vals = mod_rolls(roll_vals, per_roll_mod)
    if rolls_to_drop != 0:
        roll_vals = drop_rolls(roll_vals, rolls_to_drop, drop_lowest)
    total = sum(roll_vals)
    return total

def mult_roll(num_rolls, num_sides):
    values = []
    for i in range(num_rolls):
        values.append(base_roll(num_sides))
    return values

#basic rolling. Takes amount, sides, and per die modifier...other special cases???
def base_roll(num_sides):
    return random.randint(1, num_sides)

def mod_rolls(rolls, per_roll_mod):
    modded_rolls = []
    for roll in rolls:
        roll += per_roll_mod
        print('new roll value: ', roll)
        if roll <= 0:
            roll = 1
        modded_rolls.append(roll)
    return modded_rolls

def drop_rolls(rolls, rolls_to_drop, drop_lowest):
    print(rolls)
    if drop_lowest:
        return rolls[rolls_to_drop:]
    else:
        return rolls[:rolls_to_drop * -1]
