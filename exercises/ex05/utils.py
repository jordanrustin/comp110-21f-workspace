"""List utility functions part 2."""

__author__ = "730308364"

# Define your functions below


def only_evens(list_one: list[int]) -> list[int]:
    """Returns a list containing only the elemtents of the input list that were even."""
    even_list: list[int] = []
    i: int = 0
    while i < len(list_one):
        if list_one[i] % 2 == 0:
            even_list.append(list_one[i])
        i += 1
    return even_list


def sub(a_list: list[int], a: int, b: int) -> list[int]:
    """Generates a list which is a subset of the given list, between specified start and end indicies."""
    if a < 0:
        a = 0
    if b > len(a_list):
        b = len(a_list)
    if len(a_list) == 0 or a > len(a_list) or b <= 0:
        return []
    i: int = a
    final_list: list[int] = []
    while b > i:
        final_list.append(a_list[i])
        i += 1  
    return final_list
 

def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Generates a new list containing all of the elements of the first list followed by the second."""
    third_list: list[int] = []
    i: int = 0
    while i < len(first_list):
        third_list.append(first_list[i])
        i += 1
    j: int = 0
    while j < len(second_list):
        third_list.append(second_list[i])
        j += 1
    return third_list