"""Advent of Code 2020, jour 25 : logarithme discret.

On retrouve l'exposant secret de la carte en multipliant par 7 modulo le
nombre premier 20201227 jusqu'à retrouver sa clé publique (recherche
exhaustive). La clé commune s'obtient en élevant l'autre clé publique à cet
exposant, par multiplications répétées. (Le dernier jour n'a qu'une
partie.)
"""

MODULE = 20201227


def transformer(sujet, nb_boucles):
    v = 1
    for _ in range(nb_boucles):
        v = (v * sujet) % MODULE
    return v


def chercher_nb_boucles(sujet, cible):
    v = 1
    nb_boucles = 0
    while v != cible:
        nb_boucles += 1
        v = (v * sujet) % MODULE
    return nb_boucles


def partie1(cle_carte, cle_porte):
    boucles_porte = chercher_nb_boucles(7, cle_porte)
    return transformer(cle_carte, boucles_porte)


cle_carte, cle_porte = map(int, open('day2020_25.txt').read().split())
print('Partie 1 :', partie1(cle_carte, cle_porte))
