package java.Interface;

public class Interface {


    public static abstract class  Animal {
        
        public void sleep(){
            System.out.println("El animal duerme");
        }
        public void sound(){
            System.out.println("El animal hace sonido");
        }
        
    }
    public interface Flying {

        void fly();
        
    }
    
    public static class Bird extends Animal implements Flying{

        public void fly(){
            System.out.println("El pajaro vuela");
        }

    }

}
