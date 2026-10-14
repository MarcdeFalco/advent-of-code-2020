/* Advent of Code 2020, jour 5.
 * dicho réduit un intervalle de moitié à chaque lettre (B et R : moitié
 * haute), comme une recherche dichotomique : c'est une lecture en base 2.
 * Partie 1 : plus grand numéro de siège. Partie 2 : un tableau de booléens
 * indexé par numéro ; on saute les places inexistantes du début, puis le
 * bloc occupé, et l'on tombe sur la place libre.
 */
#include <stdio.h>
#include <stdbool.h>
#include <assert.h>

int dicho(bool *path, int path_length, int low, int high)
{
    for(int i = 0; i < path_length; i++)
    {
        int m = (low+high)/2;
        if (path[i])
            low = m+1;
        else
            high = m;
    }

    return low;
}

int main()
{
    FILE *fp = fopen("day2020_05.txt", "r");
    if (!fp) return 1;

    bool seat_taken[128 * 8] = {};
    int max_seat_id = -1;

    char c;
    while((c = fgetc(fp)) != EOF)
    {
        bool row[7] = {};
        bool col[3] = {};

        row[0] = c == 'B';
        for(int i = 1; i < 7; i++)
            row[i] = fgetc(fp) == 'B';
        for(int i = 0; i < 3; i++)
            col[i] = fgetc(fp) == 'R';

        int row_id = dicho(row, 7, 0, 127);
        int col_id = dicho(col, 3, 0, 7);

        int seat_id = 8 * row_id + col_id;
        if(seat_id > max_seat_id)
            max_seat_id = seat_id;

        seat_taken[seat_id] = true;

        fgetc(fp); // saut de ligne
    }

    printf("Partie 1 : %d\n", max_seat_id);

    int i = 0;
    // premières rangées libres
    while(!seat_taken[i])
    {
        i++;
    }
    // tout complet
    while(seat_taken[i])
    {
        i++;
    }
    // jusqu'à la place libre
    
    printf("Partie 2 : %d\n", i);

    fclose(fp);

    return 0;
}
