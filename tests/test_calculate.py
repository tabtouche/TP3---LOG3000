"""Tests de la fonction calculate() de app.py (analyse de l'expression)."""

import pytest

from app import calculate


@pytest.mark.parametrize("expr, expected", [
    ("7+3", 10.0),
    ("9-4", 5.0),
    ("6*7", 42.0),
    ("8/2", 4.0),
    ("7/2", 3.5),
])
def test_valid_expressions(expr, expected):
    """Chaque operateur doit donner le bon resultat a partir d'une expression texte."""
    assert calculate(expr) == expected


def test_spaces_are_ignored():
    """Les espaces autour de l'operateur ne doivent pas changer le resultat."""
    assert calculate(" 12 + 4 ") == 16.0


@pytest.mark.parametrize("expr", [
    "",          # vide
    "5+",        # operateur a la fin
    "+5",        # operateur au debut
    "42",        # pas d'operateur
    "1+2+3",     # plus d'un operateur
    "a+2",       # operande non numerique
])
def test_invalid_expressions(expr):
    """Une expression mal formee doit lever ValueError."""
    with pytest.raises(ValueError):
        calculate(expr)
