#include<stdio.h>
int main()
{
    char c;
    printf("enter a character");
    scanf("%c",&c);
    if(c>='0'&&c<='9')
    printf("character is a digit %c",c);
    else
    printf("not valid"); 
    return 0;
}