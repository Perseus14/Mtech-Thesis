#include<stdio.h>
#include<string.h>

int main(){
    int n,j,i,flag=0,d,k;
    scanf("%d %d",&k,&d);
    if(d==0&&k==1){printf("0");return 0;}
    if(d==0&&k!=1){printf("No solution");}
    while((d/k)<1){d=d*10;}
    for(i=1;i<k;i++){
        printf("%d",d/k);
    }
    printf("%d",d-(k-1)*(d/k));
    return 0;
}

