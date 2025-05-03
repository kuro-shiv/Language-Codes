#include<stdio.h>
int mian()
{
    int a,b;
    printf("Enter two integer");
    scanf("%d %d",&a,&b);
    int q = a/b;
   int r = a - b*q ;
    printf(" the remainder when %d is divided by %d is:%d",a,b,r);
    return 0;
}