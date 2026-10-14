/* Advent of Code 2020, jour 4.
 * Lecture caractère par caractère : deux sauts de ligne consécutifs ferment
 * une fiche. Chaque champ rencontré allume un bit du masque fields_flag ; la
 * fiche est complète quand il vaut 127 = 2^7 - 1 (partie 1). Un booléen
 * retient en parallèle si les valeurs respectent les règles (partie 2).
 * Remarque : la couleur de cheveux est testée avec alnum, qui accepte toutes
 * les lettres minuscules et pas seulement a-f.
 */
#include<stdio.h>
#include<assert.h>
#include<string.h>
#include<stdbool.h>
#include<stdlib.h>

bool alnum(char c)
{
    if (c >= '0' && c <= '9') return true;
    if (c >= 'a' && c <= 'z') return true;
    return false;
}


int main()
{
    FILE *fp = fopen("day2020_04.txt", "r");

    if(!fp)
    {
        printf("File day2020_04.txt is unreadable\n");
        return 1;
    }

    int passports_allfields = 0;
    int passports_valid = 0;
    char fields_flag = 0;

    // As we are reading char by char, we can't check for feof directly in
    // the while condition like in while(!feof(fp)) because this should wait
    // for an extra erroneous read before setting the end-of-file indicator.
    // Instead, we use a feature of the assignation: it returns the assigned
    // value. So we can store and check the value stored directly from the
    // while.
    char c;
    bool current_valid = true;
    bool previous_endline = false;

    while((c = fgetc(fp)) != EOF)
    {
        if (c == '\n' && previous_endline)
        {
            if (fields_flag == 127)
            {
                passports_allfields += 1;
                if (current_valid)
                {
                    passports_valid += 1;
                }
            }
            // end of passport
            fields_flag= 0;
            current_valid = true;
            previous_endline = false;
        }
        else if (c == ' ' || c == '\n')
        {
            previous_endline = c == '\n';
        }
        else
        {
            char code[4];
            char content[100];

            previous_endline = false;
            code[0] = c; // character just read
            code[3] = '\0';
            fscanf(fp, "%c%c:%s", &code[1], &code[2], content);

            if (strncmp(code, "byr", 3) == 0)
            {
                fields_flag = fields_flag | 1;
                int birth_year = atoi(content);
                if (birth_year < 1920 || birth_year > 2002)
                {
                    current_valid = false;
                }
            }
            if (strncmp(code, "iyr", 3) == 0)
            {
                fields_flag = fields_flag | 2;
                int issue_year = atoi(content);
                if (issue_year < 2010 || issue_year > 2020)
                {
                    current_valid = false;
                }
            }
            if (strncmp(code, "eyr", 3) == 0)
            {
                fields_flag = fields_flag | 4;
                int expiration_year = atoi(content);
                if (expiration_year < 2020 || expiration_year > 2030)
                {
                    current_valid = false;
                }
            }
            if (strncmp(code, "hgt", 3) == 0)
            {
                fields_flag = fields_flag | 8;
                int height = atoi(content);
                int n = strlen(content);
                if (content[n-1] == 'm' && content[n-2] == 'c')
                {
                    if (height < 150 || height > 193)
                    {
                        current_valid = false;
                    }
                }
                else if (content[n-1] == 'n' && content[n-2] == 'i')
                {
                    if (height < 59 || height > 76)
                    {
                        current_valid = false;
                    }
                }
                else
                {
                    current_valid = false;
                }
            }
            if (strncmp(code, "hcl", 3) == 0)
            {
                fields_flag = fields_flag | 16;
                if (strlen(content) == 7)
                { 
                    if (content[0] != '#')
                    {
                        current_valid = false;
                    }
                    for(int i = 1; i < 7; i++)
                    {
                        if (!alnum(content[i]))
                        {
                            current_valid = false;
                        }
                    }
                }
                else
                {
                    current_valid = false;
                }
            }
            if (strncmp(code, "ecl", 3) == 0)
            {
                fields_flag = fields_flag | 32;
                if   (strncmp(content, "amb", 3) != 0
                    &&strncmp(content, "blu", 3) != 0
                    &&strncmp(content, "brn", 3) != 0
                    &&strncmp(content, "gry", 3) != 0
                    &&strncmp(content, "grn", 3) != 0
                    &&strncmp(content, "hzl", 3) != 0
                    &&strncmp(content, "oth", 3) != 0)
                {
                    current_valid = false;
                }
            }
            if (strncmp(code, "pid", 3) == 0)
            {
                fields_flag = fields_flag | 64;
                if (strlen(content) == 9)
                {
                    for(int i = 0; i < 9; i++)
                    {
                        if (content[i] < '0' || content[i] > '9')
                        {
                            current_valid = false;
                        }
                    }
                }
                else
                {
                    current_valid = false;
                }
            }
        }
    }

    // last passport
    if (fields_flag == 127)
    {
        passports_allfields += 1;
        if (current_valid)
        {
            passports_valid += 1;
        }
    }
    fclose(fp);

    printf("Partie 1 : %d\n", passports_allfields);
    printf("Partie 2 : %d\n", passports_valid);

    return 0;
}
