"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730308364"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says... ")

fortune_number: int = randint(0, 100)

if fortune_number < 25:
    print("You will meet a special person tomorrow.")
else: 
    if fortune_number >= 75:
        print("Something exciting will happen during your first class on Friday.")
    else:
        if fortune_number > 50:
            print("Tomorrow will be the most exciting day of the year.")
        else:
            print("You will have an amazing meal this weekend.")

print("Now, go spread positive vibes!")    