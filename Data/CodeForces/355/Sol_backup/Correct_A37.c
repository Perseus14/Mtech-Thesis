#include <stdio.h>
int main()
{
    int n,k,i;
    scanf("%d %d",&n,&k);
    if(n>1&&k==0) printf("No solution");
    else{
        for(i=1;i<=n;i++){
            if(i==1) printf("%d",k);
            else printf("0");
        }
    }
    return 0;
}
