"""Advent of Code 2020, jour 11.

Simulation synchrone : on calcule la nouvelle grille à partir d'une copie
de l'ancienne et on recommence tant qu'une case change (point fixe).
Partie 1 : on compte les 8 voisins immédiats, seuil 4.
Partie 2 : dans chacune des 8 directions, on avance tant qu'on voit du sol,
comme un lancer de rayon ; seuil 5.
Variante : day2020_11_voisins_precalcules.py.
"""
from copy import deepcopy
from itertools import product

DIRECTIONS = [d for d in product([-1, 0, 1], repeat=2) if d != (0, 0)]


def occupes_voisins(grille, i, j):
    h, w = len(grille), len(grille[0])
    return sum(1 for di, dj in DIRECTIONS
               if 0 <= i + di < h and 0 <= j + dj < w
               and grille[i + di][j + dj] == '#')


def occupes_visibles(grille, i, j):
    h, w = len(grille), len(grille[0])
    occupes = 0
    for di, dj in DIRECTIONS:
        n = 1
        while 0 <= i + n * di < h and 0 <= j + n * dj < w:
            v = grille[i + n * di][j + n * dj]
            if v == '#':
                occupes += 1
            if v != '.':
                break
            n += 1
    return occupes


def stabiliser(grille, compter, seuil):
    change = True
    while change:
        change = False
        nouvelle = deepcopy(grille)
        for i, ligne in enumerate(grille):
            for j, s in enumerate(ligne):
                occupes = compter(grille, i, j)
                if s == 'L' and occupes == 0:
                    nouvelle[i][j] = '#'
                    change = True
                if s == '#' and occupes >= seuil:
                    nouvelle[i][j] = 'L'
                    change = True
        grille = nouvelle
    return sum(ligne.count('#') for ligne in grille)


def partie1(grille):
    return stabiliser(grille, occupes_voisins, 4)


def partie2(grille):
    return stabiliser(grille, occupes_visibles, 5)


grille = [list(ligne.strip()) for ligne in open('day2020_11.txt')]
print('Partie 1 :', partie1(grille))
print('Partie 2 :', partie2(grille))
