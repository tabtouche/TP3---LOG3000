"""Serveur Flask de la calculatrice.

Definit la route principale et la fonction calculate() qui evalue
une expression simple comme "7+3".
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Associe chaque symbole a sa fonction dans operators.py
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """Calcule une expression de la forme "a<op>b".

    Entree : expr (str), ex. "12*4". Les espaces sont ignores.
    Sortie : le resultat (float) de l'operation.
    Leve ValueError si l'expression est vide, mal formee, contient plus
    d'un operateur ou si un operande n'est pas un nombre.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # On continue apres le premier operateur pour detecter s'il y en a un deuxieme
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Affiche la calculatrice et traite le formulaire.

    Entree : en POST, le champ "display" du formulaire (l'expression).
    Sortie : la page index.html rendue avec le resultat, un message
    d'erreur ou une chaine vide (GET).
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            # On affiche l'erreur dans la calculatrice plutot que de renvoyer une erreur 500
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # debug=True seulement pour le developpement local
    app.run(debug=True)
