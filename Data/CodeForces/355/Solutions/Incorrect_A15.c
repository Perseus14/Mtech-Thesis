#include <stdio.h>

int main()
{
	int k, d, i;

	scanf ("%d %d", &k, &d);

	for (i = 1; i < k; i++)
		putchar ('9');

	putchar (d + '0');

	return 0;
}
