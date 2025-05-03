#include<stdio.h>
int main()
{
    int a,b,c; 
    printf("enter the side 1 of triangle");
    scanf("%d",&a);
    printf("enter the side 2 of triangle");
    scanf("%d",&b);
    printf("enter the side 3 of triangle");
    scanf("%d",&c);
    if(a+b>c && b+c>a && c+a>b)
    printf("it is a triangle");
    else
    printf("it is not a triangle");
    return 0;
}