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
		//d->d*10->d*10*10
		//1->10按最小的来分会比较复杂，但可以实现！
		//看来还必须按最小的来分！
		//2->11
		//3->12
		//10->19->199
		while(1){
			if(d>=k)break;
			d=d*10;
		}
		int average=d/k;
		int more=d-average*k;
		for(i=0;i<k;i++){
			if(more==0){
				printf("%d",average);
			}else{
				//保证分配后的数字不超过9
				if(more+average>9){
					printf("9");
					more=more-(9-average);
				}else{
					printf("%d",more+average);
					more=0;
				}
			}
		}
		printf("\n");
		//8 7
		//70/8=8
	}
	return 0;
}
