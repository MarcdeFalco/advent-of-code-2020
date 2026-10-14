"""Advent of Code 2020, jour 18 : priorités inhabituelles.

Analyse par descente récursive sur un itérateur de caractères avec une
lettre de prévision (`peek`), qui construit un arbre de triplets
(opérande, opérateur, opérande) évalué ensuite récursivement.
Partie 1 : + et * ont la même priorité, de gauche à droite : un seul
niveau, expr ::= ope ((+|*) ope)*.
Partie 2 : + est prioritaire : un non-terminal par niveau,
expr ::= terme (* terme)* et terme ::= ope (+ ope)*.
Variante : day2020_18_partie2_ast.py.
Une version minimale de `peekable` (bibliothèque more_itertools) est écrite
ici pour éviter la dépendance.
"""


class Peekable:
    """Itérateur avec lecture de l'élément suivant sans le consommer."""

    def __init__(self, iterable):
        self.it = iter(iterable)
        self.suivant = []

    def __next__(self):
        if self.suivant:
            return self.suivant.pop()
        return next(self.it)

    def peek(self, defaut):
        if not self.suivant:
            try:
                self.suivant.append(next(self.it))
            except StopIteration:
                return defaut
        return self.suivant[0]


def lire_operande(g, lire_expr):
    v = next(g)
    if v in '0123456789':
        return int(v)
    if v == '(':
        expr = lire_expr(g)
        next(g)  # parenthèse fermante
        return expr
    raise SyntaxError


def expr_partie1(g):
    e = lire_operande(g, expr_partie1)
    while g.peek('') in ['*', '+']:
        op = next(g)
        e = (e, op, lire_operande(g, expr_partie1))
    return e


def terme_partie2(g):
    e = lire_operande(g, expr_partie2)
    while g.peek('') == '+':
        op = next(g)
        e = (e, op, lire_operande(g, expr_partie2))
    return e


def expr_partie2(g):
    e = terme_partie2(g)
    while g.peek('') == '*':
        op = next(g)
        e = (e, op, terme_partie2(g))
    return e


def evaluer(expr):
    if type(expr) == int:
        return expr
    gauche, op, droite = expr
    if op == '+':
        return evaluer(gauche) + evaluer(droite)
    return evaluer(gauche) * evaluer(droite)


def somme(lignes, lire_expr):
    return sum(evaluer(lire_expr(Peekable(ligne.replace(' ', ''))))
               for ligne in lignes)


lignes = [ligne.strip() for ligne in open('day2020_18.txt')]
print('Partie 1 :', somme(lignes, expr_partie1))
print('Partie 2 :', somme(lignes, expr_partie2))
