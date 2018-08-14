#include<stdio.h>
#include<stdlib.h>
void main()
{
long long k;long long n;long long d;long long c;
long long x;long long l;
scanf("%lld %lld",&n,&k);

x=n/(2*(k+1));

d=x;
c=d*k;
l=n-c-d;


printf("%lld %lld %lld\n",d,c,l);
exit(0);
}