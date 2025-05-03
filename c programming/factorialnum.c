#include<stdio.h>
int main()
{
    int n,i,prod=1;
    printf("enter a no.");
    scanf("%d",&n);
    for(i=1;i<=n;i++){
    prod*=i;
    }
    printf("factorial of a num is : %d",prod);
    return 0;
}