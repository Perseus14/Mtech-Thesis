#include <stdio.h>
int dr(int n)
{
	int result = 0;
	while (n > 0)
	{
		result += (n % 10);
		n /= 10;
	}
	if (result < 10)
	{
		return result;
	}
	else
	{
		return dr(result);	
	}
}

int main(void) {
	// implement digit root function
	// increase until get required number
	int k,d;
	scanf("%d %d", &k, &d);
	int number = 1;
	for (int i = 0; i <k-1; i++)
	{
		number *= 10;
	}
	if (k == 1 && d== 0)
	{
		printf("0");
		return 0;
	}
	while (dr(number) != d)
	{
		number++;
	}
	printf("%d", number);
	
	
}
