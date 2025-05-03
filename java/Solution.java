import java.util.*;
class Solution
{
   public static void main(String[] args){
    int i,n,j;
    Scanner sc= new Scanner(System.in);
    n=sc.nextInt();
    for(i=0;i<n-1;i++)
    {
        for(j=0;j<=i;j++){
            System.out.print("#");
        }
        System.out.print("\n");
    }
   }
}
