package composicionEjercicios;

import java.util.Scanner;

public class Hoja {

    public void cortar(){
        System.out.println("cortando material.....");
    }

    static class Tijeras extends Hoja{
       final private Hoja h=new Hoja();

        public void cortar(){
            h.cortar();
        } 
    }

    public static void main(String[] args) {
        System.out.println("Cuantas veces quieres cortar?");
        Scanner sc=new Scanner(System.in);

        int veces=sc.nextInt();{
        Tijeras t=new Tijeras();
        for(int i=0; i<veces; i++)
        
        t.cortar();
        }
        sc.close();

    }
    
}
