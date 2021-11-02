"""Practice with dictionaries."""

__author__ = "730308364"

# Define your functions below


def invert(one: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of dictionary."""
    output: dict[str, str] = {}
    for key in one:
        output[one[key]] = key
    return output


def favorite_color(two: dict[str, str]) -> str:
    """Returns the color that appears most frequently."""
    color: dict[str, int] = {}
    for key in two:
        favs = two.get(key)
        if favs:
            