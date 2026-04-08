package Java.ejerciciosHerecnaiPolimorfisamo;

public class Employee {
    String name;
    double salary;

    public Employee(String name, double salary){
        this.name=name;
        this.salary=salary;
    }
    public class Manager extends Employee{
        String departament;
        public Manager(String name, double salary, String department){
            super(name, salary);
            this.departament=department;
        }
    }
    
}
