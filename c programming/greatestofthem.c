#include<stdio.h>
int main()
{
    int a,b,c;
    printf("enter the 1 positive integer ");
    scanf("%d",&a);
    printf("enter the 2 poaitive integer");
    scanf("%d",&b);
    printf("enter the 3 positive integer");
    scanf("%d",&c);
    if(a>b && a>c)
    printf("a is the greatest number%d",a);
    else if(b>c && b>a)
    printf("b is the greatest number%d",b);
    else 
    printf("c is the greatest number %d",c);
    return 0;
}