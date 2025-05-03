#include<stdio.h>
int main()
{
    int n,r=0,ld;
    printf("enter any number");
    scanf("%d",&n);
    while(n>0)
    {
        ld=n%10;
        n=n/10;
        r=r*10;
        r=r+ld;
    }
    printf("rev of given num is :%d",r);
}