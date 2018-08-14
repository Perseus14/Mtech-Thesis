#include<stdio.h>
int main()
{
    int k,d,i;
    scanf("%d %d",&k,&d);
    if(d==0)
    {
        printf("0");
        return 0;
    }
    printf("%d",d);
    for(i=1;i<k;i++)
    {
        printf("0");
    }
}
