"""Day 5 - Doesn't He Have Intern-Elves For This?"""

import re
from typing import Any
from rich.progress import track
from utils.aoc_utils import input_for_day, report_results, AoCResult


EXAMPLE1: list[tuple[str, str]] = [
    ("ugknbfddgicrmopn", "nice"),
    ("aaa", "nice"),
    ("jchzalrnumimnmhp", "naughty"),
    ("haegwjzuvuyypxyu", "naughty"),
    ("dvszwmarrgswjxmb", "naughty"),
]

EXAMPLE2: list[tuple[str, str]] = [
    ("qjhvhtzxzqqjkmpb", "nice"),
    ("xxyxx", "nice"),
    ("uurcxstgmygtbstg", "naughty"),
    ("ieodomkazucvgmuy", "naughty"),
]

DATA = input_for_day(5, 2015, ff="lines")
DATA = [x.strip() for x in DATA]


# PART 1 RULES
def three_vowels(key: str) -> bool:
    return len(re.findall(r"[aeiou]", key)) >= 3


def one_letter_twice(key: str) -> bool:
    return bool(re.search(r"([a-zA-Z])\1", key))


def no_combos(key: str) -> bool:
    bad_combos = ("ab", "cd", "pq", "xy")
    return not any(bad in key for bad in bad_combos)


# PART 2 RULES
def one_letter_twice_no_overlap(key: str) -> bool:
    return bool(re.search(r"(..).*\1", key))


def has_repeat_with_one_between(key: str) -> bool:
    return bool(re.search(r"(.).\1", key))


def check_alpha(key: str) -> None:
    if not key.isalpha():
        raise ValueError(f"Key contains non-alphabetic characters: {key}")


RULES_P1 = [three_vowels, one_letter_twice, no_combos]
RULES_P2 = [one_letter_twice_no_overlap, has_repeat_with_one_between]


def check_rules(key: str, rules: list) -> str:
    check_alpha(key)

    if all(rule(key) for rule in rules):
        return "nice"
    else:
        return "naughty"


@report_results
def solveday(data: Any) -> AoCResult:
    p1: int = sum(1 for key in data if check_rules(key, RULES_P1) == "nice")
    p2: int = sum(1 for key in data if check_rules(key, RULES_P2) == "nice")
    return p1, p2


expected_test_results: AoCResult = (0, 0)


def tests() -> None:
    """Run example tests for both parts using the labelled examples."""
    print("Running Part 1 example tests...")
    for key, expected in track(EXAMPLE1, description="P1 examples"):
        result = check_rules(key, RULES_P1)
        print(f"Key: {key} | Result: {result} | Expected: {expected}")
        assert result == expected
    print("✅ All Part 1 example tests passed\n")

    print("Running Part 2 example tests...")
    for key, expected in track(EXAMPLE2, description="P2 examples"):
        result = check_rules(key, RULES_P2)
        print(f"Key: {key} | Result: {result} | Expected: {expected}")
        assert result == expected
    print("✅ All Part 2 example tests passed\n")


if __name__ == "__main__":
    tests()
    solveday(DATA)
