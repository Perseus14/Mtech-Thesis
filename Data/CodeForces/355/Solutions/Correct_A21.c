#include <stdio.h>

int main()
{
    int d, k, i;
    scanf("%d %d", &k, &d);
    if(d==0 && k>1)
        printf("No solution\n");
    else
    {
        printf("%d", d);
        for(i=0; i<k-1; i++)
            printf("0");
        printf("\n");
    }
    return 0;
}