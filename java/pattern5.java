import java.util.*;
class pattern5
{
    public static void main (String[] args)
    {
        int i,j,n;
        System.out.println("Enter limit of pattern");
        Scanner sc= new Scanner (System.in);
        n=sc.nextInt();
        System.err.println("the pattern is");
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=n-i+1;j++)
            {
                System.out.print("*");
            }
            System.out.print("\n");
        }
       
    }
}
