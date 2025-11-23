"""Day 4 - The Ideal Stocking Stuffer"""

import hashlib
import multiprocessing
from dataclasses import dataclass
from typing import Any

from tqdm import tqdm
from utils.aoc_utils import AoCResult, input_for_day, report_results


@dataclass(frozen=True)
class Example:
    key: str
    part1: int


EXAMPLES: list[Example] = [
    Example(key="abcdef", part1=609043),
    Example(key="pqrstuv", part1=1048970),
]

DATA: str = input_for_day(4, 2015, ff="read").strip()


def _hash_key(key: str, number: int) -> str:
    to_hash = f"{key}{number}"
    return hashlib.md5(to_hash.encode()).hexdigest()


def _worker(task: tuple[str, str, int, int]) -> int | None:
    """Worker for multiprocessing pool.

    Args:
        task: (key, prefix, start, stop)

    Returns:
        First matching number in [start, stop], or None if not found.
    """
    key, prefix, start, stop = task
    for i in range(start, stop + 1):
        if _hash_key(key, i).startswith(prefix):
            return i
    return None


def find_lowest_number(
    key: str,
    prefix: str,
    batch_size: int = 50_000,
    processes: int = 5,
) -> int:
    """Find the smallest integer n such that md5(key + n) starts with prefix."""
    with multiprocessing.Pool(processes=processes) as pool:
        next_start = 0

        desc = f"Searching {key!r} for prefix {prefix!r}"
        with tqdm(desc=desc, unit="batch") as pbar:
            while True:
                tasks: list[tuple[str, str, int, int]] = []
                for worker_id in range(processes):
                    start = next_start + worker_id * batch_size
                    stop = start + batch_size - 1
                    tasks.append((key, prefix, start, stop))

                results = pool.map(_worker, tasks)

                for result in results:
                    if result is not None:
                        return result

                next_start += processes * batch_size
                pbar.update(1)


@report_results
def solveday(data: Any) -> AoCResult:
    """Solve Day 4 for a given secret key string."""
    if not isinstance(data, str):
        raise TypeError(f"Expected data to be str (the key), got {type(data)!r}")

    key = data.strip()

    # Part 1: starts with "00000"
    part1 = find_lowest_number(key, "00000")

    # Part 2: starts with "000000"
    part2 = find_lowest_number(key, "000000")

    return part1, part2


def tests() -> None:
    """Run example tests for part 1 using the known examples."""
    for i, example in enumerate(EXAMPLES, start=1):
        p1, _ = solveday(example.key)
        assert p1 == example.part1, (
            f"Example {i} failed: expected part1={example.part1}, got {p1}"
        )
        print(f"✅ Example {i} passed (key={example.key!r}, part1={p1})")

    print("☑️ All example tests passed!")


if __name__ == "__main__":
    multiprocessing.freeze_support()  # needed on Windows for multiprocessing

    tests()
    solveday(DATA)
