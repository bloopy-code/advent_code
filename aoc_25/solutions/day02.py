"""Day 2 - Gift Shop"""

from typing import Any
from utils.aoc_utils import report_results, AoCResult, input_for_day
from itertools import batched

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
    "2121212118-2121212124"
]
INPUT_DATA: str = input_for_day(2, 2025)
DATA: list[str] = INPUT_DATA.split(",")


def id_wrangle(data: list[str]) -> int:
    """Solution for Day02 AOC25.
    Part 1 - looks for ID's that are just repeats.
    Part 2 - TBA.

    Args:
        data (list[str]): Input data.

    Returns:
        int: calculated sum of invalid ids.
    """
    invalid_ids: int = 0

    for x in data:
        lower_id, upper_id = map(int, x.split("-"))
        id_range: range = range(lower_id, upper_id+1)

        for j in id_range:
            id_str = str(j)
            # print(list(batched(id_str, 2)))
            if len(id_str) % 2 == 0:
                split_id_str1, split_id_str2 = list(
                    batched(id_str, len(id_str)//2)
                )
                # print(split_id_str1, split_id_str2)
                if split_id_str1 == split_id_str2:
                    # print(id_str, ' = INVALID ID', list(batched(id_str, 2))
                    invalid_ids += int(id_str)
    return invalid_ids


@report_results
def solveday(data: list[str]) -> AoCResult:
    p1: int = id_wrangle(data)
    p2: int = 0
    return p1, p2


expected_test_results: AoCResult = (1227775554, 0)


def tests(test_input: Any) -> None:
    p1, p2 = solveday(test_input)
    assert (p1, p2) == expected_test_results
    print("☑️ Tests passed!")


if __name__ == "__main__":
    tests(EXAMPLE)
    solveday(DATA)
