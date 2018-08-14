#include <stdio.h>
int main(){
int n,k,i,d,m,c;
scanf("%d",&n);
scanf("%d",&k);
c=n/2;
i=0;
while(m<c){

   d=k*i;
   ++i;
   m=i*(1+k);
}
printf("%d %d %d",i,d,n-(i+d));
return 0;
}
