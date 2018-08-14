#include<stdio.h>
int main() {
int n,k;
int s;
scanf("%d%d",&n,&k);
if (k==0 && n==1) printf("0");
else if (k==0 && n!=1) printf("No solution");
else {
    printf("%d",k);
    for(s=0;s<n-1;s++) printf("0");
}
return 0;
}
