import java.util.*;
public class pattfunc{
public static void square(int n)
{
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
        System.out.print("*");
        }
        System.out.print("\n");
    }
    
}
public static void numbers(int n)
{
 for(int i=1;i<=n;i++)
 {
     for(int j=1;j<=i;j++){
     System.out.print(j);
     }
     System.out.print("\n");
 }
}
public static void samenm(int n)
{
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=i;j++)
        {
            System.out.print(i);
        }
        System.out.print("\n");
    }
}
public static void decpatt(int n)
{
    for(int i=1;i<=n;i++)
    {
        for(int j=i;j<=n;j++)
        {
            System.out.print(i);
        }
        System.out.print("\n");
    }
}
public static void decpattern(int n)
    {
        for(int i=1;i<=n;i++)
        {
            for(int j=i;j<=n;j++)
            {
                System.out.print(j);
            }
            System.out.print("\n");
        }
    }
    public static void decpatterns(int n)
    {
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=n-i+1;j++)
            {
                System.out.print("*");
            }
            System.out.print("\n");
        }
    }
    public static void pyramid(int n)
   {
    for(int i=0;i<=n;i++)
    {
        for(int a=0;a<=i;a++)
        {
            System.out.print(" ");
        }
        for(int j=0;j<2*n-1;j++)
        {
            System.out.print("*");
        }
        for(int a=0;a<=i;a++)
        {
            System.out.print(" ");
        }
        System.out.println();
    }
   }
   public static void pyramid2(int n)
   {
    for(int i=0; i<=n; i++)
    {
        // First Pyramid
        for(int a=0; a<=i; a++)
        {
            System.out.print(" ");
        }
        for(int j=0; j<2*n-1; j++)
        {
            System.out.print("*");
        }
        
        // Second Pyramid (repeat the same loop as above)
        for(int a=0; a<=i; a++)
        {
            System.out.print(" ");
        }
        for(int j=0; j<2*n-1; j++)
        {
            System.out.print("*");
        }
        
        // Move to the next line
        System.out.println();
    }
   }
   public static void pyramid3(int n)
   {
    for(int i=0; i<=n; i++)
    {
        // First Pyramid (normal spaces)
        for(int a=0; a<=i; a++)
        {
            System.out.print(" ");
        }
        for(int j=0; j<2*n-1; j++)
        {
            System.out.print("*");
        }
        
        // Space between the two pyramids
        System.out.print("   ");
        
        // Second Pyramid (decreasing spaces)
        for(int a=0; a<=n-i; a++)  // Spaces start from max and decrease
        {
            System.out.print(" ");
        }
        for(int j=0; j<2*n-1; j++) // Stars remain the same as in the first pyramid
        {
            System.out.print("*");
        }
        
        // Move to the next line
        System.out.println();
    }
   }
   public static void diamond(int n)
   {
   
   //for the second pyramid
   for(int i=0;i<=n;i++)
   {
       for(int a=0;a<=n-i-1;a++)
       {
           System.out.print(" ");
       }
       for(int j=0;j<2*i+1;j++)
       {
           System.out.print("*");
       }
       for(int a=0;a<=n-i-1;a++)
       {
           System.out.print(" ");
       }
       System.out.println();
   }
   for(int i=0;i<=n;i++)
   {
       for(int a=0;a<=i;a++)
       {
           System.out.print(" ");
       }
       for(int j=0;j<2*n-(2*i+1);j++)
       {
           System.out.print("*");
       }
       for(int a=0;a<=i;a++)
       {
           System.out.print(" ");
       }
       System.out.println();
   }
   }
   public static void halfdiamond(int n)
   {
   
   //for the second pyramid
   for(int i=0;i<=n;i++)
   {
   
       for(int j=0;j<2*i+1;j++)
       {
           System.out.print("*");
       }
       for(int a=0;a<=n-i-1;a++)
       {
           System.out.print(" ");
       }
       System.out.println();
   }
   for(int i=0;i<=n;i++)
   {
       for(int j=0;j<2*n-(2*i+1);j++)
       {
           System.out.print("*");
       }
       for(int a=0;a<=i;a++)
       {
           System.out.print(" ");
       }
       System.out.println();
   }
   }
   public static void pyramid4(int n)
   {
    for(int i=0;i<=n;i++)
    {
        for(int a=0;a<=i;a++)
        {
            System.out.print(" ");
        }
        for(int j=0;j<2*n-(2*i+1);j++)
        {
            System.out.print("*");
        }
        for(int a=0;a<=i;a++)
        {
            System.out.print(" ");
        }
        System.out.println();
    }
   }
public static void evenodd(int n)
{
    int start= 1;
    for(int i=0;i<=n;i++)
    {
        if(i%2==0)
        start=1;
        else start=0;
        for(int j=0;j<=i;j++){
        System.out.print(start);
       start=1-start;
        }
        System.out.println();
    }
}
public static void femalejoint(int n)  
{
    int space= 2*(n-1);
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=i;j++)
        {
            System.out.print(j);
        }
        for(int j=1;j<=space;j++)
        {
            System.out.print(" ");
        }
        for(int j=i;j>=1;j--)
        {
            System.out.print(j);
        }
        System.out.println();
        space -= 2;
    }
}
public static void rightangle(int n)
{
    int num=1;
    for(int i =0;i<=n;i++)
    {
        for(int j=0;j<=i;j++)
        {
            System.out.print(num+" ");
            num++;
        }
        System.out.println();
    }
}
public static void rightangletri(int n)
{
    for(int i =0;i<=n;i++)
    {
        for(char ch='A'; ch<='A'+i;ch++)
        {
            System.out.print(ch+" ");
        }
        System.out.println();
    }
}
public static void rightangletriangle(int n)
{
    for(int i =0;i<n;i++)
    {
        for(char ch='A'; ch<='A'+ (n - i - 1);ch++)
        {
            System.out.print(ch+" ");
        }
        System.out.println();
    }
}
public static void pattern16(int n)
{
    char ch;
    for(int i=0;i<n;i++)
    {
        ch =(char) ('A' + i) ;
        for(int j=0;j<=i;j++)
        {
            System.out.print(ch+" ");
        }
        System.out.println();
    }
}
public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println("enter limit of pattern");
    int n = sc.nextInt();
    square(n);  
    numbers(n);
    samenm(n);
    decpatt(n);
    decpattern(n);
    decpatterns(n);
    pyramid(n);
    pyramid2(n);
    pyramid3(n);
    diamond(n);
    halfdiamond(n);
    pyramid4(n);
    evenodd(n);
    femalejoint(n);
    rightangle(n);
    rightangletri(n);
    rightangletriangle(n);
    pattern16(n);
}
}
