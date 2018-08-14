#include<stdio.h>
main()
{
	int n, k, i, p=1;
	scanf("%d%d", &n, &k);
	if (n==1)
	{
		printf("%d\n", k);
	}
	else
	{
		for (i=1; i<n; i++)
		{
			p=p*10;
		}
		printf("%d\n", p+k-1);
	}
}