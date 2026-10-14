"""Advent of Code 2020, jour 16.

Partie 1 : somme des valeurs des billets voisins qui ne tombent dans aucun
intervalle.
Partie 2 : on garde les billets valides puis, pour chaque champ, la liste
des colonnes compatibles avec toutes leurs valeurs. On traite les champs
par nombre croissant de candidats, chacun prenant son unique candidat qu'on
retire des autres listes. Comme ces longueurs changent pendant le
parcours, `tri_paresseux` (une sorte de tri par sélection) recalcule le
minimum à chaque étape : `sorted` évaluerait les clés une fois pour toutes
(voir day2020_16_explication_tri.py).
"""
import math
from itertools import chain


def lire(lignes):
    regles = []
    noms = []
    while True:
        ligne = next(lignes)
        if ligne == '':
            break
        nom, intervalles = ligne.split(': ')
        regles.append([[int(n) for n in v.split('-')]
                       for v in intervalles.split(' or ')])
        noms.append(nom)
    next(lignes)  # your ticket:
    billet = list(map(int, next(lignes).split(',')))
    next(lignes)
    next(lignes)  # nearby tickets:
    autres = [list(map(int, ligne.split(','))) for ligne in lignes]
    return regles, noms, billet, autres


def valeur_possible(regles, valeur):
    return any(r[0] <= valeur <= r[1] for r in chain.from_iterable(regles))


def tri_paresseux(iterable, cle=lambda v: v):
    """Comme sorted, mais la clé est réévaluée à chaque élément produit."""
    donnees = list(iterable)
    while donnees:
        v = donnees[0]
        for autre in donnees[1:]:
            if cle(autre) < cle(v):
                v = autre
        donnees.remove(v)
        yield v


def partie1(regles, autres):
    return sum(valeur for valeur in chain.from_iterable(autres)
               if not valeur_possible(regles, valeur))


def partie2(regles, noms, billet, autres):
    valides = [b for b in autres
               if all(valeur_possible(regles, valeur) for valeur in b)]
    candidats = {
        noms[i]: [j for j in range(len(billet))
                  if all(r[0][0] <= b[j] <= r[0][1]
                         or r[1][0] <= b[j] <= r[1][1]
                         for b in valides)]
        for i, r in enumerate(regles)
    }
    position = {}
    for nom in tri_paresseux(candidats, cle=lambda r: len(candidats[r])):
        j = candidats[nom][0]
        position[nom] = j
        for autre in candidats:
            if j in candidats[autre]:
                candidats[autre].remove(j)
    return math.prod(billet[position[r]] for r in position
                     if r.startswith('departure'))


lignes = (ligne.strip() for ligne in open('day2020_16.txt'))
regles, noms, billet, autres = lire(lignes)
print('Partie 1 :', partie1(regles, autres))
print('Partie 2 :', partie2(regles, noms, billet, autres))
