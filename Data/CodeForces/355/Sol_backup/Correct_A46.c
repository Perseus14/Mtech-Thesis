#include<stdio.h>
int main()
{
	int i,j,n,k,d;
	scanf("%d%d",&k,&d);
	if(d==0&&k>=2)
	{
		printf("No solution\n");
	}
	else		
	{
		printf("%d",d);
		for(i=1;i<k;i++)
		{
			printf("0");
		}
		printf("\n");
	}
	return 0;
}



