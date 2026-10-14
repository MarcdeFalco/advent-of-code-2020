"""Advent of Code 2020, jour 18, partie 2 : version « triche ».

On échange + et * dans le texte : Python analyse alors l'expression avec
ses priorités habituelles, ce qui donne exactement l'arbre voulu (l'ancien
+, devenu *, est prioritaire). Puis on rétablit les vraies opérations en
échangeant Add et Mult dans l'arbre de syntaxe avant de l'évaluer.
"""
import ast


def echanger_plus_fois(s):
    return s.replace('*', 'OpT').replace('+', '*').replace('OpT', '+')


class Echangeur(ast.NodeTransformer):
    def visit_Add(self, node):
        return ast.Mult()

    def visit_Mult(self, node):
        return ast.Add()


total = 0
for ligne in open('day2020_18.txt'):
    arbre = ast.parse(echanger_plus_fois(ligne.strip()), mode='eval')
    arbre = Echangeur().visit(arbre)
    total += eval(compile(arbre, '', mode='eval'))
print('Partie 2 :', total)
