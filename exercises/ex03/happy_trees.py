"""Drawing forests in a loop."""

__author__ = "730308364"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth: int = int(input("Depth: "))
i: int = 0

while i < depth:
    TREE_two = TREE + " "
    print(TREE_two * i + TREE)
    i += 1