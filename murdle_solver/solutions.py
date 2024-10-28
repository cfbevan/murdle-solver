from collections.abc import Iterator


class Solutions:
    def __init__(self, groups: list[list[str]]) -> None:
        """Create a solution set.

        Args:
            groups (dict[str, list[str]]): Groups of possible answers.
        """
        self._groups = groups
        self._max = [len(x) - 1 for x in groups]
        self._current: list[int] | None = None

    def str_sol(self, solution: list[int]) -> list[str]:
        """Convert a solution int to a string solution.

        Args:
            solution (list[int]): Solution to convert.

        Returns:
            list[str]: Converted solution.
        """
        return [self._groups[group][value] for group, value in enumerate(solution)]

    def __iter__(self) -> Iterator[list[str]]:
        """Create iterator.

        Returns:
            iter: Iterator
        """
        return self

    def __next__(self) -> list[str]:
        """Generate next possible solution.

        Raises:
            StopIteration: No more solutions.

        Returns:
            list[str]: Possible solution.
        """
        if self._current is None:
            self._current = [0 for x in self._groups]
        elif self._current == self._max:
            raise StopIteration
        else:
            # increment count
            self._current[-1] = (self._current[-1] + 1) % (self._max[-1] + 1)
            # carry overflow if needed
            i = -1
            while abs(i) < len(self._current) and self._current[i] == 0:
                self._current[i - 1] = (self._current[i - 1] + 1) % (self._max[i - 1] + 1)
                i = i - 1
        return self.str_sol(self._current)
