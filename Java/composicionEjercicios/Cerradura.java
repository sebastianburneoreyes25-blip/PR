package composicionEjercicios;


import java.util.Scanner;

public class Cerradura {

    public void abrir(){
        System.out.println("Cerradura abierta");

    }

    public static class Puerta extends Cerradura{

        final private Cerradura cerradura=new Cerradura();

        @Override
        public void abrir(){
            cerradura.abrir();
        }
    }
    
    public static void main(String[] args) {
        System.out.println("Quieres abrir lapuerta?(si/no)");
        Scanner sc=new Scanner(System.in);
        String respuesta=sc.nextLine();
        Puerta p=new Puerta();
        if(respuesta.toLowerCase().equals("si")){
        p.abrir();
    }
        sc.close();

}
}
