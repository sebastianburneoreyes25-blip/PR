package abstraccion;

public class abstraccion {

    public static void main(String[] args) {

        //Abstract sirve como molde para las clases siguientes.
        var dog=new Dog();
        dog.sleep();



    }
    

    public static abstract class  Animal {
        
        public void sleep(){
            System.out.println("El animal duerme");
        }
        public void sound(){
            System.out.println("El animal hace sonido");
        }
        
    }

    public static class Dog extends Animal{

        @Override//para polimorfismo, buena practica
        public void sleep(){
            System.out.println("El perro duerme");
        }

    }

}
