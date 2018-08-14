#include<stdio.h>
int main()
{
	int n;
	scanf("%d", &n);
	printf("%d", n);
	n--;
	while( n-- )
		printf("0");
	return 0;
}