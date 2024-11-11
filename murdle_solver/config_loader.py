from io import BytesIO
from tomllib import load

from pydantic import BaseModel

from murdle_solver.rule_yacc import parser
from murdle_solver.rules import Rule


class ConfigInput(BaseModel):
    groups: list[list[str]]
    rules: list[str]


class Config(BaseModel):
    groups: list[list[str]]
    rules: list[Rule]


def load_config(fp: BytesIO) -> Config:
    """Read a config file.

    Args:
        fp (BytesIO): File to read.

    Returns:
        Config: Parsed config.
    """
    cfgin = ConfigInput.model_validate(load(fp))
    return Config(
        groups=cfgin.groups,
        rules=[parser.parse(rule) for rule in cfgin.rules],
    )
