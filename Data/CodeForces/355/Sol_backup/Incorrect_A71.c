#include<stdio.h>
int main()
{
    long long k,d,t,i,s;
    scanf("%I64d %I64d",&k,&d);
    if(k==1)
    {
     printf("%I64d",d);
    }
    else
    {
        if(d==0)
        printf("No solution");
        else
        {       
    if(d>=k)
    {
      if(d%k==0)
      {
        t=d/k;
        for(i=0;i<k;i++)
        printf("%I64d",t);
      }
      else
      {
          t=d/k;
          for(i=0;i<k-1;i++)
          printf("%I64d",t);
          s=d-(k-1)*t;
          printf("%I64d",s);
      }
    }
      else
      {
         while(d<k)
         d=d*10;
         if(d%k==0)
      {
        t=d/k;
        for(i=0;i<k;i++)
        printf("%I64d",t);
      }
      else
      {
          t=d/k;
          for(i=0;i<k-1;i++)
          printf("%I64d",t);
          s=d-(k-1)*t;
          printf("%I64d",s);
      }
    } 
  }
  }
    
    return 0;
}