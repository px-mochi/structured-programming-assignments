import java.util.*;         //imports a library package java.util.* (General utility class) 

public class JavaApplication {      //a blueprint where objects are created
   
    /**External classes cannot see "private static" variables
     * often used for constants - "input" in this case
     * Scanner scans text for primitive types and strings, breaks input into tokens
     * tokens can be used for values (the two numbers for this case)
     */
    private static Scanner input = new Scanner(System.in); //System.in - standard input stream

    //Public - visible, can be called | static - associate with class, not creating object | void - no return value
    public static void main(String[] args) { //saying it's a string, and it's those 2 inputs earlier
        int a;  //a is an integer
        int b;  //b is an integer
        
        //Prints string and terminates line
        System.out.println("Enter two numbers. This algorithm will find the greatest common denominator.");
        a = input.nextInt();    //a is the 1st token from the scanner input
        b = input.nextInt();    //b is the 2nd token from the scanner input
        while (!(b == 0)) {     //while (loops till b is 0) b is NOT equals to 0
            if (a > b) {        // if a is more than b,
                a = a - b;      
            } else {            //if not, 
                b = b - a;
            }
        }
        System.out.println(a);  //prints value of a 
    }
}
