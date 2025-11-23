"""Day 9 - Title Goes Here"""
from utils.aoc_utils import input_for_day, report_results


EXAMPLE = []
DATA = input_for_day(9)


def helperfunction(data):
    return False


@report_results
def solveday(data):
    p1 = ''
    p2 = ''
    return p1, p2


expected_test_results = ''


def tests(test_input):
    p1, p2 = solveday(test_input)
    assert (p1, p2) == expected_test_results


if __name__ == "__main__":
    tests(EXAMPLE)
    solveday(DATA)
