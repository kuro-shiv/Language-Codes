import java.util.*;
class pattern4
{
    public static void main (String[] args)
    {
        int i,j,n;
        System.out.println("Enter limit of pattern");
        Scanner sc= new Scanner (System.in);
        n=sc.nextInt();
        for(i=1;i<=n;i++)
        {
            for(j=i;j<=n;j++)
            {
                System.out.print("*");
            }
            System.out.print("\n");
        }
       
    }
}
