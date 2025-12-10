"""Day 5 - Cafeteria"""

from typing import Any
from utils.aoc_utils import report_results, AoCResult, input_for_day

IngredientIds = list[int]
FreshRanges = list[range]

EXAMPLE: str = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
DATA = input_for_day(5, 2025)


def parse_input(puzzle_input: str) -> tuple[FreshRanges, IngredientIds]:
    ranges: FreshRanges = []
    ranges_str, ingredient_ids_str = [
        x.splitlines() for x in puzzle_input.split('\n\n')
    ]
    ranges = [
        range(start, end + 1) for start, end in (map(int, r.split('-')) for r in ranges_str)
    ]

    # ranges_ints = [list(map(int, r.split('-'))) for r in ranges_str]
    # for rng in ranges_ints:
    #     ranges.extend(list(range(rng[0], rng[1]+1)))

    ingredient_ids: IngredientIds = list(map(int, ingredient_ids_str))
    return ranges, ingredient_ids


def solve_part1(data: Any) -> int:
    ranges, ingredient_ids = parse_input(data)
    valid_id = 0
    for x in ingredient_ids:
        for y in ranges:
            if x in y:
                valid_id += 1
                break
    return valid_id


@report_results
def solveday(data: Any) -> AoCResult:
    p1: int = solve_part1(data)
    p2: int = 0
    return p1, p2


expected_test_results: AoCResult = (3, 0)


def tests(test_input: Any) -> None:
    p1, p2 = solveday(test_input)
    assert (p1, p2) == expected_test_results
    print("☑️ Tests passed!")


if __name__ == "__main__":
    tests(EXAMPLE)
    solveday(DATA)
