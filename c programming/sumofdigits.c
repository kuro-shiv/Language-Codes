#include<stdio.h>
int main()
{
    int n,sum=0,ld,count=0;
    printf("enter any number");
    scanf("%d",&n);
    while(n>0)
    {
        ld=n%10;
        n=n/10;
        sum=sum+ld;
    }
    printf("sum of digit is :%d",sum);
}