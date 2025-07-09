import java.util.Scanner;

public class even_odd{
  public static void main(String[]args){

    // Scanner for user input 
    Scanner sc = new Scanner(System.in);

    System.out.print("Enter a number: ");
    int number = sc.nextInt(); // Read number from user

    // check if number is even or odd
    if (number % 2 == 0)
        System.out.println(number + " is Even.");
    else
        System.out.println(number + " is Odd.");

    sc.close();        
  }


}