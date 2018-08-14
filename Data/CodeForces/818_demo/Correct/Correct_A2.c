#include <stdio.h>
int main()
{
    long long n,k;
    scanf("%lld %lld",&n,&k);
    long long d=(n/2)/(k+1);
    printf("%lld %lld %lld\n",d,k*d,n-(k+1)*d);
    return 0;
} 