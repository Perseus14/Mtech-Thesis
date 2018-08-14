#include <stdio.h>
int main(){

		long long int dip, cert, NotWinner, n, k;
		scanf("%lli %lli", &n, &k);
		dip = n/((2*k) +2);
		cert = k*dip;
		if( dip + cert > n/2){
			dip = 0;
			cert = 0;
			NotWinner = n;
			printf("%lli %lli %lli", dip, cert, NotWinner);
		}
		else{
			NotWinner = n - (dip + cert);
			printf("%lli %lli %lli", dip, cert, NotWinner);
		}
		return 0;
}
/* 1507382664071 */
