#include<stdio.h>
int main()
{
    int num;
    printf("enter a positive integer");
    scanf("%d",&num);
    if(num>99&&num<1000)
    printf("it is a three digit number %d",num);
    else
    printf("it is not a three digit number %d",num);
    return 0;
}