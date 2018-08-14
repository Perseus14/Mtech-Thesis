/**********************************************************/
/**            Bismillahir-rahmanir-rahim                **/
/**  In the name of Allah, the Beneficent, the Merciful. **/
/**********************************************************/
/*author: Sayed Sohan, CSE 13th batch(2016), MBSTU*/
/**status : */

#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <time.h>
#include <limits.h>
typedef long long  ll;
typedef unsigned long long ull;
#define INF INT_MAX
#define FOR(i,x,n) for(i=(x);i<(n);i++)
#define IFOR(i,n,x) for(i=(n-1);i>=(x);i--)
#define clr(a,b) memset(a,b,sizeof(a))
#define MOD 1000000007
#define MAX 100000 /** can increase another 0 */
#define TRUE 1
#define FALSE 0
#define PI acos(-1)
#define maxx(a,b) (a>b)?a:b
#define minn(a,b) (a<b)?a:b
#define DIF if(0)

//ll comp(const void *i, const void*j) {return *(ll*) i - *(ll*) j;}


int main()
{
    ll i,j,k,arr[MAX],l,m,n,x,count,sum,ans,T,check;
    char str[MAX];
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);

    scanf("%lld %lld",&n,&m);

    if(n==1 && m==0) printf("0");
    else if(n>1 && m==0) printf("No solution");
    else{
        printf("%lld",m);
        for(i=0;i<n-1;i++) printf("0");
    }

    return 0;
}

