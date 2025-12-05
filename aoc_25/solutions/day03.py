"""Day 3 - Title Goes Here"""

from typing import Any
from utils.aoc_utils import report_results,input_for_day, AoCResult
from rich.progress import track

# Custom typing - can I have a medal for Best Lil Coder? ⭐
# Could I use 'Iterable'? yes. Am I going to? Not today!
# (Please don't take away my star)
ListsOfBatteryLists = list[list[int]]

# I gotta practise on the examples given because the brain cells need warming up.
EXAMPLE_LISTS: list[str] = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111"
]
INPUT_DATA: list[str] = input_for_day(3, 2025, ff='list')

# Hmm, actually I think I want a list of lists... who doesn't?
DATA: ListsOfBatteryLists = [list(map(int, list(x))) for x in INPUT_DATA]
EXAMPLE: ListsOfBatteryLists = [list(map(int, list(x))) for x in EXAMPLE_LISTS]


def part1(data: ListsOfBatteryLists) -> int:
    """Part 1 - Find highest two batteries. No re-ordering!

    Args:
        data (ListsOfBatteryLists): Lists of battery lists...

    Returns:
        int: Total joltage ⚡
    """
    p1_total_joltage: int = 0

    for x in track(data):
        # Keep track of the highest 2 batteries we find.
        current_highest: int = 0

        # Gotta sliiiide through that list like you're sliding into some DMs ;)
        for i in range(len(x)-1):
            first_battery: int = x[i]
            the_rest: list[int] = x[i+1:]  # the rest of the battery gang, yadayada

            biggest_of_the_rest: int = max(the_rest)  # Bigger IS better.

            # it dawned on me here, that I could have just done some list joining.
            # but I like to be faced with my mistakes to remind me of my humble roots
            # and so I can laugh at myself in a years time.
            new_num: int = int(str(first_battery) + str(biggest_of_the_rest))

            if new_num > current_highest:
                current_highest: int = new_num  # HIGHER AND HIIIIGHER!

        p1_total_joltage += current_highest
    return p1_total_joltage


# There's probably some duplication here and I could have smooshed them into
# one function but it's almost 10pm. Don't make me smoosh.
def part2(data: ListsOfBatteryLists) -> int:
    """Part 2 - find the highest 12 battery joltage!

    Args:
        data (ListsOfBatteryLists): list containing the battery gang

    Returns:
        int: part 2 joltage ⚡⚡
    """
    total_p2_joltage: int = 0

    for x in track(data):
        start_idx: int = 0
        biggest_batteries: list = []  # what have they been eating?!
        batteries_needed: int = 12

        while batteries_needed > 0:
            # I figure, if you need 12 batteries, there's only so far fwd you can go in a battery
            # and still get 12? So you gotta work out where the first block 'ends'?
            first_block_len: int = len(x) - batteries_needed

            # peep the catchy as heck, short, descriptive, easy to remember variable names ...
            highest_num_first_block: int = max(x[start_idx:first_block_len+1])
            biggest_batteries.append(highest_num_first_block)
            highest_num_idx: int = x.index(highest_num_first_block, start_idx, first_block_len+1)
            start_idx = highest_num_idx+1
            batteries_needed -= 1  # YEET 🔋

        highest: str = ''.join(list(map(str, biggest_batteries)))  # bigger, better, stronger.
        total_p2_joltage += int(highest)
    return total_p2_joltage


@report_results
def solveday(data: ListsOfBatteryLists) -> AoCResult:
    """Solve the Day!

    Args:
        data (ListsOfBatteryLists): Input Battery info

    Returns:
        AoCResult: p1, p2 aoc numbers
    """
    p1: int = part1(data)
    p2: int = part2(data)
    return p1, p2


# high expectations. It's not 'mad' its just 'disappointed'
expected_test_results: AoCResult = (357, 3121910778619)


def tests(test_input: Any) -> None:
    """Run code on example inputs given.
    Assert for correct answer.

    Args:
        test_input (Any): Example inputs.
    """
    p1, p2 = solveday(test_input)
    assert (p1, p2) == expected_test_results
    print("☑️ Tests passed!")


if __name__ == "__main__":
    tests(EXAMPLE)
    solveday(DATA)
