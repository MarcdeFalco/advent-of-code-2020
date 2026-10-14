"""Advent of Code 2020, jour 5.

`dicho` réduit un intervalle de moitié à chaque lettre (B et R : moitié
haute), comme une recherche dichotomique ; c'est une lecture en base 2 qui
ne dit pas son nom. Le numéro du siège est 8 * rangée + colonne.
Partie 1 : plus grand numéro. Partie 2 : numéro absent dont les deux
voisins sont présents.
"""


def dicho(chemin, bornes):
    bas, haut = bornes
    for v in chemin:
        milieu = (bas + haut) // 2
        if v in ['B', 'R']:
            bas = milieu + 1
        else:
            haut = milieu
    return bas


def numero(chemin):
    rangee = dicho(chemin[:-3], (0, 127))
    colonne = dicho(chemin[-3:], (0, 7))
    return rangee * 8 + colonne


def partie1(numeros):
    return max(numeros)


def partie2(numeros):
    numeros = sorted(numeros)
    for v in range(numeros[0], numeros[-1]):
        if v - 1 in numeros and v + 1 in numeros and v not in numeros:
            return v


numeros = [numero(v.strip()) for v in open('day2020_05.txt')]
print('Partie 1 :', partie1(numeros))
print('Partie 2 :', partie2(numeros))
