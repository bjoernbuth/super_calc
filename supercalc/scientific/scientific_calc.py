"""This module contains the code for the scientific calculator:
- sin
- cos
- tan
- log
- sqrt
"""

import click
import math

# import supercalc
from supercalc.simple.simple_calc import (add, mult, div, exp, mod)


@click.group()
def cli():
    pass


@cli.command()
@click.option('--rad', '-r', 'mode', flag_value='rad', default=True, help='Calculate sin in radians (default mode)')
@click.option('--deg', '-d', 'mode', flag_value='deg', help='Calculate sin in degrees')
@click.argument("value", type=float)
def sin(value, mode):
    """Calculate sine of a number."""
    if mode == 'deg':
        result = math.sin(math.radians(value))
    else:
        result = math.sin(value)
    click.echo(f"Result: {result}")

@cli.command()
@click.argument("x", type=float)
def cos(x):
    """Calculate cosine of x"""
    result = math.cos(x)
    click.echo(f"Cosine: {result}")



def tan(x):
    """Calculate tangent of x"""
    try:
        result = math.tan(x)
        return result
    except ZeroDivisionError:
        print(
            "Error in tan calculatation: Cannot calculate tangent of a multiple of 90 degrees"
        )



@cli.command(name='tan')
@click.argument("x", type=float)
def tan_decorated(x):
    """Calculate tangent of x"""
    try:
        result = tan(x)
        click.echo(f"Tangent: {result}")
    except ZeroDivisionError:
        click.echo(
            "Error: Cannot calculate tangent of a multiple of 90 degrees"
        )


@cli.command()
@click.argument("x", type=float)
def log(x):
    """Calculate natural logarithm of x"""
    try:
        result = math.log(x)
        click.echo(f"Natural Logarithm: {result}")
    except ValueError:
        click.echo(
            "Error: Cannot calculate logarithm of a non-positive number"
        )


@cli.command()
@click.argument("x", type=float)
def sqrt(x):
    """Calculate square root of x"""
    try:
        result = math.sqrt(x)
        click.echo(f"Square Root: {result}")
    except ValueError:
        click.echo("Error: Cannot calculate square root of a negative number")


if __name__ == "__main__":
    cli()
