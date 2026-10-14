"""Advent of Code 2020, jour 4.

Les fiches, séparées par des lignes vides, deviennent des dictionnaires
champ -> valeur.
Partie 1 : fiches qui ont les sept champs obligatoires.
Partie 2 : fiches dont les champs respectent en plus les règles ; c'est une
suite de tests avec `continue`, l'exception ValueError couvrant les
conversions impossibles.
"""

CHAMPS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def lire_fiches(lignes):
    groupes = []
    groupe = []
    for ligne in lignes:
        ligne = ligne.strip()
        if ligne == '':
            groupes.append(groupe)
            groupe = []
        else:
            groupe += ligne.split()
    groupes.append(groupe)
    return [dict(v.split(':') for v in groupe) for groupe in groupes]


def entre(texte, bas, haut):
    return bas <= int(texte) <= haut


def valide(p):
    try:
        if ('byr' not in p or len(p['byr']) != 4
                or not entre(p['byr'], 1920, 2002)):
            return False
        if ('iyr' not in p or len(p['iyr']) != 4
                or not entre(p['iyr'], 2010, 2020)):
            return False
        if ('eyr' not in p or len(p['eyr']) != 4
                or not entre(p['eyr'], 2020, 2030)):
            return False
        if ('hgt' not in p or len(p['hgt']) < 2
                or p['hgt'][-2:] not in ['cm', 'in']):
            return False
        if p['hgt'][-2:] == 'cm' and not entre(p['hgt'][:-2], 150, 193):
            return False
        if p['hgt'][-2:] == 'in' and not entre(p['hgt'][:-2], 59, 76):
            return False
        if ('hcl' not in p or len(p['hcl']) != 7 or p['hcl'][0] != '#'
                or not all(v in '0123456789abcdef' for v in p['hcl'][1:])):
            return False
        if 'ecl' not in p or p['ecl'] not in ['amb', 'blu', 'brn', 'gry',
                                              'grn', 'hzl', 'oth']:
            return False
        if ('pid' not in p or len(p['pid']) != 9
                or not all(v in '0123456789' for v in p['pid'])):
            return False
    except ValueError:
        return False
    return True


def partie1(fiches):
    return sum(1 for p in fiches if all(c in p for c in CHAMPS))


def partie2(fiches):
    return sum(1 for p in fiches if valide(p))


fiches = lire_fiches(open('day2020_04.txt'))
print('Partie 1 :', partie1(fiches))
print('Partie 2 :', partie2(fiches))
