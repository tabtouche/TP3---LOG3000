# Flask Calculator

**Équipe 9** — Sarah Tabti, Tidiane Cissé, Yacine Makhlouf

## Description

Calculatrice web simple faite en Python avec Flask. L'utilisateur entre une expression avec deux nombres et un opérateur (par exemple `7+3`) à l'aide des boutons. L'expression est envoyée au serveur, qui calcule le résultat et l'affiche dans la page.

Les opérations supportées sont l'addition, la soustraction, la multiplication et la division. Une seule opération est permise à la fois (pas de `1+2+3`, pas de parenthèses ni de nombres négatifs). Si l'expression est invalide, un message `Error: ...` est affiché.

## Structure du projet

```
app.py           serveur Flask et fonction calculate()
operators.py     fonctions add, subtract, multiply, divide
templates/       page HTML (voir templates/README.md)
static/          fichier CSS (voir static/README.md)
```

- `app.py` crée l'application Flask et définit la route `/`. En GET, elle affiche la page. En POST, elle récupère l'expression du formulaire, la passe à `calculate()` et renvoie la page avec le résultat. `calculate()` sépare l'expression autour de l'opérateur, convertit les deux côtés en nombres et appelle la bonne fonction de `operators.py`.
- `operators.py` contient une fonction par opération. Chacune prend deux nombres `a` et `b` (gauche et droite).

## Prérequis

- Python 3.8 ou plus récent
- pip
- Git

## Installation

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/tabtouche/TP3---LOG3000.git
   cd TP3---LOG3000
   ```

2. (Optionnel) Créer un environnement virtuel :
   ```bash
   python -m venv .venv
   .venv\Scripts\activate        # Windows
   source .venv/bin/activate     # macOS / Linux
   ```

3. Installer Flask et pytest :
   ```bash
   pip install flask pytest
   ```

## Utilisation

Lancer le serveur depuis la racine du projet :

```bash
python app.py
```

Ouvrir ensuite http://127.0.0.1:5000 dans un navigateur. `Ctrl+C` arrête le serveur.

Pour faire un calcul :

1. Cliquer sur les chiffres du premier nombre.
2. Cliquer sur un opérateur (`+`, `-`, `*`, `/`).
3. Cliquer sur les chiffres du deuxième nombre.
4. Cliquer sur `=` pour obtenir le résultat.
5. Cliquer sur `C` pour effacer l'écran.

Par exemple, `7+3` devrait afficher `10.0` et `8/2` devrait afficher `4.0`. Les résultats sont affichés en décimal parce que les nombres sont convertis en `float`.

## Tests

Les tests sont dans le dossier `tests/` et utilisent pytest. Le fichier `tests/README.md` explique ce qu'ils couvrent.

Pour lancer tous les tests depuis la racine du projet :

```bash
python -m pytest
```

On utilise `python -m pytest` plutôt que `pytest` pour que les tests puissent importer `app.py` et `operators.py`. On peut ajouter `-v` pour voir le résultat de chaque test, ou donner le chemin d'un fichier pour lancer seulement ce fichier.

## Contribution

On ne pousse jamais directement sur `main`.

1. **Issue** : chaque bogue ou nouvelle fonctionnalité a une issue GitHub. Pour un bogue, on y met la description, les étapes pour le reproduire (ou le test qui échoue) et le résultat attendu. L'issue est assignée à un membre de l'équipe.
2. **Branche** : on crée une branche à partir de `main` pour chaque issue, nommée `fix/<numéro>-<description>`, par exemple `fix/2-division`.
3. **Commits** : les messages expliquent ce qui a été changé et pourquoi, et mentionnent l'issue (`Fixes #2`). On lance les tests avant de pousser.
4. **Pull Request** : on ouvre une PR vers `main` qui référence l'issue. Un autre membre de l'équipe la relit avant de la fusionner, puis on supprime la branche.
