package Exepcion;

public class Exceptions {
    
    public static void main(String[] args) {
        try {
            var result=10/0;
        System.out.println(result);
        } catch (ArithmeticException e) {
            System.out.println("Algo fallo, prueba de nuevo. Error: "+e.getMessage());


        }
        try {
            var result=10/0;
        System.out.println(result);
        } catch (ArithmeticException e) {
            System.out.println("Algo fallo, prueba de nuevo. Error: "+e.getMessage());


        }finally{
            System.out.println("Pos eso");
        }
        


    }
}
