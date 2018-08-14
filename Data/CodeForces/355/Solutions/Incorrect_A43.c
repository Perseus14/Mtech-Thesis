#include <stdio.h>
#include <string.h>
int main()
{
   long long n,k;
   scanf("%lld",&n);
   while(n!=0){
        k=n%10;
    if(k==0) printf("O-|-OOOO\n");
    else if(k==1) printf("O-|O-OOO\n");
    else if(k==2) printf("O-|OO-OO\n");
    else if(k==3) printf("O-|OOO-O\n");
    else if(k==4) printf("O-|OOOO-\n");
    else if(k==5) printf("-O|-OOOO\n");
    else if(k==6) printf("-O|O-OOO\n");
    else if(k==7) printf("-O|OO-OO\n");
    else if(k==8) printf("-O|OOO-O\n");
    else if(k==9) printf("-O|OOOO-\n");
    n /=10;
   }

   return 0;
}

     	 		 	 	       	 	   			