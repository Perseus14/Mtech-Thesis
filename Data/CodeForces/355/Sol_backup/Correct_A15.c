#include<stdio.h>
#include<math.h>
int main()
{
    long long k,d,n,i;
    scanf("%I64d %I64d",&k,&d);
    if(d==0){
        if(k==1)printf("0");
        else printf("No solution");
    }
    if(d>0){
        printf("%I64d",d);
        for(i=1;i<=k-1;i++){
            printf("0");
        }

    }
}