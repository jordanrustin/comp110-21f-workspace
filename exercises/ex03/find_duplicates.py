"""Finding duplicate letters in a word."""

__author__ = "730308364"

word: str = input("Enter a word: ")
dup: bool = False

i: int = 0
while i < len(word):
    z = word[i]
    j: int = i + 1
    while j < len(word):
        if z == word[j]:
            dup = True
        j += 1
    i += 1
print("Found duplicate: " + str(dup))
