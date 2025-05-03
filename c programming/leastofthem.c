#include<stdio.h>
int main()
{
    int a,b,c;
    printf("enter 1 positive integer \n");
    scanf("%d",&a);
    printf("enter 2 positive integer\n");
    scanf("%d",&b);
    printf("enter 3 positive integer\n ");
    scanf("%d",&c);
    if(a<b && a<c)
    printf("least positive integer  is :%d ",a);
    else if(b<c && b<a)
    printf("least positive integer is %d",b);
    else 
    printf("the least positive integer is :%d",c);
}
