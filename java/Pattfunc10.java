import java.util.*;

public class Pattfunc10
{
    public static void pyramidWithGap(int n)
    {
        // Loop through each row
        for(int i = 0; i < n; i++)
        {
            // First Pyramid (increasing spaces)
            for(int a = 0; a < i; a++)
            {
                System.out.print(" ");
            }
            for(int j = 0; j < 15; j++) // You can adjust 15 for the number of stars in each row
            {
                System.out.print("*");
            }
            
            // Space between the two pyramids (forming a V shape, decreasing each row)
            for(int gap = 0; gap < 2 * (n - i) - 1; gap++)
            {
                System.out.print(" ");
            }
            
            // Second Pyramid (decreasing spaces)
            for(int j = 0; j < 15; j++) // Keep the same number of stars for the second pyramid
            {
                System.out.print("*");
            }
            
            // Move to the next line
            System.out.println();
        }
    }

    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in); 
        System.out.println("Enter the number of rows for the pattern:");
        int n = sc.nextInt();
        pyramidWithGap(n);
    }
}
