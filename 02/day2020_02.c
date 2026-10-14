/* Advent of Code 2020, jour 2.
 * Chaque ligne est lue d'un coup avec fscanf et le format "%d-%d %c: %s".
 * Partie 1 : nombre d'occurrences du caractère entre i et j.
 * Partie 2 : le caractère est en position i ou en position j, mais pas aux
 * deux (ou exclusif).
 */
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

struct entree {
    int i;
    int j;
    char c;
    char password[100];
};
typedef struct entree entree;

int main()
{
    FILE *fp = fopen("day2020_02.txt", "r");

    entree entrees[2000];
    int n = 0;
    while(!feof(fp))
    {
        fscanf(fp, "%d-%d %c: %s\n",
                &entrees[n].i, &entrees[n].j, 
                &entrees[n].c, entrees[n].password);
        n++;
    }

    fclose(fp);

    int count_valid = 0;
    for (int i = 0; i < n; i++)
    {
        entree e = entrees[i];
        int count = 0;
        for (int j = 0; j < strlen(e.password); j++)
        {
            if (e.c == e.password[j])
            {
                count++;
            }
        }
        bool valid = count >= e.i && count <= e.j;
        if (valid)
        {
            count_valid++;
        }
    }

    printf("Partie 1 : %d\n", count_valid);

    count_valid = 0;
    for (int i = 0; i < n; i++)
    {
        entree e = entrees[i];
        bool eci = e.password[e.i-1] == e.c;
        bool ecj = e.password[e.j-1] == e.c;

        bool valid = (eci && !ecj) || (ecj && !eci);
        // oui, on pouvait aussi utiliser xor directement avec eci ^ ecj

        if (valid)
        {
            count_valid++;
        }
    }

    printf("Partie 2 : %d\n", count_valid);

    return 0;
}
