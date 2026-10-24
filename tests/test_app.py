"""Tests de la route Flask et de la page HTML, avec le client de test de Flask."""

import re

import pytest

from app import app


@pytest.fixture
def client():
    """Client de test Flask (pas besoin de lancer le serveur)."""
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_get_page(client):
    """La page d'accueil doit s'afficher avec l'ecran vide."""
    response = client.get("/")
    assert response.status_code == 200
    assert b'id="display"' in response.data


def test_post_shows_result(client):
    """Soumettre une expression doit afficher le resultat dans l'ecran."""
    response = client.post("/", data={"display": "7+3"})
    assert response.status_code == 200
    assert b'value="10.0"' in response.data


def test_post_invalid_shows_error(client):
    """Une expression invalide doit afficher un message d'erreur, pas une erreur 500."""
    response = client.post("/", data={"display": "5+"})
    assert response.status_code == 200
    assert b"Error:" in response.data


def test_post_division_by_zero_shows_error(client):
    """La division par zero doit etre affichee comme une erreur dans la page."""
    response = client.post("/", data={"display": "5/0"})
    assert response.status_code == 200
    assert b"Error:" in response.data


def test_button_labels_match_values(client):
    """Le texte de chaque bouton doit correspondre au caractere qu'il ajoute a l'ecran."""
    html = client.get("/").get_data(as_text=True)
    buttons = re.findall(r"appendToDisplay\('(.)'\)\">([^<]*)</button>", html)

    # 10 chiffres + 4 operateurs
    assert len(buttons) == 14
    # On liste tous les boutons incorrects pour les voir d'un coup dans le message d'erreur
    wrong = [(value, label) for value, label in buttons if label.strip() != value]
    assert wrong == [], f"boutons (valeur, texte affiche) incorrects : {wrong}"
