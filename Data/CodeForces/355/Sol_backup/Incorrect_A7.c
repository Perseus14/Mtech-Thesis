#include<stdio.h>
#include<math.h>
int main()
{
	long long int k,d;
	scanf("%I64d%I64d",&k,&d);
	long long int i,flag=0;
	if(d==9)
		d=9-d;
	else if(d==0 && k==1)
	{
		printf("0");
		return 0;
	}
	else  if(d==0 && k>1)
		flag=0;
	else
	{
		printf("1");
		for(i=0;i<k-2;i++)
			printf("0");
		printf("%I64d",d-1);
		flag=1;
	}
	if(flag==0)
		printf("No solution");
	return 0;
}
