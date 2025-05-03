#include<stdio.h>
int main()
{
    float pi=3.14,r,v;
    printf("enter radius of sphere");
    scanf("%f",&r);
    v=(4*pi*r*r*r)/3;
    printf("the volume of sphere is:%f",v);
    return 0;
}