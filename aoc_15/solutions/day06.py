"""Day 6 - Probably a Fire Hazard"""

from collections.abc import Callable
import re
from typing import Any
from utils.aoc_utils import input_for_day, report_results, AoCResult

# custom typing
Commands = tuple[str, str, str]
OpFunc = Callable[[int], int]
StateMapping = dict[str, OpFunc]
GridResult = list[list[int]]


EXAMPLE: list[str] = [
    "turn on 0,0 through 999,999",
    "toggle 0,0 through 999,0",
    "turn off 499,499 through 500,500",
]

DATA: list[str] = input_for_day(6, 2015, ff="lists")


x: int = 1000
y: int = 1000

initial_grid: list[list[int]] = [[0 for _ in range(x)] for _ in range(y)]

state_operations: StateMapping = {
    "turn on": lambda _: 1,
    "turn off": lambda _: 0,
    "toggle": lambda v: 1 - v,
}

state_operations2: StateMapping = {
    "turn on": lambda v: v + 1,
    "turn off": lambda v: max(0, v - 1),
    "toggle": lambda v: v + 2,
}


def parse_commands(input_data: list[str]) -> list[Commands]:
    pattern = r"(turn on|turn off|toggle) (\d+,\d+) through (\d+,\d+)"
    commands: list[tuple[str, str, str]] = []

    for line in input_data:
        m = re.match(pattern, line)
        if m is None:
            raise ValueError(f"Invalid command: {line!r}")
        op, start, end = m.groups()
        commands.append((op, start, end))

    return commands


def light_count(grid):
    rows = [x.count(1) for x in grid]
    return sum(rows)


def apply_command(grid, commands, ops):
    for command, start, end in commands:
        operation = ops.get(command)
        if not operation:
            raise ValueError(f"Unknown command: {command}")

        x1, y1 = list(map(int, start.split(",")))
        x2, y2 = list(map(int, end.split(",")))

        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                grid[y][x] = operation(grid[y][x])

    return grid


@report_results
def solveday(data: Any, label: str = "TEST") -> AoCResult:
    print(f"=== Solving {label} ===")

    commands: list[Commands] = parse_commands(data)

    # Part 1
    tmp_grid1: GridResult = [[0 for _ in range(x)] for _ in range(y)]
    grid1: GridResult = apply_command(tmp_grid1, commands, state_operations)
    p1: int = light_count(grid1)

    # Part 2
    tmp_grid2: GridResult = [[0 for _ in range(x)] for _ in range(y)]
    grid2: GridResult = apply_command(tmp_grid2, commands, state_operations2)
    p2: int = sum(sum(row) for row in grid2)

    return p1, p2


expected_test_results: AoCResult = (998996, 1001996)


def tests(test_input: list[str]) -> None:
    p1, p2 = solveday(test_input, label="EXAMPLE")
    assert (p1, p2) == expected_test_results
    print("☑️ Tests passed!")


if __name__ == "__main__":
    tests(EXAMPLE)
    solveday(DATA, "REAL")
