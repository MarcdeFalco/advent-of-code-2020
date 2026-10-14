/* Advent of Code 2020, jour 9.
 * Partie 1 : pour chaque nombre, on cherche une paire de somme égale parmi
 * les 25 précédents (double boucle). Partie 2 : les nombres étant positifs,
 * deux pointeurs délimitent une plage dont la somme glisse : on avance la
 * borne haute si la somme est trop petite, la borne basse sinon, en O(n).
 */
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

/* Returns next positive number in file stream fp
 * returns -1 if end of file
 */
long next_number(FILE *fp)
{
    char line[500];
    if (fgets(line, 500, fp) == NULL)
        return -1;

    return atol(line);
}

bool valid(long *message, int i)
{
    for (int j = i-25; j < i; j++)
        for (int k = j+1; k < i; k++)
            if (message[j] + message[k] == message[i])
                return true;
    return false;
}

int main()
{
    FILE *fp = fopen("day2020_09.txt", "r");
    if (!fp) return 1;

    long message[1000];
    int i = 0;
    long r;
    while( (r = next_number(fp)) != -1 )
    {
        message[i] = r;
        i++;
    }

    i = 25;
    while (valid(message, i))
    {
        i++;
    }
    printf("Partie 1 : %ld\n", message[i]);

    // O(n) algorithm using a sliding sum as summing natural integers is always
    // increasing.
    long target = message[i];
    int low = 0;
    int high = 1;
    long s = message[low] + message[high];
    while(high < 1000 && s != target)
    {
        if (s < target)
        {
            high++;
            s += message[high];
        }
        else
        {
            s -= message[low];
            low++;
            if (low == high)
            {
                high++;
                s += message[high];
            }
        }
    }

    long min = message[low];
    long max = message[low];
    for(i = low+1; i <= high; i++)
    {
        long v = message[i];
        if (v < min) min = v;
        if (v > max) max = v;
    }
    printf("Partie 2 : %ld\n", min+max);
    
    fclose(fp);

    return 0;
}
