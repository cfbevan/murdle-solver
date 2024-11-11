from typing import cast

from murdle_solver.rules import BinaryRule
from murdle_solver.rules import Fact
from murdle_solver.rules import Rule
from murdle_solver.rules import UnaryRule
from murdle_solver.solutions import gen_solutions


def solve(rule: Rule, solution: tuple[tuple[str, ...]]) -> bool:
    """Check if given solution matches rule.

    Args:
        rule (Rule): Rule to test.
        solution (tuple[tuple[str, ...]]): Solution to test.

    Returns:
        bool: Boolean value of solution applied to rule.
            True if solution matches rule. False otherwise.
    """
    match rule["op"]:
        case "fact":
            return _fact(cast(Fact, rule), solution)
        case "not":
            return _not(cast(UnaryRule, rule), solution)
        case "and":
            return _and(cast(BinaryRule, rule), solution)
        case "or":
            return _or(cast(BinaryRule, rule), solution)
        case "xor":
            return _xor(cast(BinaryRule, rule), solution)
        case _:
            raise ValueError(f"Unknown operator: {rule['op']}")


def _fact(rule: Fact, solution: tuple[tuple[str, ...]]) -> bool:
    """A fact is a given truth.

    Args:
        rule (Rule): Rule to test.
        solution (tuple[tuple[str, ...]]): Solution to test.

    Returns:
        bool: True if rule fact matches solution.
    """
    return any(all(r == "*" or r == s[i] for i, r in enumerate(rule["right"])) for s in solution)


def _not(rule: UnaryRule, solution: tuple[tuple[str, ...]]) -> bool:
    """Evaluate not Rule.

    Args:
        rule (Rule): Rule to test.
        solution (tuple[tuple[str, ...]]): Solution to test.

    Returns:
        bool: True if not Right.
    """
    return not solve(rule["right"], solution)


def _or(rule: BinaryRule, solution: tuple[tuple[str, ...]]) -> bool:
    """Evaluate or Rule.

    Args:
        rule (Rule): Rule to test.
        solution (tuple[tuple[str, ...]]): Solution to test.

    Returns:
        bool: True if Left OR Right.
    """
    return solve(rule["left"], solution) or solve(rule["right"], solution)


def _and(rule: BinaryRule, solution: tuple[tuple[str, ...]]) -> bool:
    """Evaluate and Rule.

    Args:
        rule (Rule): Rule to test.
        solution (tuple[tuple[str, ...]]): Solution to test.

    Returns:
        bool: True if Left AND Right.
    """
    return solve(rule["left"], solution) and solve(rule["right"], solution)


def _xor(rule: BinaryRule, solution: tuple[tuple[str, ...]]) -> bool:
    """Evaluate and Rule.

    Args:
        rule (Rule): Rule to test.
        solution (tuple[tuple[str, ...]]): Solution to test.

    Returns:
        bool: True if Left AND Right.
    """
    return _or(rule, solution) and not _and(rule, solution)


class Solver:
    def __init__(self, groups: list[list[str]], rules: list[Rule]) -> None:
        """Create solver class.

        Args:
            groups (list[list[str]]): Groups of items to create solutions with.
            rules (list[Rule]): Rules for solutions.
        """
        self.solutions = gen_solutions(groups)
        self.rules = rules

    def solve(self) -> list[tuple[tuple[str, ...]]]:
        """Get possible solutions based on rules.

        Returns:
            list[tuple[tuple[str, ...]]]: All solutions.
        """
        return [
            solution
            for solution in self.solutions
            if all(solve(rule, solution) for rule in self.rules)
        ]
