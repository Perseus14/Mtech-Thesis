#include<stdio.h>
main()
{
    int k,d;
    scanf("%d %d",&k,&d);
    if(k>1&&d==0) printf("No solution");
    else
    {
        printf("%d",d);
        while(k>1)
        {
            printf("0");k--;
        }
    }
    return 0;
}


