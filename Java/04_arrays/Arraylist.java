import java.util.ArrayList;

public class Arraylist {
    
    public static void main(String[] args) {
        ArrayList<String> names=new ArrayList<>();
        var numbers=new ArrayList<Integer>();

        //tamaño
        System.out.println( names.size());

        //Insercion
        names.add("Sebas");
        names.add("B");
        names.add("R");

        System.out.println(names.size());

        //Modificacion
        names.set(2, "Email");
        System.out.println(names.getFirst());
        System.out.println(names.get(1));
        System.out.println(names.getLast());

        //Eliminar
        names.remove(2);
        System.out.println(names.size());


    }

}
