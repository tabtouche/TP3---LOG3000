# static/

## Raison d'être

Contient les fichiers statiques de l'application. Flask les sert automatiquement à l'URL `/static/...`.

## Fichiers

- `style.css` : mise en page et couleurs de la calculatrice (écran, grille de boutons, couleur des opérateurs).

## Dépendances et hypothèses

- Pas de dépendance externe.
- Les sélecteurs (`#display`, `.calculator`, `.buttons`, `.btn`, `.operator`) correspondent aux id et classes de `templates/index.html`. Si on les renomme dans le HTML, il faut aussi les changer ici.
- La grille a 4 colonnes, donc chaque rangée de boutons dans le HTML doit avoir 4 boutons.
