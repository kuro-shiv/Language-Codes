#include<stdio.h>
int main()
{
    int alpha,n,i;
    printf("enter a number");
    scanf("%d",&n);
    while(n>0)
    alpha=(char)n;
    printf("alphabet of this ascii value is :%c",alpha);
return 0;
}