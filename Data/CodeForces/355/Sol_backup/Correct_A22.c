#include <stdio.h>

int main(int argc, char const *argv[])
{
	int k, d, i;

	scanf("%d %d", &k, &d);
	if (d == 0 && k != 1)
	{
		printf("No solution");
		return 0;
	}
	else
	{
		printf("%d", d);
		for (i = 1; i < k; ++i)
		{
			printf("0");
		}
	}
	return 0;
}