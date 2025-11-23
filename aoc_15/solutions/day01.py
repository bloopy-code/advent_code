"""Day 1 - Title Goes Here"""
from itertools import accumulate
from utils.aoc_utils import input_for_day, report_results

EXAMPLE: list[str] = [
    "(())", "()()",
    "(((", "(()(()(",
    "))(((((",
    "())", "))(",
    ")))", ")())())"
]
DATA: str = input_for_day(1, 2015)


def helperfunction(data: str) -> accumulate[int]:
    floors: accumulate[int] = accumulate(
        1 if x == '(' else -1 for x in data
    )
    return floors


@report_results
def solveday(data: str) -> tuple[int, int]:
    p1: int = sum(1 if x == '(' else -1 for x in data)
    p2: int = list(helperfunction(data)).index(-1)
    return p1, p2+1


expected_test_results: tuple[int, int] = (3, 1)


@report_results
def tests(test_input: str) -> None:
    p1, p2 = solveday(test_input)
    assert (p1, p2) == expected_test_results
    print("☑️ Tests passed!")


if __name__ == "__main__":
    tests(EXAMPLE[4])
    solveday(DATA)
