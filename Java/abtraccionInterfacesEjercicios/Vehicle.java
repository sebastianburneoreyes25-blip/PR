package abtraccionInterfacesEjercicios;


public class Vehicle {

    public interface Movable {
    
        void move();
    }
    
    public static class Car implements Movable{
        @Override
        public void move(){
            System.out.println("El coche rueda");
        }
    }
public static class Robot implements Movable{
        @Override
        public void move(){
            System.out.println("El robot camina");
        }
    }

    public static void main(String[] args) {
        Car c=new Car();
    Robot r=new Robot();
    c.move();
    r.move();
    }

}
