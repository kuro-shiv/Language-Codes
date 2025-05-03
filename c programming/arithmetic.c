#include<stdio.h>
int main()
    {
        int a,b,c,result;
        printf("enter 1 numbers");
        scanf("%d",&a);
        printf("enter 2 numbers");
        scanf("%d",&b);
        printf("enter 3 numbers");
        scanf("%d",&c);
        result=a*(b/b)*c;
        printf("result is %d",result);
        return 0; 
    }