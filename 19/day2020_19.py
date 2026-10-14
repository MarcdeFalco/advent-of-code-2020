"""Advent of Code 2020, jour 19 : mots engendrés par une grammaire.

`filtrer(n, mot)` consomme un préfixe du mot reconnu par la règle n et
renvoie le reste, ou None ; pour une alternative, on garde la première
production qui réussit (sans retour arrière, ce qui suffit pour ces
grammaires).
Partie 1 : le mot est valide si la règle 0 le consomme entièrement.
Partie 2 : les nouvelles règles 8 et 11 rendent la règle 0 de la forme
42^p 31^q avec p > q >= 1 : on consomme des blocs 42, puis on essaie de
finir le mot avec moins de blocs 31 qu'on a lu de blocs 42.
Variante : day2020_19_regex.py (partie 1 par expression régulière).
"""


def lire(lignes):
    regles = {}
    while True:
        ligne = next(lignes).strip()
        if ligne == '':
            break
        num, regle = ligne.split(': ')
        if '"' in regle:
            regles[num] = regle.strip(' "')  # une lettre
        else:
            regles[num] = [choix.split() for choix in regle.split('|')]
    return regles, [ligne.strip() for ligne in lignes]


def filtrer_production(regles, production, mot):
    for n in production:
        mot = filtrer(regles, n, mot)
        if mot is None:
            break
    return mot


def filtrer(regles, n, mot):
    regle = regles[n]
    if type(regle) == str:
        if mot != '' and mot[0] == regle:
            return mot[1:]
        return None
    for production in regle:
        reste = filtrer_production(regles, production, mot)
        if reste is not None:
            return reste
    return None


def valide_boucle(regles, mot):
    nb_42 = 0
    while True:
        mot = filtrer(regles, '42', mot)
        if mot is None:
            return False
        nb_42 += 1
        # on tente de finir avec 1, 2, ..., nb_42 - 1 blocs 31
        reste = mot
        for _ in range(1, nb_42):
            reste = filtrer(regles, '31', reste)
            if reste is None:
                break
            if reste == '':
                return True


def partie1(regles, mots):
    return sum(1 for mot in mots if filtrer(regles, '0', mot) == '')


def partie2(regles, mots):
    return sum(1 for mot in mots if valide_boucle(regles, mot))


regles, mots = lire(iter(open('day2020_19.txt')))
print('Partie 1 :', partie1(regles, mots))
print('Partie 2 :', partie2(regles, mots))
