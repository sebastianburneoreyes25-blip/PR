package abtraccionInterfacesEjercicios;

public abstract class Employee {

    float salarioHora=12;

     abstract void calcularSalario();

    public static class Fulltime extends Employee {
        float horasTrabajo=40;

        @Override 
        void calcularSalario(){
            System.out.println("Salario: "+this.salarioHora*this.horasTrabajo);
        }
        
    }
    public static class PartTime extends Employee {
        float horasTrabajo=20;

        @Override 
        void calcularSalario(){
            System.out.println("Salario: "+this.salarioHora*this.horasTrabajo);
        }
        
    }

    public static void main(String[] args) {
        Employee ft=new Fulltime();
        Employee pt=new PartTime();
        ft.calcularSalario();
        pt.calcularSalario();

    }

}
