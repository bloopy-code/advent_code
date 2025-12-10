"""Day 5 - Cafeteria"""

from typing import Any, Iterator
from utils.aoc_utils import report_results, AoCResult, input_for_day

IngredientIds = list[int]
FreshRanges = list[range]
FreshRange = tuple[int, int]

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
DATA: str = input_for_day(5, 2025)


def parse_input(puzzle_input: str) -> tuple[FreshRanges, IngredientIds]:
    """Convert input of str.
    Split on the \n\n, remove any \n from each line.
    Then parse fresh ranges into list of ranges, and
    ingredient ids into a list of ints.

    Args:
        puzzle_input (str): Puzzle input.

    Returns:
        tuple[FreshRanges, IngredientIds]: ranges of fresh ids, fresh ids.
    """
    ranges_str, ingredient_ids_str = [
        x.splitlines() for x in puzzle_input.split('\n\n')
    ]
    ranges: FreshRanges = [
        range(start, end + 1) for start,
        end in (map(int, r.split('-')) for r in ranges_str)
    ]

    ingredient_ids: IngredientIds = list(map(int, ingredient_ids_str))
    return ranges, ingredient_ids


def merge_ranges(ranges: FreshRanges) -> Iterator[FreshRange]:
    """Merge current ranges if overlap in any way.

    Args:
        ranges (FreshRanges): ranges of fresh ids

    Yields:
        Iterator[FreshRange]: merged ranges
    """
    # change ranges back to tuples of the start/stop
    sorted_rngs: Iterator[FreshRange] = iter(
        sorted((x.start, x.stop-1) for x in ranges)
    )
    start, end = next(sorted_rngs)  # get first fresh range

    for s, e in sorted_rngs:
        # if the next interval starts before/at current end
        # they overlap so merge range by getting biggest end
        if s <= end:
            end = max(end, e)
        else:
            # if they dont overlap - start a new fresh range
            # and yield the current one
            yield (start, end)
            start, end = s, e
    yield start, end


def solve_part2(ranges: FreshRanges) -> int:
    """Sum up the merged range lengths

    Args:
        ranges (FreshRanges): fresh id ranges.

    Returns:
        int: sum of lengths of ranges.
    """
    # sum the lengths of each range
    return sum(len(range(x[0], x[1]+1)) for x in merge_ranges(ranges))


def solve_day05(data: Any) -> tuple[int, int]:
    """solve both days - check if an ingredient id is
    in any of the ranges. If so - break and count.

    Then apply solve_part2.

    Args:
        data (Any): Puzzle data.

    Returns:
        tuple[int, int]: part 1 value, part 2 value.
    """
    ranges, ingredient_ids = parse_input(data)
    valid_id: int = 0
    for ingredient in ingredient_ids:
        # THE OLD WAY I DID IT.
        #     for y in ranges:
        #         if x in y:
        #             valid_id += 1
        #             break
        if any(ingredient in r for r in ranges):
            valid_id += 1
    return valid_id, solve_part2(ranges)


@report_results
def solveday(data: Any) -> AoCResult:
    p1, p2 = solve_day05(data)
    return p1, p2


expected_test_results: AoCResult = (3, 14)


def tests(test_input: Any) -> None:
    p1, p2 = solveday(test_input)
    assert (p1, p2) == expected_test_results
    print("☑️ Tests passed!")


if __name__ == "__main__":
    tests(EXAMPLE)
    solveday(DATA)
