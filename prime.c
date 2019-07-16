#include <stdio.h>
int main()
{
    int a,b,flag = 0;

    scanf("%d", &a);
    for(i=2; b<= a/2;++i)
    {
        if(a%b == 0)
        {
            flag = 1;
            break;
        }
    }
    if(a == 1) 
    {
      printf("no");
    }
    else 
    {
        if (flag == 0)
          printf("yes");
        else
          printf("no");
    }
    
    return 0;
}
