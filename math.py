import random
import unittest


def rand_divis_3():
    num = random.randint(0, 100)

    print "Number selected is: ", num

    if num % 3 == 0:
        print "  True - Randomly selected number is divisible by 3"
    else:
        print " False - Randomly selected number is not divisible by 3"


rand_divis_3()


# def roll_dice(sides, dice):
# 	sides = raw_input("How many sides do the dice have? ")
# 	dice = raw_input("How many dice do y'all have?")


def roll_dice(sides, dice):
    for die in range(dice):
        num = random.randint(1, sides)
        print "Dice #" + str(die + 1) + " rolled a " + str(num) + "."


roll_dice(4, 2)


# class MyTest(object):
# 	"""docstring for MyTest"""
# 	def __init__(self, arg):
# 		super(MyTest, self).__init__()
# 		self.arg = arg
#
