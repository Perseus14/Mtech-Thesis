#include<stdio.h>
int main()
{
	int n, d;
	scanf("%d%d", &n, &d);
	printf("%d", d);
	n--;
	while( n-- )
		printf("0");
	return 0;
}