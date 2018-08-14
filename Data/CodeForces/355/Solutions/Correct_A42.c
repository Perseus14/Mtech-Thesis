#include<stdio.h>
int main()
{
	int n, d;
	scanf("%d%d", &n, &d);
	if( 0 == d && n > 1 ){
		printf("No solution");
		return 0;
	}
	printf("%d", d);
	n--;
	while( n-- )
		printf("0");
	return 0;
}