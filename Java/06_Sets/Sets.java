import java.util.HashSet;

public class Sets {

    public static void main(String[] args) {
    
        //Declaracion de un Set
        HashSet<String> names= new HashSet<>();
        var numbers=new HashSet<Integer>();

        //Tamaño
        System.out.println(names.size());

        //Insercion 
        names.add("Sebas");
        names.add("Bur");
        names.add("Rey");
        System.out.println(names.size());
        System.out.println(names);

        numbers.add(1);
        numbers.add(10);
        numbers.add(100);
        numbers.add(1000);
        System.out.println(numbers);

        //Busqueda

        System.out.println(names.contains("Sebas"));
        System.out.println(names);
        names.add("Sebas");
        System.out.println(names);

        //Eliminar
        names.remove("Bur");
        System.out.println(names);

        //Conjuntos
        var countries=new HashSet<String>();
        countries.add("Spain");
        countries.add("Norway");
        countries.add("South Africa");

        names.addAll(countries);
        System.out.println(names);

        names.removeAll(countries);
        System.out.println(names);

        names.retainAll(countries);//Se queda con los comunes
        System.out.println(names);
    }
}
