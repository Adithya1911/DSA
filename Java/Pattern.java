// Pattern-1: Rectangular Star Pattern
// In this problem you need to print the pattern of stars in the square of size nxn matrix


import java.util.Scanner;

public class Pattern {
    public void printRectangularStarPattern(int x){
        for(int i=0;i<x;i++){
            for(int j=0;j<x;j++){
                System.out.print("*");
            }
            System.out.println();
        }
    }

    public void printTriangularStarPattern(int x){
        for(int i=0;i<x;i++){
            for(int j=0;j<=i;j++){
                System.out.print("* ");
            }
            System.out.println();
        }
    }
    
    public void printTriangularNumberPattern(int x){
        for(int i=1; i<=x; i++){
            for(int j=1; j<=i; j++){
                System.out.print(i + " ");
            }
            System.out.println();
        }
    }
    public void printTriangularNumberPattern2(int x){
        for(int i=1; i<=x; i++){
            for(int j=1; j<=i; j++){
                System.out.print(j + " ");
            }
            System.out.println();
        }
    }

    public void printInverseTrangular(int x){
        for(int i=x; i>=1; i--){
            for(int j=1; j<=i; j++){
                System.out.print(j + " ");
            }
            System.out.println();
        }
    }

    public void printInverseTriangularStar(int x){
        for(int i=x;i>=1;i--){
            for(int j=1;j<=i;j++){
                System.out.print("* ");
            }
            System.out.println();
        }
    }

    public void printInverseTrangularNumber(int x){
        for(int i=x;i>=1;i--){
            for(int j=1;j<=i;j++){
                System.out.print(j+ " ");
            }
            System.out.println();
        }
    }
    
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter the value for n: ");
            int n = scanner.nextInt();
            Pattern pattern = new Pattern();
            // pattern.printRectangularStarPattern(n);
            // pattern.printTriangularStarPattern(n);
            // pattern.printTriangularNumberPattern(n);
            // pattern.printTriangularNumberPattern2(n);
            // pattern.printInverseTriangularStar(n);
            pattern.printInverseTrangularNumber(n);
            
        }
    }
    
}
