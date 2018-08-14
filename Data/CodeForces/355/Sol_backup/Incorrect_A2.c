#include<stdio.h>
main()
{
	int n, k, i;
	char a[1010];
	scanf("%d%d", &n, &k);
	if (n==1)
	{
		printf("%d\n", k);
	}
	else
	{
		a[0]='1';
		for (i=1; i<n-1; i++)
		{
		a[i]='0';
		}
		if (k==1)
		{
			a[n-1]='0';
		}
		else if (k==2)
		{
			a[n-1]='1';
		}
		else if (k==3)
		{
			a[n-1]='2';
		}
		else if (k==4)
		{
			a[n-1]='3';
		}
		else if (k==5)
		{
			a[n-1]='4';
		}
		else if (k==6)
		{
			a[n-1]='5';
		}
		else if (k==7)
		{
			a[n-1]='6';
		}
		else if (k==8)
		{
			a[n-1]='7';
		}
		else if (k==9)
		{
			a[n-1]='8';
		}
		printf("%s\n", a);
	}
}