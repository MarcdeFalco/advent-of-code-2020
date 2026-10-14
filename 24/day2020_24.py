"""Advent of Code 2020, jour 24 : grille hexagonale.

On remplace d'abord les directions à deux lettres par une lettre, puis on
suit le chemin dans un repère où une ligne sur deux est décalée d'un
demi-pas : x est un multiple de 1/2, valeur exacte en flottant. Un
defaultdict(bool) retient la couleur des cases (True = noire).
Partie 1 : nombre de cases noires après tous les retournements.
Partie 2 : jeu de la vie à 6 voisins pendant 100 jours ; on n'examine que
les cases noires et leurs voisines (liste `a_examiner`, testée avec `in`,
d'où un coût quadratique par étape).
"""
from collections import defaultdict

DEPLACEMENTS = {'e': (1, 0), 'w': (-1, 0), 'S': (0.5, -1), 's': (-0.5, -1),
                'N': (0.5, 1), 'n': (-0.5, 1)}


def voisins(x, y):
    return [(x - 1, y), (x + 1, y), (x - 0.5, y + 1), (x + 0.5, y + 1),
            (x - 0.5, y - 1), (x + 0.5, y - 1)]


def pavage_initial(lignes):
    pavage = defaultdict(bool)
    for ligne in lignes:
        ligne = ligne.strip()
        for a, b in [('se', 'S'), ('sw', 's'), ('ne', 'N'), ('nw', 'n')]:
            ligne = ligne.replace(a, b)
        x, y = 0, 0
        for d in ligne:
            dx, dy = DEPLACEMENTS[d]
            x, y = x + dx, y + dy
        pavage[x, y] = not pavage[x, y]
    return pavage


def noires(pavage):
    return sum(1 for v in pavage.values() if v)


def partie1(pavage):
    return noires(pavage)


def partie2(pavage):
    for _ in range(100):
        nouveau = defaultdict(bool)
        a_examiner = []
        for x, y in list(pavage):
            if pavage[x, y]:
                for v in [(x, y)] + voisins(x, y):
                    if v not in a_examiner:
                        a_examiner.append(v)
        for x, y in a_examiner:
            nb_noires = sum(1 for v in voisins(x, y) if pavage[v])
            if pavage[x, y] and nb_noires in [1, 2]:
                nouveau[x, y] = True
            if not pavage[x, y] and nb_noires == 2:
                nouveau[x, y] = True
        pavage = nouveau
    return noires(pavage)


pavage = pavage_initial(open('day2020_24.txt'))
print('Partie 1 :', partie1(pavage))
print('Partie 2 :', partie2(pavage))
