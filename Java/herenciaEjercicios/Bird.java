

public class Bird {

    public static void main(String[] args) {
        Eagle eagle=new Eagle();
        eagle.fly();
    }


    
public static class Pajaro {

    public  void fly(){
        System.out.println("El pajaro vuela");
    }
}
public static class Eagle extends Pajaro {
        
        @Override
        public  void fly(){
            super.fly();
            System.out.println("El pajaro es un aguila");
        }
        
    }
    
    
}
