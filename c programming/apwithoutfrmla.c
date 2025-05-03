#include<stdio.h>
int main()
{
    int a,i,n;
    printf("enter number of terms");
    scanf("%d",&n);
    a=1;
    for(i=0;i<n;i++){
    printf("%d",a);
    a=a+3;
    }
    return 0;
    }