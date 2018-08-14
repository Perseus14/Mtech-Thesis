#include<stdio.h>
int main()
{
	int k,d,ans=0,m,n=1;
	scanf("%d%d",&k,&d);
	if(k==1&&d==0)
	{
		ans=0;
		printf("%d",ans);
	}
	else if(k!=1&&d==0)
		printf("No solution");
		else
		{
		ans=d;
		printf("%d",ans);
		for(m=0;m<k-1;m++)
		printf("0");
	}
}