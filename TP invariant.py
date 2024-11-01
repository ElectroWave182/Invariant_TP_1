# Exercice 1 :

def contientZero(t):

    return 0 in t


def indiceZero(t):

    # précondition
    n = len(t)
    assert n > 0, "Erreur : liste vide"
    assert contientZero(t), "Erreur : pas de zéro"

    # initialisation
    i = 0

    # invariant
    assert 0 <= i < n, "Erreur 1 : indice i en dehors des limites"
    assert not(contientZero(t[: i])), "Erreur 1 : un zéro a été oublié"

    # boucle
    while t[i] != 0:

        # invariant et (non condition d'arrêt)
        assert 0 <= i < n, "Erreur 2 : indice i en dehors des limites"
        assert not(contientZero(t[: i])), "Erreur 2 : un zéro a été oublié"
        assert t[i] != 0, "Erreur : non condition d'arrêt"

        # corps
        i += 1

        # invariant
        assert 0 <= i < n, "Erreur 3 : indice i en dehors des limites"
        assert not(contientZero(t[: i])), "Erreur 3 : un zéro a été oublié"

    # invariant
    assert 0 <= i < n, "Erreur 4 : indice i en dehors des limites"
    assert not(contientZero(t[: i])), "Erreur 4 : un zéro a été oublié"
    assert t[i] == 0, "Erreur : condition d'arrêt"

    # postcondition

    # sortie
    return i


print(indiceZero([4, 5, -2, 0, 6, 0]))
print(indiceZero([0, 0, 0, -2, 0, 9]))
print(indiceZero([4, 5, -2, 6, 9, 0]))


# Exercice 2 :

from random import *

def sommeTableau(t):

    # précondition
    n = len(t)
    assert n > 0, "Erreur : liste vide"

    # initialisation
    i = 0
    s = 0

    # invariant
    assert 0 <= i < n, "Erreur 1 : indice i en dehors des limites"
    assert s == sum(t[: i]), "Erreur 1 : somme fausse"

    # boucle
    while i != n:

        # invariant et (non condition d'arrêt)
        assert 0 <= i < n, "Erreur 2 : indice i en dehors des limites"
        assert s == sum(t[: i]), "Erreur 2 : somme fausse"
        assert i != n, "Erreur : non condition d'arrêt"

        # corps
        s += t[i]
        i += 1

        # invariant
        assert 0 <= i < n, "Erreur 3 : indice i en dehors des limites"
        assert s == sum(t[: i]), "Erreur 3 : somme fausse"

    # invariant
    assert 0 <= i < n, "Erreur 4 : indice i en dehors des limites"
    assert s == sum(t[: i]), "Erreur 4 : somme fausse"
    assert i == n, "Erreur : condition d'arrêt"

    # postcondition
    assert s >= 0, "Erreur : somme négative"

    # sortie
    return s


tests = [[randint(-10, 10) for _ in range(randint(1, 20))] for _ in range(100)]

cpt = 0
for t in tests:
    cpt += 1
    assert sum(t) == sommeTableau(t), "Erreur " + str(cpt)


# Exercice 3 :

def sommeTableau(t):

    # précondition
    n = len(t)
    assert n > 0, "Erreur : liste vide"

    # initialisation
    i = 0
    s = 0

    # invariant
    assert 0 <= i < n, "Erreur 1 : indice i en dehors des limites"
    assert s == sum(t[: i]), "Erreur 1 : somme fausse"

    # boucle
    while i != n:

        # invariant et (non condition d'arrêt)
        assert 0 <= i < n, "Erreur 2 : indice i en dehors des limites"
        assert s == sum(t[: i]), "Erreur 2 : somme fausse"
        assert i != n, "Erreur : non condition d'arrêt"

        # corps
        s += t[i]
        i += 1

        # invariant
        assert 0 <= i < n, "Erreur 3 : indice i en dehors des limites"
        assert s == sum(t[: i]), "Erreur 3 : somme fausse"

    # invariant
    assert 0 <= i < n, "Erreur 4 : indice i en dehors des limites"
    assert s == sum(t[: i]), "Erreur 4 : somme fausse"
    assert i == n, "Erreur : condition d'arrêt"

    # postcondition
    assert s >= 0, "Erreur : somme négative"

    # sortie
    return s


tests = [[randint(-10, 10) for _ in range(randint(1, 20))] for _ in range(100)]

cpt = 0
for t in tests:
    cpt += 1
    assert sum(t) == sommeTableau(t), "Erreur " + str(cpt)