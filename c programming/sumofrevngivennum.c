#include<stdio.h>
int main()
{
    int n,r=0,ld,sum=0;
    printf("enter any number");
    scanf("%d",&n);
    while(n>0){
    ld=n%10;
    sum=sum+ld;
    r=(r*10)+ld;
    n=n/10;
    }
    printf("the sum of rev and given number is:%d",sum);
    return 0;
}