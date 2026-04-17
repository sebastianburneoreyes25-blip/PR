package abtraccionInterfacesEjercicios;
public  abstract class Apliance {
    

    public  void turnOn(){
        System.out.println("Se ha encendido");
    }

    public  void turnOff(){
        System.out.println("Se ha apagado");
    }


    public static class TV extends Apliance{
        
        @Override
    public  void turnOn(){
    System.out.println("Se ha encendido la TV");
    }
        @Override

    public  void turnOff(){
        System.out.println("Se ha apagado la TV");
    }

    }
    public static class WashingMachine extends Apliance{
        
        @Override
    public  void turnOn(){
    System.out.println("Se ha encendido la lavadora");
    }
        @Override

    public  void turnOff(){
        System.out.println("Se ha apagado la lavadora");
    }
    
    }

    public static void main(String[] args) {
        TV tv=new TV();
        WashingMachine lavadora= new WashingMachine();
        tv.turnOn();
        lavadora.turnOn();
    }

    
}
