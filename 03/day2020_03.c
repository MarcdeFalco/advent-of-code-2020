/* Advent of Code 2020, jour 3.
 * La grille est lue dans un tableau de dimensions fixées. check_slope avance
 * d'un pas (right, down) constant et lit la case map[x % W][y] : le modulo
 * rend la grille infinie vers la droite sans la recopier.
 * Partie 1 : pente (3, 1). Partie 2 : produit sur cinq pentes.
 */
#include <stdio.h>
#include <assert.h>

// Ces commandes préprocesseurs permettent de définir
// des alias. Chaque fois qu'on écrit W, on écrira en fait 31
#define W 31
#define H 323

int check_slope(char map[W][H], int right, int down)
{
    int trees = 0;
    int x = 0;
    int y = 0;
    while (y < H)
    {
        if (map[x % W][y] == '#')
            trees++;
        x += right;
        y += down;
    }
    return trees;
}

int main()
{
    FILE *fp = fopen("day2020_03.txt","r");

    if (!fp)
    {
        printf("ERREUR: Fichier non trouvé.\n"); 
        return 1;
    }

    char map[W][H]; // 31x323
    for(int j = 0; j < H; j++)
    {
        for(int i = 0; i < W; i++)
        {
            map[i][j] = fgetc(fp);
        }
        assert(fgetc(fp) == '\n');
    }

    fclose(fp);

    printf("Partie 1 : %d\n", check_slope(map, 3, 1));

    // ATTENTION : on doit faire attention a prendre un entier
    // sur 64 bits sinon le résultat provoque un dépassement
    long long total_trees = 1;
    total_trees *= check_slope(map, 1, 1);
    total_trees *= check_slope(map, 3, 1);
    total_trees *= check_slope(map, 5, 1);
    total_trees *= check_slope(map, 7, 1);
    total_trees *= check_slope(map, 1, 2);

    printf("Partie 2 : %lld\n", total_trees);

    return 0;
}
