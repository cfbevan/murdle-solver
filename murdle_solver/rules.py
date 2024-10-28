from __future__ import annotations

from typing import Literal

from typing_extensions import TypedDict


class Fact(TypedDict):
    op: Literal["fact"]
    right: list[str]


class UnaryRule(TypedDict):
    op: Literal["not"]
    right: Rule


class BinaryRule(TypedDict):
    op: Literal["and", "or", "xor"]
    left: Rule
    right: Rule


Rule = Fact | UnaryRule | BinaryRule
