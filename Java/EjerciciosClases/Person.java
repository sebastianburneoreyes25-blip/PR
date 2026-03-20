package Java.EjerciciosClases;

public class Person {
    
    
    //atributos
    String nombre;
    Integer edad;

    //metodos
    public void hola(){
        System.out.println(String.format("Hola soy %s y tengo %d años",nombre,edad));
    }
    
    //Constructor
    public Person(String nombre, Integer edad){
        this.nombre=nombre;
        this.edad=edad;
    
}
}
