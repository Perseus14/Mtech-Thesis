#include <stdio.h>
#include <stdlib.h>

int main()
{
    int k, d, i;
    scanf("%d %d", &k, &d);
    if ((d == 0) && (k != 1)) printf("No solution\n");
    else if (d == 0) printf("0\n");
    else {
        for (i = 0; i < k; i++){
            if ((k - i) == 1) printf("%d", d);
            else printf("9");
        }
        printf("\n");
    }
    return 0;
}
