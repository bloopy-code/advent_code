"""Day 1 - Secret Entrance"""
from typing import Any
from utils.aoc_utils import report_results, AoCResult, input_for_day

# example for testing solution
EXAMPLE: list[str] = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82"
]
DATA = input_for_day(1, 2025, ff='list')


def parse_input(data: list[str]) -> tuple[int, int]:
    """Parse input for AOC25 Day1.

    Args:
        data (list[str]): Input list with instructions.

    Returns:
        tuple[int, int]: land on zero, click over zero.
    """
    zero_counter: int = 0
    # click_over_count: int = 0
    start: int = 50

    for x in data:
        # assuming data will always be in a valid format
        direction, num = x[0], int(x[1:])
        # print(direction, num)

        if direction == 'L':
            start -= num
        else:
            start += num

        start %= 100

        if start == 0:
            # lands on zero following a turn
            zero_counter += 1

    return zero_counter, 0


@report_results
def solveday(data: list[str]) -> AoCResult:
    p1, p2 = parse_input(data)
    return p1, p2


expected_test_results: AoCResult = (3, 0)


def tests(test_input: Any) -> None:
    p1, p2 = solveday(test_input)
    assert (p1, p2) == expected_test_results
    print("☑️ Tests passed!")


if __name__ == "__main__":
    tests(EXAMPLE)
    solveday(DATA)
