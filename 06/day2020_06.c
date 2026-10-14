/* Advent of Code 2020, jour 6.
 * Pour chaque groupe, un tableau de 128 compteurs indexé par code ASCII
 * compte le nombre de personnes qui ont coché chaque lettre : la lettre est
 * dans l'union si son compteur est non nul (partie 1), dans l'intersection
 * s'il vaut le nombre de personnes du groupe (partie 2).
 * Fragilité : si le fichier se terminait par une ligne vide, la boucle
 * externe traiterait un groupe vide et ajouterait 128 à la partie 2.
 */
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

int main()
{
    FILE *fp = fopen("day2020_06.txt", "r"); 
    if (!fp) return 1;

    int count_any = 0;
    int count_all = 0;

    while(!feof(fp))
    {
        int any[128] = {};

        int nanswer = 0;
        char answer[200];

        while(fgets(answer, 200, fp))
        {
            if (answer[0] == '\n') // dernière réponse
                break;

            int i = 0;
            while(answer[i] != '\n')
            {
                any[answer[i]]++;
                i++;
            }
            nanswer++;
        }

        for (int i = 0; i < 128; i++)
        {
            if (any[i] > 0) count_any++;
            if (any[i] == nanswer) count_all++;
        }
    }

    printf("Partie 1 : %d\n", count_any);
    printf("Partie 2 : %d\n", count_all);

    fclose(fp);

    return 0;
}
