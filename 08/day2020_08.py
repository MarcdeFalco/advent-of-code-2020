"""Advent of Code 2020, jour 8.

`executer` simule le programme en mémorisant les instructions déjà
exécutées : repasser par l'une d'elles signifie boucler.
Partie 1 : accumulateur au moment où le programme boucle.
Partie 2 : on essaie chaque échange jmp/nop et on garde celui qui fait
terminer le programme.
"""
import re

INSTRUCTION = re.compile(r'(?P<ope>[a-z][a-z][a-z]) (?P<arg>(\+|-)\d+)')


def executer(instructions):
    """Renvoie (termine, accumulateur)."""
    executees = []
    pc, acc = 0, 0
    while pc not in executees:
        if pc >= len(instructions):
            return True, acc
        executees.append(pc)
        ope, arg = instructions[pc]
        if ope == 'jmp':
            pc += arg
        else:
            if ope == 'acc':
                acc += arg
            pc += 1
    return False, acc


def partie1(instructions):
    return executer(instructions)[1]


def partie2(instructions):
    for i, (ope, arg) in enumerate(instructions):
        if ope == 'acc':
            continue
        instructions[i] = ('nop' if ope == 'jmp' else 'jmp', arg)
        termine, acc = executer(instructions)
        instructions[i] = (ope, arg)
        if termine:
            return acc


instructions = [(m.group('ope'), int(m.group('arg')))
                for m in map(INSTRUCTION.search, open('day2020_08.txt'))]
print('Partie 1 :', partie1(instructions))
print('Partie 2 :', partie2(instructions))
