from random import random


def roll_dice():
    die1 = random.randrange(1,7)
    die2 = random.randrange(1,7)
    print(die1,die2)
roll_dice()
