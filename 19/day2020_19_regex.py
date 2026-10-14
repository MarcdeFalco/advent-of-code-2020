"""Advent of Code 2020, jour 19, partie 1 par expression régulière.

Sans les règles récursives de la partie 2, la grammaire n'engendre qu'un
langage fini : on la traduit en une expression régulière (une alternative
entre parenthèses par règle à plusieurs productions) et on teste chaque mot
avec fullmatch. Partie 2 : pas de solution dans cette version.
"""
import re


def lire(lignes):
    regles = {}
    while True:
        ligne = next(lignes).strip()
        if ligne == '':
            break
        num, regle = ligne.split(': ')
        if '"' in regle:
            regles[num] = regle.strip(' "')
        else:
            regles[num] = [choix.split() for choix in regle.split('|')]
    return regles, [ligne.strip() for ligne in lignes]


def regle_en_regex(regles, n):
    regle = regles[n]
    if type(regle) == str:
        return regle

    def production(p):
        return ''.join(regle_en_regex(regles, m) for m in p)

    if len(regle) == 1:
        return production(regle[0])
    return '(' + '|'.join(production(p) for p in regle) + ')'


regles, mots = lire(iter(open('day2020_19.txt')))
expression = re.compile(regle_en_regex(regles, '0'))
print('Partie 1 :', sum(1 for mot in mots if expression.fullmatch(mot)))
