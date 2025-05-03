#include<stdio.h>
int main()
{
    int a,w,l,p;
    printf("enter the width of rectangle");
    scanf("%d",&w);
    printf("enter the length of rectangle ");
    scanf("%d",&l);
    a=w*l;
    p=2*(l+w);
    if(a>p)
    printf("the area of recatangle is greater than perimeter rectangle");
    else
    printf("the area is not greater than perimeter of rectangle");
    return 0;
}