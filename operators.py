"""Operations arithmetiques utilisees par app.py.

Pour chaque fonction, a est l'operande de gauche et b celui de droite.
"""

def add(a,b):
    """Retourne la somme a + b.

    Entrees : a, b (float). Sortie : float.
    """
    return a + b

def subtract(a,b):
    """Retourne la difference a - b.

    Entrees : a, b (float). Sortie : float.
    """
    return b - a

def multiply(a,b):
    """Retourne le produit a * b.

    Entrees : a, b (float). Sortie : float.
    """
    return a * b

def divide(a,b):
    """Retourne le quotient a / b.

    Entrees : a, b (float). Sortie : float.
    Leve ZeroDivisionError si b vaut 0.
    """
    return a / b
