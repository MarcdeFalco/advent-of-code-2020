"""Advent of Code 2020, jour 22 : bataille, puis bataille récursive.

Les deux paquets sont des deque : on retire en tête et on ajoute en queue
en O(1). Chaque partie garde l'historique des configurations (couples de
tuples) pour détecter une répétition, qui donne la victoire au joueur 1.
Partie 1 : la plus forte carte gagne le pli.
Partie 2 : si chaque joueur a au moins autant de cartes que la valeur
qu'il vient de tirer, le pli se décide par une sous-partie jouée
récursivement sur des copies tronquées des paquets.
La partie 1 utilise la même fonction, sans sous-partie.
"""
from collections import deque
from copy import copy


def lire_paquets(lignes):
    paquets = []
    for _ in range(2):
        next(lignes)  # « Player n: »
        paquet = deque()
        for ligne in lignes:
            if ligne == '\n':
                break
            paquet.append(int(ligne))
        paquets.append(paquet)
    return paquets


def combat(p1, p2, recursif):
    """Renvoie (le joueur 1 gagne ?, paquet du gagnant)."""
    historique = []
    while len(p1) != 0 and len(p2) != 0:
        configuration = (tuple(p1), tuple(p2))
        if configuration in historique:
            return True, p1
        historique.append(configuration)
        c1, c2 = p1.popleft(), p2.popleft()
        if recursif and c1 <= len(p1) and c2 <= len(p2):
            # sous-partie avec les c1 (resp. c2) premières cartes
            q1 = copy(p1)
            while len(q1) != c1:
                q1.pop()
            q2 = copy(p2)
            while len(q2) != c2:
                q2.pop()
            joueur1_gagne = combat(q1, q2, recursif)[0]
        else:
            joueur1_gagne = c1 > c2
        if joueur1_gagne:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
    if len(p2) == 0:
        return True, p1
    return False, p2


def score(paquet):
    return sum((i + 1) * c for i, c in enumerate(reversed(paquet)))


def partie1(paquets):
    _, gagnant = combat(copy(paquets[0]), copy(paquets[1]), False)
    return score(gagnant)


def partie2(paquets):
    _, gagnant = combat(copy(paquets[0]), copy(paquets[1]), True)
    return score(gagnant)


paquets = lire_paquets(iter(open('day2020_22.txt')))
print('Partie 1 :', partie1(paquets))
print('Partie 2 :', partie2(paquets))
