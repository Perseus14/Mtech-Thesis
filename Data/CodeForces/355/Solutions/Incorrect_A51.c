#include<stdio.h>
int main()
{
	int k,d,i;
	scanf("%d %d",&k,&d);
	if(d==0&&k>1)
		printf("No Solution");
	else
	{
		printf("%d",d);
		for(i=1;i<k;i++)
		{
			printf("%d",0);
		}
	}
	printf("\n");
	return 0;
}
