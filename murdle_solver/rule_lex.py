# ------------------------------------------------------------
# rule_lex.py
#
# tokenizer for a simple expression evaluator for rules
# ------------------------------------------------------------
import logging

from ply import lex
from ply.lex import LexToken


# List of token names.   This is always required
tokens = (
    "LPAREN",
    "RPAREN",
    "AND",
    "OR",
    "XOR",
    "NOT",
    "string",
)

# Regular expression rules for simple tokens
t_AND = r"[Aa][Nn][Dd]"
t_OR = r"[Oo][Rr]"
t_XOR = r"[Xx][Oo][Rr]"
t_NOT = r"[Nn][Oo][Tt]"
t_LPAREN = r"\("
t_RPAREN = r"\)"


# A regular expression rule with some action code
def t_string(t: LexToken) -> LexToken:
    r"""["'][^"']+["']"""
    t.value = str(t.value).strip("'\"")
    return t


# A string containing ignored characters (spaces and tabs)
t_ignore = " \t"


# Error handling rule
def t_error(t: LexToken) -> None:
    """Error handling rule"."""
    logging.error("Illegal character '%s'", t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer: lex.Lexer = lex.lex()
