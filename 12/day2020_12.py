"""Advent of Code 2020, jour 12.

L'état est un triplet (x, y, vecteur) et chaque instruction est une
fonction de l'état vers le nouvel état, rangée dans un dictionnaire de
lambda indexé par la lettre. Les rotations sont des quarts de tour du
vecteur ((x, y) -> (-y, x) pour 90° à gauche) ; tourner à droite de n
degrés, c'est tourner à gauche de 360 - n.
Partie 1 : le vecteur est la direction du navire, N/S/E/W déplacent le
navire. Partie 2 : le vecteur est un point de cap, que N/S/E/W déplacent ;
F avance du vecteur multiplié par n dans les deux cas.
"""

ROTATION = {90: lambda d: (-d[1], d[0]),
            180: lambda d: (-d[0], -d[1]),
            270: lambda d: (d[1], -d[0])}

INSTRUCTIONS_PARTIE1 = {
    'R': lambda n, x, y, d: (x, y, ROTATION[360 - n](d)),
    'L': lambda n, x, y, d: (x, y, ROTATION[n](d)),
    'N': lambda n, x, y, d: (x, y + n, d),
    'S': lambda n, x, y, d: (x, y - n, d),
    'E': lambda n, x, y, d: (x + n, y, d),
    'W': lambda n, x, y, d: (x - n, y, d),
    'F': lambda n, x, y, d: (x + n * d[0], y + n * d[1], d),
}

INSTRUCTIONS_PARTIE2 = {
    'R': lambda n, x, y, w: (x, y, ROTATION[360 - n](w)),
    'L': lambda n, x, y, w: (x, y, ROTATION[n](w)),
    'N': lambda n, x, y, w: (x, y, (w[0], w[1] + n)),
    'S': lambda n, x, y, w: (x, y, (w[0], w[1] - n)),
    'E': lambda n, x, y, w: (x, y, (w[0] + n, w[1])),
    'W': lambda n, x, y, w: (x, y, (w[0] - n, w[1])),
    'F': lambda n, x, y, w: (x + n * w[0], y + n * w[1], w),
}


def naviguer(itineraire, instructions, etat):
    for lettre, n in itineraire:
        etat = instructions[lettre](n, *etat)
    x, y, _ = etat
    return abs(x) + abs(y)


def partie1(itineraire):
    return naviguer(itineraire, INSTRUCTIONS_PARTIE1, (0, 0, (1, 0)))


def partie2(itineraire):
    return naviguer(itineraire, INSTRUCTIONS_PARTIE2, (0, 0, (10, 1)))


itineraire = [(ligne[0], int(ligne[1:])) for ligne in open('day2020_12.txt')]
print('Partie 1 :', partie1(itineraire))
print('Partie 2 :', partie2(itineraire))
