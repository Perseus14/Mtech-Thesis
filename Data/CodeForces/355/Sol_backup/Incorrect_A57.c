#include<stdio.h>
#include<stdlib.h>


int main()
{
	int i;
	int k,n;
	scanf("%d %d",&k,&n);
	if(n==0&&k!=1) printf("No solution");
	printf("%d",n);
	for(i=1;i<k;i++) printf("0");
	return 0;	
} 
    	 		 		   	  			  	 		 	 		