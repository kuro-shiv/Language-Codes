import java.util.*;
class pattern2
{
    public static void main (String[] args)
    {
        int i,j,n;
        System.out.println("Enter limit of pattern");
        Scanner sc= new Scanner (System.in);
        n=sc.nextInt();
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=i;j++)
            {
                System.out.print(j);
            }
            System.out.print("\n");
        }
       
    }
}