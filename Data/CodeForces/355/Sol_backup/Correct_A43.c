#include<stdio.h>
arr[1000];
int main()
{
    int k, d, i, x, sum, y;
    while(scanf("%d %d",&k,&d)!= EOF)
    {
        for(i=0,x=k-1; i<k ; i++)
        {
            arr[i]=5;
        }
        while(1)
        {
            for(i=0,sum=0 ; i<k ; i++)
            {
                sum+=arr[i];
            }
            while(sum>=10)
            {
                for(y=sum,sum=0 ; y!=0 ; y/=10)
                {
                    sum+=y%10;
                }
            }
            if(sum==d)
            {break;}
            else if(sum < d)
            {
                arr[x]++;
                if(arr[x]==9)
                {x--;}
            }else if(sum > d)
            {
                arr[x]--;
                if(arr[x]==0)
                {x--;}
            }
        }
        if(arr[0]==0 && k!=1)
        {
            printf("No solution\n");
            continue;
        }
        for(i=0 ; i<k ; i++)
        {
            printf("%d",arr[i]);
        }printf("\n");
    }
}
