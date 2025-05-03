#include<stdio.h>
int main()
{
    int n,sum=0,r;
    printf("enter the number");
    scanf("%d",&n);
    while(n>0){
        r=n%10;
        if(r%2==0){
        sum=sum+r;
    }
    n=n/10;
}
printf("the sum of even digit from a number %d",sum);

    return 0;
}