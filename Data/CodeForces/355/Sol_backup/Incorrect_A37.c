#include<stdio.h>
#include<math.h>
int main()
{
	long long k,d,ans=0,o=0,m;
	scanf("%d%d",&k,&d);
	if(d==0&&k==1)
	{
		ans=0;
		o=1;
	}
	else if(d==0&&k!=1)
	{
		o=2;
	}
	else
	{
		m=pow(10,k-1);
		ans=d*m;
		o=1;
	}
	if(o=1)
	printf("%ld",ans);
	else
	printf("No solution");
}