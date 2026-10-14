"""Advent of Code 2020, jour 9.

Partie 1 : fenêtre glissante des 25 nombres précédents, rangée dans un
ensemble ; un nombre est valide si v - k est dans la fenêtre pour un k.
(L'ensemble perd les doublons de la fenêtre, sans conséquence ici.)
Partie 2 : les nombres étant positifs, deux pointeurs délimitent une plage
dont on fait glisser la somme : on avance la fin si elle est trop petite,
le début si elle est trop grande, en O(n).
"""

TAILLE_FENETRE = 25


def partie1(nombres):
    fenetre = set(nombres[:TAILLE_FENETRE])
    for i, v in enumerate(nombres[TAILLE_FENETRE:]):
        if not any(v - k != k and v - k in fenetre for k in fenetre):
            return v
        fenetre.remove(nombres[i])
        fenetre.add(v)


def partie2(nombres, cible):
    somme = nombres[0] + nombres[1]
    debut, fin = 0, 1
    for _ in range(len(nombres)):
        if somme > cible:
            somme -= nombres[debut]
            debut += 1
        elif somme < cible:
            fin += 1
            somme += nombres[fin]
        else:
            break
    plage = nombres[debut:fin + 1]
    return min(plage) + max(plage)


nombres = [int(n) for n in open('day2020_09.txt')]
cible = partie1(nombres)
print('Partie 1 :', cible)
print('Partie 2 :', partie2(nombres, cible))
