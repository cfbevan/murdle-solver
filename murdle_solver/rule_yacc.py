import logging
from typing import Any

from ply import yacc

from murdle_solver.rule_lex import tokens  # noqa: F401


def p_op_and(p: list[Any]) -> None:
    "op : LPAREN AND op op RPAREN"
    p[0] = {"op": "and", "left": p[3], "right": p[4]}


def p_op_or(p: list[Any]) -> None:
    "op : LPAREN OR op op RPAREN"
    p[0] = {"op": "or", "left": p[3], "right": p[4]}


def p_op_xor(p: list[Any]) -> None:
    "op : LPAREN XOR op op RPAREN"
    p[0] = {"op": "xor", "left": p[3], "right": p[4]}


def p_op_not(p: list[Any]) -> None:
    "op : LPAREN NOT op RPAREN"
    p[0] = {"op": "not", "right": p[3]}


def p_op_fact(p: list[Any]) -> None:
    "op : LPAREN strings RPAREN"
    p[0] = {"op": "fact", "right": p[2]}


def p_strings_single(p: list[Any]) -> None:
    "strings : string"
    p[0] = [p[1]]


def p_strings_multiple(p: list[Any]) -> None:
    "strings : strings string"
    p[1].append(p[2])
    p[0] = p[1]


# Error rule for syntax errors
def p_error(p: list[Any]) -> None:  # noqa: ARG001
    logging.error("Syntax error in input!")


# Build the parser
parser: yacc = yacc.yacc(debug=False)
