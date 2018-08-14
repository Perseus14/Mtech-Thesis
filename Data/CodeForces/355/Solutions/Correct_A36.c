#include <stdio.h>
#include <string.h>
#include <math.h>
#define ABS(x) ((x) < 0 ? -1*(x) : (x))
#define MAX(x,y) ((x) > (y) ? (x) : (y))
#define MIN(x,y) ((x) < (y) ? (x) : (y))
#define MOD 1000000007
#define INF 2000000000

int main()
{
    int k,d,i;
    scanf("%d",&k);
    scanf("%d",&d);

    if(d == 0)
    {
        if(k == 1)
            printf("0\n");
        else
            printf("No solution\n");

        return 0;
    }

    printf("%d", d);

    for(i = 1; i < k; ++i)
        printf("0");

    printf("\n");

    return 0;
}