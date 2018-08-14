#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, k, d, c, v, p, t;

    scanf("%d %d", &n,&k);

    t = 2*( k + 1);
    d = n/t;
    c = k*d;
    v = c + d;
    p = n - v;

    printf("%d %d %d", d, c, p);


    return 0;
}
