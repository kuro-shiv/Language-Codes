#include<stdio.h>
int main()
{
    int n, count=0;
    printf("enter any number");
    scanf("%d",&n);
    while(n>0){
    n=n/10;//to find 1 digit of number
    count ++;
   }
     printf("the number of digit in number is :%d",count);
    return 0;
}