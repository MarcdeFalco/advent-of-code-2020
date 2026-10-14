"""Advent of Code 2020, jour 23 : déplacements dans une liste circulaire.

Partie 1 : simulation avec des listes Python et des tranches ; la tasse
courante est toujours en tête, puis passe en queue. O(n) par coup, ce qui
va pour 100 coups sur 9 tasses.
Partie 2 : un million de tasses et dix millions de coups. Liste doublement
chaînée circulaire, plus un tableau qui associe à chaque valeur son
maillon : retirer les trois tasses qui suivent la courante et les
réinsérer après la destination coûte O(1).
"""


def partie1(tasses):
    l = list(tasses)
    M, m = max(l), min(l)
    for _ in range(100):
        courante = l[0]
        prises = l[1:4]
        l = l[4:]
        destination = courante - 1
        if destination < m:
            destination = M
        while destination in [courante] + prises:
            destination -= 1
            if destination < m:
                destination = M
        i = l.index(destination)
        l = l[:i + 1] + prises + l[i + 1:]
        l.append(courante)
    while l[0] != 1:
        l = l[1:] + [l[0]]
    return ''.join(map(str, l[1:]))


class Maillon:
    def __init__(self, valeur, gauche=None, droite=None):
        self.gauche = gauche if gauche is not None else self
        self.droite = droite if droite is not None else self
        self.valeur = valeur


def partie2(tasses, nb_tasses=1000000, nb_coups=10000000):
    maillon_de = [None] * (nb_tasses + 1)  # valeur -> maillon
    debut = Maillon(tasses[0])
    maillon_de[debut.valeur] = debut
    precedent = debut
    valeurs = tasses[1:] + list(range(len(tasses) + 1, nb_tasses + 1))
    for v in valeurs:
        maillon = Maillon(v, gauche=precedent, droite=debut)
        precedent.droite = maillon
        debut.gauche = maillon
        maillon_de[v] = maillon
        precedent = maillon

    def moins_un(v):
        return nb_tasses if v == 1 else v - 1

    courant = debut
    for _ in range(nb_coups):
        # les trois maillons qui suivent : de premier à dernier
        premier = courant.droite
        dernier = courant
        prises = []
        for _ in range(3):
            dernier = dernier.droite
            prises.append(dernier.valeur)
        destination = moins_un(courant.valeur)
        while destination in prises:
            destination = moins_un(destination)
        dest = maillon_de[destination]
        # on décroche les trois maillons...
        courant.droite = dernier.droite
        dernier.droite.gauche = courant
        # ... et on les raccroche après la destination
        dernier.droite = dest.droite
        dernier.droite.gauche = dernier
        premier.gauche = dest
        dest.droite = premier
        courant = courant.droite

    un = maillon_de[1]
    return un.droite.valeur * un.droite.droite.valeur


tasses = list(map(int, open('day2020_23.txt').read().strip()))
print('Partie 1 :', partie1(tasses))
print('Partie 2 :', partie2(tasses))
