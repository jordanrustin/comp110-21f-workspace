"""Practice with dictionaries."""

__author__ = "730308364"

# Define your functions below


def invert(one: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of dictionary."""
    output: dict[str, str] = {}
    for key in one:
        output[one[key]] = key
        if key in output:
            raise KeyError
    return output


def favorite_color(one: dict[str, str]) -> str:
    """Returns the color that appears most frequently."""
    color_times: dict[str, int] = {}
    for key in one:
        if one[key] in color_times:
            color_times[one[key]] += 1
        else:
            color_times[one[key]] = 1
        
    high: int = 0
    fav: str = ""

    for key in color_times:
        if color_times[key] > high:
            high = color_times[key]
            fav = key
    return fav


def count(freq: list[str]) -> dict[str, int]:
    """Produces a dictionary where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    
    for column in freq:
        if column in result:
            result[column] += 1
        else:
            result[column] = 1
    return result