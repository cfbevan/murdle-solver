import pytest

from murdle_solver.rules import Rule
from murdle_solver.solver import Solver


def test_solver_not() -> None:
    """End to end test of simple solution."""
    groups = [["a", "b"], ["c", "d"]]
    rules: list[Rule] = [
        {
            "op": "not",
            "right": {
                "op": "fact",
                "right": ["a", "c"],
            },
        },
    ]
    assert Solver(groups, rules).solve() == [(("a", "d"), ("b", "c"))]


def test_solver_and() -> None:
    """End to end test of simple solution."""
    groups = [["a", "b"], ["c", "d"]]
    rules: list[Rule] = [
        {
            "op": "and",
            "left": {
                "op": "fact",
                "right": ["b", "d"],
            },
            "right": {
                "op": "fact",
                "right": ["a", "c"],
            },
        },
    ]
    assert Solver(groups, rules).solve() == [(("a", "c"), ("b", "d"))]


def test_solver_or() -> None:
    """End to end test of simple solution."""
    groups = [["a", "b"], ["c", "d"]]
    rules: list[Rule] = [
        {
            "op": "or",
            "left": {
                "op": "fact",
                "right": ["b", "d"],
            },
            "right": {
                "op": "fact",
                "right": ["a", "c"],
            },
        },
    ]
    assert Solver(groups, rules).solve() == [(("a", "c"), ("b", "d"))]


def test_solver_xor() -> None:
    """End to end test of simple solution."""
    groups = [["a", "b"], ["c", "d"]]
    rules: list[Rule] = [
        {
            "op": "xor",
            "left": {
                "op": "fact",
                "right": ["a", "d"],
            },
            "right": {
                "op": "fact",
                "right": ["a", "c"],
            },
        },
    ]
    assert Solver(groups, rules).solve() == [(("a", "c"), ("b", "d")), (("a", "d"), ("b", "c"))]


def test_solver_bad_op() -> None:
    """End to end test of simple solution."""
    groups = [["a", "b"], ["c", "d"]]
    rules = [
        {
            "op": "bad",
            "right": {
                "op": "fact",
                "right": ["a", "c"],
            },
        },
    ]
    with pytest.raises(ValueError, match="Unknown operator: bad"):
        Solver(groups, rules).solve()  # type: ignore[arg-type]
