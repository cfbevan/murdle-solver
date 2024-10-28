# Murdle Solver

Solve Murdle like puzzles.

## Usage

Install program

```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

Create config file (see below).

Run config file

```
python3 -m murdle_solver config.toml
```

## Config Files

A config file contains two main sections `groups` and `rules`.

Example

```toml
groups = [["a", "b"], ["c", "d"]]

[[rules]]
op = "not"

[rules.right]
op = "fact"
right = ["a", "*"]

[[rules]]
op = "fact"
right = ["*", "d"]
```

### Groups

This section represents items that can be parts of a solution.

The following config:

```toml
groups = [["a", "b"], ["c", "d"], ["e", "f"]]
```

will produce solutions

```
["a", "c", "e"]
["a", "c", "f"]
["a", "d", "e"]
["a", "d", "f"]
["b", "c", "e"]
["b", "c", "f"]
["b", "d", "e"]
["b", "d", "f"]
```

## Rules

Rules filter down the generated solutions to "correct" solutions. Supported rule operations are `fact`, `not`, `and`, `or`, and `xor`. These need to be translated from the hints given in a puzzle.

### Examples

The following examples use the following groups.

```toml
groups = [
    ["person1", "person2", "person3"],
    ["weapon1", "weapon2", "weapon3"],
    ["place1", "place2", "place3"]
]
```

**person2 brought weapon1**

```toml
[[rules]]
op="fact"
right = ["person2", "weapon1", "*"]
```

**person1 was at place2**

```toml
[[rules]]
op="fact"
right = ["person2", "*", "place2"]
```

**nobody put weapon1 at place3**

```toml
[[rules]]
op = "not"

[rules.right]
op = "fact"
right = ["*", "weapon1", "place3"]
```

***person1 admired the person who brought weapon2**

```toml
[[rules]]
op = "not"

[rules.right]
op = "fact"
right = ["person1", "weapon2", "*"]
```

**either person1 brought weapon2 or weapon2 was at place1**

```toml
[[rules]]
op = "xor"

[rules.left]
op = "fact"
right = ["person1", "weapon2", "*"]

[rules.right]
op = "fact"
right = ["*", "weapon2", "place1"]
```

## Development

This project uses `poetry` for development. Development is being done using `python3.13`.

Setup

```
poetry env use 3.13
poetry install
pre-commit install --install-hooks
```

This project uses `pre-commit` and `poe` to run tests and checks.

- `poe test` - run ruff and pytest
- `poe cli` - run the cli locally
