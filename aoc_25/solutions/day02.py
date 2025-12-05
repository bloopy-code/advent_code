"""Day 2 - Gift Shop"""

from typing import Any
from utils.aoc_utils import report_results, AoCResult, input_for_day
from itertools import batched
from rich.progress import track

EXAMPLE: list[str] = [
    "11-22",
    "95-115",
    "998-1012",
    "1188511880-1188511890",
    "222220-222224",
    "1698522-1698528",
    "446443-446449",
    "38593856-38593862",
    "565653-565659",
    "824824821-824824827",
    "2121212118-2121212124",
]
INPUT_DATA: str = input_for_day(2, 2025)
DATA: list[str] = INPUT_DATA.split(",")


def part2_wrangle(id_str: str) -> int:
    """Part 2 wrangle.
    Find chunks of string id to make it even chunks.
    If a len(set) of those chunks == 1 - invalid id!

    Args:
        id_str (str): ID String

    Returns:
        int: either the invalid id int or 0
    """
    # find each divisor
    id_len: int = len(id_str)
    divisors: list[int] = [x for x in range(1, id_len) if id_len % x == 0]

    for d in divisors:
        if id_len / d >= 2:
            b: list[tuple[str, ...]] = list(batched(id_str, d))
            if len(set(b)) == 1:
                return int(id_str)
    return 0


def id_wrangle(data: list[str]) -> AoCResult:
    """Solution for Day02 AOC25.
    Part 1 - looks for ID's that are just repeats.
    Part 2 - TBA.

    Args:
        data (list[str]): Input data.

    Returns:
        AoCResult: part1 invalid ids, part 2 invalid ids
    """
    invalid_ids_p1: int = 0
    invalid_ids_p2: int = 0

    for x in track(data):
        lower_id, upper_id = map(int, x.split("-"))
        id_range: range = range(lower_id, upper_id + 1)

        for j in id_range:
            id_str: str = str(j)
            invalid_ids_p2 += part2_wrangle(id_str)
            # print(list(batched(id_str, 2)))
            if len(id_str) % 2 == 0:
                split_id_str1, split_id_str2 = list(batched(id_str, len(id_str) // 2))
                # print(split_id_str1, split_id_str2)
                if split_id_str1 == split_id_str2:
                    # print(id_str, ' = INVALID ID', list(batched(id_str, 2))
                    invalid_ids_p1 += int(id_str)

    return invalid_ids_p1, invalid_ids_p2


@report_results
def solveday(data: list[str]) -> AoCResult:
    p1, p2 = id_wrangle(data)
    return p1, p2


expected_test_results: AoCResult = (1227775554, 4174379265)


def tests(test_input: Any) -> None:
    p1, p2 = solveday(test_input)
    assert (p1, p2) == expected_test_results
    print("☑️ Tests passed!")


if __name__ == "__main__":
    tests(EXAMPLE)
    solveday(DATA)
