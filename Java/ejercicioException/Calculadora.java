import java.util.Scanner;

public class Calculadora {
    public static void main(String[] args) {
        
        System.out.println("¿Cuantos datos de gastos deseas introducir?(Numero entero");
        Scanner sc=new Scanner(System.in);
        int cantidad=sc.nextInt();
        sc.nextLine();
        
        
        String[] gastosarray=new String[cantidad];
        for(int i=0; i<cantidad;i++){
           System.out.println("Escribe el gasto"); 
                       
           String gasto=sc.nextLine();
           System.out.println("Gasto guardado");
            gastosarray[i]=gasto;
        }
       
        double sumaTotal=0;
        for (String string : gastosarray) {
            try{
                sumaTotal+=stringToDouble(string);
            }catch(NumberFormatException e){
                System.out.println("El dato introducido no es un numero. Error: "+e.getMessage());
            }catch(Exception e){
                System.out.println("Error: "+e.getMessage());
            }
        }
         System.out.println("Dame un numero por el que dividirlo");
        double divisor=sc.nextDouble();
        try{
            System.out.println("Promedio: "+sumaTotal/divisor);
        }catch(ArithmeticException e){
            System.out.println("No se pudo realizar la operacion. Error "+e.getMessage());
        }catch(Exception e){
            System.out.println("Error inesperado. Erro: "+e.getMessage());
        }
        sc.close();
    }

    public static double stringToDouble(String string){
        double gasto=Double.parseDouble(string);
        return gasto;
    }

}
