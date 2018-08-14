#include<stdio.h>
int main()
{
    int i,j,d,k,t,a,b,p=0,x,y;
    scanf("%d%d",&k,&d);
    int arr[k];
    for(i=0;i<k;i++)
    arr[i]=0;
    if(d==0&&k==1)
    printf("0");
    else if(d==1&&k==1)
    printf("1");
    else
    {
        if(d==1)
    d=d*10;
    for(i=1;i<=d;i++)
    {
        t=i*10+(d-i);
        x=t/9;
        y=t%9;
        if(t%9==0)
        a=x;
        else
        a=x+1;
        if(a<=k)
        {
            p=1;
        }
        if(p==1)
        break;
    }
    }
    if(p==1&&d>0)
    {
        if(a==x)
        {
            for(j=0;j<a;j++)
            arr[j]=9;
        }
        else
        {
            for(j=0;j<a;j++)
            arr[j]=9;
            arr[j]=y;
        }
         for(i=0;i<k;i++)
    printf("%d",arr[i]);
    }
    if(p==0&&k!=1)
    printf("No solution");
}