#include<stdio.h>
int main()
{
    int a,i,n;
    printf("enter number of terms");
    scanf("%d",&n);
    a=3;
    for(i=0;i<n;i++){
    printf("%d ",a);
    a=a*4;
    }
    return 0;
    }