"""Advent of Code 2020, jour 11 : variante à voisinage précalculé.

Le sol ne change jamais : la liste des sièges voisins (partie 1) ou
visibles (partie 2) depuis chaque case est donc fixe. On la calcule une
fois pour toutes, ce qui évite de relancer les rayons à chaque tour.
"""
from copy import deepcopy
from itertools import product

DIRECTIONS = [d for d in product([-1, 0, 1], repeat=2) if d != (0, 0)]


def voisinage_partie1(grille):
    h, w = len(grille), len(grille[0])
    return [[[(i + di, j + dj) for di, dj in DIRECTIONS
              if 0 <= i + di < h and 0 <= j + dj < w]
             for j in range(w)] for i in range(h)]


def voisinage_partie2(grille):
    h, w = len(grille), len(grille[0])

    def visibles(i, j):
        sieges = []
        for di, dj in DIRECTIONS:
            n = 1
            while 0 <= i + n * di < h and 0 <= j + n * dj < w:
                if grille[i + n * di][j + n * dj] != '.':
                    sieges.append((i + n * di, j + n * dj))
                    break
                n += 1
        return sieges

    return [[visibles(i, j) for j in range(w)] for i in range(h)]


def stabiliser(grille, voisins, seuil):
    change = True
    while change:
        change = False
        nouvelle = deepcopy(grille)
        for i, ligne in enumerate(grille):
            for j, s in enumerate(ligne):
                occupes = sum(1 for vi, vj in voisins[i][j]
                              if grille[vi][vj] == '#')
                if s == 'L' and occupes == 0:
                    nouvelle[i][j] = '#'
                    change = True
                if s == '#' and occupes >= seuil:
                    nouvelle[i][j] = 'L'
                    change = True
        grille = nouvelle
    return sum(ligne.count('#') for ligne in grille)


grille = [list(ligne.strip()) for ligne in open('day2020_11.txt')]
print('Partie 1 :', stabiliser(grille, voisinage_partie1(grille), 4))
print('Partie 2 :', stabiliser(grille, voisinage_partie2(grille), 5))
