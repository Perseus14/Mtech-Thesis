#include <stdio.h>
#include <math.h>

int s (int n)
{
	int k = 0;
	while (n != 0)
	{
		k += n % 10;
		n = n / 10;
	}
	if (k > 9)
	{
		k = s(k);
	}
	return (k);
}

int main(int argc, char const *argv[])
{
	int k, d;
	int i;

	scanf("%d %d", &k, &d);
	if (d == 0)
	{
		printf("0");
		return 0;
	}
	for (i = ceil(pow(10, k - 1)); i < (pow(10, k ) - 1); ++i)
	{
		printf("i=%d\n", i );
		if (s(i) == d)
		{
			return 0;
		}
	}
	printf("No solution");
	return 0;
}