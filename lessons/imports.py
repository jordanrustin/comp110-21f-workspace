"""Examples of imports."""

from lessons import helpers

# import using an alias
from lessons import helpers as hp

# import names directly from globals of a module
from lessons.helpers import powerful, THE_ANSWER


def main() -> None:
    # Access the first import
    print(helpers.powerful(2, 4))

    # Access the aliased import
    print(hp.THE_ANSWER)

    # Call the function directly
    print(powerful(2, 4))
    print(THE_ANSWER)

    print(f"imports.py: {__name__}")


if __name__ == "__main__":
    main()