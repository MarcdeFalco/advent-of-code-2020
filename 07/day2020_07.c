/* Advent of Code 2020, jour 7.
 * Graphe orienté acyclique pondéré : bags_content[i] est la liste des
 * couples (quantité, indice du sac contenu), terminée par -1.
 * Partie 1 : sacs depuis lesquels on atteint « shiny gold » (parcours
 * récursif, non mémoïsé). Partie 2 : nombre de sacs contenus, par la
 * récurrence N(a) = 1 + somme des k * N(b), moins le sac lui-même.
 */
#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int search_bag_name(char bags[1000][100], int nbags, char *name)
{
    for(int i = 0; i < nbags; i++)
    {
        if(strncmp(name,bags[i], 100) == 0)
            return i;
    }

    return -1;
}

char *read_bag_name(char *line, char *name)
{
    char *word;
    while((word = strtok(line, " ")) != NULL)
    {
        if (strncmp(word, "bag", 3) == 0)
        {
            return name;
        }
        strcat(name, word);
        line = NULL; // for strtok to work on the same line
    }

    return NULL;
}

bool part1_rec_search(int bags[1000][100], int nbags, int start, int shiny_gold)
{
    int i = 0;
    bool found = false;

    while(bags[start][i] != -1)
    {
        int b = bags[start][i+1];
        if (b == shiny_gold) return true;
        found = found || part1_rec_search(bags, nbags, b, shiny_gold);
        i += 2;
    }

    return found;
}

/* Basic algorithm is tree recursive traversal.
 * For each node, recurse into each children nodes.
 */
int part1(int bags[1000][100], int nbags, int shiny_gold)
{
    int s = 0;
    for(int i = 0; i < nbags; i++)
    {
        if(part1_rec_search(bags, nbags, i, shiny_gold))
        {
            s++;
        }
    }
    return s;
}

int part2_rec_count(int bags[1000][100], int nbags, int start)
{
    int i = 0;
    int count = 1;

    while(bags[start][i] != -1)
    {
        int b = bags[start][i+1];
        count = count + part2_rec_count(bags, nbags, b) * bags[start][i];
        i += 2;
    }

    return count;
}

int part2(int bags[1000][100], int nbags, int shiny_gold)
{
    return part2_rec_count(bags, nbags, shiny_gold);
}

int main()
{
    FILE *fp = fopen("day2020_07.txt", "r");
    if(!fp) return 1;
    
    char bags_name[1000][100]; // 1000 bags name of length at most 100
    int nbags = 0; // count of bags
    int bags_content[1000][100]; // 1000 bags name containing at most 100 bags
    // bags_content is an array of n entries of 2 int : count of bag, idx of
    // bag in bags_name
    for(int i = 0; i < 1000; i++)
        bags_content[i][0] = -1; // sentinel for end of list of content

    char line[500];
    while(fgets(line, 500, fp) != NULL)
    {
        char container[100] = "";

        read_bag_name(line, container);
        int container_idx = search_bag_name(bags_name, nbags, container);
        if (container_idx < 0)
        {
            strcpy(bags_name[nbags], container);
            container_idx = nbags;
            nbags++;
        }

        strtok(NULL, " "); // contain
        
        int content_count = 0;
        // scanning for content
        while(true)
        {
            char *num = strtok(NULL, " "); // indication de nombre
            if (num == NULL || strncmp(num, "no", 2) == 0)
                break; // soit fin de phrase, soit no other bags

            int count = atoi(num);
            char content[100] = "";

            read_bag_name(NULL, content);
            int content_idx = search_bag_name(bags_name, nbags, content);
            if (content_idx < 0)
            {
                strcpy(bags_name[nbags], content);
                content_idx = nbags;
                nbags++;
            }
            bags_content[container_idx][content_count] = count;
            bags_content[container_idx][content_count+1] = content_idx;
            bags_content[container_idx][content_count+2] = -1;
            content_count += 2;
        }
    }

    int shiny_gold = search_bag_name(bags_name, nbags, "shinygold");

    printf("Partie 1 : %d\n", part1(bags_content, nbags, shiny_gold));
    printf("Partie 2 : %d\n", part2(bags_content, nbags, shiny_gold)-1);

    fclose(fp);

    return 0;
}
