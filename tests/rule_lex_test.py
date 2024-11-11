from murdle_solver.rule_lex import lexer


def test_fact() -> None:
    """Test the lexer for a fact."""
    text = '( "a" "b" "*" )'
    lexer.input(text)
    token = lexer.token()
    assert token.type == "LPAREN"
    assert token.value == "("
    token = lexer.token()
    assert token.type == "string"
    assert token.value == "a"
    token = lexer.token()
    assert token.type == "string"
    assert token.value == "b"
    token = lexer.token()
    assert token.type == "string"
    assert token.value == "*"
    token = lexer.token()
    assert token.type == "RPAREN"
    assert token.value == ")"
    assert lexer.token() is None


def test_and() -> None:
    """Test the lexer for an and rule."""
    text = '( AND ("a" "b") ("c" "d") )'
    lexer.input(text)
    token = lexer.token()
    assert token.type == "LPAREN"
    assert token.value == "("
    token = lexer.token()
    assert token.type == "AND"
    assert token.value == "AND"
    token = lexer.token()
    assert token.type == "LPAREN"
    assert token.value == "("
    token = lexer.token()
    assert token.type == "string"
    assert token.value == "a"
    token = lexer.token()
    assert token.type == "string"
    assert token.value == "b"
    token = lexer.token()
    assert token.type == "RPAREN"
    assert token.value == ")"
    token = lexer.token()
    assert token.type == "LPAREN"
    assert token.value == "("
    token = lexer.token()
    assert token.type == "string"
    assert token.value == "c"
    token = lexer.token()
    assert token.type == "string"
    assert token.value == "d"
    token = lexer.token()
    assert token.type == "RPAREN"
    assert token.value == ")"
    token = lexer.token()
    assert token.type == "RPAREN"
    assert token.value == ")"
    assert lexer.token() is None


def test_or() -> None:
    """Test the lexer for an or rule."""
    text = '( OR ("a" "b") ("c" "d") )'
    lexer.input(text)
    token = lexer.token()
    assert token.type == "LPAREN"
    assert token.value == "("
    token = lexer.token()
    assert token.type == "OR"
    assert token.value == "OR"
    token = lexer.token()
    assert token.type == "LPAREN"
    assert token.value == "("
    token = lexer.token()
    assert token.type == "string"
    assert token.value == "a"
    token = lexer.token()
    assert token.type == "string"
    assert token.value == "b"
    token = lexer.token()
    assert token.type == "RPAREN"
    assert token.value == ")"
    token = lexer.token()
    assert token.type == "LPAREN"
    assert token.value == "("
    token = lexer.token()
    assert token.type == "string"
    assert token.value == "c"
    token = lexer.token()
    assert token.type == "string"
    assert token.value == "d"
    token = lexer.token()
    assert token.type == "RPAREN"
    assert token.value == ")"
    token = lexer.token()
    assert token.type == "RPAREN"
    assert token.value == ")"
    assert lexer.token() is None


def test_xor() -> None:
    """Test the lexer for an xor rule."""
    text = '( XOR ("a" "b") ("c" "d") )'
    lexer.input(text)
    token = lexer.token()
    assert token.type == "LPAREN"
    assert token.value == "("
    token = lexer.token()
    assert token.type == "XOR"
    assert token.value == "XOR"
    token = lexer.token()
    assert token.type == "LPAREN"
    assert token.value == "("
    token = lexer.token()
    assert token.type == "string"
    assert token.value == "a"
    token = lexer.token()
    assert token.type == "string"
    assert token.value == "b"
    token = lexer.token()
    assert token.type == "RPAREN"
    assert token.value == ")"
    token = lexer.token()
    assert token.type == "LPAREN"
    assert token.value == "("
    token = lexer.token()
    assert token.type == "string"
    assert token.value == "c"
    token = lexer.token()
    assert token.type == "string"
    assert token.value == "d"
    token = lexer.token()
    assert token.type == "RPAREN"
    assert token.value == ")"
    token = lexer.token()
    assert token.type == "RPAREN"
    assert token.value == ")"
    assert lexer.token() is None


def test_not() -> None:
    """Test the lexer for a not rule."""
    text = '( NOT ("a" "b") )'
    lexer.input(text)
    token = lexer.token()
    assert token.type == "LPAREN"
    assert token.value == "("
    token = lexer.token()
    assert token.type == "NOT"
    assert token.value == "NOT"
    token = lexer.token()
    assert token.type == "LPAREN"
    assert token.value == "("
    token = lexer.token()
    assert token.type == "string"
    assert token.value == "a"
    token = lexer.token()
    assert token.type == "string"
    assert token.value == "b"
    token = lexer.token()
    assert token.type == "RPAREN"
    assert token.value == ")"
    token = lexer.token()
    assert token.type == "RPAREN"
    assert token.value == ")"
    assert lexer.token() is None


def test_error() -> None:
    """Test the lexer for an error."""
    text = "+"
    lexer.input(text)
    token = lexer.token()
    assert token is None
