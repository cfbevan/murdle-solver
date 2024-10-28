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
                "right": ["a", "*"],
            },
        },
        {
            "op": "fact",
            "right": ["*", "d"],
        },
    ]
    assert Solver(groups, rules).solve() == [["b", "d"]]


def test_solver_and() -> None:
    """End to end test of simple solution."""
    groups = [["a", "b"], ["c", "d"]]
    rules: list[Rule] = [
        {
            "op": "and",
            "left": {
                "op": "fact",
                "right": ["*", "d"],
            },
            "right": {
                "op": "fact",
                "right": ["a", "*"],
            },
        },
    ]
    assert Solver(groups, rules).solve() == [["a", "d"]]


def test_solver_or() -> None:
    """End to end test of simple solution."""
    groups = [["a", "b"], ["c", "d"]]
    rules: list[Rule] = [
        {
            "op": "or",
            "left": {
                "op": "fact",
                "right": ["*", "d"],
            },
            "right": {
                "op": "fact",
                "right": ["a", "*"],
            },
        },
    ]
    assert Solver(groups, rules).solve() == [
        ["a", "c"],
        ["a", "d"],
        ["b", "d"],
    ]


def test_solver_xor() -> None:
    """End to end test of simple solution."""
    groups = [["a", "b"], ["c", "d"]]
    rules: list[Rule] = [
        {
            "op": "xor",
            "left": {
                "op": "fact",
                "right": ["*", "d"],
            },
            "right": {
                "op": "fact",
                "right": ["a", "*"],
            },
        },
    ]
    assert Solver(groups, rules).solve() == [
        ["a", "c"],
        ["b", "d"],
    ]
