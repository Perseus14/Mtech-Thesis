#include<stdio.h>
#include<string.h>

int main(){
    int n,j,i,d,k,c=0;
    scanf("%d %d",&k,&d);
    if(d==0&&k==1){printf("0");return 0;}
    if(d==0&&k!=1){printf("No solution");return 0;}

    if(k>=d){
        for(i=0;i<d;i++){
            printf("1");
        }
        for(i=0;i<k-d;i++){
            printf("0");
        }
        return 0;
    }
    if(d>k){
        for(i=0;i<k-1;i++){
            printf("%d",d/k);
            c=c+d/k;
        }
        printf("%d",d-c);
    }
    return 0;
}

