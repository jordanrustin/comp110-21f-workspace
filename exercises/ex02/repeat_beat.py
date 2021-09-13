"""Repeating a beat in a loop."""

__author__ = "730308364"


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
number_times: int = int(input("How many times do you want to repeat it? "))
beat_multiplier: str = beat + " "
beat_counter: int = 0

while beat_counter < number_times:
    print((beat_counter - 1) * beat_multiplier + beat)
    beat_counter = number_times
if number_times <= 0:
    print("No beat...")