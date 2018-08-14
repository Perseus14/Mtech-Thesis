#include<stdio.h>

int main()
{
    long long int n , c , d , x,k ;
    scanf("%lld%lld",&n,&k);
    d= (n/(2*(k+1)));
    printf("%lld", d );
    c = k*(n/(2*(k+1)));
    printf(" %lld",c);
    printf(" %lld\n",(n-(c+d)));
    
    
    return 0;
}