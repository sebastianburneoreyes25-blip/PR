

public class Vehiculo {

    public static void main(String[] args) {
        Vehiculo.move();
        Car.honk();

    }
    
    
    
    
    
    public static void move(){
        System.out.println("Se mueve");
    }
    public class Car extends Vehiculo {
        public static void honk(){
            System.out.println("HONK HONK");
        }
    
    }


}

