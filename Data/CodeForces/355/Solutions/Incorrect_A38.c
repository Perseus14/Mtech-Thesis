#include<stdio.h>
int main() {
	int k,d;
	scanf("%d%d",&k,&d);
	int i;
	if(d==0){
		if(k==1){
			printf("0\n");
		}else{
			printf("No solution\n");
		}
	}else{
		//d大于等于k就够分了！
		//以平均值的办法去分！
		while(1){
			if(d>=k)break;
			d=d*10;
		}
		int average=d/k;
		int more=d-average*k;
		printf("%d",average+more);
		for(i=0;i<k-1;i++){
			printf("%d",average);
		}
		printf("\n");
	}
	return 0;
}
