#include<stdio.h>
#include<math.h>
int main()
{
	int k,d;
	scanf("%d%d",&k,&d);
	int i,flag=0;
	if(k==1)
	{
		printf("%d",d);
		return 0;
	}
	else  if(d==0 && k>1)
		flag=0;
	else
	{
		printf("1");
		for(i=0;i<k-2;i++)
			printf("0");
		printf("%d",d-1);
		flag=1;
	}
	if(flag==0)
		printf("No solution");
	return 0;
}
