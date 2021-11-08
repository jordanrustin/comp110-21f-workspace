"""Utility functions."""

__author__ = "730308364"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
        
    return result


def head(original: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produces a column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}

    for column in original:
        if N >= len(original[column]):
            return original
        else:
            N_values: list[str] = []
            item = original[column]
            i: int = 0
            while i < N:
                N_values.append(item[i])
                i += 1
            result[column] = N_values
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produces a new column-based table with only a specific subset of the originial columns."""
    result: dict[str, list[str]] = {}
    
    for column in names:
        result[column] = table[column]
    return result


def concat(one: dict[str, list[str]], two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}

    for column in one:
        result[column] = one[column]
    for column in two:
        if column in result:
            one[column] + two[column]
        else:
            result[column] = two[column]
    return result
