"""Advent of Code 2020, jour 7.

Les règles forment un graphe orienté acyclique pondéré : sac -> liste de
(quantité, sac contenu).
Partie 1 : sacs qui peuvent contenir « shiny gold », par un parcours
récursif mémoïsé (dictionnaire `cache`).
Partie 2 : nombre de sacs dans « shiny gold », par la récurrence mémoïsée
N(a) = somme sur a -> b de k * (1 + N(b)).
"""

CIBLE = 'shiny gold'


def lire_regle(ligne):
    ligne = ligne.strip()[:-1]  # point final
    ligne = ligne.replace(' bags', '').replace(' bag', '')
    sac, contenu = ligne.split(' contain ')
    if contenu == 'no other':
        return sac, []
    couples = []
    for v in contenu.split(', '):
        mots = v.split()
        couples.append((int(mots[0]), ' '.join(mots[1:])))
    return sac, couples


def partie1(regles):
    cache = {}

    def peut_contenir(sac):
        if sac in cache:
            return cache[sac]
        v = False
        for _, autre in regles[sac]:
            if autre == CIBLE or peut_contenir(autre):
                v = True
                break
        cache[sac] = v
        return v

    return sum(1 for sac in regles if peut_contenir(sac))


def partie2(regles):
    cache = {}

    def nombre(sac):
        if sac in cache:
            return cache[sac]
        v = 0
        for n, autre in regles[sac]:
            v += n * (1 + nombre(autre))
        cache[sac] = v
        return v

    return nombre(CIBLE)


regles = dict(lire_regle(ligne) for ligne in open('day2020_07.txt'))
print('Partie 1 :', partie1(regles))
print('Partie 2 :', partie2(regles))
