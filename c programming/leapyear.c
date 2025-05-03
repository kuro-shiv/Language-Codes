#include<stdio.h>
int main()
    {
        int month;
        printf("enter the year to check ");
        scanf("%d",& month);
        if(month%4==0)
        printf("the year is a leap year");
        else 
        printf("the year is not a leap year");
        return 0;
    }