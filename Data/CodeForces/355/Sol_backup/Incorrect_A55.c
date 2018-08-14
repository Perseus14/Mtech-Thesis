#include <stdio.h>
int k,d,a,b,i,c,s;
int digit_count( int n)
{
    int c1 = 0  ;
    while ( n > 0)
    {
        n =  n/10 ;
        c1  = c1 + 1 ;
  //      printf("this the value of c1 in loop : %d\n", c1);
    }
  //  printf("this the value of c1 : %d\n", c1);
    return c1 ;

}
int digit_sum( int n )
{
    int s1=0 ;
    while ( n > 0)
    {
        s1 += n%10;
        n = n/10 ;
    }
   // printf("this the value of s1 : %d\n", s1);
    return s1 ;
}
int main()
{
    scanf("%d %d", &k, &d);
    if ( d == 0)
    {
        if( k == 1)
        {
            printf("0");
            return 0 ;
        }
        else{
            printf("No solution");
        }
    }
   else  if ( k == digit_count(d))
        {
                  printf("%d", d ) ;
                  return 0 ;
                  }
    else{
            while (k != digit_count(d))
            {
                s = digit_sum(d) ;
               // printf("this the value of s & k : %d %d\n", s,k);
                while ( 1 != digit_count(s) )
                {
                    s = digit_sum(s) ;
                }

                for ( i = 1; i < k ;i++){
                     s = s* 10 ;
                }
                d = s ;


            }
    }
    printf("%d", d);
    return 0 ;
}
