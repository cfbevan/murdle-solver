from itertools import chain
from itertools import filterfalse
from itertools import product

from more_itertools import chunked


def unique(solution: tuple[tuple[str, ...]]) -> bool:
    """Check if items in sublist are unique.

    Args:
        solution (tuple[tuple[str, ...]]): Set to check.

    Returns:
        bool: True if all sublists contain unique items. False otherwise.
    """
    to_check = list(chain.from_iterable(solution))
    return len(to_check) != len(set(to_check))


def gen_solutions(groups: list[list[str]]) -> list[tuple[tuple[str, ...]]]:
    """Generate solutions.

    Args:
        groups (list[list[str]]): Groups of possible items.

    Returns:
        list[tuple[tuple[str, ...]]]: Solutions.
    """
    p1 = list(product(*groups))
    return list(filterfalse(unique, product(*chunked(p1, int(len(p1) / len(groups))))))
