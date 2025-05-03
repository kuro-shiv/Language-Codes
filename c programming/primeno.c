#include<stdio.h>
int main()
{
    int n,i;
    printf("enter any number");
    scanf("%d",&n);
    for (  i = 2; i < n/2; i++)
    {
        if(i%1==0 && i%n==0)
        printf("it is a prime number : %d",n);
        else 
        printf("it is not a prime number : %d",i);
    }
}