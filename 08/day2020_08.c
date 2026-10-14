/* Advent of Code 2020, jour 8.
 * L'état de la machine se réduit au compteur ordinal et à l'accumulateur ;
 * repasser par une instruction signifie boucler. On marque les instructions
 * exécutées dans un tableau de booléens.
 * Partie 1 : accumulateur juste avant la boucle. Partie 2 : on essaie chaque
 * échange jmp/nop jusqu'à ce que le programme se termine, en O(n^2).
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

const int ACC = 0;
const int JMP = 1;
const int NOP = 2;

struct instr {
    int opcode;
    int arg;
};
typedef struct instr instr;

int execute(instr program[1000], int ninstr, bool *terminates)
{
    int acc = 0;
    int pc = 0;
    bool watch[1000] = {};
    while(pc < ninstr)
    {
        if(watch[pc])
            break;
        watch[pc] = true;
        if (program[pc].opcode == JMP)
            pc += program[pc].arg;
        else
        {
            if (program[pc].opcode == ACC)
            {
                acc += program[pc].arg;
            }
            pc++;
        }
    }

    // terminating flag is optional
    if(terminates)
    {
        *terminates = pc == ninstr;
    }

    return acc;
}

int main()
{
    FILE *fp = fopen("day2020_08.txt", "r");
    if(!fp) return 1;

    instr program[1000];
    int ninstr = 0;
    char line[400];
    while( fgets(line, 400, fp) != NULL )
    {
        instr i;
        if (strncmp(line, "acc", 3) == 0)
            i.opcode = ACC;
        if (strncmp(line, "nop", 3) == 0)
            i.opcode = NOP;
        if (strncmp(line, "jmp", 3) == 0)
            i.opcode = JMP;
        i.arg = atoi(&(line[5]));
        if (line[4] == '-')
            i.arg  = -i.arg;
        program[ninstr] = i;
        ninstr++; 
    }

    printf("Partie 1 : %d\n", execute(program, ninstr, NULL));

    for (int i = 0; i < ninstr; i++)
    {
        int opcode = program[i].opcode;
        if (opcode == ACC)
            continue;
        if (opcode == NOP)
            program[i].opcode = JMP;
        else
            program[i].opcode = NOP;

        bool terminates;
        int acc = execute(program, ninstr, &terminates);
        if(terminates)
        {
            printf("Partie 2 : %d\n", acc);
            break;
        }

        program[i].opcode = opcode;
    }

    fclose(fp);
        
    return 0;
}
