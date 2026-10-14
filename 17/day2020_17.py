"""Advent of Code 2020, jour 17 : automate cellulaire en dimension 3 puis 4.

L'espace infini est un defaultdict qui renvoie '.' pour toute case
inconnue. On maintient une boîte englobante (`boite`, un intervalle par
axe), élargie de 1 dans chaque direction à chaque étape, et on applique la
règle à toutes ses cases en comptant les 3^d - 1 voisins avec
itertools.product. Le code vaut pour une dimension quelconque.
Partie 1 : dimension 3 ; partie 2 : dimension 4.
"""
from collections import defaultdict
from itertools import product


def cases(boite):
    return product(*(range(*intervalle) for intervalle in boite))


def decaler(v, dv):
    return tuple(a + b for a, b in zip(v, dv))


def etape(boite, etat, dimension):
    nouvelle_boite = tuple((a - 1, b + 1) for a, b in boite)
    nouvel_etat = defaultdict(lambda: '.')
    for v in cases(nouvelle_boite):
        voisins = [etat[decaler(v, dv)]
                   for dv in product([-1, 0, 1], repeat=dimension)
                   if any(x != 0 for x in dv)]
        actifs = voisins.count('#')
        if etat[v] == '.' and actifs == 3:
            nouvel_etat[v] = '#'
        if etat[v] == '#' and 2 <= actifs <= 3:
            nouvel_etat[v] = '#'
    return nouvelle_boite, nouvel_etat


def simuler(plan, dimension, nb_etapes=6):
    boite = [(0, len(plan[0])), (0, len(plan))] + [(0, 1)] * (dimension - 2)
    etat = defaultdict(lambda: '.',
                       {t: plan[t[1]][t[0]] for t in cases(boite)})
    for _ in range(nb_etapes):
        boite, etat = etape(boite, etat, dimension)
    return sum(1 for v in cases(boite) if etat[v] == '#')


def partie1(plan):
    return simuler(plan, 3)


def partie2(plan):
    return simuler(plan, 4)


plan = open('day2020_17.txt').read().strip().split('\n')
print('Partie 1 :', partie1(plan))
print('Partie 2 :', partie2(plan))
