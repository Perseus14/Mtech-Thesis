#include<stdio.h>
#include<math.h>
int main()
{
	long int n,m,a;
	long int p;
	scanf("%li %li %li",&n,&m,&a);
	p=ceil((double)n/a)*ceil((double)m/a);
	printf("%li",p);
	return 0;
}
