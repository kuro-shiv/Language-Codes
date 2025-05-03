#include<stdio.h>
int main()
{
    int a, b;
    printf("enter a no.");
    scanf("%d",&a);
    printf("enter second no.");
    scanf("%d",&b);
    if(a<b)
    printf("a is smallest %d",a);
    else 
    printf("b is smallest %d",b);
    return 0;
}