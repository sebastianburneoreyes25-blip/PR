package Java.ejerciciosHerecnaiPolimorfisamo;

public class Person {
    String name;
    int age;

    public Person(String name, int age){
        this.name=name;
        this.age=age;
    }

    public class Student extends Person {
        float grade;

        public Student(String name, int age, float grade){
            super(name, age);
            this.grade=grade;
            
        }
        public void study(){

        }
        
    }

}
