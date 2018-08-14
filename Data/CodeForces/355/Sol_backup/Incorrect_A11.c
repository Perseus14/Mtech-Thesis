#include <stdio.h>

int k, d;
int i;

int main ()
{
	scanf ( "%d%d", &k, &d );

	if ( k >= d )
	{
		for ( i = 0; i < d; ++ i )
			putchar ( '1' );
		for ( i = 0; i < k-d; ++ i )
			putchar ( '0' );
	}
	else
	{
		for ( i = 0; i < k-1; ++ i )
			putchar ( '1' );
		putchar ( d-k+1+'0' );
	}

	putchar ( '\n' );

	return 0;
}
