#--------------------------{HEADER}------------------------------
# NAME
# DATE
# craps.py
#----------------------------------------------------------------
#------------------------{DESCRIPTION}---------------------------
"""
Here are the rules for a pass bet in the game of craps: Roll two 6-sided dice, and let x be their sum.
If x is 7 or 11, you win. If x is 2, 3, or 12, you lose.
Otherwise, repeatedly roll two the dice until their sum is either x or 7.
If their sum is x, you win. If their sum is 7, you lose.
Compose a modular program to estimate the probability of winning a pass bet.
Modify your program to handle loaded dice, where the probability of a die
landing on 1 is taken from the command line, the probability of landing 
on 6 is 1/6 minus that probability, and 2-5 are assumed equally likely.
"""
#----------------------------------------------------------------
#--------------------------{IMPORTS}-----------------------------

import random
import stdio
import sys
import stdarray

#----------------------------------------------------------------
#-------------------------{FUNCTIONS}----------------------------

#Argument should be between 0 and 1 determines probability of number 1 being generated.
def set_probability(user_input):
    secondary_prob = (1-user_input)/5
    distributions = [user_input, secondary_prob, secondary_prob, secondary_prob, secondary_prob, secondary_prob]
    return distributions

#Generates 2 random numbers between 1 and 6 based off of a command-line probability
#returns total
def die_roll(prob):
    numbers = [1, 2, 3, 4, 5, 6]
    die1 = random.choices(numbers, weights = prob)
    die2 = random.choices(numbers, weights = prob)
    roll_total = die1 + die2
    return roll_total

#Determines if you win or lose
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

# Command-line argument sets probability of landing on 1. argument should be between (0,1)
n = float(sys.argv[1])

# Sets probability with user input
probability_of_one = set_probability(n)

# Runs 1000000 trials and prints percentage of play bet wins
wins = 0
for i in range(1000000):
    result = win_lose(probability_of_one)
    wins += result

stdio.writeln('-'*65)
stdio.writeln('Probability of winning pass bet with loaded Probability of (' + str(n) + '):')
stdio.writeln(str(wins/10000) + '%')
stdio.writeln('-'*65)

#----------------------------------------------------------------