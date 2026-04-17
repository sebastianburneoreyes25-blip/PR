public class Vehicle {
    void describe(){
        System.out.println("Es un vehiculo");

    }
    

    
    public class Bike extends Vehicle {
    @Override
        void describe(){
        System.out.println("Es una bici");

    }
        
    }
    public class Car extends Vehicle {
    @Override
        void describe(){
        System.out.println("Es un coche");

    }
        
    }
    public class Truck extends Vehicle {
    
        @Override
        void describe(){
        System.out.println("Es un camion");

    }
        
    }
}
