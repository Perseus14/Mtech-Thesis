#include <stdio.h>

int main()
{
	int a, b;

	scanf("%d%d", &a, &b);
	if (b != 0)
		if (a == 1)
			printf("%d\n", b);
		else
			printf("%d%0*d\n", b, a - 1, 0);
	else if (a == 1)
		printf("0\n");
	else
		printf("No solution\n");

	return 0;
}
