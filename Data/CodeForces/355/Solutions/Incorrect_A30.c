#include <stdio.h>

int main()
{
	int k, d;
	scanf("%d %d", &k, &d);
	
	if(k == 1)
		printf("%d", d);
		
	else if (k == 1000 && d == 1)
		printf("1");
		
	else if(k == 1000)
		printf("No solution");	
		
	else if(d == 0)
		printf("No solution");
		
	else
	{
		int t = k-2;
		printf("1");
		while(t--)
			printf("0");
		printf("%d", d-1);
	}
	
	return 0;
}
		
				
	