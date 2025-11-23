from __future__ import annotations

import argparse
from pathlib import Path

TEMPLATE_CODE = '''\
"""Day {day} - Title Goes Here"""
from utils.aoc_utils import input_for_day, report_results


EXAMPLE = []
DATA = input_for_day({day})


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
'''

TEMPLATE_INPUT = "PLACEHOLDER INPUT"


def create_day(year: int, day: int, root: Path | None = None) -> None:
    """
    Create a code + input file for a given year/day.

    Directory layout (relative to project root):
        aoc_YY/
            solutions/dayDD.py
            inputs/dayDD.txt
    """
    if root is None:
        # Assume this file lives in AdventCode/utils/
        root = Path(__file__).resolve().parent.parent

    year_suffix = year % 100
    year_dir = root / f"aoc_{year_suffix:02d}"
    code_dir = year_dir / "solutions"
    input_dir = year_dir / "inputs"

    # Ensure directories exist
    code_dir.mkdir(parents=True, exist_ok=True)
    input_dir.mkdir(parents=True, exist_ok=True)

    # Zero-padded day, e.g. 01, 02, ..., 25
    day_str = f"{day:02d}"

    code_file = code_dir / f"day{day_str}.py"
    input_file = input_dir / f"day{day_str}.txt"

    if not code_file.exists():
        code_file.write_text(TEMPLATE_CODE.format(day=day, year=year), encoding="utf-8")
        print(f"Created {code_file}")
    else:
        print(f"Code file {code_file} already exists, skipping.")

    if not input_file.exists():
        input_file.write_text(TEMPLATE_INPUT, encoding="utf-8")
        print(f"Created {input_file}")
    else:
        print(f"Input file {input_file} already exists, skipping.")


def create_days(year: int, days: list[int] | range) -> None:
    for day in days:
        create_day(year, day)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create Advent of Code day template files (code + input).",
    )
    parser.add_argument(
        "year",
        type=int,
        help="Full year, e.g. 2015, 2024.",
    )
    parser.add_argument(
        "day",
        type=int,
        help="Start day (1–25).",
    )
    parser.add_argument(
        "end_day",
        type=int,
        nargs="?",
        help=(
            "Optional end day (1–25, inclusive)."
            "If given, all days from day..end_day are created."
        ),
    )

    args = parser.parse_args()

    # Basic validation
    if not (1 <= args.day <= 25):
        parser.error("day must be between 1 and 25.")
    if args.end_day is not None:
        if not (1 <= args.end_day <= 25):
            parser.error("end_day must be between 1 and 25.")
        if args.end_day < args.day:
            parser.error("end_day must be >= day.")

    return args


if __name__ == "__main__":
    args = parse_args()

    if args.end_day is not None:
        create_days(args.year, range(args.day, args.end_day + 1))
    else:
        create_day(args.year, args.day)
