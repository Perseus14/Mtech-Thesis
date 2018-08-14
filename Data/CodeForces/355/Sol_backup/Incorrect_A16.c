#include <stdio.h>

int main()
{
	int k, d, i, r;

	scanf ("%d %d", &k, &d);

	for (i = 1; i < k; i++)
		putchar ('9');

	r = ((d + 10) - ((k - 1) * 9) % 10) % 10;

	putchar (r + '0');

	return 0;
}
