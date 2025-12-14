"""Day 6 - Trash Compactor"""

from math import prod
import re
from utils.aoc_utils import report_results, AoCResult, input_for_day

# DISCLAIMER - THIS IS SO MESSY AND TYPING IS A MESS
# BUT IT WORKS.

GridSplits = list[list[str]]  # output of format as splits
# e.g. [['123', '343'],['45', '500']]
GridTokens = list[list[str]]  # output of format as lists
# e.g. [['1', '2', '3', ' ', '3', '4', '3'], [...]]
HomeworkInts = list[list[int | str]]  # [[1, 2, '+']]
ColumnsStr = list[list[str]]

EXAMPLE: str = """123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   + """
DATA: str = input_for_day(6, 2025)


def format_homework_as_splits(puzzle_input: str) -> GridSplits:
    """Format homework by splitting on spaces.

    Args:
        puzzle_input (str): Input puzzle grid.

    Returns:
        GridSplits: [['40', '30', '1'], ['10', '20', '3']]
    """
    return [line.split() for line in puzzle_input.splitlines()]


def format_homework_as_lists(puzzle_input: str) -> GridTokens:
    """Format homework; everything is a list!

    Args:
        puzzle_input (str): Input puzzle grid.

    Returns:
        GridTokens: [['4', '0', '3', '0', '1'], ['1', '0', '2', '0', '3']]
    """
    return [list(line) for line in puzzle_input.splitlines()]


def rearrange_homework_ints(data: GridSplits) -> HomeworkInts:
    """Rearrange homework and convert to ints.

    Args:
        data (GridSplits): e.g.  [['40', '30', '1'], ['10', '20', '3']]

    Returns:
        HomeworkInts:  [[40, 10], [30, 20],[1, 3]]
    """
    new: HomeworkInts = []
    for i in range(len(data[0])):
        n: list[int | str] = []
        for row in data:
            try:
                n.append(int(row[i]))
            except ValueError:
                n.append(row[i])
        new.append(n)
    return new


def rearrange_homework_str(data: GridTokens) -> ColumnsStr:
    """Rearrange homework into R-L cols?

    Args:
        data (GridTokens):  [['A', 'B', 'C'], ['1', '2', '3']]

    Returns:
        ColumnsStr: [['A', '1'], ['B', '2'], ['C', '3']... etc]
    """
    new: ColumnsStr = []
    for i in range(len(data[0])):
        col: list[str] = []
        for row in data:
            col.append(row[i])
        new.append(col)
    return new


def add_or_sum(numbers: list[int], operator: str) -> int:
    """Add or sum the numbers provided, depending on operator.

    Args:
        numbers (list[int]): [1, 2, 3]
        operator (str): * or +

    Returns:
        int: result of operation on list.
    """
    if operator == '+':
        return sum(numbers)
    elif operator == '*':
        return prod(numbers)
    else:
        raise ValueError('What operator is that?!')


def calculate_homework(data: str) -> int:
    """PART 1:
    Data comes in as string.
    Gets split into lines and then each line split by space.
    Each string number gets converted to int, and operator should
    be final element in list.

    Then for each row [int, int, int, operator], get the value of
    them sum or prod, add to total.

    Args:
        data (str): puzzle input data.

    Returns:
        int: answer for part 1
    """
    homework: GridSplits = format_homework_as_splits(data)
    int_homework: HomeworkInts = rearrange_homework_ints(homework)
    total: int = 0

    for row in int_homework:
        nums: list[int] = [v for v in row[:-1] if isinstance(v, int)]
        sign = row[-1]
        assert isinstance(sign, str)

        total += add_or_sum(nums, sign)
    return total


def solve_p2(data: str) -> int:
    """PART 2:
    Input data as str, gets split into lines, then each line split
    into a list.
    It then gets rearranged column wise, and seperated whenever
    there's a column of all spaces.
    It ends up as a janky string so then just regex the numbers/operators
    and do the same sum/prod to get total.

    Args:
        data (str): _description_

    Returns:
        int: _description_
    """
    formatted_data: GridTokens = format_homework_as_lists(data)
    max_len: int = max(len(x) for x in formatted_data)

    for grid_row in formatted_data:
        extra: list[str] = [' '] * (max_len - len(grid_row))
        grid_row.extend(extra)

    homework: GridTokens = rearrange_homework_str(formatted_data)
    t2: list[str] = []
    current: list[str] = []

    # col of all spaces seperates 'problems'
    for col in homework:
        if all(c == ' ' for c in col):
            if current:
                t2.append(''.join(current))
                current = []
        else:
            current.append(''.join(col))

    if current:
        t2.append(''.join(current))

    total_p2: int = 0

    for x in t2:
        numbers = list(map(int, re.findall(r'\d+', x)))
        sign = re.findall(r'\*|\+', x)
        total_p2 += add_or_sum(numbers, sign[0])

    return total_p2


@report_results
def solveday(data: str) -> AoCResult:
    p1: int = calculate_homework(data)
    p2: int = solve_p2(data)
    return p1, p2


expected_test_results: AoCResult = (4277556, 3263827)


def tests(test_input: str) -> None:
    p1, p2 = solveday(test_input)
    assert (p1, p2) == expected_test_results
    print("☑️ Tests passed!")


if __name__ == "__main__":
    tests(EXAMPLE)
    solveday(DATA)
