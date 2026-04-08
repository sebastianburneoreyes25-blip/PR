package Java.ejerciciosHerecnaiPolimorfisamo;

import Java.EjerciciosClases.main;

public class Animal {
    
    public static void makeSound(){
    System.out.println("Sonido del animal");    
    }
    public class Dog extends Animal {
        public static void makeSound(){
            System.out.println( "wofwof");
        } 
        
    }
    public class Cat extends Animal {
        public static void makeSound(){
            System.out.println( "Miau");
        } 
        
    }
    
    public static void main(String[] args) {
        Animal.makeSound();
        Dog.makeSound();
        Cat.makeSound();
    }
}
