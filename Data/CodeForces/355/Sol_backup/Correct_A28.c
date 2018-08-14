#include <stdio.h>
#include <stdlib.h>

int main()
{
     int k, d, i;
     while (scanf("%d%d", &k, &d) != EOF){
              if (d == 0 && k == 1)
                        printf("0\n");
              else if (d == 0 && k > 1)
                        printf("No solution\n");
              else
              {
                   printf("%d", d);
               for (i = 0; i < k-1; i++)
              {
                   printf("0");
             }
                  printf("\n");
              }
        }
    return 0;
}

	   	 	   			   	 					 	  	 		