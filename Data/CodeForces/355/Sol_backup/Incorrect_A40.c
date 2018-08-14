#include <stdio.h>
#include <stdlib.h>

int main()
{
    int k,d;
    int i,j,flag = 1,t ;
    scanf("%d %d",&k,&d);

    if(d == 0 && k == 1)
    {

        printf("0");
        return 0 ;
    }
    else if ( d == 0 && k != 1)
    {
        printf("No solution");
        return 0;
    }
    else
    {

            for(j=1;flag;j++)
            {
                if(d == 1  + j )
                {
                    flag = 0;
                }
            }

    }

    int s;

    s = 10 + j-1;
    flag = 1;

    for(i=1;i<=9&&flag;i++)
    {
        for(j=1;j<=9&&flag;j++)
        {
            if(i+j == s)
            {
                flag = 0;
            }
        }
    }

    if(flag == 0)
    {
        printf("%d%d",i-1,j-1);
        for(t =0 ;t<k-2; t++)
        {
            printf("0");
        }
    }
    else
    {
        printf("No solution");
    }

    return 0;
}
