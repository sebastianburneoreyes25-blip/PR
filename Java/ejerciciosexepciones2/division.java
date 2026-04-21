package ejerciciosexepciones2;

import java.util.Scanner;

public class division {

    public static void main(String[] args) {
        try{
        System.out.println("Dame el primer numero");
        Scanner sc=new Scanner(System.in);
        int n1=sc.nextInt();
        System.out.println("Dame el segundo numero");
        int n2=sc.nextInt();
        var n3=n1/n2;
        System.out.println(String.format("La division de %d y %d es "+n3, n1,n2));
        sc.close();
        }catch (ArithmeticException e){
            System.out.println("Error: "+e.getMessage());
        }catch (Exception e){
            System.out.println("Error: "+e.getMessage());

        }
    }
    
}
