"""Advent of Code 2020, jour 20 : puzzle de tuiles, puis recherche d'un motif.

Chaque tuile a 8 orientations (symétrie ou non, puis 0 à 3 quarts de
tour), codées par `symetrie_rotation`, qui transforme les coordonnées au
lieu de recopier la tuile.
Partie 1 : on remplit la grille case par case, ligne par ligne, par retour
sur trace : une tuile n'est posée que si son bord gauche coïncide avec le
bord droit de sa voisine de gauche et son bord haut avec le bord bas de
celle du dessus. Réponse : produit des numéros des quatre coins.
Partie 2 : on assemble l'image sans les bords des tuiles, puis on essaie
ses 8 orientations en cherchant le monstre à toutes les positions et en
marquant ses cases ; réponse : cases # restantes. (Les bornes des boucles
de recherche oublient la dernière position en x et en y ; sans conséquence
sur cette entrée.)
"""
from itertools import chain, product
from math import sqrt

HAUT, DROITE, BAS, GAUCHE = 0, 1, 2, 3

MONSTRE = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''.split('\n')


def lire_tuiles(lignes):
    # chaque tuile occupe 12 lignes : « Tile n: », 10 lignes, ligne vide
    return {int(lignes[12 * k][5:-2]): [list(lignes[12 * k + i].strip())
                                        for i in range(1, 11)]
            for k in range(len(lignes) // 12)}


def symetrie_rotation(x, y, taille, symetrie, rotation):
    if symetrie:
        x = taille - 1 - x
    for _ in range(rotation):
        x, y = taille - 1 - y, x
    return x, y


def bord(tuiles, direction, numero, symetrie, rotation):
    tuile = tuiles[numero]

    def case(x, y):
        x, y = symetrie_rotation(x, y, 10, symetrie, rotation)
        return tuile[y][x]

    position = [lambda i: (i, 0), lambda i: (9, i),
                lambda i: (i, 9), lambda i: (0, i)][direction]
    return [case(*position(i)) for i in range(10)]


def assembler(tuiles, n):
    def suivante(x, y):
        if x < n - 1:
            return (x + 1, y)
        if y < n - 1:
            return (0, y + 1)
        return None

    def retour_sur_trace(pos, restantes, posees):
        if restantes == []:
            return posees
        x, y = pos
        for numero, symetrie, rotation in product(restantes, [True, False],
                                                  [0, 1, 2, 3]):
            if x > 0 and (bord(tuiles, DROITE, *posees[x - 1, y])
                          != bord(tuiles, GAUCHE, numero, symetrie, rotation)):
                continue
            if y > 0 and (bord(tuiles, BAS, *posees[x, y - 1])
                          != bord(tuiles, HAUT, numero, symetrie, rotation)):
                continue
            posees[x, y] = (numero, symetrie, rotation)
            res = retour_sur_trace(suivante(x, y),
                                   [t for t in restantes if t != numero],
                                   posees)
            if res is not None:
                return res
            del posees[x, y]
        return None

    return retour_sur_trace((0, 0), list(tuiles.keys()), {})


def partie1(tuiles, n, pavage):
    return (pavage[0, 0][0] * pavage[n - 1, 0][0]
            * pavage[0, n - 1][0] * pavage[n - 1, n - 1][0])


def partie2(tuiles, n, pavage):
    cote = 8 * n
    image = [['.'] * cote for _ in range(cote)]
    for i, j in product(range(n), repeat=2):
        numero, symetrie, rotation = pavage[i, j]
        tuile = tuiles[numero]
        for x, y in product(range(8), repeat=2):
            tx, ty = symetrie_rotation(x + 1, y + 1, 10, symetrie, rotation)
            image[8 * j + y][8 * i + x] = tuile[ty][tx]

    monstre = [(i, j) for j, ligne in enumerate(MONSTRE)
               for i in range(len(ligne)) if ligne[i] == '#']
    largeur_m, hauteur_m = len(MONSTRE[0]), len(MONSTRE)

    for symetrie, rotation in product([False, True], range(4)):
        def case(x, y):
            x, y = symetrie_rotation(x, y, cote, symetrie, rotation)
            return image[y][x]
        vue = [[case(x, y) for x in range(cote)] for y in range(cote)]
        trouves = 0
        for x in range(cote - largeur_m):
            for y in range(cote - hauteur_m):
                if all(vue[y + dy][x + dx] == '#' for dx, dy in monstre):
                    trouves += 1
                    for dx, dy in monstre:
                        vue[y + dy][x + dx] = 'O'
        if trouves != 0:
            return sum(1 for c in chain.from_iterable(vue) if c == '#')


lignes = list(open('day2020_20.txt'))
tuiles = lire_tuiles(lignes)
n = int(sqrt(len(tuiles)))
pavage = assembler(tuiles, n)
print('Partie 1 :', partie1(tuiles, n, pavage))
print('Partie 2 :', partie2(tuiles, n, pavage))
