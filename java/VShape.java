import java.util.*;

public class VShape {
    public static void printVShape(int n) {
        for (int i = 0; i < n; i++) {
            // Print leading spaces for the left side of the 'V'
            for (int j = 0; j < n; j++) {
                System.out.print(" ");
            }
            // Print the left side asterisk
            System.out.print("*");

            // Print spaces between the two rows
            int spacesBetween = (n - i - 1) * 2 - 1; // Calculate the spaces between the two rows
            if (spacesBetween > 0) {
                for (int j = 0; j < spacesBetween; j++) {
                    System.out.print(" ");
                }
                // Print the right side asterisk
                System.out.print("*");
            }
            
            // Move to the next line
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of '*' to print on each line:");
        int n = sc.nextInt();
        printVShape(n);
    }
}