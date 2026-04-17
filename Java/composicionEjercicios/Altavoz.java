package composicionEjercicios;

import java.util.Scanner;

public class Altavoz {
    
    void reproducir(String sonido){
        System.out.println("Reproduciendo "+sonido);
    }
    public static class  Radio extends Altavoz {
    
        private final Altavoz a=new Altavoz();

        
        void reproducir(String sonido) {
            
            a.reproducir(sonido);
        }
    }

    public static void main(String[] args) {
        System.out.println("Dame el nombre de la emisora");
        Scanner sc=new Scanner(System.in);
        String emisora=sc.nextLine();
        Radio r=new Radio();
        r.reproducir(emisora);
        sc.close();

    }
}
