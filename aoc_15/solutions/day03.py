"""Day 3 - Perfectly Spherical Houses in a Vacuum"""

from itertools import accumulate, batched
from utils.aoc_utils import input_for_day, report_results, AoCResult

Coord = tuple[int, int]

EXAMPLE: list[str] = [">", "^>v<", "^v^v^v^v^v"]
DATA: str = input_for_day(3, 2015)


def move(a: Coord, b: Coord) -> Coord:
    return (a[0] + b[0], a[1] + b[1])


move_map: dict[str, Coord] = {"^": (0, 1), ">": (1, 0), "<": (-1, 0), "v": (0, -1)}


@report_results
def solveday(data: str) -> AoCResult:
    movements = (move_map[x] for x in data)
    p1: int = len(set(accumulate(movements, move, initial=(0, 0))))

    # inefficient/repeated but meh
    movements = (move_map[x] for x in data)
    santa, robo = zip(*list(batched(movements, 2)))
    santas_moves = accumulate(santa, move, initial=(0, 0))
    robo_moves = accumulate(robo, move, initial=(0, 0))
    p2: int = len(set(list(santas_moves) + list(robo_moves)))
    return p1, p2


expected_test_results: AoCResult = (2, 11)


def tests(test_input: str) -> None:
    p1, p2 = solveday(test_input)
    assert (p1, p2) == expected_test_results
    print("☑️ Tests passed!")


if __name__ == "__main__":
    tests(EXAMPLE[-1])
    solveday(DATA)
