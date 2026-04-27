import java.util.Scanner;

public class RegistroUsuarios {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Escribe el nombre del usuario");
        String nombre=sc.nextLine();
        try{
            System.out.println("Escribe la edad");
            int edad=sc.nextInt();
            if(edad<0){
                throw new IllegalArgumentException();
            }
            System.out.println("Usuario registrado correctamente");
        }catch (IllegalArgumentException e){
            System.out.println("La edad no debe ser negativa. Error: "+e.getMessage());
        }catch(Exception e){
            System.out.println("Error: "+e.getMessage());
        }

    }
    
}
