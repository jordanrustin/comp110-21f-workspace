"""List utility functions."""

__author__ = "730308364"


# TODO: Implement your functions here.

def all(xs: list[int], y: int) -> bool:
    """Return true if all number in the list match the indicated number."""
    i: int = 0
    if len(xs) == 0:
        return False
    while i < len(xs):
        if xs[i] != y:
            return False
        i += 1
    return True


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Return True if every element at every index is equal in both lists."""
    i: int = 0
    if len(list_one) and len(list_two) != 0:
        while i < len(list_one):
            if list_one[i] != list_two[i]:
                return False
            i += 1
    else:
        if len(list_one) != len(list_two):
            return False
    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        max_one = input[0]
        i: int = 0
        i += 1
        while i < len(input):
            if max_one < input[i]:
                max_one = input[i]
            i += 1
    return max_one