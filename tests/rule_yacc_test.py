from murdle_solver.rule_yacc import parser


def test_fact() -> None:
    """Test the parser for a fact."""
    text = '( "a" "b" "*" )'
    result = parser.parse(text)
    assert result == {"op": "fact", "right": ["a", "b", "*"]}


def test_and() -> None:
    """Test the parser for an and rule."""
    text = '( AND ("a" "b") ("c" "d") )'
    result = parser.parse(text)
    assert result == {
        "op": "and",
        "left": {"op": "fact", "right": ["a", "b"]},
        "right": {"op": "fact", "right": ["c", "d"]},
    }


def test_or() -> None:
    """Test the parser for an or rule."""
    text = '( OR ("a" "b") ("c" "d") )'
    result = parser.parse(text)
    assert result == {
        "op": "or",
        "left": {"op": "fact", "right": ["a", "b"]},
        "right": {"op": "fact", "right": ["c", "d"]},
    }


def test_xor() -> None:
    """Test the parser for an xor rule."""
    text = '( XOR ("a" "b") ("c" "d") )'
    result = parser.parse(text)
    assert result == {
        "op": "xor",
        "left": {"op": "fact", "right": ["a", "b"]},
        "right": {"op": "fact", "right": ["c", "d"]},
    }


def test_not() -> None:
    """Test the parser for a not rule."""
    text = '( NOT ("a" "b") )'
    result = parser.parse(text)
    assert result == {"op": "not", "right": {"op": "fact", "right": ["a", "b"]}}


def test_nested() -> None:
    """Test the parser for a nested rule."""
    text = '( AND ("a" "b") ( OR ("c" "d") ("e" "f") ) )'
    result = parser.parse(text)
    assert result == {
        "op": "and",
        "left": {"op": "fact", "right": ["a", "b"]},
        "right": {
            "op": "or",
            "left": {"op": "fact", "right": ["c", "d"]},
            "right": {"op": "fact", "right": ["e", "f"]},
        },
    }


def test_error() -> None:
    """Test the parser for a syntax error."""
    text = '( AND ("a" "b") ( OR ("c" "d") ("e" "f") )'
    result = parser.parse(text)
    assert result is None
