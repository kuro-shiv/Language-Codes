#include<stdio.h>
int main()
{
    int n,i;
    printf("enter number of terms");
    scanf("%d",&n);
        for(i=1;i<=2*n-1;i=i+2){
        printf("%d",i);
    }
}