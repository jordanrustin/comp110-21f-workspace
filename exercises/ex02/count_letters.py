"""Counting letters in a string."""

__author__ = "730308364"


# Begin your solution here...
prompt: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")

i: int = 0
letter_counter: int = 0

while i < len(word):
    if prompt == word[i]:
        letter_counter = letter_counter + 1
    i = i + 1 

print("Count: " + str(letter_counter))