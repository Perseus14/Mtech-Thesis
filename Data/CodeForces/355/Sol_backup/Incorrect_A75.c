#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)
#define SWAP(a,b) 			do{a+=b; b=a-b; a=a-b;
#define MID(s,e)   		( s + (e -s)/2)
//loop
#define fall(i,a,b)               for(i=a;i<b;i++)
#define feall(i,a,b)               for(i=a;i<=b;i++)
//arith.
#define MAX(a,b)                     ( (a) > (b) ? (a) : (b))
#define MIN(a,b)                     ( (a) < (b) ? (a) : (b))
#define abs(x)			 (x<0?(-x):x)
#define PI 3.1415926535897932384626
typedef long long ll;
#include<stdio.h>
#include<string.h>
#include<math.h>
int main()
{
int n,k,i,num;
s(n);
s(k);
num=k;
if(k==0)
    printf("0\n");
else
{
    for(i=1;i<=n-1;i++)
        num=num*10;
    printf("%d\n",num);
}
return 0;
}
