"""Advent of Code 2020, jour 13.

Partie 1 : on teste les attentes 0, 1, 2... jusqu'à ce qu'une période
divise l'instant d'arrivée.
Partie 2 : on cherche t avec t = -i (mod b) pour chaque bus b de rang i.
Pour chaque b, l'algorithme d'Euclide étendu donne u b + v P = 1, où P est
le produit des autres périodes ; e = v P vaut 1 modulo b et 0 modulo les
autres. La solution est -somme(i * e) modulo le produit de toutes les
périodes (théorème chinois ; les périodes sont premières entre elles).
"""
import math


def euclide_etendu(a, b):
    """(d, u, v) avec u a + v b = d = pgcd(a, b)."""
    u, v, up, vp = 0, 1, 1, 0
    while b != 0:
        q, a, b = a // b, b, a % b
        u, v, up, vp = up - q * u, vp - q * v, u, v
    return (a, up, vp)


def partie1(instant, bus):
    attente = 0
    while True:
        for b in bus:
            if (attente + instant) % b == 0:
                return b * attente
        attente += 1


def partie2(horaires, bus):
    t = 0
    for b in bus:
        produit_autres = math.prod(autre for autre in bus if autre != b)
        _, _, v = euclide_etendu(b, produit_autres)
        t -= horaires.index(b) * v * produit_autres
    return t % math.prod(bus)


ligne1, ligne2 = open('day2020_13.txt').readlines()
instant = int(ligne1)
horaires = [int(b) if b != 'x' else None for b in ligne2.strip().split(',')]
bus = [b for b in horaires if b is not None]
print('Partie 1 :', partie1(instant, bus))
print('Partie 2 :', partie2(horaires, bus))
