/* Problem: 355A - Vasya and Digital Root */
/* Solver: Gusztav Szmolik */

#include <stdio.h>

int main ()
    {
    unsigned short k;
    unsigned short d;
    unsigned short kd;
    unsigned short i;
    
    if (scanf("%hu %hu",&k,&d) != 2)
        return -1;
    if (k < 1 || k > 1000 || d > 9)
        return -1;
    if (!d && k > 1)
        {
        printf ("No solution\n");
        return 0;
        }
    putchar ('0'+d);
    kd = k-1;
    for (i = 0; i < kd; i++)
        putchar ('0');
    putchar ('\n');
    return 0;
    }
