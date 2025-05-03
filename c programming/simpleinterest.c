#include<stdio.h>
int main()
{
    float s,p,r,t;
    printf("enter profit\n");
    scanf("%f",&p);
    printf("enter rate\n");
    scanf("%f",&r);
    printf("enter time\n");
    scanf("%f",&t);
    s=(p*r*t)/100;
    printf("the simple interest is:%f",s);
    return 0;
}
