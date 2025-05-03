#include<stdio.h>
int main()
{
    int a,b,c, avg;
    printf("enter first no\n");
    scanf("%d",&a);
    printf("enter second no.\n");
    scanf("%d",&b);
    printf("enter third no.\n");
    scanf("%d",&c);
    avg=(a+b+c)/3;
    printf("the avg of three no. is %d\n",avg);
    return 0;
}