from murdle_solver.solutions import Solutions


def test_solutions_even() -> None:
    """Test the solutions generation."""
    groups = [["a", "b"], ["c", "d"]]
    assert list(Solutions(groups)) == [
        ["a", "c"],
        ["a", "d"],
        ["b", "c"],
        ["b", "d"],
    ]


def test_solutions_uneven() -> None:
    """Test the solutions generation."""
    groups = [["x", "y"], ["a", "b", "z"], ["c", "d"]]
    assert list(Solutions(groups)) == [
        ["x", "a", "c"],
        ["x", "a", "d"],
        ["x", "b", "c"],
        ["x", "b", "d"],
        ["x", "z", "c"],
        ["x", "z", "d"],
        ["y", "a", "c"],
        ["y", "a", "d"],
        ["y", "b", "c"],
        ["y", "b", "d"],
        ["y", "z", "c"],
        ["y", "z", "d"],
    ]
