#include<stdio.h>
int main()
{
int k,d,i;
scanf("%d %d",&k,&d);
for(i=0;i<k;i++)
{
if(i==0)
printf("%d",d);
else
printf("0");
}
return 0;
}
