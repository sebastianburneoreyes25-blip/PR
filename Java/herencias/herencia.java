package Java.herencias;

public class herencia {
    

    public static class Animal {
        String name;

        public void eat(){
            System.out.println(String.format("EL animal %s esta comiento", this.name ));
        }
    
    }
    public static class dog extends Animal {
     
        public void eat(){//Polimorfismo
            System.out.println("El perro hace wow");
        }
    
    }
}
