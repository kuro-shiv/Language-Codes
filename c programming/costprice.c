#include<stdio.h>
int main()
{
    float prof,loss, sp, cp;
    printf("enter cost price");
    scanf("%f",&cp);
    printf("enter selling price");
    scanf("%f",&sp);
    if(cp>sp){
    printf("there is a loss incured %f",sp,cp);
    loss=cp-sp;
    printf("the loss he incurred is :%f",loss);
    }
    else {
    printf("there is a profit %f",cp,sp);
    prof=sp-cp;
    printf("the profit he made is: %f",prof);
    }
    return 0;
}