# templates/

## Raison d'être

Contient les gabarits HTML (Jinja2) rendus par Flask avec `render_template()`. C'est l'interface utilisateur de la calculatrice.

## Fichiers

- `index.html` : la seule page de l'application. Elle affiche l'écran et les boutons. Deux petites fonctions JavaScript (`appendToDisplay` et `clearDisplay`) modifient l'écran. Le bouton `=` envoie l'expression au serveur en POST, et la page est renvoyée avec le résultat.

## Dépendances et hypothèses

- La variable `result` est fournie par la fonction `index()` de `app.py`.
- Le champ texte doit garder le nom `display`, car c'est ce que lit `app.py`.
- Le style vient de `static/style.css`.
- Le champ est en lecture seule : on ne peut pas taper au clavier, seulement utiliser les boutons. Il n'y a pas de bouton pour le point décimal ni pour les nombres négatifs.
