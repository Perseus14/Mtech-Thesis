#include <stdio.h>

int main()
{
	int k, d, i;

	scanf ("%d %d", &k, &d);

	if (k > 1 && d == 0)
		puts ("No solution");
	else {
		for (i = 1; i < k; i++)
			putchar ('9');

		putchar (d + '0');
	}

	return 0;
}
