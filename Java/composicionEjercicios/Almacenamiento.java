package composicionEjercicios;

import java.util.Scanner;

public class Almacenamiento {
    
    public static class MemoriaFlash{
        
        public void escribirDato(String dato){
            System.out.println("Dato guardado en hardware");
        }
    }

    public static class Pendrive extends MemoriaFlash {
    
        final private MemoriaFlash m=new MemoriaFlash();

        public void escribirDato(String dato){
            m.escribirDato(dato);
        }
        
    }

    public static void main(String[] args) {
        System.out.println("Escribe el dato a guardar");
        Scanner sc=new Scanner(System.in);
        String dato=sc.nextLine();
        Pendrive p=new Pendrive();
        p.escribirDato(dato);
        sc.close();
    }

}
