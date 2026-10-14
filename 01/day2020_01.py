"""Advent of Code 2020, jour 1.

`paire_de_somme(v)` cherche deux nombres de somme v en un seul passage, en
gardant dans un ensemble les valeurs déjà vues : le complément se teste en
O(1). Partie 1 : une paire de somme 2020. Partie 2 : pour chaque e, une
paire de somme 2020 - e, d'où O(n^2) au total (rien n'empêche cette paire
de réutiliser e lui-même).
"""


def paire_de_somme(nombres, v):
    vus = set()
    for k in nombres:
        if v - k in vus:
            return (k, v - k)
        vus.add(k)
    return None


def partie1(nombres):
    a, b = paire_de_somme(nombres, 2020)
    return a * b


def partie2(nombres):
    for e in nombres:
        paire = paire_de_somme(nombres, 2020 - e)
        if paire is not None:
            return e * paire[0] * paire[1]


nombres = [int(n) for n in open('day2020_01.txt')]
print('Partie 1 :', partie1(nombres))
print('Partie 2 :', partie2(nombres))
