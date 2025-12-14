"""Day 4 - Printing Department"""

from typing import Any
from utils.aoc_utils import report_results, AoCResult, input_for_day

LooRollGrid = list[list[str]]
RollCoord = tuple[int, int]

ORIGINAL_EXAMPLE: str = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

EXAMPLE: LooRollGrid = [list(x) for x in ORIGINAL_EXAMPLE.splitlines()]
INPUT_DATA: list[str] = input_for_day(4, 2025, ff="lines")
DATA: LooRollGrid = [list(x) for x in INPUT_DATA]


def forklift(data: LooRollGrid) -> list[RollCoord]:
    """Forklift operations. Go through grid, find '@',
    get window and check adjacent '@'.
    If valid - add to list of valid coordinates.

    Args:
        data (LooRollGrid): Puzzle input as a list of lists.

    Returns:
        list[RollCoord]: list of valid coordinates.
    """
    # trundle through the grid
    coords: list[RollCoord] = []
    row_idx: int
    col_idx: int

    for row_idx, row in enumerate(data[1:-1], 1):
        # print(ri, row[1:-1])
        for col_idx, col in enumerate(row[1:-1], 1):
            if "@" in col:
                # grab a 3x3 window
                window: LooRollGrid = [
                    row[col_idx - 1:col_idx + 2]
                    for row in data[row_idx - 1:row_idx + 2]
                ]
                # smoosh it together
                join_window: str = "".join("".join(row) for row in window)
                # deduct the initial @
                num_rolls: int = join_window.count("@") - 1
                if num_rolls < 4:
                    coords.append((row_idx, col_idx))

    return coords


def pad_data(data: LooRollGrid) -> LooRollGrid:
    """Pad initial grid with blanks.

    Args:
        data (LooRollGrid): Puzzle input grid.

    Returns:
        LooRollGrid: Padded puzzle grid.
    """
    # add an extra padding 0 and -1
    padded_data: LooRollGrid = data.copy()
    for row in padded_data:
        row.insert(0, ".")
        row.insert(len(data[0]), ".")

    # add an extra layer of padding...
    padded_data.insert(0, list("." * len(padded_data[0])))
    padded_data.insert(len(padded_data), list("." * len(padded_data[0])))

    return padded_data


def solve_p1(data: LooRollGrid) -> int:
    """Solve P1. Iterate once - find valid coords.

    Args:
        data (LooRollGrid): Puzzle input.

    Returns:
        int: Number of valid loo roll coords.
    """
    padded_data = pad_data(data)
    valid_rolls = forklift(padded_data)
    return len(valid_rolls)


def solve_p2(data: LooRollGrid) -> int:
    """Search for valid coords,
    add to coordinate list. Replace those coords with 'x',
    then repeat until no more can be replaced.

    Args:
        data (LooRollGrid): Puzzle input.

    Returns:
        int: Total valid loo roll removals.
    """
    padded_data: LooRollGrid = pad_data(data)
    total_removed: int = 0

    while True:
        coords: list[RollCoord] = forklift(padded_data)
        if not coords:
            break

        for x in coords:
            padded_data[x[0]][x[1]] = 'x'
        total_removed += len(coords)

    return total_removed


@report_results
def solveday(data: Any) -> AoCResult:
    p1: int = solve_p1([row.copy() for row in data])
    p2: int = solve_p2([row.copy() for row in data])
    return p1, p2


expected_test_results: AoCResult = (13, 43)


def tests(test_input: Any) -> None:
    p1, p2 = solveday(test_input)
    assert (p1, p2) == expected_test_results
    print("☑️ Tests passed!")


if __name__ == "__main__":
    tests(EXAMPLE)
    solveday(DATA)
