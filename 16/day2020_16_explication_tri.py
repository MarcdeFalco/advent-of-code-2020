"""Petite expérience autour du jour 16 : sorted calcule la
liste triée une fois pour toutes, au début ; les modifications de d faites
pendant le parcours n'y changent rien. D'où le tri « paresseux » écrit à la
main dans day2020_16.py, qui réévalue la clé à chaque étape.
"""

d = {i: i for i in range(10)}

for v in sorted(d, key=lambda v: v):
    print(v, d[v])
    for autre in d:
        if autre % 2 == 0:
            d[autre] -= 1
