#include<stdio.h>
#include<conio.h>
int main()
{
    int i, s, arr[20],loc,n,j,temp,low,high,mid,F=0;
    printf("enter limit of array");
    scanf("%d",&n);
    printf("enter elements of array");
    for(i=0;i<n;i++)
    {
    scanf("%d",&arr[i]);
    }
    for(i=0;i<n;i++)
    {
        for(j=n+1;j<n;j++)
        {
        if(arr[j]<arr[i])
        {
        temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
    }
    }
    }
    printf("enter element for search");
    scanf("%d",&s);
    low=0;
    high=n-1;
    while(low<=high)
    {
    mid=(low+high)/2;
    if(arr[mid]==s)
    {
        F=1;
        break;
    }
    else
    if(s<arr[mid])
    high=mid-1;
    else
    low=mid+1;
    }
    if(F==1)
    {
        loc=i;
        printf("element is found at index%d",loc);
    }
    else
    printf("element is not found");
   getch();
   }
    