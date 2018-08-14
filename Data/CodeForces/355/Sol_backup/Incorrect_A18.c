#include <stdio.h>
#include <stdlib.h>

int main()
{
    double  digits, num,i;
    scanf("%e %e",&digits,&num);
    for (i=0; i<digits-1; i++)
        num=num*10;
    if (num!=0)
        printf("%e",num);
    else if ( num == 0 && digits>1)
        printf("No solution");
    else
        printf("0");

    return 0;
}
