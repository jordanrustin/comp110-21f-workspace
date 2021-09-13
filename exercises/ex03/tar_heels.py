"""An exercise in remainders and boolean logic."""

__author__ = "730308364"


# Begin your solution here...
response: str = input("Enter an int: ")
number: int = int(response)

if (number % 2) == 0 or (number % 7) == 0:
    if (number % 2) == 0 and (number % 7) == 0:
        print("TAR HEELS") 
    else:
        if (number % 2) == 0:
            print("TAR")
        if (number % 7) == 0:
            print("HEELS")
else:
    print("CAROLINA")