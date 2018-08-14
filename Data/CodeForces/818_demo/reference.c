#include <stdio.h>
# include <assert.h>
int main()
{
    unsigned long n,k;
    scanf("%lu %lu",&n,&k);
    assert(n>=1 && n<=1000000000000);
    assert(k>=1 && k<=1000000000000);
    long long d=(n/2)/(k+1);
    printf("%lld %lld %lld\n",d,k*d,n-(k+1)*d);
    return 0;
} 
