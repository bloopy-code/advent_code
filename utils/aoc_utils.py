"""Usefulish helper functions"""
import time
import functools
from pathlib import Path
import json
from typing import Any

AoCResult = tuple[int, int]


def input_for_day(day: int, year: int | None = None, ff: str = "read") -> Any:
    """_summary_

    Args:
        day (int): _description_
        year (int, optional): _description_. Defaults to None.
        ff (str, optional): _description_. Defaults to "read".

    Raises:
        ValueError: _description_
        FileNotFoundError: _description_

    Returns:
        _type_: _description_
    """
    # Guess the year from the folder if not given
    if year is None:
        # Look at the current script's path
        import inspect
        caller_path = Path(inspect.stack()[1].filename)
        # Search for a folder like 'year2015' in the parent directories
        for parent in caller_path.parents:
            if parent.name.startswith("year"):
                try:
                    year = int(parent.name.replace("year", ""))
                    break
                except ValueError:
                    continue
        if year is None:
            raise ValueError("Please specify year manually.")

    if day < 10:
        filename = f"day0{day}.txt"
    else:
        filename = f"day{day}.txt"
    input_path = Path.cwd() / f"aoc_{str(year)[-2:]}" / "inputs" / filename
    print(f"Loading input from: {input_path}")

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    with open(input_path, "r", encoding="utf-8") as f:
        if ff == "read":
            return f.read()
        elif ff == "json":
            return json.load(f)
        else:
            return [line.strip() for line in f.readlines()]
        # return f.read() if ff == "read" else
        # [line.strip() for line in f.readlines()]


def report_results(func):
    """Decorator to time a function and print
    Part 1 and Part 2 results nicely.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        results = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time

        print("\n===== RESULTS =====")
        if isinstance(results, tuple) and len(results) == 2:
            p1, p2 = results
            print(f"PART 1: {p1}")
            print(f"PART 2: {p2}")
        else:
            print(f"Result: {results}")
        print("-------------------")
        print(f"Time Taken: {total_time:.4f} seconds")
        print("===================")

        return results
    return wrapper
