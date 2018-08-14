#include <stdio.h>
#include <stdlib.h>

int main()
{
    int  digits , num ,i;
   scanf("%i %i ",&digits,&num);
   for (i=0;i<digits;i++)
    num=num*10;
    if (num!=0)
   printf("%i",&num);
   else
    printf("No solution");
    return 0;
}
