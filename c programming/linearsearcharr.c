#include<stdio.h>
#include<conio.h>
void main()
{
int i,arr[20],n,s,F=0,loc;
printf("enter limit of array ");
scanf("%d",&n);
printf("enter the elements of array");
{
for(i=0;i<n;i++)
scanf("%d",&arr[i]);
}
printf("enter the element to be search");
scanf("%d",&s);
for(i=0;i<n;i++)
{
    if(arr[i]==s)
    {
    F=1;
    break;
    }
}
if(F==1)
{
loc=i;
printf("element is found %d at the index",loc);
}
else
printf("element is not found");
getch();
}