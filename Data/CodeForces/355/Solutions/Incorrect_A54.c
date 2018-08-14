#include <stdio.h>

int main(void) {
    // your code goes here
    int n,d,i;
    scanf("%d %d",&n,&d);
    int a[n];
    for(i=0;i<n;i++)
    a[i]=0;
    if(d==0)
    {
        if(n>1)
        printf("No solution");
        else
        printf("0");
    }
    else
    {
        if(d==1)
        {
            a[0]=1;
            a[n-1]=9;
        }
        else
        {
            a[0]=1;
            
            a[n-1]=d-1;
        }
    for(i=0;i<n;i++)
    printf("%d",a[i]);
    }
    return 0;
}
