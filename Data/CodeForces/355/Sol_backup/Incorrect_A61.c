#include<stdio.h>
int main()
{
	int i,k,d;
	scanf("%d %d",&k,&d);
	if(d==0)
		printf("No solution");
	else{
	printf("%d",d);
	for(i=1;i<k;i++)
		printf("0");}
return 0;
}
