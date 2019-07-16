#include <stdio.h>
int main()
{
int a,b,c;
scanf("%d %d %d",&a,&b,&c);
if(a>=b && b>=c && c>=a)
{
	printf("%d",a);
}
	if(b>=a && b>=c)
{
	printf("%d",b);
}
  else
{
	printf("%d",c);
}
return 0;
}
