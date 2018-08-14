#include<stdio.h>
#include<string.h>
int main() {
int n,k;
int s;
scanf("%d%d",&n,&k);
if (k==0) printf("0");
else {
    printf("%d",k);
    for(s=0;s<n-1;s++) printf("0");
}
return 0;
}
