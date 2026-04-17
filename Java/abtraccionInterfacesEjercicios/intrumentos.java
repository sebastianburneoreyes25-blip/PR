package abtraccionInterfacesEjercicios;



public class intrumentos {

    public interface Playable {
    
        void play();
        
    }

    public static class Guitar implements Playable {

        @Override
        public void play(){
            System.out.println("*Sonido de guitarrita");
        }
    
        
    }
    public static class Piano implements Playable {

        @Override
        public void play(){
            System.out.println("*Sonido de piano");
        }
    
        
    }
    public static void main(String[] args) {
        Piano p =new Piano();
        Guitar g=new Guitar();
        p.play();
        g.play();
    }
    
}
