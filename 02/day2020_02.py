"""Advent of Code 2020, jour 2.

Chaque ligne est découpée par une expression régulière à groupes nommés.
Partie 1 : nombre d'occurrences du caractère entre les deux bornes.
Partie 2 : le caractère est à exactement une des deux positions.
"""
import re

LIGNE = re.compile(r'(?P<m>\d+)-(?P<M>\d+) (?P<c>[a-z]): (?P<password>[a-z]*)')


def lire_entrees(lignes):
    entrees = []
    for ligne in lignes:
        m, M, c, password = LIGNE.search(ligne).groups()
        entrees.append((int(m), int(M), c, password))
    return entrees


def partie1(entrees):
    return sum(1 for m, M, c, password in entrees
               if m <= password.count(c) <= M)


def partie2(entrees):
    total = 0
    for m, M, c, password in entrees:
        a, b = password[m - 1], password[M - 1]
        if (a == c or b == c) and a != b:
            total += 1
    return total


entrees = lire_entrees(open('day2020_02.txt'))
print('Partie 1 :', partie1(entrees))
print('Partie 2 :', partie2(entrees))
