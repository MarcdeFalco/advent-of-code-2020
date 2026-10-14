/* Advent of Code 2020, jour 10.
 * Après un tri par sélection, la partie 1 compte les écarts de 1 et de 3
 * entre voisins (l'appareil final ajoute un écart de 3).
 * Partie 2 : programmation dynamique de bas en haut : count[i] est la somme
 * des count[j] pour les j < i à distance au plus 3, plus 1 si l'adaptateur
 * se branche directement sur la prise.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void swap(int *t, int i, int j)
{
    int z = t[i];
    t[i] = t[j];
    t[j] = z;
}

void sort(int *t, int n)
{
    for (int i = 0; i < n-1; i++)
    {
        int m = i;
        for (int j = i+1; j < n; j++)
        {
            if (t[j] < t[m])
                m = j;
        }
        swap(t, i, m);
    }
}

int main()
{
    FILE *fp = fopen("day2020_10.txt", "r");
    if (!fp) return 1;

    int nadapters = 0;
    int adapters[500];
    char line[500];
    while( fgets(line, 500, fp) != NULL )
    {
        adapters[nadapters] = atoi(line);
        nadapters++;
    }
    fclose(fp);

    sort(adapters, nadapters);

    int count_1 = 0;
    int count_3 = 1;

    int p = 0;
    for (int i = 0; i < nadapters; i++)
    {
        int n = adapters[i];
        if (n - p == 1) count_1++;
        if (n - p == 3) count_3++;
        p = n;
    }

    printf("Partie 1 : %d\n", count_1 * count_3);
    adapters[nadapters] = 3 + adapters[nadapters-1];

    // Dynamic programming algorithm
    long count[1000] = {};
    for (int i = 0; i <= nadapters; i++)
    {
        int v = adapters[i];

        if (v <= 3) // directly plugged
            count[i]++;

        int j = i-1;
        while(j >= 0 && v - adapters[j] <= 3)
        {
            count[i] += count[j];
            j--;
        }
    }

    printf("Partie 2 : %ld\n", count[nadapters]);

    return 0;
}
