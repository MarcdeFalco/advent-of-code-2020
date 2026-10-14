"""Advent of Code 2020, jour 6.

Les groupes sont séparés par des lignes vides.
Partie 1 : taille de l'union des réponses du groupe (un ensemble).
Partie 2 : taille de l'intersection, via un dictionnaire de booléens
« tout le monde a répondu oui ».
"""


def lire_groupes(lignes):
    groupes = []
    groupe = []
    for ligne in lignes:
        ligne = ligne.strip()
        if ligne == '':
            groupes.append(groupe)
            groupe = []
        else:
            groupe.append(ligne)
    groupes.append(groupe)
    return groupes


def questions(groupe):
    return {q for reponses in groupe for q in reponses}


def partie1(groupes):
    return sum(len(questions(groupe)) for groupe in groupes)


def partie2(groupes):
    total = 0
    for groupe in groupes:
        tous_oui = {q: True for q in questions(groupe)}
        for reponses in groupe:
            for q in tous_oui:
                if q not in reponses:
                    tous_oui[q] = False
        total += sum(1 for q in tous_oui if tous_oui[q])
    return total


groupes = lire_groupes(open('day2020_06.txt'))
print('Partie 1 :', partie1(groupes))
print('Partie 2 :', partie2(groupes))
