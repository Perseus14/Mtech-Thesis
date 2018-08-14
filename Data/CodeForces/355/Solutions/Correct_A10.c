#include <stdio.h>
#include <stdlib.h>

int main()
{
  int  digits, num,i;
    scanf("%d %d",&digits,&num);
    if (num!=0  )
        {   printf("%i",num);
            for (i=0;i<digits-1;i++)
                printf("0");
        }
    else if ( num == 0 && digits==1)
        printf("0");
    else
        printf("No solution");
    return 0;
}
