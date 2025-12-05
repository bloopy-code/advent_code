"""Day 4 - Title Goes Here"""

from typing import Any
from utils.aoc_utils import input_for_day, report_results, AoCResult


EXAMPLE: list = []
DATA = input_for_day(4)


def helperfunction(data: Any) -> None:
    return None


@report_results
def solveday(data: Any) -> AoCResult:
    p1: int = 0
    p2: int = 0
    return p1, p2


expected_test_results: AoCResult = (0, 0)


def tests(test_input: Any) -> None:
    p1, p2 = solveday(test_input)
    assert (p1, p2) == expected_test_results
    print("☑️ Tests passed!")


if __name__ == "__main__":
    tests(EXAMPLE)
    solveday(DATA)
