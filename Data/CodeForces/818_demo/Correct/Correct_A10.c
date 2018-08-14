#include<stdio.h>

int main()
{
    long long int a,b,i,d,c,e;
    scanf("%lld %lld",&a,&b);
    if((a/2)>b)
    {
        d=(a/(2*(b+1)));
        c=b*d;
        e=a-(c+d);
        printf("%lld %lld %lld",d,c,e);
    }
    else
    {
        d=(a/(2*(b+1)));
        c=b*d;
        e=a-(c+d);
        printf("%lld %lld %lld",d,c,e);
    }
    return 0;
}
