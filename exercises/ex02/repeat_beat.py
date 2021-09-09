"""Repeating a beat in a loop."""

__author__ = "730308364"


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
number_times: int = int(input("How many times do you want to repeat it? "))
beat_multiplier: str = " "

while number_times:
    if number_times <= 0:
        print("No beat...")
        number_times = 0
    else:
        beat_multiplier = beat + " " +  beat_multiplier 
        number_times = number_times - 1
print(beat_multiplier)


