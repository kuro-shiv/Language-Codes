#include<stdio.h>
int main()
{
    int a;
    printf("enter a positive integer");
    scanf("%d",&a);
    if(a%5==0 && a%3==0 && a%15!=0)
    printf("the number is divisble by 5 or 3 bt not divisible by 15");
    else
    printf("not the statement is not true");
    return 0;
}