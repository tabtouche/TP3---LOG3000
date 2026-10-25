# tests/

## Raison d'être

Contient les tests automatisés du projet, écrits avec pytest. Ils servent à vérifier que les calculs sont corrects et que l'application web répond comme prévu.

## Fichiers

- `test_operators.py` : teste chaque fonction de `operators.py` (addition, soustraction, multiplication, division, division par zéro).
- `test_calculate.py` : teste `calculate()` de `app.py` avec des expressions valides (un cas par opérateur, espaces) et invalides (vide, opérateur au début ou à la fin, aucun opérateur, plusieurs opérateurs, opérande non numérique).
- `test_app.py` : teste la route `/` avec le client de test de Flask (affichage de la page, résultat après un POST, message d'erreur) et vérifie que le texte de chaque bouton de `index.html` correspond au caractère qu'il ajoute.

## Exécuter les tests

Il faut avoir installé les dépendances (voir le README principal) :

```bash
pip install flask pytest
```

Depuis la racine du projet :

```bash
python -m pytest              # tous les tests
python -m pytest -v           # avec le détail de chaque test
python -m pytest tests/test_operators.py   # un seul fichier
```

Il faut lancer la commande depuis la racine et avec `python -m pytest`, sinon les tests ne trouvent pas `app.py` et `operators.py`.

## Dépendances et hypothèses

- pytest et Flask. Le serveur n'a pas besoin d'être lancé, car `test_app.py` utilise `app.test_client()`.
- Les tests vérifient le comportement attendu décrit dans les docstrings et le README principal, pas le comportement actuel du code. Un test qui échoue indique donc un bogue.

## Suivi des correctifs

Avant les correctifs, 7 des 22 tests échouaient. Chaque bogue a eu sa propre issue et sa propre branche.

### #1 : erreur de soustraction (branche `fix/1-subtraction`)

- **Problème** : `subtract` inversait les opérandes en utilisant `b - a`, donc `9 - 4` donnait `-5` au lieu de `5`.
- **Correctif** : remplacé `return b - a` par `return a - b`.
- **Tests qui échouaient** : `test_operators.py::test_subtract` et `test_calculate.py::test_valid_expressions[9-4-5.0]`.
- **Résultat sur la branche** : les deux tests passent.

```bash
python -m pytest tests/test_operators.py::test_subtract "tests/test_calculate.py::test_valid_expressions[9-4-5.0]"
# 2 passed
```

### #2 : erreur de multiplication (branche `fix/2-corriger-multiplication`)

- **Problème** : `multiply` calculait une puissance en utilisant `a ** b`, donc `6 * 7` donnait `279936.0` au lieu de `42.0`.
- **Correctif** : remplacé `return a ** b` par `return a * b`.
- **Tests qui échouaient** : `test_operators.py::test_multiply` et `test_calculate.py::test_valid_expressions[6*7-42.0]`.
- **Résultat sur la branche** : les deux tests passent.

```bash
python -m pytest tests/test_operators.py::test_multiply "tests/test_calculate.py::test_valid_expressions[6*7-42.0]"
# 2 passed
```

### #3 : division entière (branche `fix/3-division-entiere`)

- **Problème** : `divide` utilisait `//`, donc `7/2` donnait `3` au lieu de `3.5`.
- **Correctif** : remplacé par `/`.
- **Tests qui échouaient** : `test_operators.py::test_divide` et `test_calculate.py::test_valid_expressions[7/2-3.5]`.
- **Résultat sur la branche** : les deux tests passent.

```bash
python -m pytest tests/test_operators.py::test_divide "tests/test_calculate.py::test_valid_expressions[7/2-3.5]"
# 2 passed
```

### #4 : libellés des boutons (branche `fix/4-libelles-boutons`)

- **Problème** : dans `index.html`, les boutons 2 et 8 affichaient `02` et `88`, et les boutons `*` et `/` étaient vides.
- **Correctif** : chaque bouton affiche maintenant le caractère qu'il ajoute.
- **Test qui échouait** : `test_app.py::test_button_labels_match_values`.
- **Résultat sur la branche** : le test passe.

```bash
python -m pytest tests/test_app.py::test_button_labels_match_values
# 1 passed
```

## Résultat final sur `main`

Après la fusion des PR #6, #7, #8 et #9, la suite complète a été relancée sur `main` :

```bash
python -m pytest
# 22 passed
```

Tous les tests passent, y compris les 7 qui échouaient au départ.
