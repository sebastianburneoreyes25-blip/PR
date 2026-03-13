import java.util.ArrayList;

public class Ejercicios {

    public static void main(String[] args) {
        
    // 1. Concatena dos cadenas de texto.
    String name="Sebas";
    String surname="BR";
    

    System.out.println(String.format("Me llamo %s %s", name,surname));
    // 2. Muestra la longitud de una cadena de texto.
    System.out.println(name.length());

    // 3. Muestra el primer y último carácter de un string.
   System.out.println(name.charAt(0));
   System.out.println(name.charAt(name.length()-1));

    // 4. Convierte a mayúsculas y minúsculas un string.
    System.out.println(name.toUpperCase());
    System.out.println(name.toLowerCase());

    // 5. Comprueba si una cadena de texto contiene una palabra concreta.
    System.out.println(name.contains("hola"));

    // 6. Formatea un string con un entero.
    int a=5;
    System.out.println(String.format("Buenos dias, hoy he dormino %d horas", a));
    

    // 7. Elimina los espacios en blanco al principio y final de un string.
    System.out.println(name.trim());

    // 8. Sustituye todos los espacios en blanco de un string por un guión (-).
    String newString="Hola buenos dias ";
    System.out.println(newString.replace(" ", "-"));

    // 9. Comprueba si dos strings son iguales.
    System.out.println(name.equals(newString));

    // 10. Comprueba si dos strings tienen la misma longitud.
    String surname2="BR";
    System.out.println(surname.length()==surname2.length());

    // 11. Crea un Array con 5 valores e imprime su longitud.
    String[] names={"Sebas","B","R","26","HOLA"};
    System.out.println(names.length);

    // 12. Modifica uno de los valores del Array e imprime el valor del índice antes y después de modificarlo.
    System.out.println(names[4]);
    names[4]="Adios";
    System.out.println(names[4]);
    // 13. Crea un ArrayList vacío.
    ArrayList<Integer> numbers=new ArrayList<>();

    // 14. Añade 4 valores al ArrayList y elimina uno a continuación.
    numbers.add(1);
    numbers.add(10);
    numbers.add(100);
    numbers.add(1000);
    System.out.println(numbers.size());
    numbers.removeFirst();
    System.out.println(numbers.size());

    }

}
