"""Day 4 - Printing Department"""

from typing import Any
from utils.aoc_utils import report_results, AoCResult, input_for_day

LooRollGrid = list[list[str]]

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


def parse_loogrid_p1(data: LooRollGrid) -> int:
    """Navigate through the Loo Roll Grid for AOCD4P1.

    Insert an extra layer of blank padding, slide a
    3x3 window and count adjacent loo rolls.
    If less than 4 adjacent loo rolls, count it!

    Args:
        data (LooRollGrid): List of lists, @ = loo roll.

    Returns:
        int: Count of valid positions.
    """
    forklift_access: int = 0
    # add an extra padding 0 and -1
    for row in data:
        row.insert(0, ".")
        row.insert(len(data[0]), ".")

    # add an extra layer of padding...
    data.insert(0, list("." * len(data[0])))
    data.insert(len(data), list("." * len(data[0])))

    # trundle through the grid
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
                    forklift_access += 1
    return forklift_access


@report_results
def solveday(data: Any) -> AoCResult:
    p1: int = parse_loogrid_p1(data)
    p2: int = 0
    return p1, p2


expected_test_results: AoCResult = (13, 0)


def tests(test_input: Any) -> None:
    p1, p2 = solveday(test_input)
    assert (p1, p2) == expected_test_results
    print("☑️ Tests passed!")


if __name__ == "__main__":
    tests(EXAMPLE)
    solveday(DATA)
