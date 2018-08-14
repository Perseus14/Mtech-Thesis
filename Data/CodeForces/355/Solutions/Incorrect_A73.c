#include<stdio.h>
#include<math.h>
int main()
{
    int k,d;
    long long num;
    scanf("%d %d",&k,&d);
    if(d==0)
    {
        if(k==1)
            printf("0");
        else
            printf("No Solution");
    }
    else
     {
         num=d*pow(10,k-1);
         printf("%lld",num);
     }

    return 0;
}
