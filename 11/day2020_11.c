/* Advent of Code 2020, jour 11.
 * Simulation synchrone avec double tampon (dest) jusqu'au point fixe.
 * Partie 1 : les 8 voisins immédiats ; partie 2 : dans chacune des 8
 * directions, on avance tant qu'on voit du sol (comme un rayon). Les deux
 * parties partagent la boucle, le seuil passant de 4 à 5 avec 4 + part.
 */
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#define W 91
#define H 97

int main()
{
    for (int part = 0; part < 2; part++)
    {
        char map[W][H];

        FILE *fp = fopen("day2020_11.txt", "r");
        if(!fp) return 1;
        
        for(int j = 0; j < H; j++)
        {
            for(int i = 0; i < W; i++)
                map[i][j] = fgetc(fp);
            fgetc(fp); // end of line
        }

        fclose(fp);

        bool changed = true;
        while(changed)
        {
            char dest[W][H];
            changed = false;
            for(int i = 0; i < W; i++)
                for(int j = 0; j < H; j++)
                {
                    int occupied = 0;

                    if (part == 0)
                    {
                        for (int di = i-1; di <= i+1; di++)
                            for (int dj = j-1; dj <= j+1; dj++)
                                if((di != i || dj != j) && 0 <= di && di < W 
                                    && 0 <= dj && dj < H && map[di][dj] == '#')
                                    occupied++;
                    }
                    else
                    {
                        for (int di = -1; di <= 1; di++)
                            for (int dj = -1; dj <= 1; dj++)
                            {
                                if(di == 0 && dj == 0)
                                    continue;
                                int x = i + di;
                                int y = j + dj;
                                while(0 <= x && x < W 
                                   && 0 <= y && y < H
                                   && map[x][y] == '.')
                                {
                                    x += di;
                                    y += dj;
                                }
                                if(0 <= x && x < W 
                                   && 0 <= y && y < H
                                   && map[x][y] == '#')
                                    occupied++;
                            }
                    }

                    if (map[i][j] == '#' && occupied >= 4 + part)
                    {
                        changed = true;
                        dest[i][j] = 'L';
                    }
                    else if (map[i][j] == 'L' && occupied == 0)
                    {
                        changed = true;
                        dest[i][j] = '#';
                    }
                    else
                        dest[i][j] = map[i][j];
                }

            for(int j = 0; j < H; j++)
                for(int i = 0; i < W; i++)
                    map[i][j] = dest[i][j];
        }

        int count = 0;
        for(int i = 0; i < W; i++)
            for(int j = 0; j < H; j++)
                if(map[i][j] == '#')
                    count++;

        printf("Partie %d : %d\n", part+1, count);
    }

    return 0;
}
