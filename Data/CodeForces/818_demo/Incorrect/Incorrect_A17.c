#include<stdio.h>
int main()
{
    int n,k,t,u;
    while(scanf("%d%d",&n,&k)==2)
    {
        t=(n/2)/(k+1);
        u=k*t;
        printf("%d %d %d\n",t,u,n-t-u);
    }
}
