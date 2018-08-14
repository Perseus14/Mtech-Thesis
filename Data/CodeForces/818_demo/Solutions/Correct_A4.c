#include<stdio.h>
int main()
{
long long int n,k,x,y,z;
scanf("%lld%lld",&n,&k);
x=n/(2*(k+1));
y=x*k;
z=n-x-y;
printf("%lld %lld %lld\n",x,y,z);
return 0;
}
