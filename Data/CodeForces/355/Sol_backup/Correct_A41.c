#include<stdio.h>

int main(){

    int k,d,i;

    scanf("%d%d",&k,&d);

    if(k>1 && d==0){
        printf("No solution");
    }
    else{
        printf("%d",d);
        for(i=0;i<k-1;i++){
            printf("%d",0);
        }
    }

    return 0;

}