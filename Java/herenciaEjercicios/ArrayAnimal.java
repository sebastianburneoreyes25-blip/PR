import java.util.ArrayList;



public class ArrayAnimal {

    public  void makeSound(){
    System.out.println("Sonido del animal");    
    }
    public static class Dog extends ArrayAnimal {
        @Override
        
        public  void makeSound(){
            System.out.println( "wofwof");
        } 
        
    }
    public static class Cat extends ArrayAnimal {
        @Override
        
        public  void makeSound(){
            System.out.println( "Miau");
        } 
        
    }
    public static class Bird extends ArrayAnimal {
        @Override
        public  void makeSound(){
            System.out.println( "PioPio");
        } 
        
    }
    
    
    public static void main(String[] args) {
        ArrayList<ArrayAnimal> array=new ArrayList<>();
        Dog dog=new Dog();
        Cat cat=new Cat();
        Bird bird=new Bird();
        array.add(dog);
        array.add(cat);
        array.add(bird);
        for (ArrayAnimal arrayAnimal : array) {
            arrayAnimal.makeSound();
        }


    }
    
}
