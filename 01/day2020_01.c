/* Advent of Code 2020, jour 1.
 * Partie 1 : deux boucles imbriquées sur des indices croissants (j > i),
 * en O(n^2). Partie 2 : trois boucles (k > j > i), en O(n^3) ; cela suffit
 * pour quelques centaines de nombres.
 */
#include <stdio.h>

int main()
{
    FILE *fp = fopen("day2020_01.txt", "r");
    int data[1000] = {};
    int ndata = 0;

    while(!feof(fp))
    {
        fscanf(fp, "%d\n", &data[ndata]);
        ndata++;
    }
    printf("%d entiers lus.\n", ndata);

    printf("Partie 1\n");
    for(int i = 0; i < ndata; i++)
    {
        for(int j = i+1; j < ndata; j++)
        {
            if(data[i]+data[j] == 2020)
            {
                printf("La réponse est %d\n", data[i]*data[j]);
            }
        }
    }

    printf("Partie 2\n");
    for(int i = 0; i < ndata; i++)
    {
        for(int j = i+1; j < ndata; j++)
        {
            for(int k = j+1; k < ndata; k++)
            {
                if(data[i]+data[j]+data[k] == 2020)
                {
                    printf("La réponse est %d\n", data[i]*data[j]*data[k]);
                }
            }
        }
    }

    return 0;
}
