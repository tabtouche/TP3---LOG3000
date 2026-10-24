"""Tests unitaires des fonctions de operators.py."""

import pytest

from operators import add, subtract, multiply, divide


def test_add():
    """add doit retourner la somme des deux nombres."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    """subtract doit retourner a - b (l'ordre des operandes compte)."""
    assert subtract(9, 4) == 5
    assert subtract(4, 9) == -5


def test_multiply():
    """multiply doit retourner le produit a * b."""
    assert multiply(6, 7) == 42
    # 2 * 3 et 2 ** 3 donnent des resultats differents, ce qui permet de les distinguer
    assert multiply(2, 3) == 6


def test_divide():
    """divide doit retourner le quotient reel, pas la division entiere."""
    assert divide(8, 2) == 4
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    """Une division par zero doit lever ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
