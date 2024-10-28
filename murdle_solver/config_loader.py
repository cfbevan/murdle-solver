from io import BytesIO
from tomllib import load

from pydantic import BaseModel

from murdle_solver.rules import Rule


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
    return Config.model_validate(load(fp))
