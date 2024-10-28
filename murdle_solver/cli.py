from io import BytesIO

import click

from murdle_solver.config_loader import load_config
from murdle_solver.solver import Solver


@click.command()
@click.argument("config", type=click.File("rb"))
def solve(config: BytesIO) -> None:
    """Solve a problem stored in a config file."""
    cfg = load_config(config)
    solver = Solver(groups=cfg.groups, rules=cfg.rules)
    click.echo(solver.solve())
