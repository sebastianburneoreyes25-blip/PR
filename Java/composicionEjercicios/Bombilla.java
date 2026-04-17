package composicionEjercicios;

import java.util.Scanner;

public class Bombilla {
    
    public void iluminar(){
        System.out.println("Luz encencida");
    }

    static class Linterna extends Bombilla {
    final private Bombilla b=new Bombilla();

    public void iluminar(){
        b.iluminar();
    }
        
    public static void main(String[] args) {
        System.out.println("Presiona \"f\" para encender la linterna");
    Scanner sc=new Scanner(System.in);
        String encender=sc.nextLine();
        if(encender.equals("f")){
        Linterna l=new Linterna();
        l.iluminar();
        sc.close();

    }
    }
    }
}
