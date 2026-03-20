package Java.EjerciciosClases;

public class Worker {

    String nombre;
    float salario;
    
    public Worker(String nombre,float salario){
        this.nombre=nombre;
        this.salario=salario;
    }

    public void showSalario(){
        System.out.println("Salario= "+this.salario);
    }
    
}
