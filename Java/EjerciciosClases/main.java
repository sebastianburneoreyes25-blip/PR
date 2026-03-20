package Java.EjerciciosClases;

import java.util.ArrayList;

public class main {
        public static void main(String[] args) {
            //1. Crea una clase Book con atributos title y author. Crea un objeto y muestra sus datos.
            Book libro=new Book("Elantris","Brandon Sanderson");
            libro.mostrar();
            //2. Crea una clase Dog con un método bark() que imprima su sonido.
            Dog.barck();
            //3. Añade un constructor a la clase Book que reciba title y author.
            Book libro2=new Book("Nacidos de la bruma","Brandon Sanderson");
            //4. Crea una clase Car con atributos brand y model y un método showData().
                Car coche=new Car("Mazda", "Mazda3");
                coche.showData();
            //5. Crea una clase Student con atributo score y un método que diga si aprobó (mayor o igual a 60).
               
                Student estudiante=new Student(50);
                estudiante.aprobo(estudiante.score);
            //6. Crea una clase BankAccount con atributo balance y un método deposit() que sume el saldo.
                BankAcount cuenta=new BankAcount(200);
                cuenta.deposit(20);
                System.out.println(cuenta.balance);
            //7. Crea una clase Rectangle con métodos para calcular el área y el perímetro.
                Rectangle rectangulo=new Rectangle(10, 5);
                rectangulo.calcularArea();
                rectangulo.calcularPerimetro();
            
            //8. Crea una clase Worker que reciba nombre y salario, y un método para mostrar su salario.
                Worker trabajador= new Worker("Ivan", 2500.5f);
                trabajador.showSalario();
            //9. Crea varios objetos Person y guárdalos en un ArrayList.
                Person person1=new Person("Sebas", 26);
                Person person2=new Person("Ivan", 26);
                Person person3=new Person("Taki", 26);
                Person person4=new Person("Desi", 26);
                ArrayList<Person> personas=new ArrayList<>();
                personas.add(person1);
                personas.add(person2);
                personas.add(person3);
                personas.add(person4);
                for (Person person : personas) {
                    System.out.println(person);
                }


            //10. Crea una clase Product y un método que aplique un descuento sobre su precio. 
            Product manzana=new Product("Manzana", 5.9f);
            manzana.descuento();
        }
   


}
