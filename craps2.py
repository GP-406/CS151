#--------------------------{HEADER}------------------------------
# NAME
# DATE
# FILE NAME
#----------------------------------------------------------------
#------------------------{DESCRIPTION}---------------------------
"""

"""
#----------------------------------------------------------------
#--------------------------{IMPORTS}-----------------------------

import random
import stdio
import sys
import stdarray

#----------------------------------------------------------------
#-------------------------{FUNCTIONS}----------------------------

def set_probability(user_input):
    other_prob = (1-user_input)/5
    distributions = [user_input, other_prob, other_prob, other_prob, other_prob, other_prob]
    return distributions

#Generates 2 random numbers between 1 and 6 based off of a command-line probability
#returns total
def die_roll(prob):
    numbers = [1, 2, 3, 4, 5, 6]
    die1 = random.choices(numbers, weights = prob)
    die2 = random.choices(numbers, weights = prob)
    roll_total = die1 + die2
    return roll_total

#determines if you win or lose
def win_lose(prob):    
    wins = 0
    set_roll = sum(die_roll(prob))
    if set_roll == 7 or set_roll == 11:
        wins += 1
        return wins
    elif set_roll == 2 or set_roll == 3 or set_roll == 12:
        wins += 0
    else:
        new_roll = sum(die_roll(prob))
        while new_roll != 7 and new_roll != set_roll:
            if new_roll == set_roll:
                wins += 1
                return wins
            elif new_roll == 7:
                wins += 0
            new_roll = sum(die_roll(prob))
    return wins



#----------------------------------------------------------------
#------------------------{GLOBAL CODE}---------------------------
n = float(sys.argv[1])
probability_of_one = set_probability(n)

wins = 0
for i in range(1000000):
    result = win_lose(probability_of_one)
    wins += result
stdio.writeln(wins/10000)

#----------------------------------------------------------------