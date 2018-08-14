#include<stdio.h>
int main(){
	int d,k;
	scanf("%d%d",&k,&d);
	if(d==0){
		if(k==1){
			printf("0");
			return 0;
		}
		else{
			puts("No solution");
			return 0;
		}
	}
	char c=d+'0';putchar(c);
	for(int i=0;i<k-1;++i)putchar('0');
	return 0; 
}
