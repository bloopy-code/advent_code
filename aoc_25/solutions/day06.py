"""Day 6 - Trash Compactor"""

from math import prod
from typing import List
from utils.aoc_utils import report_results, AoCResult, input_for_day


HomeworkStr = list[list[str]]
HomeworkInt = List[list[str | int]]

EXAMPLE: str = """123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   + """
DATA = input_for_day(6, 2025)


def format_homework(data: str) -> HomeworkStr:
    return [line.split() for line in data.splitlines()]


EXAMPLE_LINES: HomeworkStr = format_homework(EXAMPLE)
DATA_LINES: HomeworkStr = format_homework(DATA)
#print([list(x) for x in EXAMPLE.splitlines()])
# transpose
tmp = [list(x) for x in EXAMPLE.splitlines()]

tmptmp = []
for i in range(len(tmp[0])):
    n: list[int | str] = []
    for row in tmp:
        try:
            n.append(row[i])
        except ValueError:
            n.append(row[i])
    tmptmp.append(n)
for x in tmptmp:
    y = ''.join(x)
    print(y)


def rearrange_homework(data: HomeworkStr) -> HomeworkInt:
    new: HomeworkInt = []
    print(len(data[0]))
    for i in range(len(data[0])):
        n: list[int | str] = []
        for row in data:
            try:
                n.append(int(row[i]))
            except ValueError:
                n.append(row[i])
        new.append(n)
    return new


def calculate_homework(data: HomeworkStr) -> int:
    homework: HomeworkInt = rearrange_homework(data)
    total: int = 0
    for row in homework:
        nums: list[int] = [v for v in row[:-1] if isinstance(v, int)]
        if row[-1] == '+':
            total += sum(nums)
        elif row[-1] == '*':
            total += prod(nums)
    return total


@report_results
def solveday(data: HomeworkStr) -> AoCResult:
    p1: int = calculate_homework(data)
    p2: int = 0
    return p1, p2


expected_test_results: AoCResult = (4277556, 0)


def tests(test_input: HomeworkStr) -> None:
    p1, p2 = solveday(test_input)
    assert (p1, p2) == expected_test_results
    print("☑️ Tests passed!")


if __name__ == "__main__":
    tests(EXAMPLE_LINES)
    #solveday(DATA_LINES)
