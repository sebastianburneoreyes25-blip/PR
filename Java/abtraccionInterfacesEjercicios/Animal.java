package abtraccionInterfacesEjercicios;

public abstract class Animal {
    
    void makeSound(){
        System.out.println("sonido");
    }

    public static class Dog extends Animal {
    
        @Override
        void makeSound(){
            System.out.println("WOFWOF");
        }
        
    }
    public static class Cat extends Animal {
    
        @Override
        void makeSound(){
            System.out.println("MEWMEW");
        }
        
    }
    public static void main(String[] args) {
        Dog d=new Dog();
        Cat c=new Cat();
        d.makeSound();
        c.makeSound();
    }


}
