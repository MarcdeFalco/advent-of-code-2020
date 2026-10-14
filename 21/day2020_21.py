"""Advent of Code 2020, jour 21 : intersections et élimination.

Pour chaque allergène, on intersecte les listes d'aliments des lignes qui
le mentionnent. On répète ensuite : trouver un allergène qui n'a plus
qu'un candidat, le fixer, retirer cet aliment des autres listes (la boucle
suppose qu'un candidat unique apparaît à chaque tour).
Partie 1 : occurrences des aliments jamais attribués.
Partie 2 : aliments dangereux triés par nom d'allergène.
"""


def intersection(l1, l2):
    return [e for e in l2 if e in l1]


def analyser(lignes):
    candidats = {}  # allergène -> aliments possibles
    occurrences = {}
    for ligne in lignes:
        aliments, allergenes = ligne.strip()[:-1].split(' (contains ')
        aliments = aliments.split()
        for aliment in aliments:
            occurrences[aliment] = 1 + occurrences.get(aliment, 0)
        for allergene in allergenes.split(', '):
            if allergene not in candidats:
                candidats[allergene] = aliments
            else:
                candidats[allergene] = intersection(aliments,
                                                    candidats[allergene])

    allergene_de = {}  # aliment -> allergène
    restants = list(candidats.keys())
    while restants != []:
        for allergene in restants:
            if len(candidats[allergene]) == 1:
                aliment = candidats[allergene][0]
                restants.remove(allergene)
                allergene_de[aliment] = allergene
                for autre in restants:
                    if aliment in candidats[autre]:
                        candidats[autre].remove(aliment)
                break
    return occurrences, allergene_de


def partie1(occurrences, allergene_de):
    return sum(o for aliment, o in occurrences.items()
               if aliment not in allergene_de)


def partie2(allergene_de):
    return ','.join(sorted(allergene_de, key=lambda a: allergene_de[a]))


occurrences, allergene_de = analyser(open('day2020_21.txt'))
print('Partie 1 :', partie1(occurrences, allergene_de))
print('Partie 2 :', partie2(allergene_de))
