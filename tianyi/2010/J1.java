import java.util.Scanner;

public class J1{

    public static void main(String[] args) {
        
        Scanner scan = new Scanner(System.in);
        System.out.println("");
        int userInput = scan.nextInt();
        if (userInput == 2){
            System.out.println("2");
            
        }
        else if (userInput <= 6){
            if (userInput % 2 == 1){
                System.out.println((userInput/2)+1);
            }
            else{
                System.out.println("3");
            }
        } 
        else{
            if (userInput <= 8){
                System.out.println("2");
            }
            else{
                System.out.println("1");
            }
        }
    }

}
