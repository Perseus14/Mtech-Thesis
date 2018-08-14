#include<stdio.h>

int main()
{
	int k,d,i;
	
	scanf("%d%d",&k,&d);
	
	if(k==1)
		printf("%d",d);
	else
	{
		int a[10]={0,10,11,12,13,14,15,16,17,18};
		
		if(k==2)
			printf("%d",a[d]);
		else
		{
			printf("%d",a[d]-9);
			for(i=1;i<=k-2;i++)
				printf("0");
			printf("9");
			
		}

	}
	
	return 0;
}