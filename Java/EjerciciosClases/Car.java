package Java.EjerciciosClases;

public class Car {
    
    String brand;
    String model;

    public Car(String brand, String model){
        this.brand=brand;
        this.model=model;

    }

    public  void showData(){
        System.out.println(this.brand+" "+this.model);
    }
}
