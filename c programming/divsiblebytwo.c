#include<stdio.h>
int main()
{
    int n;
    printf("enter a no.");
    scanf("%d",&n);
    if(n%2==0)
    printf("the no. is divisible by 2: %d", n);
    else
    printf("the no. is not divisbleby 2:%d",n);
    return 0;
}