package abtraccionInterfacesEjercicios;

public class Duck {

    
    public interface Swimable {
    
        void swim();
        
    }
    public interface Flyable {
    void fly();
        
    }
    
    public class Pato implements Swimable, Flyable {
    
        @Override 
        public void swim(){
            System.out.println("El pato nada");

        }
        @Override
        public void fly(){
            System.out.println("El pato vuela");
        }
        
    }
}
