"""Day 2 - Title Goes Here"""

from utils.aoc_utils import input_for_day, report_results


EXAMPLE: list[str] = ["2x3x4", "1x1x10"]
DATA = input_for_day(2, 2015, ff="lists")


def wrapping_paper(dim: str) -> int:
    """Surface area calc for Day 2 -2015

    Args:
        l (int): length
        w (int): width
        h (int): height

    Returns:
        tuple(int, int): surface area,
            smallest side extra wrapping
    """
    length, w, h = parse_dims(dim)
    sqft: int = 2 * length * w + 2 * w * h + 2 * h * length
    smallest_side: int = min([length * w, w * h, h * length])
    return sqft + smallest_side


def ribbon(dim: str) -> int:
    """Ribbon calc.

    Args:
        dim (str): dims length, width, height

    Returns:
        int: ribbon length including bow
    """
    length, w, h = parse_dims(dim)
    shdst: int = 2 * sum(sorted((length, w, h))[:2])
    bow: int = length * w * h
    return shdst + bow


def parse_dims(dims: str) -> map[int]:
    return map(int, dims.split("x"))


@report_results
def solveday(data) -> tuple[int, int]:
    p1: int = sum(wrapping_paper(x) for x in data)
    p2: int = sum(ribbon(x) for x in data)
    return p1, p2


expected_test_results: tuple[int, int] = (58, 34)


def tests(test_input: list) -> None:
    p1, p2 = solveday(test_input)
    assert (p1, p2) == expected_test_results
    print("☑️ Tests passed!")


if __name__ == "__main__":
    tests(EXAMPLE[0:1])
    solveday(DATA)
